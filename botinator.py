import discord
from discord.ext import commands
from secret import secret as token
from assets import reponses
import random

client = commands.Bot(command_prefix= '!') # set the command prefix to !

@client.event
async def on_ready():
	print('We are online')

@client.event
async def on_member_join(member):
	await member.send(f'O morcão {member} entrou no server')
	await print(f'O morcão {member} entrou no server')

@client.event
async def on_member_remove(member):
	await member.send(f'Xau {member} morre longe')
	await print(f'Xau {member} morre longe')

@client.command()
async def ping(ctx): #migration  ctx == context
	await ctx.send(f'Pong with ping of {round(client.latency*1000)}ms!')

@client.command()
async def maia(ctx, *,question):
	await ctx.send(f'Pergunta:{question}\nResposta: {random.choice(reponses)}')

@client.command()
async def pm(ctx, target: discord.User, *, message): #!pm @target 'message'
	await target.send(message)

client.run(token)
