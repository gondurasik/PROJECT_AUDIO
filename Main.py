import weather_lib as lw
import time
from Input_Audio import input_audio
from Sintez_Audio import synthesize_voice
from Play import play

while True:
    synthesize_voice('Я Жду')
    play()
    x = input()              # input_audio()
    if x != 'ок':
        while x != 'ок':
            x = input()                # input_audio()
            time.sleep(0.3)

    synthesize_voice('слушаю')
    play()
    x = input()    # input_audio()
    if x == lw.KEYS:
        synthesize_voice('Город?')
        play()
        synthesize_voice(lw.func())
        play()
    synthesize_voice('конец')
    play()
