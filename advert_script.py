import discord
import os
from discord.ext import commands
from asyncio import sleep

me = commands.Bot(command_prefix='.', self_bot=True)
token = open("token", "r").readline()

def makeAdvertEmbed():

    desc = "We are **The Duck Pond** - a social guild planning casual raid progression with a moderate focus on PVP. Our membership core consists of multiple 2k+ arena rated players and decades of combined raid and WoW experience. We strive to be the most welcoming guild in the server by helping each other throughout the leveling process and teaching mechanics and strategy to newer players while also having a loot system that makes it possible to earn loot even if you can't make it to every raid."

    events = "The biweekly events that our guild host are what make us special. We plan to make the World of Warcraft the most fun place to spend your time. We will be hosting serious events like World Boss attempts, World PVP and dueling tournaments to more casual fun events like hide and seek in Orgrimmar, races across Azeroth and more!"

    loot = "We will be using a modified dkp system where points are earned for raid attendance but also for attending biweekly guild events. We know that not everyone can make it to every raid night so having this alternate system for earning points allow players with variable free time to still earn points on their own schedule. Moreover, the goal of dkp is to reward players for helping out the guild and expanding that past raids is the only logical conclusion." 

    goals = "We want to provide a guild for the people out there who don't have as much time as they used to - parents, people in service jobs and people who generally have responsibilities outside of gaming. With all these things in mind our goal is to progress through every Raid when it is current content with a mostly casual schedule while also getting multiple members to the higher ranks in PVP."

    requirements="We don't have any express requirements other than we expect our members to be mature and our guild to be drama free and love fun!"

    #Duck Yellow
    embed = discord.Embed(title="The Duck Pond - Horde - NA - PVP",colour=0xFFEF01, description=desc)
    
    embed.add_field(name="Our Goals", value=goals)

    embed.add_field(name="Events", value=events)
    
    embed.add_field(name="Loot", value=loot)
    
    embed.add_field(name="Requirements", value=requirements)
    
    embed.add_field(name = "Join us!", value="If you are interested in joining, follow the link! https://discord.gg/dykThXM")

    embed.set_thumbnail(url="https://i.imgur.com/DQv2tzl.png")

    # Return to user
    return embed


@me.event
async def on_message(message):
    if message.author.id != me.user.id:
        return
    if len(message.embeds) > 0:
        return

    actualDict = {}
    name = message.clean_content

    replacement = makeAdvertEmbed()
    await message.edit(content='  ', embed=replacement)



me.run(token.strip(), bot=False)
