#event_based_sequencer
#een rommelige semi code waarin ik veel heb gestruggled en uiteindelijk de code
#van Semuel heb gebruikt om te proberen het te begrijpen.
import simpleaudio  as sa
import time

# Load Samples
kick = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Kick1.wav")
snare = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Snare1.wav")
hihat = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Hihat1.wav")

# Determine BPM
bpm = 120
print("Default BPM: ", bpm)

input_bpm = input("Would you like to change the BPM? yes/no: ")

if input_bpm == "yes" or input_bpm == "Yes" or input_bpm == "YES" or input_bpm == "Yes, please":
    bpm = input("Insert new BPM: ")




timestamps16th = [0]                                             # a 0 to start with because this is the first timestamp of the first note we'll hear.

note_dur_kick = [1, 1, 1, 1, 1, 1, 1, 1]
note_dur_snare = [1, 2, 2, 2]
note_dur_hh = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# Note durations to 16th notes, depending on BPM
def durations_to_time_stamps16th(durations_list):
   
    timestamp_current = 0                                        # a variable that will later help with adding up the times to make a list of time stamps (16ths)
   
    for note_dur in range(len(durations_list)):
        timestamp_new = durations_list.pop(0) * 4.0              # note durations x4 to change from quarter notes to 16ths.
        timestamp_current = timestamp_new + timestamp_current    # adding up the current timestamp with the new timestamp and defining this as the "new current" stamp so they keep adding up.
        timestamps16th.append(timestamp_current)                 # every updated current timestamp is added to our final list of timestamps in 16ths.
    
    return timestamps16th


# DIT KAN EFFICIENTER?
# Function per instrument
durs_kick = durations_to_time_stamps16th(note_dur_kick)
print("durs kick: ", durs_kick)

# Emptying the timestamps16th list before re-using the function:
timestamps16th = [0] 

durs_snare = durations_to_time_stamps16th(note_dur_snare)
print("durs snare: ", durs_snare)

timestamps16th = [0] 

durs_hh = durations_to_time_stamps16th(note_dur_hh)
print("durs hi-hat: ", durs_hh)

timestamps16th = [0] 

# Note duration to timestamps
def timestamps(timestamps16ths, bpm):

    sixteenth_note_duration = 60.0 / float(bpm) / 4.0                       # the duration of 1 sixteenth is calculated, depending on the BPM

    for i in range(len(timestamps16ths)):                                   # had to work with range(len(timestamps16ths)) because just timestamps16ths gave a float error
       timestamps16ths[i] = timestamps16ths[i] * sixteenth_note_duration    # timestamps are created by multiplying timestamps16ths with the BPM-related sixteenth_note_duration

    return timestamps16ths

stamps_kick = timestamps(durs_kick, bpm)
stamps_snare = timestamps(durs_snare, bpm)
stamps_hh = timestamps(durs_hh, bpm)

#print(timestamps(durs_kick, bpm))
#print(timestamps(durs_snare, bpm))
#print(timestamps(durs_hh, bpm))

# Make events (bron: Semuel)
def make_events(timestamps, instrument):
    events = []
    for i in timestamps:
        new_event = {
            'timestamp': i,
            'instrument': instrument
        }
        events.append(new_event)

    return events
    
#print(make_events(stamps_snare, snare))

# (bron: Semuel)
def get_timestamps(event):
    return event['timestamp']

# Sort events (bron: Semuel)
events = make_events(stamps_kick, kick) + make_events(stamps_snare, snare) + make_events(stamps_hh, hihat)
events.sort(key=get_timestamps)

#print(events)


######### Play according to timestamps

start_time = time.time()


# uit eventlist de timestamps lezen en vergelijken met de tijd nu

#for event in events:

#print("Full events: ", events)
#print(events[5]['timestamp'])

# Function to play (bron: Semuel)
def handle_event (event):
    #print("play!!")
    event['instrument'].play()




# Tijd aflezen en vergelijken met timestamps (bron: wederom Semuel)
while events:
    current_time = time.time()
    current_timestamp = events[0]['timestamp']

    if(current_time - start_time >= current_timestamp):
        simultaneous_events = []

        while events and events[0]['timestamp'] == current_timestamp:
            simultaneous_events.append(events.pop(0))
        for event in simultaneous_events:
            #print()
            handle_event(event)
        
    else:  
        time.sleep(0.001)



time.sleep(1)   # for the last note to 'ring out'