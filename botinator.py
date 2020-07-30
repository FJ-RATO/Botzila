import discord
from discord.ext import commands
from secret import secret as token
from assets import *
import random

client = commands.Bot(command_prefix= '!') # set the command prefix to !

@client.event
async def on_ready():
	print('We are online')

@client.event
async def on_member_join(member):
	await member.send(f'O morcão {member} entrou no server') #this is a pm
	print(f'O morcão {member} entrou no server')

@client.event
async def on_member_remove(member):
	print(f'Xau {member} morre longe')

@client.command()
async def ping(ctx): #migration  ctx == context
	await ctx.send(f'Pong with ping of {round(client.latency*1000)}ms!') #gives out ping from bot to server

@client.command()
async def maia(ctx, *,question):
	await ctx.send(f'Pergunta:{question}\nResposta: {random.choice(reponses)}') #prints question and answer

@client.command()
async def pm(ctx, target: discord.User, *, message): #!pm @target 'message'
	await target.send(message)


client.run(token)
