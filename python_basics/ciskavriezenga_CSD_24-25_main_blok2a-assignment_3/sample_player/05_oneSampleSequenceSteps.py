"""
An example project in which a sequence of one bar is played, using only one audio file.
  - One bar, time signature: 3 / 4
  - 3 * 4 sixteenth notes per bar = 12 'steps'.
    Steps correspond with equally spaced 16th notes. This defines the grid, or
    the highest time resolution we will use.

------ EXERCISES ------
- Run the code, read the code and answer the following question:
  This script does not use a list with time intervals, but does play a
  rhythm. Explain how this works.

Het systeem werkt met berekende stapjes van een 16e slaap (afhankelijk vh bpm). Dit wordt in sec berekend zodat
de sleep weet hoelang een 16e duurt en dus hoe lang er gewacht moet worden met een volgende stap.
De stap die wordt gezet wordt vergeleken met het vooraf geschreven ritme (vastgelegd in een list, sequence)
en als is besloten dat op die stap een geluid moet klinken dan komt er een true uit de vergelijking (het if-statement)
en wordt duidelijk dat er een geluid moet klinken. Deze info verdwijnt uit de lijst(/sequence) en het eerste
element uit die lijst kan weer vergeleken worden met de stappen die worden doorlopen totdat er weer een match is
en er weer een sample klinkt.

- Alter the code:
  Fix the bug that occurs: "IndexError: pop from empty list"
Ik heb een getal toegevoegd aan het einde van de sequence lijst omdat er niet gepopt kan worden uit een lijst die daarna leeg is...?
"""

import simpleaudio as sa
import time
import random

# load an audio file and store it into a list
# note: using a list is a preparation for the next assignment in which we
# will use multiple audio files
samples = [sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Pop.wav")]

bpm = 120
# calculate quarterNote with bpm
quarterNote = 60 / bpm

# number of quarterNotes per bar (time signature: 3 / 4 = 3 quarterNotes per bar)
quarterNotesPerBar = 3

# number of steps per quarterNote (4 steps per quarterNote -> using sixteenth notes)
stepsPerQuarterNote = 4

# calculate stepDuration
stepDuration = quarterNote / stepsPerQuarterNote

# calculate the number of steps (16th notes) in a bar
stepsPerBar = stepsPerQuarterNote * quarterNotesPerBar

# create a list with a rhythm: the steps at which the sample will be played
# Remember we have a maximum of 12 steps in a bar.
sequence = [0, 2, 4, 8, 11, 0]

# retrieve first step of the bar
# NOTE: pop(0) returns the element at index 0 and removes it from the list
step = sequence.pop(0)


# play the sequence
for currentStep in range(int(stepsPerBar)):
  print("Current step: ", currentStep)
  if(currentStep == step):
    samples[0].play()
    print(f"step: {step}")
    # retrieve the next step at which we need to play a sample
    step = sequence.pop(0)
    print(f"step: {step}")

  time.sleep(stepDuration)

