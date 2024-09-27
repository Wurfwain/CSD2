import simpleaudio as sa
import time

bpm = 120

print(f"Default BPM: {bpm}")

input_bpm = input("Would you like to change the BPM? yes/no: ")

if input_bpm == "yes" or input_bpm == "Yes" or input_bpm == "YES":
    bpm = input("Insert new BPM: ")

timestamps16th = [0]                                             # a 0 to start with because this is the first timestamp of the first note we'll hear.

note_dur = [0.25, 0.5, 0.25, 0.5, 0.5, 1, 1]

def durations_to_time_stamps16th(durations_list):
   
    timestamp_current = 0                                        # a variable that will later help with adding up the times to make a list of time stamps (16ths)
   
    for i in range(len(durations_list)):
        timestamp_new = durations_list.pop(0) * 4.0              # note durations x4 to change from quarter notes to 16ths.
        timestamp_current = timestamp_new + timestamp_current    # adding up the current timestamp with the new timestamp and defining this as the "new current" stamp so they keep adding up.
        timestamps16th.append(timestamp_current)                 # every updated current timestamp is added to our final list of timestamps in 16ths.
    
    return timestamps16th

durations_to_time_stamps16th(note_dur)
print(timestamps16th)

def timestamps(timestamps16ths, bpm):

    sixteenth_note_duration = 60.0 / float(bpm) / 4.0                       # the duration of 1 sixteenth is calculated, depending on the BPM

    for i in range(len(timestamps16ths)):                                   # had to work with range(len(timestamps16ths)) because just timestamps16ths gave a float error
       timestamps16ths[i] = timestamps16ths[i] * sixteenth_note_duration    # timestamps are created by multiplying timestamps16ths with the BPM-related sixteenth_note_duration

    return timestamps16ths

print(timestamps(timestamps16th, bpm))
#print(timestamps(timestamps16th, bpm))

