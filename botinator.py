import discord
from discord.ext import commands
from secret import secret as token
from assets import *
import random
import sqlite3

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

#economic commands

#balance
@client.command()
async def carteira(ctx):
	bank = sqlite3.connect('main.sqlite')
	cursor = bank.cursor()
	cursor.execute(f"SELECT id FROM bank where id = {ctx.author.id}")
	result = cursor.fetchone()
	if result is None:
		cursor.execute(f'INSERT INTO bank(id,cash) VALUES({ctx.author.id},0)')
		await ctx.send(f'{ctx.author} agora é capitalista')
	else:
		cursor.execute(f'SELECT cash FROM bank where id = {ctx.author.id}')
		result = cursor.fetchone()
		await ctx.send(f'{ctx.author} tem {result} botes')
	bank.commit()
	cursor.close()
	bank.close()

#(ADMIN TEST) add entry

#event handle ROLES

@client.event
async def on_raw_reaction_add(payload):
	message_id = payload.message_id
	if message_id == 744271808630620350:
		role = discord.utils.get(client.guilds[0].roles , name = payload.emoji.name)
		await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
	message_id = payload.message_id
	if message_id == 744271808630620350:
		role = discord.utils.get(client.guilds[0].roles , name = payload.emoji.name)
		user = discord.utils.get(client.guilds[0].members,id = payload.user_id)
		await user.remove_roles(role)

#@client.event
#async def on_raw_reaction_remove(payload):

client.run(token)
