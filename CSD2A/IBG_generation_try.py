""" 
The irregular beat generator ==== rhythm generation try

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
        bpm = abs(float(input("Insert new BPM: ")))

    if bpm < 60:
        bpm = int(bpm) + 60
        print("That might be a bit slow, we've sped it up to: ", bpm)
        break
    elif bpm > 240:
        print("That might be a bit fast. Please choose a BPM under 240.")
    else:
        new_bpm = True
        print("You've set the BPM to: ", int(bpm))
    

# Determine time signature (give option between 5/4 (default) and 7/4)
steps = 5*2
print("Default time signature = 5/4")
input_time_signature = input("Would you like to change this to 7/4? yes/no: ").lower()

if input_time_signature == "yes" or input_time_signature == "Yes, please":
    steps = 7*2

pulses = random.randint(2, steps)


# Generate rhythm

# Make a sequence
def gen_seq(steps, pulses):
    min_note_length = int(steps/pulses)
    seq = []

    for i in range(pulses):
        seq.append(min_note_length)
    
    rest = steps - (pulses * min_note_length)

    # Add the rest values to the list of minimun note lengths
    for i in range(rest):
        seq[i] += 1
    
    # Shuffle the seq randomly, which is (in a way) rotating
    random.shuffle(seq)
    
    return seq

# Make 3 different sequences for the 3 instruments
for i in range(3):
    pulses = random.randint(2, steps)
    print(gen_seq(steps, pulses))

