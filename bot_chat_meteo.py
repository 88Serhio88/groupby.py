#goodbot, langoodpybot name

import telebot
import pyowm
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM("47fb6ff2341bc02a35a987807ce9cba1", config_dict)


bot = telebot.TeleBot("6053554060:AAG7I4GA6NFekESWxMjQcBykYtPscHtTV8c") # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def send_echo(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather

	temp = w.temperature('celsius') ['temp']
	weather = mgr.weather_at_place(message.text).weather
	 

	answer = ("В городе " + message.text + "  сейчас " + str (temp))
	answer += str(w)

	
	if temp < 10:
		answer +=  " Сейчас холодно, оденься потеплее"
	elif temp < 20:
		answer +=  " Сейчас нормальная погода, одевай шарф"
	else:
		answer +=  " Отличная погода, одевай, что хочешь!"


	

	bot.send_message(message.chat.id, answer)
bot.infinity_polling(none_stop = True)
