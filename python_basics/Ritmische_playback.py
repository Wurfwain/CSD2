import simpleaudio as sa
import time

plays = int(input("How many times do you want to hear the sample? "))

times = []
input("Please write down below how many beats would you like to have in between the samples")

# iterating till the range
for i in range(plays):
    ele = float(input("Beats: "))
    # adding the element
    times.append(ele)  
 
# print(times)

#bpm = int(input("What do you want to be the BPM? "))

for i in range(plays):
    wave_obj = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Drum1.wav")
    play_obj = wave_obj.play()
    time.sleep(times[i])
    #time.sleep(times)



    # Tijd omzetten in beats mbv BPM.
    # len(times) is de lengte van een lijst
    # times.insert(...) om iets toe te voegen aan de lijst times.