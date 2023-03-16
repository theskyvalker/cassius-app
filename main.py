import openai
import os
import discord
from keep_alive import keep_alive
import prompts

intents = discord.Intents.all()
openai.api_key = os.environ['OPENAI_API_KEY']
client = discord.Client(intents=intents)
'''
**Cassius Clarke  tone translator**
cc say - Cassius Clarke  will say what you write in his own words
cc repeat - Cassius Clarke  will say exactly what you write, how you write it

**Cassius Clarke  will use his own words**
Cassius Clarke  will use the replied to message as a prompt if you type:
cc reply - Cassius Clarke  will reply to a message in his own words
cc comment - Cassius Clarke  will comment on the event of the replied message
cc headline - Cassius Clarke  will spin a headline based on the replied message

**Delete last message**
cc delete - will delete his last message if it is within 50 messages
'''

#AUTHORIZED_ROLES = [1009894592562339902, 1074067345917624373]


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  '''
  # We will use this to implement role gating
  authorized_role_list = len(
    [x.id for x in message.author.roles if x.id in AUTHORIZED_ROLES])
  if authorized_role_list == 0:
    print("not authorized")
    return
  '''

  # SAY OR REPLY IN AUTHORS WORDS
  if message.content.startswith('cc say'):
    referenced_message = await message.channel.fetch_message(
      message.reference.message_id) if message.reference is not None else None
    referenced_user = referenced_message.author.name if message.reference is not None else 'X'
    human_input = message.content[len('cc say'):].strip()
    await message.delete()

    set_up = '''You are a brilliant fantasy writer. You are able to take dialogue from one character and reword it to sound like a completely different character said it, with their tone and mannerisms.'''

    prompt = f'''{prompts.who_is_Cassius_Clarke}
    {prompts.Cassius_Clarke_background}
    {prompts.tone}

    You are a brilliant fantasy writer. You are able to take dialogue from one character and reword it to sound like a completely different character said it, with their tone and mannerisms. Take the dialogue from 'X' below, and reword it to sound like Cassius Clarke would say it, with their tone and mannerisms. Output your answer as 'Cassius Clarke'.
    X:{human_input}
    Cassius Clark:'''

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                              {
                                                "role": "system",
                                                "content": set_up,
                                                "role": "user",
                                                "content": prompt
                                              },
                                            ])
    print(response.choices[0].message.content)
    await message.channel.send(response.choices[0].message.content,
                               reference=referenced_message)

  if message.content.startswith('cc repeat'):
    referenced_message = await message.channel.fetch_message(
      message.reference.message_id) if message.reference is not None else None
    human_input = message.content[len('cc repeat'):].strip()
    await message.delete()
    print(human_input)
    await message.channel.send(human_input, reference=referenced_message)

  # REPLY IN OWN WORDS
  if message.content.startswith('cc reply') and message.reference is not None:
    referenced_message = await message.channel.fetch_message(
      message.reference.message_id)
    referenced_user = referenced_message.author.name
    human_input = referenced_message.content
    await message.delete()

    set_up = '''You are a brilliant Shakespearean journalist. You specialize in war journalism. You ask great questions and are comedic and charistmatic.'''
    prompt = f'''{prompts.who_is_Cassius_Clarke}
    {prompts.Cassius_Clarke_background}
    {prompts.tone}

    You are a brilliant Shakespearean journalist. You specialize in war journalism. You ask great questions and are comedic and charistmatic. Read the dialogue from {referenced_user} below, and reply to it in the way that Cassius Clarke would, with their tone and mannerisms. Output your answer in 'Cassius Clark'.
    {referenced_user}:{human_input}
    Cassius Clark:'''

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                              {
                                                "role": "system",
                                                "content": set_up,
                                                "role": "user",
                                                "content": prompt
                                              },
                                            ])
    print(response.choices[0].message.content)
    await message.channel.send(response.choices[0].message.content,
                               reference=referenced_message)

  if message.content.startswith(
      'cc comment') and message.reference is not None:
    referenced_message = await message.channel.fetch_message(
      message.reference.message_id)
    referenced_user = referenced_message.author.name
    human_input = referenced_message.content
    await message.delete()

    set_up = '''You are a brilliant Shakespearean journalist. You specialize in war journalism. You report and make highly engaging comments, and are comedic and charistmatic.'''
    prompt = f'''{prompts.who_is_Cassius_Clarke}
    {prompts.Cassius_Clarke_background}
    {prompts.tone}

    You are a brilliant Shakespearean journalist. You specialize in war journalism. You report and make highly engaging comments, and are comedic and charistmatic. Read the dialogue from {referenced_user} below, and make a comment on it in the Cassius Clarke would, with their tone and mannerisms. Output your answer in 'Cassius Clark'.
    {referenced_user}:{human_input}
    Cassius Clark:'''

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                              {
                                                "role": "system",
                                                "content": set_up,
                                                "role": "user",
                                                "content": prompt
                                              },
                                            ])
    print(response.choices[0].message.content)
    await message.channel.send(response.choices[0].message.content,
                               reference=referenced_message)

  if message.content.startswith(
      'cc headline') and message.reference is not None:
    referenced_message = await message.channel.fetch_message(
      message.reference.message_id)
    referenced_user = referenced_message.author.name
    human_input = referenced_message.content
    await message.delete()

    set_up = '''You are a brilliant Shakespearean journalist. You specialize in war journalism. You write great headlines and are comedic and charistmatic.'''
    prompt = f'''{prompts.who_is_Cassius_Clarke}
    {prompts.Cassius_Clarke_background}
    {prompts.tone}

    You are a brilliant Shakespearean journalist. You specialize in war journalism. You write great headlines and are comedic and charistmatic. Read the dialogue from {referenced_user}, and turn it into a headline, in the way that Cassius Clarke would, with their tone and mannerisms. Write it in all-caps. Output your answer in 'Cassius Clark'.
    {referenced_user}:{human_input}
    Cassius Clark:'''

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                              {
                                                "role": "system",
                                                "content": set_up,
                                                "role": "user",
                                                "content": prompt
                                              },
                                            ])
    print(response.choices[0].message.content)
    await message.channel.send(response.choices[0].message.content,
                               reference=referenced_message)


keep_alive()
TOKEN = os.environ['CASSIUS_TOKEN']
print(TOKEN)
client.run(TOKEN)