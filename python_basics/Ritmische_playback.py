import simpleaudio as sa
import time

plays = int(input("How many times do you want to hear the sample? "))

times = [] #een times array aanmaken waarin opgeslagen wordt wat de lengte wordt tussen elke beat. De lengte vd array wordt het aantal plays vd input hierboven.

input("Please write down below how many beats(/quarter notes) would you like to have in between the samples")

# for loop om de elementen van input hierboven toe te voegen aan de times array
for i in range(plays-1): #de lengte vd plays lijst -1 omdat je niet hoeft te vragen hoe lang het stil hoeft te zijn na de laatste noot, alleen tussen de noten.
    ele = float(input("Beats: "))
    times.append(ele)  
times.append(1.0) #een vaste tijd toegevoegd op het einde omdat de laatste sample anders wordt afgekapt.
print(times)

#bpm input omrekenen om de times input afhankelijk te kunnen maken van gegeven bpm.
bpm = int(input("What do you want to be the BPM? "))
bps = bpm/60 #bpm omrekenen naar beats per second
spb = 1/bps #bps omrekenen naar de lengte van 1 beat in secondes

#for loop voor het afspelen vd sample met de times (in sec) * het bpm omgerekend naar seconds per beat.
for i in range(plays):
    wave_obj = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Drum1.wav")
    play_obj = wave_obj.play()
    time.sleep(times[i]*spb)
