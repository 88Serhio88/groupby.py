
import pyowm
from pyowm.utils.config import g

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM("47fb6ff2341bc02a35a987807ce9cba1", config_dict)

place = input ("В каком городе/стране?")

mgr = owm.weather_manager()

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius') ['temp'] #[]- добавление в словарь

weather = mgr.weather_at_place(place).weather
temp_dict_celsius = weather.temperature('celsius')

print ("В городе " + place + " сейчас " + str (temp) )
print (w)

if temp < 10:
	print ("Сейчас холодно, оденься потеплее")
elif temp < 20:
	print ("Сейчас нормальная погода, одевай шарф")
else:
	print ("Отличная погода, одевай, что хочешь!")

input ()