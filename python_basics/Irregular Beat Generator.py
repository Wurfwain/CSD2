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
# ======== PREPARATION ========
import simpleaudio  as sa
import time
import random

# Load Samples
kick = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Kick1.wav")
snare = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Snare1.wav")
hihat = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Hihat1.wav")

# ======== USER INPUT ========
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
        print("That might be a bit fast. Please choose a BPM under 241.")
    else:
        new_bpm = True
        print("You've set the BPM to: ", int(bpm))
    

# Determine time signature (give option between 5/4 (default) and 7/4)
steps = 5*2
print("Default time signature = 5/4")
input_time_signature = input("Would you like to change this to 7/4? yes/no: ").lower()

if input_time_signature == "yes" or input_time_signature == "Yes, please":
    steps = 7*2

# Asking for repeats
repeats = 4
print("The default amount of rhythm repeats is: ", repeats)
input_repeats = input("Would you like to change the amount of rhythm repeats? yes/no: ").lower()
new_repeats = False

while new_repeats == False:

    if input_repeats == "yes" or input_repeats == "yes, please":
        repeats = int(input("How many times would you like to hear the rhythm? "))

        if repeats < 1 or repeats > 8:
            print("Can't do that, sorry. Please choose a number between 1 - 8")
        else:
            new_repeats = True
    else:
        new_repeats = True

print(repeats)

# ======== GENERATE RHYTHM ========

# Make a sequence
def gen_seq(max_steps):
    pulses = random.randint(2, max_steps)
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
note_dur_kick = gen_seq(int(steps/2))       # /2 to make the kick and snare appair less often than the hh
note_dur_snare = gen_seq(int(steps/2))
note_dur_hh = gen_seq(steps)

print("kick durs: ", note_dur_kick)
print("snare durs: ", note_dur_snare)
print("hh durs: ", note_dur_hh)



# Note durations to time stamps, depending on BPM
def durations_to_time_stamps8th(durations_list):
   # Change quarter note_durs to 8ths
    timestamps8th = []                                          # a 0 to start with because this is the first timestamp of the first note we'll hear.
    timestamp_current = 0                                        # a variable that will later help with adding up the times to make a list of time stamps (8ths)

    for note_dur in range(len(durations_list)):
        timestamp_new = durations_list.pop(0)
        timestamp_current = timestamp_new + timestamp_current    # adding up the current timestamp with the new timestamp and defining this as the "new current" stamp so they keep adding up.
        timestamps8th.append(timestamp_current)                  # every updated current timestamp is added to our final list of timestamps in 16ths.
   
    eighth_note_duration = (60.0 / float(bpm)) / 2.0               # the duration of 1 8th is calculated, depending on the BPM

    for i in range(len(timestamps8th)):                              # had to work with range(len(timestamps16ths)) because just timestamps16ths gave a float error
       timestamps8th[i] = timestamps8th[i] * eighth_note_duration    # timestamps are created by multiplying timestamps16ths with the BPM-related sixteenth_note_duration

    return timestamps8th


# KAN OPTIMALER?
# Function per instrument
ts_kick = durations_to_time_stamps8th(note_dur_kick)
print("ts kick: ", ts_kick)

# Emptying the timestamps16th list before re-using the function:
timestamps8th = [0] 

ts_snare = durations_to_time_stamps8th(note_dur_snare)
print("ts snare: ", ts_snare)

timestamps8th = [0] 

ts_hh = durations_to_time_stamps8th(note_dur_hh)
print("ts hi-hat: ", ts_hh)

timestamps8th = [0]

# HIER NOG MIDI INFO AAN TOEVOEGEN
# Make events (bron: Semuel: multi_sample_sequencer.py)
def make_events(timestamps, instrument):
    events = []
    for i in timestamps:
        new_event = {
            'timestamp': i,
            'instrument': instrument
        }
        events.append(new_event)

    return events


# (bron: Semuel: multi_sample_sequencer.py and Ciska: 4d_dictionary_sorting_function.py)
def get_timestamps(event):
    return event['timestamp']

# Sort events (bron: Semuel: multi_sample_sequencer.py and Ciska: 4d_dictionary_sorting_function.py)
events = make_events(ts_kick, kick) + make_events(ts_snare, snare) + make_events(ts_hh, hihat)
events.sort(key=get_timestamps)
print(events)

######### Play according to timestamps
start_time = time.time()

# Function to play (bron: Semuel: multi_sample_sequencer.py and Ciska: 4d_dictionary_sorting_function.py)
def handle_event (event):
    #print("play!!")
    event['instrument'].play()



# List to temporarily store events
temp_events = []

for i in range(repeats):
    temp_events.extend(events)

    passed_time = 0

    if i != 0:
        passed_time = (steps/(bpm*(1/30)))           # bpm afhankelijk

    for event in temp_events:
        event['timestamp'] = event['timestamp']  + passed_time
    
    #print("Passed time: ", passed_time)

    print(i, steps, temp_events)

    
    # Tijd aflezen en vergelijken met timestamps (bron: wederom deels Semuel: multi_sample_sequencer.py and Ciska: 4d_dictionary_sorting_function.py)
    while temp_events:
        current_time = time.time()
        current_timestamp = temp_events[0]['timestamp']
        #print(current_timestamp)

        if(current_time - start_time >= current_timestamp):
            simultaneous_events = []

            while temp_events and temp_events[0]['timestamp'] == current_timestamp:
                simultaneous_events.append(temp_events.pop(0))
                #print(simultaneous_events)
            for event in simultaneous_events:
                handle_event(event)
            
        else:  
            time.sleep(0.001)
    





time.sleep(1)   # for the last note to 'ring out'