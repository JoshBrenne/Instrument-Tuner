import time # for measuring time between ticks
import winsound # for playing audio


def playTick(): # first beat
    Tick = 'C:/Users/brenj644/Desktop/Metronome/Tick.wav'
    return winsound.PlaySound(Tick, winsound.SND_ASYNC)

def playTock(): # subsequent beats
    Tock = 'C:/Users/brenj644/Desktop/Metronome/Tock.wav'
    return winsound.PlaySound(Tock, winsound.SND_ASYNC)

def error(): # for errors
    print('\nPlease enter a number greater than zero.')

def function(): # main function
    while True:
        try:
            bpm = 60/int(input('\nHow many beats per MINUTE?: ')) # ask for bpm
            if bpm < 0: # if entered anything less than zero
                error()
            elif bpm < 60/350 and bpm > 0: # if entered more than 350, as anything faster than 350 results in audio glitches
                bpm = 60/350
                break
            else:
                break
        except ZeroDivisionError: # if entered zero
            error()
        except ValueError: # if entered anything not a number
            error()

    while True:
        try:
            time_sig = int(input('\nHow many beats per MEASURE?: ')) # ask for time signature
            if time_sig <= 0: # if entered anything less than or equal to zero
                error()
            else:
                break
        except ValueError: # if entered anything not a number
            error()

    while True:
        try:
            measure = int(input('\nHow many measures?: ')) # ask for measure
            if measure <= 0: # if entered anything less than or equal to zero
                error()
            else:
                break
        except ValueError: # if entered anything not a number
            error()

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
    function()


function()
