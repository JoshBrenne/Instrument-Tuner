import time # for measuring time between ticks
import winsound # for playing audio


def playTick(): # first beat
    return winsound.PlaySound('Tick.wav', winsound.SND_ASYNC)

def playTock(): # subsequent beats
    return winsound.PlaySound('Tock.wav', winsound.SND_ASYNC)

def error(): # for errors
    print('\nPlease enter a WHOLE NUMBER greater than zero.')

def function(): # main function
    while True:
        try:
            bpm = 60/int(input('\nHow many beats per MINUTE?: ')) # ask for bpm
            if bpm < 0: # if entered anything less than zero
                error()
            elif bpm < 60/300 and bpm > 0: # if entered more than 300; sets bpm to 300
                bpm = 60/300
                break
            else:
                break
        except ZeroDivisionError: # if entered zero
            error()
        except ValueError: # if entered anything not an integer
            error()
        except EOFError: # if entered Ctrl + C
            print('')
            error()

    while True:
        try:
            time_sig = int(input('\nHow many beats per MEASURE?: ')) # ask for time signature
            if time_sig <= 0: # if entered anything less than or equal to zero
                error()
            else:
                break
        except ValueError: # if entered anything not an integer
            error()
        except EOFError: # if entered Ctrl + C
            print('')
            error()

    while True:
        try:
            measure = int(input('\nHow many measures?: ')) # ask for measure
            if measure <= 0: # if entered anything less than or equal to zero
                error()
            else:
                break
        except ValueError: # if entered anything not an integer
            error()
        except EOFError: # if entered Ctrl + C
            print('')
            error()

    while True: # play metronome
        print('\nPress Ctrl + C to restart the metronome.')
        try:
            for i in range(measure): # iterates through every measure
                n = 0 # for time signature
                x = 0 # for measure
                for j in range(time_sig): # iterates through every beat
                    if x <= measure:
                        if n == 0: # first beat
                            print(n+1) # prints 1 instead of 0
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
        except KeyboardInterrupt:
            break

        print('')
        function()


function()
