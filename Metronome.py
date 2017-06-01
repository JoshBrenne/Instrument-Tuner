import time
import winsound


def playTick(): # first beat
    Tick = 'C:/Users/brenj644/Desktop/Metronome/Tick.wav'
    return winsound.PlaySound(Tick, winsound.SND_ASYNC)

def playTock(): # subsequent beats
    Tock = 'C:/Users/brenj644/Desktop/Metronome/Tock.wav'
    return winsound.PlaySound(Tock, winsound.SND_ASYNC)

def Function():
    while True:
        try:
            bpm = 60/int(input('How many beats per minute?: ')) # ask for bpm
            break
        except ZeroDivisionError: # if entered 0
            print('\nPlease enter a whole number')
        except ValueError: # if entered anything not a number
            print('\nPlease enter a whole number')

    while True:
        try:
            time_sig = int(input('\nHow many beats per measure?: ')) # ask for time signature
            break
        except ValueError: # if entered anything not a number
            print('\nPlease enter a whole number')
        except time_sig <= 0: # if entered 0
            print('\nPlease enter a whole number')

    while True:
        try:
            measure = int(input('\nHow many measures?: ')) # ask for measure
            break
        except ValueError: # if entered anything not a number
            print('\nPlease enter a whole number')
        except measure <= 0: # if entered 0
            print('\nPlease enter a whole number')

    for i in range(measure): # play the metronome
        n = 0 # for time signature
        x = 0 # for measure
        for j in range(time_sig):
            if x <= measure:
                if n == 0: # first beat
                    print(n+1)
                    n += 1
                    playTick()
                    time.sleep(bpm)

                elif n < time_sig and n > 0: # middle beats
                    print(n+1)
                    n += 1
                    playTock()
                    time.sleep(bpm)

                else: # last beat
                    x += 1
                    n = 0
    print(' ')
    Function()

Function()
