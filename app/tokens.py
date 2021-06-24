from secrets import infura_project_id
from web3 import Web3

RPC_URL_INFURA = "https://mainnet.infura.io/v3/" + infura_project_id

w3 = Web3(Web3.HTTPProvider(RPC_URL_INFURA))

AAVE = {
'symbol': 'AAVE',
'name': 'Aave',
'address': hex(0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9),
'cksum_address': w3.toChecksumAddress('0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9'),
'decimals': 18,
}
AMP = {
'symbol': 'AMP',
'name': 'Amp',
'address': hex(0xfF20817765cB7f73d4bde2e66e067E58D11095C2),
'cksum_address': w3.toChecksumAddress('0xfF20817765cB7f73d4bde2e66e067E58D11095C2'),
'decimals': 18,
}
ANT = {
'symbol': 'ANT',
'name': 'Aragon Network Token',
'address': hex(0x960b236A07cf122663c4303350609A66A7B288C0),
'cksum_address': w3.toChecksumAddress('0x960b236A07cf122663c4303350609A66A7B288C0'),
'decimals': 18,
}
BAL = {
'symbol': 'BAL',
'name': 'Balancer',
'address': hex(0xba100000625a3754423978a60c9317c58a424e3D),
'cksum_address': w3.toChecksumAddress('0xba100000625a3754423978a60c9317c58a424e3D'),
'decimals': 18,
}
BAND = {
'symbol': 'BAND',
'name': 'Band Protocol',
'address': hex(0xBA11D00c5f74255f56a5E366F4F77f5A186d7f55),
'cksum_address': w3.toChecksumAddress('0xBA11D00c5f74255f56a5E366F4F77f5A186d7f55'),
'decimals': 18,
}
BNT = {
'symbol': 'BNT',
'name': 'Bancor Network Token',
'address': hex(0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C),
'cksum_address': w3.toChecksumAddress('0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C'),
'decimals': 18,
}
COMP = {
'symbol': 'COMP',
'name': 'Compound',
'address': hex(0xc00e94Cb662C3520282E6f5717214004A7f26888),
'cksum_address': w3.toChecksumAddress('0xc00e94Cb662C3520282E6f5717214004A7f26888'),
'decimals': 18,
}
CRV = {
'symbol': 'CRV',
'name': 'Curve DAO Token',
'address': hex(0xD533a949740bb3306d119CC777fa900bA034cd52),
'cksum_address': w3.toChecksumAddress('0xD533a949740bb3306d119CC777fa900bA034cd52'),
'decimals': 18,
}
CVC = {
'symbol': 'CVC',
'name': 'Civic',
'address': hex(0x41e5560054824eA6B0732E656E3Ad64E20e94E45),
'cksum_address': w3.toChecksumAddress('0x41e5560054824eA6B0732E656E3Ad64E20e94E45'),
'decimals': 8,
}
DAI = {
'symbol': 'DAI',
'name': 'Dai Stablecoin',
'address': hex(0x6B175474E89094C44Da98b954EedeAC495271d0F),
'cksum_address': w3.toChecksumAddress('0x6B175474E89094C44Da98b954EedeAC495271d0F'),
'decimals': 18,
}
DNT = {
'symbol': 'DNT',
'name': 'district0x',
'address': hex(0x0AbdAce70D3790235af448C88547603b945604ea),
'cksum_address': w3.toChecksumAddress('0x0AbdAce70D3790235af448C88547603b945604ea'),
'decimals': 18,
}
GNO = {
'symbol': 'GNO',
'name': 'Gnosis Token',
'address': hex(0x6810e776880C02933D47DB1b9fc05908e5386b96),
'cksum_address': w3.toChecksumAddress('0x6810e776880C02933D47DB1b9fc05908e5386b96'),
'decimals': 18,
}
GRT = {
'symbol': 'GRT',
'name': 'The Graph',
'address': hex(0xc944E90C64B2c07662A292be6244BDf05Cda44a7),
'cksum_address': w3.toChecksumAddress('0xc944E90C64B2c07662A292be6244BDf05Cda44a7'),
'decimals': 18,
}
KEEP = {
'symbol': 'KEEP',
'name': 'Keep Network',
'address': hex(0x85Eee30c52B0b379b046Fb0F85F4f3Dc3009aFEC),
'cksum_address': w3.toChecksumAddress('0x85Eee30c52B0b379b046Fb0F85F4f3Dc3009aFEC'),
'decimals': 18,
}
KNC = {
'symbol': 'KNC',
'name': 'Kyber Network Crystal',
'address': hex(0xdd974D5C2e2928deA5F71b9825b8b646686BD200),
'cksum_address': w3.toChecksumAddress('0xdd974D5C2e2928deA5F71b9825b8b646686BD200'),
'decimals': 18,
}
LINK = {
'symbol': 'LINK',
'name': 'ChainLink Token',
'address': hex(0x514910771AF9Ca656af840dff83E8264EcF986CA),
'cksum_address': w3.toChecksumAddress('0x514910771AF9Ca656af840dff83E8264EcF986CA'),
'decimals': 18,
}
LOOM = {
'symbol': 'LOOM',
'name': 'Loom Network',
'address': hex(0xA4e8C3Ec456107eA67d3075bF9e3DF3A75823DB0),
'cksum_address': w3.toChecksumAddress('0xA4e8C3Ec456107eA67d3075bF9e3DF3A75823DB0'),
'decimals': 18,
}
LRC = {
'symbol': 'LRC',
'name': 'LoopringCoin V2',
'address': hex(0xBBbbCA6A901c926F240b89EacB641d8Aec7AEafD),
'cksum_address': w3.toChecksumAddress('0xBBbbCA6A901c926F240b89EacB641d8Aec7AEafD'),
'decimals': 18,
}
MATIC = {
    'symbol': 'MATIC',
    'name': 'Polygon',
    'address': hex(0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0),
    'cksum_address': w3.toChecksumAddress(0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0),
    'decimals': 18,
}
MANA = {
'symbol': 'MANA',
'name': 'Decentraland',
'address': hex(0x0F5D2fB29fb7d3CFeE444a200298f468908cC942),
'cksum_address': w3.toChecksumAddress('0x0F5D2fB29fb7d3CFeE444a200298f468908cC942'),
'decimals': 18,
}
MKR = {
'symbol': 'MKR',
'name': 'Maker',
'address': hex(0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2),
'cksum_address': w3.toChecksumAddress('0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2'),
'decimals': 18,
}
MLN = {
'symbol': 'MLN',
'name': 'Melon',
'address': hex(0xec67005c4E498Ec7f55E092bd1d35cbC47C91892),
'cksum_address': w3.toChecksumAddress('0xec67005c4E498Ec7f55E092bd1d35cbC47C91892'),
'decimals': 18,
}
NMR = {
'symbol': 'NMR',
'name': 'Numeraire',
'address': hex(0x1776e1F26f98b1A5dF9cD347953a26dd3Cb46671),
'cksum_address': w3.toChecksumAddress('0x1776e1F26f98b1A5dF9cD347953a26dd3Cb46671'),
'decimals': 18,
}
NU = {
'symbol': 'NU',
'name': 'NuCypher',
'address': hex(0x4fE83213D56308330EC302a8BD641f1d0113A4Cc),
'cksum_address': w3.toChecksumAddress('0x4fE83213D56308330EC302a8BD641f1d0113A4Cc'),
'decimals': 18,
}
OXT = {
'symbol': 'OXT',
'name': 'Orchid',
'address': hex(0x4575f41308EC1483f3d399aa9a2826d74Da13Deb),
'cksum_address': w3.toChecksumAddress('0x4575f41308EC1483f3d399aa9a2826d74Da13Deb'),
'decimals': 18,
}
REN = {
'symbol': 'REN',
'name': 'Republic Token',
'address': hex(0x408e41876cCCDC0F92210600ef50372656052a38),
'cksum_address': w3.toChecksumAddress('0x408e41876cCCDC0F92210600ef50372656052a38'),
'decimals': 18,
}
REP = {
'symbol': 'REP',
'name': 'Reputation Augur v1',
'address': hex(0x1985365e9f78359a9B6AD760e32412f4a445E862),
'cksum_address': w3.toChecksumAddress('0x1985365e9f78359a9B6AD760e32412f4a445E862'),
'decimals': 18,
}
REPv2 = {
'symbol': 'REPv2',
'name': 'Reputation Augur v2',
'address': hex(0x221657776846890989a759BA2973e427DfF5C9bB),
'cksum_address': w3.toChecksumAddress('0x221657776846890989a759BA2973e427DfF5C9bB'),
'decimals': 18,
}
SNX = {
'symbol': 'SNX',
'name': 'Synthetix Network Token',
'address': hex(0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F),
'cksum_address': w3.toChecksumAddress('0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F'),
'decimals': 18,
}
STORJ = {
'symbol': 'STORJ',
'name': 'Storj Token',
'address': hex(0xB64ef51C888972c908CFacf59B47C1AfBC0Ab8aC),
'cksum_address': w3.toChecksumAddress('0xB64ef51C888972c908CFacf59B47C1AfBC0Ab8aC'),
'decimals': 8,
}
TBTC = {
'symbol': 'TBTC',
'name': 'tBTC',
'address': hex(0x8dAEBADE922dF735c38C80C7eBD708Af50815fAa),
'cksum_address': w3.toChecksumAddress('0x8dAEBADE922dF735c38C80C7eBD708Af50815fAa'),
'decimals': 18,
}
UMA = {
'symbol': 'UMA',
'name': 'UMA Voting Token v1',
'address': hex(0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828),
'cksum_address': w3.toChecksumAddress('0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828'),
'decimals': 18,
}
UNI = {
'symbol': 'UNI',
'name': 'Uniswap',
'address': hex(0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984),
'cksum_address': w3.toChecksumAddress('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984'),
'decimals': 18,
}
USDC = {
'symbol': 'USDC',
'name': 'USDCoin',
'address': hex(0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48),
'cksum_address': w3.toChecksumAddress('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'),
'decimals': 6,
}
USDT = {
'symbol': 'USDT',
'name': 'Tether USD',
'address': hex(0xdAC17F958D2ee523a2206206994597C13D831ec7),
'cksum_address': w3.toChecksumAddress('0xdAC17F958D2ee523a2206206994597C13D831ec7'),
'decimals': 6,
}
WBTC = {
'symbol': 'WBTC',
'name': 'Wrapped BTC',
'address': hex(0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599),
'cksum_address': w3.toChecksumAddress('0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599'),
'decimals': 8,
}
WETH = {
'symbol': 'WETH',
'name': 'Wrapped Ether',
'address': hex(0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2),
'cksum_address': w3.toChecksumAddress('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'),
'decimals': 18,
}
YFI = {
'symbol': 'YFI',
'name': 'yearn finance',
'address': hex(0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e),
'cksum_address': w3.toChecksumAddress('0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e'),
'decimals': 18,
}
ZRX = {
'symbol': 'ZRX',
'name': '0x Protocol Token',
'address': hex(0xE41d2489571d322189246DaFA5ebDe1F4699F498),
'cksum_address': w3.toChecksumAddress('0xE41d2489571d322189246DaFA5ebDe1F4699F498'),
'decimals': 18,
}
SUSHI = {
'symbol': 'SUSHI',
'name': 'SushiSwap',
'address': hex(0x6B3595068778DD592e39A122f4f5a5cF09C90fE2),
'cksum_address': w3.toChecksumAddress('0x6B3595068778DD592e39A122f4f5a5cF09C90fE2'),
'decimals': 18,
}
OCC = {
    'symbol': 'OCC',
    'name': 'OccamFi',
    'address': hex(0x2f109021afe75b949429fe30523ee7c0d5b27207),
    'cksum_address': w3.toChecksumAddress(0x2f109021afe75b949429fe30523ee7c0d5b27207),
    'decimals': 18,
}