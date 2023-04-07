# -*- coding: utf-8 -*-

# # # # Copyright (C) 2023 Vladimir Zakharov
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
def ru_lang(ntext):
  ntext=int(ntext)
  if ntext==1:
    tr="Информация: Бот включается"
  elif ntext==2:
    tr="Инфорация: Токен не действителен. Проверьте config.py"
  elif ntext==3:
    tr="Информация: соединение установлено!"
  elif ntext==4:
    tr="Список команд: https://vk.com/@advtranslate-cmd"
  elif ntext==5:
    tr="используйте: <<Переведи (язык), (текст)>>"
  elif ntext==7 or ntext==6:
    tr="Ошибка: не указан текст или он слишком длинный"
  elif ntext==8:
    tr="✅ Перевод:"
  elif ntext==9:
    tr="произошла ошибка."
  return tr
def en_lang(ntext):
  ntext=int(ntext)
  if ntext==1:
    tr="Information: The bot is turned on"
  elif ntext==2:
    tr="Information: The token is invalid. Check it out config.py "
  elif ntext==3:
    tr="Info: connection is established!"
  elif ntext==4:
    tr="Command list: https://vk.com/@advtranslate-cmd"
  elif ntext==5:
    tr="use: <<Translate (language), (text)>>"
  elif ntext==7 or ntext==6:
    tr="Mistake: the text is not specified or it is too long"
  elif ntext==8:
    tr=" ✅ Translation:"
  elif ntext==9:
    tr="an error has occurred."
  return tr
