import simpleaudio as sa
import time
# simpleaudio is nodig om de sample af te kunnen spelen.
# time is nodig om verderop (in de for loop) met time.sleep de code even te laten stilstaan.

plays = int(input("How many times do you want to hear the sample? "))
# De gebruiker vragen hoevaak de sample moet spelen.


for i in range(plays):
    wave_obj = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Drum1.wav")
    play_obj = wave_obj.play()
    time.sleep(0.2)
# for loop om het object een (plays)aantal keer af te spelen, met een tijd ertussen van 0.2 sec.

# play_obj.wait_done() De code werkt ook zonder deze line. Kan ik die weglaten?