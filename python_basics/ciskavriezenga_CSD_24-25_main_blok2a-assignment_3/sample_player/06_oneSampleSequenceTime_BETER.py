"""
An example project in which a rhythmical sequence is played, using one
audio file.
  - Sixteenth note is the smallest used note duration.
  - One bar, time signature: 3 / 4

Instead of using steps to iterate through a sequence, we are checking the time.
We will trigger events based on a timestamp.

------ EXERCISES ------
- Run the code, read the code and answer the following question:
  - This script transforms a list of 'sixteenth notes timestamps' into a list of
    regular timestamps.
    In the playback loop, the time difference (currentTime minus startTime)
    is compared to the upcomming timestamp.
    Why is this a more accurate method then the methods used in the examples
    "04_randomNoteDuration.py" and "05_oneSampleSequenceSteps.py"?
    Notate your answer below this line (Dutch is allowed)!

- Alter the code:
  Currently one sample is played. Add another sample to the script.
  When a sample needs to be played, choose one of the two samples
  randomly.
  (See the hint about the 'random' package in script "02_timedPlayback".)

- Alter the code:
  Currently the sequence is only played once.
  Alter the code to play it multiple times.
  hint: The timestamps list is emptied using the pop() function.
  (multiple possible solutions)

"""

import simpleaudio as sa
import time
import random


# load 1 audioFile and store it into a list
# note: using a list taking the next step into account: using multiple samples
samples = [sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Pop.wav"), 
           sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Dog2.wav")]

bpm = 120
quarterNoteDuration = 60 / bpm
# calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0

# create a list to hold the timestamps
timestamps = []

# create a list with 'note timestamps' specified as 16th notes, indicating
# the time at which the sample must be played
timestamps16th = [0, 2, 4, 8, 11]

# transform the sixteenthTimestamps to a timestamps list with time values
for timestamp in timestamps16th:
  timestamps.append(timestamp * sixteenthNoteDuration)



# fill in the number of wanted loop repeats:
repeats = 3

for repeat in range(repeats):
  # retrieve the first timestamp
  # NOTE: pop(0) returns and removes the element at index 0
  timestamp = timestamps.pop(0)

  # retrieve the startime: current time     (moet in for loop anders wordt er niet vanaf het begin weer gerekend steeds)
  startTime = time.time()

  # play the sequence
  while True:
    # retrieve current time
    currentTime = time.time()

    # check whether the current time is beyond the timestamp's time,
    # meaning it is time to play the sample
    if(currentTime - startTime >= timestamp):
      samples[random.randint(0, 1)].play()
      #samples[0].play()     # Even aangemaakt om het met 1 geluid te checken.
      #print("sample")       # Aangemaakt om visueel te krijgen wanneer er een sample heeft geklonken en dit terug te kunnen kijken.

      # if there are timestamps left in the timestamps list
      if timestamps:

        print(f"current timestamp: {timestamp}")

        # retrieve the next timestamp
        timestamp = timestamps.pop(0)

        #print(f"new: {new16th}")                         # een boel prints om overzichtelijk te krijgen wat er nu eigenlijk gebeurde.
        #print(f"Timestamps16th: {timestamps16th}")
        #print(f"Timestamps list: {timestamps}")

      else:

        # refill list
        #timestamps.extend(timestamps16th * sixteenthNoteDuration)
        for timestamp in timestamps16th:
          timestamps.append(timestamp * sixteenthNoteDuration)

        # print(timestamps)
        # stop the loop
        break

    else:
      # short wait to prevent we'll keep the processor busy when there's
      # nothing to do
      time.sleep(0.001)




time.sleep(1) # let the last 'note' ring out

