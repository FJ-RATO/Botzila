import discord
from secret import secret as token

prefix = '!'

class Myclient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self,message):
		if message.author == client.user:
			return #bot wont listen to itself
		if message.content.startswith(prefix + 'ping'):
			await message.channel.send('pong')
		#print('Message from {0.author}: {0.content}'.format(message))



client = Myclient()
client.run(token)