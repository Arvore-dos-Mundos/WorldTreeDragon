import discord
from objectClass import Iniciativa
from discord.ext import commands

class BasicCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        super().__init__()
    
    @commands.command(name="ajuda")
    async def Test(self, ctx: commands.context):
        e = discord.Embed(title="COMANDOS", description='''
                          !adicionar <nome> <iniciativa>
                          
                          !mostrar
                          
                          ''')
        await ctx.reply(embed = e)
    
    @commands.command(name="adicionar")
    async def Adicionar(self, ctx: commands.context, nome: str, iniciativa: int):
        # chamar a função de adicionar
        
        #-----------------------------
        await ctx.reply("Adicionado")
    
    @commands.command(name="mostrar")
    async def Mostrar(self, ctx: commands.context):
        # chamar a função de mostrar
        
        #-----------------------------
        e = discord.Embed(title="INICIATIVA", description="mensagem")
        await ctx.reply(embed = e)
        
def setup(bot: commands.Bot):
    bot.add_cog(BasicCommands(bot))
    