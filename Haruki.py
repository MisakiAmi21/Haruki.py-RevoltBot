from pymongo import MongoClient
import aiohttp
import asyncio
import random
import revolt
from revolt.ext import commands

client = MongoClient('mongodb+srv://Misaki:Him09@cluster0.wcov7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['db1']

class Client(commands.CommandsClient):
    async def get_prefix(self, message:revolt.Message):
        return "r"
    async def on_ready(self):
        await self.edit_status(text="its gonna be a long day...", presence=revolt.PresenceType.idle)
        print(f"We have logged in as {self.user.name}")
    def __init__(self, *args, **kwargs):
        super().__init__(help_command=None, *args, **kwargs)
#HELP
    @commands.command()
    async def help(self, ctx:commands.Context):
        file = revolt.File("14.png")
        stuff = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#00b7eb", title="Heyy there!! I am Haruki", media=stuff.id, description =f"""{ctx.author.mention} my commands are :
        **MISC :** `info` , `ping` , `love` , `eight` , 
        **ECONOMY :** WIP
        **CARD GAME :** WIP
        **GIFS :** `hug` , `slap` , `dance` , `eat` , `pic` ,
        `revive` , `deadchat` , `hi` ,
        `happy` , `angry` , `lonely` , `cry` , `confused` , `flustered` ,""")
        await ctx.send(embed=embed)
#MISC
    @commands.command()
    async def info(self, ctx:commands.Context):
        file = revolt.File("3.png")
        stuff = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#9966cc", title = "This is da : Information Section", description=f"""{ctx.author.mention} 
        [Discord](https://discord.gg/sVUTKpKEVt) / [Revolt](https://rvlt.gg/eqhNQc0w)
        MisakiAmi21: 
        [Instagram](https://www.instagram.com/misakiami21/)
        [YT](https://www.youtube.com/channel/UC_7XzwQUZ7Rq9P4N_giHAVQ)
        [Wattpad](https://www.wattpad.com/user/MisakiAmi21)
        [Quotev](https://www.quotev.com/MisakiAmi21)
        [Twitch](https://www.twitch.tv/misakiami21)""", media=stuff.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def love(self, ctx:commands.Context, user: revolt.ext.commands.MemberConverter):
        file = revolt.File("9.png")
        stuff = await self.upload_file(file, 'attachments')
        love_score = random.randint(1, 100)
        embed = revolt.SendableEmbed(colour="#9966cc", title="Love Meter", description=f"{user.mention} likes you {ctx.author.mention} by {love_score}%.",
                                     media=stuff.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def eight(self, ctx:commands.Context, *, question):
        file = revolt.File("10.png")
        stuff = await self.upload_file(file, 'attachments')
        responses = ["yes" , "no" , "maybe"]
        answer = random.choice(responses)
        embed = revolt.SendableEmbed(colour="#9966cc", title="Eightball", description=f"{ctx.author.mention}\nYour Question: {question}\nThe Response: {answer}", 
                                     media=stuff.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx:commands.Context):
        await ctx.send("pong")
#ECONOMY

#CARD GAME

#GIFS
#Interaction
    @commands.command()
    async def revive(self, ctx:commands.Context):
        file = revolt.File("revive.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} Is Raising the Dead", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def deadchat(self, ctx:commands.Context):
        file = revolt.File("dead.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} has noticed the chat is dead. RIP!", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def hi(self, ctx:commands.Context):
        file = revolt.File("hello.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} 'I am here' ", media=rev.id)
        await ctx.send(embed=embed)
#Action
    @commands.command()
    async def hug(self, ctx:commands.Context, user: revolt.ext.commands.MemberConverter):
        file = revolt.File("hug.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} is giving {user.mention} a hug", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx:commands.Context, user: revolt.ext.commands.MemberConverter):
        file = revolt.File("slap.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} slapped {user.mention}", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def dance(self, ctx:commands.Context):
        file = revolt.File("dance.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} is dancing, but we dk why", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def eat(self, ctx:commands.Context):
        file = revolt.File("eat.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} is going afk to eat", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def pic(self, ctx:commands.Context):
        file = revolt.File("caught.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} has caught another user in 4k", media=rev.id)
        await ctx.send(embed=embed)
#Emotion
    @commands.command()
    async def happy(self, ctx:commands.Context):
        file = revolt.File("happy.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} is very happy today", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def angry(self, ctx:commands.Context):
        file = revolt.File("angry.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} may very well go with violence", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def lonely(self, ctx:commands.Context):
        file = revolt.File("lonely.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} is looking to chat!!", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx:commands.Context):
        file = revolt.File("sad.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} seems to be very upset", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def confused(self, ctx:commands.Context):
        file = revolt.File("confused.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} just doesn't know whats happening", media=rev.id)
        await ctx.send(embed=embed)

    @commands.command()
    async def flustered(self, ctx:commands.Context):
        file = revolt.File("flustered.gif")
        rev = await self.upload_file(file, 'attachments')
        embed = revolt.SendableEmbed(colour="#ffc87c", description=f"{ctx.author.mention} is blushing.", media=rev.id)
        await ctx.send(embed=embed)
    
async def main():
    async with aiohttp.ClientSession()as session:
        client = Client(session, "zoAcL2uG7wjMO-oje183exsdTOyAIdpldIjNXekXQDu33KorLwq468IWv9P1R11m")
        await client.start()
asyncio.run(main())