import discord
from analyzer.analyze import analyze_sport
import random
import time

last_done = 0

def get_random_msg():
	msgs = [
		"Oh zin j'ai pas capté",
		"Ok frr",
		"J'ai pas compris le zincou",
		"Chepa frr",
		"Mdrr",
		"Ah oue bene",
		"Bene de loco",
		"Ramcho",
		"Ramcho de loco",
		"Parle français",
		"¯\_(ツ)_/¯",
		"侮辱",
		"оскорблять",
		"Jsuis chaud",
		"Quoicoubeh",
		"Apagnan"
	]
	return msgs[random.randint(0, len(msgs)-1)]

def get_help_msg():
	ret = "C'est simple, tu fais ! avec le sport que tu veux\n Par exemple !football\nPour l'instant y'a que football, tennis, baseball, handball"
	return ret

def check_time():
	global last_done
	if time.time() - last_done < 900:
		return False
	return True

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
	print('We have loggin in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.channel.id != 1108192516446097459:
		return

	msg = message.content

	if '!help' in msg:
		await message.channel.send(get_help_msg())
		return

	if '!football' not in msg and '!tennis' not in msg and '!handball' not in msg and '!baseball' not in msg:
		await message.channel.send(get_random_msg())
		return

	if check_time() == False and message.author.id != 241282052283039745:
		await message.channel.send("Attend un peu je peux pas trop spam, sinon je me fait ban des sites de paris sportifs loco")
		return

	if '!football' in msg:
		tosend = analyze_sport('football')
	elif '!tennis' in msg:
		tosend = analyze_sport('tennis')
	elif '!handball' in msg:
		tosend = analyze_sport('handball')
	elif '!baseball' in msg:
		tosend = analyze_sport('baseball')
	buf = ''
	for i in range(len(tosend)):
		buf = buf + tosend[i]
		if len(buf) >= 1000:
			await message.channel.send(buf)
			buf = ''
	if len(buf) > 0:
		await message.channel.send(buf)
	global last_done
	last_done = time.time()
	print(f'last done here = {last_done}')

client.run('Ahahahahahahahaha')
