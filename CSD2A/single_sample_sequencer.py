import simpleaudio as sa
import time

samples = [sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Pop.wav"), 
           sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Dog2.wav")]

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

    sixteenth_note_duration = 60.0 / float(bpm) / 4.0                       # The duration of 1 sixteenth is calculated, depending on the BPM

    for i in range(len(timestamps16ths)):                                   # Had to work with range(len(timestamps16ths)) because just timestamps16ths gave a float error
       timestamps16ths[i] = timestamps16ths[i] * sixteenth_note_duration    # Timestamps are created by multiplying timestamps16ths with the BPM-related sixteenth_note_duration

    return timestamps16ths

stamps_for_loop = timestamps(timestamps16th, bpm)                 # Call the function timestamps to receive the correct times
timestamps = []                                                   # An extra list from which we can pop
timestamps.extend(stamps_for_loop)                                # First time we fill it up with the source stamps_for_loop. In case of looping, there'll be a refill.


# fill in the number of wanted loop repeats:
repeats = 3


for repeat in range(repeats):                             # repeat the sequence
  
  #print(f"timestamps: {timestamps}")                     # Some prints for 
  #print(f"stamps_for_loop: {stamps_for_loop}")           # trouble shooting
  
  timestamp = timestamps.pop(0)                           # Grab first stamp from the list

  # retrieve the startime: current time (moet in for loop anders wordt er niet vanaf het begin weer gerekend steeds)
  startTime = time.time()


  while True:                                             # play the sequence
    currentTime = time.time()

    if(currentTime - startTime >= timestamp):             # compare current time with startTime and the timestamp,
      samples[0].play()                                   # to check whether it is time to play the sample

      if timestamps:                                      # if there are timestamps left in the timestamps list

        print(f"current timestamp: {timestamp}")
        timestamp = timestamps.pop(0)                     # Grab next timestamp

        #print(f"new: {new16th}")                         # Once again a lot of prints
        #print(f"Timestamps16th: {timestamps16th}")       # to check what was actually
        #print(f"Timestamps list: {timestamps}")          # going on...

      else:
        timestamps.extend(stamps_for_loop)                # refill list to loop with

        break

    else:
      time.sleep(0.001)                                   # short wait to prevent we'll keep the processor busy when there's nothing to do


time.sleep(1)                   # let the last 'note' ring out
