"""
An example project in which three wav files are played after the other with a
pause in between.

------ EXERCISES ------
- Alter the code:
  Write a function that plays the samples a given number of times.
  Call this function.

- Alter the code:
  Change the time in between samples into a random value.
  E.g. wait 0.25, 0.5, or 1 second.
  hint:  there is a standard 'random' package available with a 'random' function
         https://docs.python.org/2/library/random.html
         A standard package does not need to be installed with pip, but it does
         need to be imported when you want to use it.
"""

import simpleaudio as sa
import time
import random

# load audio files into a list
samples = [ sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Pop.wav"),
            sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Laser1.wav"),
            sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Dog2.wav")]


num_plays = 3
# Lijst aanmaken waar de randomfunctie daaronder uit kan kiezen.
seq = [0, 0.25, 0.5, 0.75, 1]
num_random = random.choice(seq)

def lets_play():
  # play samples, wait 1 second in between
  for sample in samples:
    for plays in range(num_plays):
      print(sample) # display the sample object
      sample_play = sample.play() # play sample
      sample_play.wait_done()
      time.sleep(num_random) # wait random amount of time
    time.sleep(num_random)



lets_play()
print("sleep time = ", num_random)


#Geprobeerd met een for loop in een for loop elke sample een eigen aantal keer af te laten spelen met iedere keer een nieuwe random time.sleep. Nog niet gelukt, waarom niet?
