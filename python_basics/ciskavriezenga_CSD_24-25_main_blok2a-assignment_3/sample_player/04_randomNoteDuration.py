"""
An example project in which three .wav files are played after the other with a
break in between of a random note duration.
Used note durations are: sixteenth, eight, quarter notes

------ EXERCISES ------
- Answer the following questions before running the code:
  - How many different samples will be played?                                        3
  - How many times a sample will be played?                                           4
  - How many seconds will there be in between the playback of samples? (3 answers)    Random 16th 8th or quarter note in a 120 bpm (= 0.125, 0.25 or 0.5 secs)
  Check your answers by running the code.

- Alter the code:
  Write a function which returns a list with time intervals based on two
  arguments:
  - the bpm
  - a list of note durations
  Use this function.
"""

import simpleaudio as sa
import time
import random

#load audio files into a list
samples = [sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Pop.wav"),
              sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Laser1.wav"),
              sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Dog2.wav")]

# create a list with possible note durations: sixteenth, eighth and a quarter note
noteDurations = [0.25, 0.5, 1]
bpm = 120
# create a list to hold timeIntervals
timeIntervals = []





def get_intervals(bpm, noteDur):
  # transform noteDurations into timeIntervals, depending on bpm
  # calculate quarterNote in seconds (duration of a quarter note)
  quarterNote = 60.0 / bpm
  
  for noteDuration in noteDur:
    # calculate timeDuration and add to the list
    timeIntervals.append(quarterNote * noteDuration)
  
    # display timeIntervals
    #print("Selection of time intervals: ", timeIntervals )


  #print("waiting: " + str(timeInterval) + " seconds.")
  return timeIntervals

print(f"Available intervals: {get_intervals(bpm, noteDurations)}")


# a function that plays a list of samples with random timeIntervals in between,
# based on the values in the passed in interval list.
def playSamples(samplae, intervals):
  # play samples and wait in between (random duration)
  for sample in samplae:
    sample.play()
    # retrieve a random timeInterval
    # use the random.choice function -> returns a random element from a sequence
    timeInterval = random.choice(intervals)
    print("waiting: " + str(timeInterval) + " seconds.")
    #print(get_intervals(bpm, timeIntervals))
    time.sleep(timeInterval)

# call the playSamples function 4 times
for i in range(4):
  playSamples(samples, timeIntervals)


