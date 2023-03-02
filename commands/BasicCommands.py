import discord
from objectClass import Iniciativa
from discord.ext import commands

objeto = Iniciativa()

class BasicCommands(commands.Cog):
    
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()
    
    
    
    @discord.slash_command(name="ajuda")
    async def Test(self, ctx: commands.context):
        e = discord.Embed(title="COMANDOS", description='''
                          /adicionar <nome> <iniciativa>
                          
                          /mostrar
                          
                          ''')
        await ctx.respond(embed = e)
    
    @discord.slash_command(name="adicionar")
    async def Adicionar(self, ctx: commands.context, nome: str, iniciativa: int):
        # chamar a função de adicionar
        objeto.adicionar(nome, iniciativa)
        #-----------------------------
        await ctx.respond("Adicionado")
    
    @discord.slash_command(name="mostrar")
    async def Mostrar(self, ctx: commands.context):
        # chamar a função de mostrar
        mensagem = objeto.mostrar()
        #-----------------------------
        e = discord.Embed(title="INICIATIVA", description=mensagem)
        await ctx.respond(embed = e)
        
def setup(bot: commands.Bot):
    bot.add_cog(BasicCommands(bot))
    