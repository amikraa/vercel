# Youtube-Downloader-Bot 
## Об проекте
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yt_dlp)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiogram)



A simple bot that download videos from YouTube

## Installation (GNU/Linux)

```bash
git clone https://github.com/ZeroNiki/Youtube-Downloader-Bot.git 
```

Go to the Youtube-Downloader-Bot folder and create a virtual environment:

```bash
cd Youtube-Downloader-Bot
python3 -m venv venv && source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

First, get your bot token from @botfather. Then create a config.py file, and in it the TOKEN variable and insert your bot’s token (in quotes):

```python
TOKEN = 'Your bot token'
```

Run main.py

------

### Внимание!
**!Бот устанавливает файлы в директорию video и mp3**

Создайте папку mp3, jpg и video

***Папки автомотически очищаются после отправки файла*** 

----
### Планы на проект
 - ~~Отправка файла пользователю~~
- ~~Convert to audio~~
- ~~Inline buttonи~~

Recently added:
- Ability to choose quality
- Очистка дерикторий jpg, mp3, video


