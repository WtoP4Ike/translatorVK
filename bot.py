# -*- coding: utf-8 -*-

# # # # Copyright (C) 2023-2024 Vladimir Zakharov
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # This file is part of TranslatorVK
#
# TranslatorVK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
#
# TranslatorVK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

try:
  from deep_translator import GoogleTranslator
  from vkbottle.bot import Bot, Message
  from vkbottle import API
  import time
  from loguru import logger
  from trconfig import *
  from readlg import *
except:
  quit("Make sure you have installed all the libraries!")

if lang!="ru" and lang!="en":
  quit("No language selected\nСheck config.py")

def get_msg(ntext):
  global lang
  if lang=="ru":
    return ru_lang(ntext)
      
  if lang=="en":
     return en_land(ntext)

  
  
print("""╔══╗╔══╗╔═══╗╔╗╔╗╔═══╗╔══╗╔═══╗╔╗╔╗╔════╗───╔═╗╔══╗╔═╗───╔══╗╔══╗╔══╗╔══╗
║╔═╝║╔╗║║╔═╗║║║║║║╔═╗║╚╗╔╝║╔══╝║║║║╚═╗╔═╝───║╔╝║╔═╝╚╗║───╚═╗║║╔╗║╚═╗║╚═╗║
║║──║║║║║╚═╝║║╚╝║║╚═╝║─║║─║║╔═╗║╚╝║──║║─────║║─║║───║║───╔═╝║║║║║╔═╝║╔═╝║
║║──║║║║║╔══╝╚═╗║║╔╗╔╝─║║─║║╚╗║║╔╗║──║║─────║║─║║───║║───║╔═╝║║║║║╔═╝╚═╗║
║╚═╗║╚╝║║║────╔╝║║║║║─╔╝╚╗║╚═╝║║║║║──║║─────║╚╗║╚═╗╔╝║───║╚═╗║╚╝║║╚═╗╔═╝║
╚══╝╚══╝╚╝────╚═╝╚╝╚╝─╚══╝╚═══╝╚╝╚╝──╚╝─────╚═╝╚══╝╚═╝───╚══╝╚══╝╚══╝╚══╝
\n\n╔╗╔╗╔╗╔════╗╔══╗╔═══╗╔╗╔╗╔══╗╔╗╔══╗╔═══╗
║║║║║║╚═╗╔═╝║╔╗║║╔═╗║║║║║╚╗╔╝║║║╔═╝║╔══╝
║║║║║║──║║──║║║║║╚═╝║║╚╝║─║║─║╚╝║──║╚══╗
║║║║║║──║║──║║║║║╔══╝╚═╗║─║║─║╔╗║──║╔══╝
║╚╝╚╝║──║║──║╚╝║║║─────║║╔╝╚╗║║║╚═╗║╚══╗
╚═╝╚═╝──╚╝──╚══╝╚╝─────╚╝╚══╝╚╝╚══╝╚═══╝
Author: https://vk.com/id520366971\n\nGitHub: https://github.com/WtoP4Ike/translatorVK\n\n""")
text1=get_msg(1)
print(text1)


if len(token)<25:
  text2=get_msg(2)
  quit(text2)
else:
  bot = Bot(token=token)
  api = API(token=token)
text3=get_msg(3)
print(text3)
def translate(text, to):
  to_translate = text
  translated = GoogleTranslator(source='auto',   target=to).translate(to_translate)
  return translated
  
@bot.on.message(text=["Команды", "команды","commands","Commands"])
async def help_handler(message: Message):
    id = message.from_id
    peer = message.peer_id

    text4=get_msg(4)
    await message.reply(text4)


@bot.on.message(text=["Переведи","переведи","Translate","translate"])
async def translatehelp_handler(message: Message,):
    users_info = await bot.api.users.get(message.from_id)
    text5=get_msg(5)
    nm=users_info[0].first_name
    answ=f"⛔ | {nm}, {text5}"
    await message.answer(answ)


@bot.on.chat_message(text=["/peer"])
async def help_handler(message: Message):
    id = message.from_id
    peer = message.peer_id
    await message.answer(f"peer_id: {peer}")


@bot.on.message(text=["Переведи <to>, <text>","переведи <to>, <text>", "translate <to>,<text>","Translate <to>,<text>","Переведи <to>","переведи <to>", "translate <to>","Translate <to>"])
async def translate_handler(message: Message,to=None,text=None):
    users_info = await bot.api.users.get(message.from_id)
    if text is None:
       text6=get_msg(6)
       await message.reply(text6)
    elif len(text)>100:
      text7=get_msg(7)
      answ=text7
      await message.reply('{0}'.format(answ))
    else:
      answ=translate(text, to)
      try:
       id = message.from_id
       peer = message.peer_id
       text8=get_msg(8)
       await api.messages.send(peer_id=log_chat, message=f"@id{id} - {answ}.", random_id=0)
       await message.reply(f'{text8} {answ}')
      except:
       text9=get_msg(9)
       nm=format(users_info[0].first_name)
       await message.answer(f"⛔ | {nm}, {text9}")

bot.run_forever()
