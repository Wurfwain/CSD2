""" 
The irregular beat generator

step 1: user input (BPM, maatsoort)
step 2: generate rhythm (note seq)
step 2.1: note dur to timestamps
step 3: transform timestamps to events
step 4: play events
step 5: store to MIDI? (user input)
step 6: store and/or loop
"""

import simpleaudio  as sa
import time
import random

# Load Samples
kick = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Kick1.wav")
snare = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Snare1.wav")
hihat = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Hihat1.wav")

# Determine BPM
bpm = 120
print("Default BPM: ", bpm)

input_bpm = input("Would you like to change the BPM? yes/no: ").lower()         #Credits voor .lower() naar Semuel Leijten.
new_bpm = False

# Checking the BPM
while new_bpm == False:
    if input_bpm == "yes" or input_bpm == "yes, please":
        bpm = float(input("Insert new BPM: "))

    if bpm < 60:
        bpm = int(bpm) + 60
        print("That might be a bit slow, we've sped it up to: ", bpm)
        break
    elif bpm > 240:
        print("That might be a bit fast. Please choose a BPM under 240.")
    else:
        new_bpm = True

# Determine time signature (give option between 5/4 (default) and 7/4)
steps = 5
pulses = [2, 3]
print("Default time signature = 5/4")
input_time_signature = input("Would you like to change this to 7/4? yes/no: ").lower()

if input_time_signature == "yes" or input_time_signature == "Yes, please":
    steps = 7
    pulses = [2, 3, 4, 5, 5]    # TODO oplossing vinden voor de tweede 5


# Generate rhythm

# Generating list of note durations
num_pulses = random.choice(pulses)
print("pulses: ",pulses)
print("num_pulses: ",num_pulses)

note_durs = []

# Generating 5/4
if steps == 5 and num_pulses == 2:
    note_durs = [2, 3]              # In case of 2 pulses
else:
    note_durs = [2, 2, 1]           # In case of 3 pulses

print("note_durs: ", note_durs)

# Random rotation
