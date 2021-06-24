
import discord
from datetime import datetime

def crossDex(pair, inputAmount, out0, out1, version):
    
    embed = discord.Embed(title="Arbitrage opportunity on " + pair,
                        description="Version: " + str(version),
                        color=discord.Colour.green())
    
    embed.add_field(name="Out0", value=out0)
    embed.add_field(name="Out1", value=out1)    
    embed.add_field(name="Gain %", value=(((out1 / inputAmount) - 1.0) * 100), inline=False)
    embed.add_field(name="Gain in token", value=out1 - inputAmount, inline=False)
    embed.add_field(name="Timestamp", value=datetime.now())
    
    return embed