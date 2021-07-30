from telegram.ext import Updater, MessageHandler,Filters 

def fanon(bot,update):
  chat_id=bot.message.chat_id
  path='https://1pe0fth3fkc49y78cjoiygdd-wpengine.netdna-ssl.com/wp-content/uploads/2019/05/Ceiling-fans-can-becoming-noisy-if-not-properly-installed.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the fan is on")

  from Adafruit_IO import Client
  aio = Client('ramprasad11235', 'aio_vYcJ09W0tMUHijkn3F0ubidfhQzF')
  aio.send('fan', 1)
  data = aio.receive('fan')
  print('Received value: {0}'.format(data.value))

def fanoff(bot,update):
  chat_id=bot.message.chat_id
  path='https://n3.sdlcdn.com/imgs/a/v/8/Crompton-Greaves-Amour-3-Blade-SDL965105491-1-dc2a3.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the fan is off")
  from Adafruit_IO import Client
  aio = Client('ramprasad11235', 'aio_RMUg38A4s8KN9OyxdpfbHZUGZAF7')
  aio.send('fan', 0)
  data = aio.receive('fan')
  print('Received value: {0}'.format(data.value))

def lighton(bot,update):
  chat_id=bot.message.chat_id
  path='https://cdn5.vectorstock.com/i/1000x1000/60/94/cartoon-glowing-yellow-light-bulb-vector-18016094.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the light is on")
  from Adafruit_IO import Client
  aio = Client('ramprasad11235', 'aio_RMUg38A4s8KN9OyxdpfbHZUGZAF7')
  aio.send('light', 1)
  data = aio.receive('light')
  print('Received value: {0}'.format(data.value))
 
def lightoff(bot,update):
  chat_id=bot.message.chat_id
  path='https://upload.wikimedia.org/wikipedia/commons/8/85/Light-bulb-1.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the light is off")
  from Adafruit_IO import Client
  aio = Client('ramprasad11235', 'aio_RMUg38A4s8KN9OyxdpfbHZUGZAF7')
  aio.send('light', 0)
  data = aioreceive('light')
  print('Received value: {0}'.format(data.value)) 

def rinex(bot,update):
  a=bot.message.text.lower()
  if a=="light on":
    lighton(bot,update)
  elif a=="light off":
    lightoff(bot,update)
  elif a=="fan on":
    fanon(bot,update)
  elif a=="fan off":
    fanoff(bot,update)
  else:
    bot.message.reply_text("INVALID COMMAND")  

  

BOT_TOKEN='1905722282:AAGLDrira7Jg6d_DE3ct32cLt0bVf1GQuLc'
u=Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,rinex))
u.start_polling()
u.idle()




