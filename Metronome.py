import time # for measuring time between ticks
import winsound # for playing audio


def playTick(): # first beat
    return winsound.PlaySound('Tick.wav', winsound.SND_ASYNC)

def playTock(): # subsequent beats
    return winsound.PlaySound('Tock.wav', winsound.SND_ASYNC)

def error(): # for errors
    print('Please enter an integer greater than zero.')

def function(): # main function
    while True:
        try:
            raw_bpm = input('\nHow many beats per MINUTE?: ') # ask for bpm
            bpm = 60/int(raw_bpm) # sets bpm to time interval
            if bpm < 0: # if entered anything less than zero
                error()
            elif bpm < 60/252: # if entered more than 252; sets bpm to 252
                print('Tempo too high; BPM set to 252.')
                bpm = 60/252
                break
            elif bpm > 2: # if entered less than 30; sets bpm to 30
                print('Tempo too low; BPM set to 30.')
                bpm = 2
                break
            else:
                print('BPM set to ' + raw_bpm + '.')
                break
        except ZeroDivisionError: # if entered zero
            error()
        except ValueError: # if entered anything not an integer
            error()
        except KeyboardInterrupt: # if entered Ctrl + C
            error()

    while True:
        try:
            time_sig = int(input('\nHow many beats per MEASURE?: ')) # ask for time signature
            if time_sig <= 0: # if entered anything less than or equal to zero
                error()
            else:
                print('Time signature set to ' + str(time_sig) + '/4.')
                break
        except ValueError: # if entered anything not an integer
            error()
        except KeyboardInterrupt: # if entered Ctrl + C
            error()

    while True:
        try:
            measure = int(input('\nHow many measures?: ')) # ask for measure
            if measure <= 0: # if entered anything less than or equal to zero
                error()
            else:
                print('Playing for ' + str(measure) + ' measures.')
                time.sleep(1) # so metronome doesn't start immediately
                break
        except ValueError: # if entered anything not an integer
            error()
        except KeyboardInterrupt: # if entered Ctrl + C
            error()

    while True: # play metronome
        print('\nPress Ctrl + C to restart the metronome.')
        try:
            for i in range(measure): # iterates through every measure
                n = 0 # for time signature
                for j in range(time_sig): # iterates through every beat
                    if n == 0: # first beat
                        print(n+1) # prints 1 instead of 0
                        n += 1
                        playTick()
                        time.sleep(bpm)

                    elif n < time_sig and n > 0: # middle beats
                        print(n+1) # prints 1 instead of 0
                        n += 1
                        playTock()
                        time.sleep(bpm)

                    else: # last beat
                        n = 0
        except KeyboardInterrupt: # if entered Ctrl + C
            pass

        print('')
        function()


# intro
print('This program will let you configure and play a metronome.')
time.sleep(2.25)
print('That is, a device used by musicians that marks time at a selected rate by giving a regular tick.')
time.sleep(3.75)
function()
