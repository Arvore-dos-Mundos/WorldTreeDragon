import discord
from objectClass import Iniciativa
from discord.ext import commands


class BasicCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.objeto = Iniciativa()
        
    @commands.slash_command(name="mostrar")
    async def Mostrar(self, ctx: commands.Context):
        iniciativas = self.objeto.iniciativas.get(ctx.channel.id, [])
        if not iniciativas:
            mensagem = "Não há iniciativas nesse chat."
        else:
            mensagem = "\n".join("{:2d}       {:<10}       [{:2d}]".format(i, nome, iniciativa) for i, (nome, iniciativa) in enumerate(iniciativas))
        e = discord.Embed(title="INICIATIVA")
        e.add_field(name="Iniciativas", value=mensagem, inline=True)
        await ctx.respond(embed=e)
        
    @commands.slash_command(name="ajuda")
    async def Ajuda(self, ctx: commands.Context):
        e = discord.Embed(title="COMANDOS", description='''
                          /adicionar <nome> <iniciativa>
                          /mostrar
                          /matar <ID ou NOME>
                          ''')
        await ctx.respond(embed=e)

    @commands.slash_command(name="nova_iniciativa")
    async def NovaIniciativa(self, ctx: commands.Context):
        self.objeto.iniciativas[ctx.channel.id] = []
        await self.Mostrar(ctx)
        await ctx.respond("Nova iniciativa criada.")

    @commands.slash_command(name="adicionar")
    async def Adicionar(self, ctx: commands.Context, nome: str, iniciativa: int):
        self.objeto.adicionar_iniciativa_chat(ctx.channel.id, nome, iniciativa)
        await self.Mostrar(ctx)
        await ctx.respond("Adicionado")
    
    @discord.slash_command(name="matar")
    async def Matar(self, ctx: commands.context, referencia: str):
        chat_id = ctx.channel.id
        iniciativas = self.objeto.iniciativas.get(chat_id, [])
            
        if referencia.isnumeric():
            # Se a referência for um número, consideramos que é o índice da iniciativa na lista
            index = int(referencia)
            if index < 0 or index >= len(iniciativas):
                await self.Mostrar(ctx)
                await ctx.respond("Índice inválido.")
                return
            del iniciativas[index]
        else:
            # Se a referência for uma string, consideramos que é o nome da iniciativa
            # Procuramos pelo nome na lista de iniciativas
            for i, (nome, _) in enumerate(iniciativas):
                if nome.lower() == referencia.lower():
                    del iniciativas[i]
                    break
            else:
                await self.Mostrar(ctx)
                await ctx.respond("Nome inválido.")
                return
            
        self.objeto.iniciativas[chat_id] = sorted(iniciativas, key=lambda x: x[1]) # ordena a lista pelo valor da iniciativa
        await self.Mostrar(ctx)
        await ctx.respond("Iniciativa deletada com sucesso.")

def setup(bot: commands.Bot):
    bot.add_cog(BasicCommands(bot))