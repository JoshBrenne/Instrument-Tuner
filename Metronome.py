import time
import winsound


def playTick():
    Tick = 'C:/Users/Steve/Desktop/Metronome/Tick.wav'
    return winsound.PlaySound(Tick, winsound.SND_ASYNC)

def playTock():
    Tock = 'C:/Users/Steve/Desktop/Metronome/Tock.wav'
    return winsound.PlaySound(Tock, winsound.SND_ASYNC)

    
bpm = 60/int(input('How many beats per minute?: '))
time_sig = int(input('How many beats per measure?: '))
measure = int(input('How many measures?: '))


n = 0 # for time signature
for x in range(measure):
    while True:
        if n == 0:
            print(n+1)
            n += 1
            playTick()
            time.sleep(bpm)
                    
        elif n < time_sig and n > 0:
            print(n+1)
            n += 1
            playTock()
            time.sleep(bpm)

        else:
            n = 0
            x += 1
            
    if x > measure:
        break



