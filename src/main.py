import yt_dlp as ytd
import requests
from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from config import TOKEN

import os, shutil

bot = Bot(TOKEN)
dp = Dispatcher(bot)
"""Start"""


@dp.message_handler(commands='start')
async def hello(message: types.Message):
  # eRegular button
  start_button = ['download?']
  keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
  keyboards.add(*start_button)

  # Inline button
  link_buttons = [
      InlineKeyboardButton(
          text='Youtube',
          url='https://youtube.com/@zairavfx?si=QXP8wOEA4RoxLPVh')
  ]
  link_keyboards = InlineKeyboardMarkup(row_width=1)
  link_keyboards.add(*link_buttons)

  await message.answer("↓↓↓Subscribe to my Youtube↓↓↓",
                       reply_markup=link_keyboards)
  await message.answer("This bot download video from youtube",
                       reply_markup=keyboards)


"""Selectiob of Quality"""


@dp.callback_query_handler(text='download_mp4')
async def question(call: types.CallbackQuery):
  link_buttons = [
      InlineKeyboardButton(text='360p', callback_data='360p'),
      InlineKeyboardButton(text='720p', callback_data='720p'),
      InlineKeyboardButton(text='1080p', callback_data='1080p'),
  ]
  link_keyboards = InlineKeyboardMarkup(row_width=1)
  link_keyboards.add(*link_buttons)

  await call.message.answer('select your quality', reply_markup=link_keyboards)


"""Inline button format .mp4 (360p)"""


@dp.callback_query_handler(text='360p')
async def inline_keyboard_mp4_360(call: types.CallbackQuery):
  await call.message.answer("please wait...")

  options = {
      'skip-download': True,
      'format_sort': ['res:360', 'ext:mp4:m4a'],
      'outtmpl': 'video/%(title)s.%(ext)s'
  }

  with ytd.YoutubeDL(options) as ytdl:
    ytdl.download([link])
    result = ytdl.extract_info("{}".format(link))
    title = ytdl.prepare_filename(result)
    video = open(f'{title}', 'rb')

    await call.message.answer_video(video=video)

    folder = 'video/'

    for filename in os.listdir(folder):
      file_path = os.path.join(folder, filename)
      try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
          os.unlink(file_path)
        elif os.path.isdir(file_path):
          shutil.rmtree(file_path)

      except Exception as e:
        print('Error %s. Reason: %s' % (file_path, e))


"""Inline button format .mp4 (720p)"""


@dp.callback_query_handler(text='720p')
async def inline_keyboard_mp4_720(call: types.CallbackQuery):
  await call.message.answer("please wait...")
  options = {
      'skip-download': True,
      'format_sort': ['res:720', 'ext:mp4:m4a'],
      'outtmpl': 'video/%(title)s.%(ext)s'
  }

  with ytd.YoutubeDL(options) as ytdl:
    ytdl.download([link])
    result = ytdl.extract_info("{}".format(link))
    title = ytdl.prepare_filename(result)
    video = open(f'{title}', 'rb')

    await call.message.answer_video(video=video)

    folder = 'video/'

    for filename in os.listdir(folder):
      file_path = os.path.join(folder, filename)
      try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
          os.unlink(file_path)
        elif os.path.isdir(file_path):
          shutil.rmtree(file_path)

      except Exception as e:
        print('Error %s. Reason: %s' % (file_path, e))


"""Inline button format .mp4 (1080p)"""


@dp.callback_query_handler(text='1080p')
async def inline_keyboard_mp4_1080(call: types.CallbackQuery):
  await call.message.answer("please wait...")

  options = {
      'skip-download': True,
      'format_sort': ['res:1080', 'ext:mp4:m4a'],
      'outtmpl': 'video/%(title)s.%(ext)s'
  }

  with ytd.YoutubeDL(options) as ytdl:
    ytdl.download([link])
    result = ytdl.extract_info("{}".format(link))
    title = ytdl.prepare_filename(result)
    video = open(f'{title}', 'rb')

    await call.message.answer_video(video=video)

    folder = 'video/'

    for filename in os.listdir(folder):
      file_path = os.path.join(folder, filename)
      try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
          os.unlink(file_path)
        elif os.path.isdir(file_path):
          shutil.rmtree(file_path)

      except Exception as e:
        print('Error %s. Reason: %s' % (file_path, e))


"""Inline button format .mp3"""


@dp.callback_query_handler(text='download_mp3')
async def inline_keyboard_mp3(call: types.CallbackQuery):
  await call.message.answer("please wait...")

  options = {
      'skip-download':
      True,
      'format':
      'bestaudio/best',
      'outtmpl':
      'mp3/%(title)s.%(ext)s',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
  }

  with ytd.YoutubeDL(options) as ytdl:
    ytdl.download([link])
    result = ytdl.extract_info("{}".format(link))
    title = ytdl.prepare_filename(result)[:-5]
    audio = open(f'{title}.mp3', 'rb')

    await call.message.answer_audio(audio=audio)

  folder = 'mp3/'

  for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
      if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
      elif os.path.isdir(file_path):
        shutil.rmtree(file_path)

    except Exception as e:
      print('Error %s. Reason: %s' % (file_path, e))


"""Setting the image"""


@dp.callback_query_handler(text='download_jpg')
async def inline_keyboard_jpg(call: types.CallbackQuery):
  await call.message.answer("please wait...")

  with ytd.YoutubeDL({}) as ytdl:
    info_dict = ytdl.extract_info(link, download=False)
    get_id = info_dict.get('id', None)

  thumbnail = f'https://img.youtube.com/vi/{get_id}/maxresdefault.jpg'
  r = requests.get(thumbnail)

  if r.status_code == 200:
    with open(f"jpg/{get_id}.jpg", "wb") as file:
      file.write(r.content)

  with open(f"jpg/{get_id}.jpg", "rb") as f:
    content = f.read()
    await call.message.answer_photo(photo=content)

  folder = 'jpg/'

  for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
      if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
      elif os.path.isdir(file_path):
        shutil.rmtree(file_path)

    except Exception as e:
      print('Error %s. Reason: %s' % (file_path, e))


"""download?"""


@dp.message_handler(Text(equals='download?'))
async def start_dw(message: types.Message):
  await message.reply('Post the link!')


@dp.message_handler(content_types='text')
async def downloading(message: types.Message):
  global link
  link = message.text
  keyboard = InlineKeyboardMarkup()

  keyboard.add(
      InlineKeyboardButton(text='.mp4', callback_data='download_mp4'),
      InlineKeyboardButton(text='.mp3', callback_data='download_mp3'),
      InlineKeyboardButton(text='outlook', callback_data='download_jpg'))

  await message.answer(message.text, reply_markup=keyboard)
  await message.delete()


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
