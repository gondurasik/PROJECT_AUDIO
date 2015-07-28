from Input_Audio import input_audio
import Translate
import pywapi

KEYS = 'погода'


def func():

    def get_position(city):
        x = 0
        pos = pywapi.get_location_ids(city)
        for i in pos:
            x += 1
            location_id = i
        result = pywapi.get_weather_from_weather_com(location_id)
        return result['current_conditions']['temperature']

    try:
        x= input() # input_audio()
    except:
        return "don't understand"

    try:
        return get_position(Translate.Goslate().translate(x, 'en'))
    except:
        return (x, 'not a city')