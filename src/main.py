from secrets import infura_project_id, discord_bot_token, arbi_channel

import logging
from tokens import WBTC, WETH

import discord
from discord.ext import commands, tasks
from web3 import Web3

import Embed
import tokens
import pairs
from contracts import sushiswap_router, uniswap_quoter, kyberNetworkProxy

# infura node url
RPC_URL_INFURA = "https://mainnet.infura.io/v3/" + infura_project_id


# create formats for logging
date_strftime_format = "%d-%b-%y %H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(message)s"

# setup the logger
logging.basicConfig(filename="./info.log",
                    format=message_format, datefmt=date_strftime_format)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# initializing the discord client
disc_bot = discord.Client()
logger.info(f"Discord Client started")

# connect to infura node
w3 = Web3(Web3.HTTPProvider(RPC_URL_INFURA))

# get contracts
sushi_router = w3.eth.contract(
    address=sushiswap_router.SUSHISWAP_ROUTER_ADDRESS, abi=sushiswap_router.SUSHISWAP_ROUTER_ABI)
uni_quoter = w3.eth.contract(
    address=uniswap_quoter.UNISWAP_QUOTER_ADDRESS, abi=uniswap_quoter.UNISWAP_QUOTER_ABI)
kyber_network_proxy = w3.eth.contract(
    address=kyberNetworkProxy.KyberNetworkProxy_ADDRESS, abi=kyberNetworkProxy.KyberNetworkProxy_ABI)

# all pairs in the array will get checked for opportunities
pairs = [[pairs.AAVE_WETH, 5],
         [pairs.COMP_WETH, 5],
         [pairs.DAI_WETH, 2000],
         [pairs.DAI_USDC, 1000],
         # no liquidity on sushi
         #[pairs.DAI_USDT, 1000],
         [pairs.LINK_WETH, 100],
         # no liquidity on sushi
         #[pairs.MATIC_USDC, 2000],
         [pairs.MATIC_WETH, 2000],
         [pairs.OCC_USDC, 100],
         [pairs.MKR_WETH, 1],
         [pairs.UNI_WETH, 100],
         [pairs.USDC_WETH, 2000],
         # pairs.WBTC_USDC,],
         [pairs.WBTC_WETH, 0.2],
         [pairs.WETH_USDT, 1]]
# dict to track embed messages in the disc channel
embeds = {}
for pair in pairs:
    embeds[pair[0]['name']] = [None, None]


@disc_bot.event
async def on_ready():
    checkUniSushi.start()
    get_ETH_price.start()

# checks opportunities for a cross exchange swap between Sushiswap and Uniswap


@tasks.loop(seconds=90.0)
async def checkUniSushi():
    # get the disc channel to post the opportunity
    channel = disc_bot.get_channel(arbi_channel)
    # keeps track of the pair we are at
    i = 0
    # got through all pairs
    for pair in pairs:
        token0 = pair[0]['token0']
        token1 = pair[0]['token1']
        fee = pair[0]['fee']
        startAmount = pair[1]

        # check how many tokens will be available after swap in Uni and Sushi pool
        (uni_out, sushi_out) = swapUniSushi(token0, token1, fee, startAmount)
        # check how many tokens will be available after swap in Uni and Kyber pool
        logger.info("Watching on kyber")
        (uni_out_1, kyber_out) = swapUniSushi(token0, token1, fee, startAmount)
        # convert to full tokens
        uni_out = uni_out * (10 ** -(token1['decimals']))
        sushi_out = sushi_out * (10 ** -(token0['decimals']))

        await notifyOnOpportunity(pair[0], startAmount, uni_out, sushi_out, 0, channel)

        # outher way round, sushi to uni
        # check how much tokens will be available after swap in Sushi and Uni pool
        (sushi_out, uni_out) = swapSushiUni(token0, token1, fee, startAmount)

        sushi_out = sushi_out * (10 ** -(token1['decimals']))
        uni_out = uni_out * (10 ** -(token0['decimals']))

        await notifyOnOpportunity(pair[0], startAmount, sushi_out, uni_out, 1, channel)
        # increment counter
        i = i+1

@tasks.loop(minutes=10.0)
async def get_ETH_price():
    # this is just to check if the bot is still running
    uni_out = uni_quoter.functions.quoteExactInputSingle(
        tokenIn=tokens.WETH['cksum_address'],
        tokenOut=tokens.USDC['cksum_address'],
        fee=500,
        amountIn=1 * (10 ** 18),
        sqrtPriceLimitX96=0
    ).call()
    uni_out = uni_out * (10 ** -6)
    logger.info(f"ETH/USDC: " + str(uni_out))


def swapUniSushi(token0, token1, fee, amount):
    uni_out = uni_quoter.functions.quoteExactInputSingle(
        tokenIn=token0['cksum_address'],
        tokenOut=token1['cksum_address'],
        fee=fee,
        amountIn=int(amount * (10 ** token0['decimals'])),
        sqrtPriceLimitX96=0
    ).call()

    sushi_out = sushi_router.functions.getAmountsOut(
        amountIn=uni_out,
        path=[token1["cksum_address"], token0["cksum_address"]]
    ).call()[1]

    return (uni_out, sushi_out)


def swapSushiUni(token0, token1, fee, amount):
    sushi_out = sushi_router.functions.getAmountsOut(
        amountIn=int(amount * (10 ** token0['decimals'])),
        path=[token0["cksum_address"], token1["cksum_address"]]
    ).call()[1]

    uni_out = uni_quoter.functions.quoteExactInputSingle(
        tokenIn=token1["cksum_address"],
        tokenOut=token0["cksum_address"],
        fee=fee,
        amountIn=sushi_out,
        sqrtPriceLimitX96=0
    ).call()

    return (sushi_out, uni_out)

@tasks.loop(seconds=2.0)
async def swapUniKyber(token0, token1, fee, amount):
    uni_out = uni_quoter.functions.quoteExactInputSingle(
        tokenIn=token1["cksum_address"],
        tokenOut=token0["cksum_address"],
        fee=fee,
        amountIn=int(amount * (10 ** token0['decimals'])),
        sqrtPriceLimitX96=0
    ).call()
    
    kyber_out = kyber_network_proxy.functions.getExpectedRate(
        token0['cksum_address'], token1['cksum_address'], uni_out).call()[1]
    
    logger.info("Uni_out: " + (uni_out * (10 ** -token1['decimals'])))
    logger.info("Kyber_out: " + (kyber_out * (10 ** -token0['decimals'])))
    print(uni_out, kyber_out)


async def notifyOnOpportunity(pair, startAmount, out0, out1, version, channel):
    if embeds[pair['name']][version] == None:
        if out1 > startAmount:
            embed = Embed.crossDex(
                pair['name'], startAmount, out0, out1, version)
            # also log the info to file
            logger.info("Found Opportunity with Version " +
                        str(version) + " on " + pair['name'])
            logger.info("Percentage Gain: " +
                        str(((out1 / startAmount) - 1.0) * 100))

            embeds[pair['name']][version] = await channel.send(embed=embed)
    else:
        if out1 > startAmount:
            embed = Embed.crossDex(
                pair['name'], startAmount, out0, out1, version)
            await embeds[pair['name']][version].edit(embed=embed)
        else:
            await embeds[pair['name']][version].delete()
            embeds[pair['name']][version] = None

# start the disc bot
disc_bot.run(discord_bot_token)
