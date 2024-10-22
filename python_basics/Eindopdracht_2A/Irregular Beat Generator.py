""" 
Welcome to my irregular beat generator code.
Have fun reading it.
Small side note. I noticed two things I eventually haven't managed to fix:

- it seems to take a lot of time before the loops gets repeated when the user want to hear it again
- Something goes wrong while creating the time stamps. 
  I didn't work with off sets. That way I'm always a couple ms late with starting the loop.
  It doesn't seem to go wrong with the MIDI though. The MIDI when imported in a DAW does start at 0.
  So I guess it's good enough for a user. I don't see any other problems occur there, so it works.
"""
# ======== PREPARATION ========
import simpleaudio  as sa
import time
import random
import os
from midiutil import MIDIFile

# Load samples
# Kit 1
kick1 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Kick1.wav")
snare1 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Snare1.wav")
hihat1 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Hihat1.wav")

# Kit 2
kick2 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Kick2.wav")
snare2 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Snare2.wav")
hihat2 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Hihat2.wav")

# Kit 3
kick3 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Kick3.wav")
snare3 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Snare3.wav")
hihat3 = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Hihat3.wav")

# ======== INTRODUCTION ========
print("Hi! Welcome to the Euclidean Random Beat Generator")
# Sleep for user to read
time.sleep(1)
print("You're going to create a beat. Please set the settings first.")
time.sleep(1)

run_program = True

while run_program == True:

    # ======== USER INPUT ========

    # Choose a kit
    def show_kit(kit, kick_sample, snare_sample, hh_sample):
        print("===", kit, "===")
        print("- Kick")
        kick_sample.play()
        time.sleep(1)

        print("- Snare")
        snare_sample.play()
        time.sleep(1)

        print("- Hi-hat")
        hh_sample.play()
        time.sleep(0.5)

    enter = input("You can choose a kit. Press enter to hear kit 1.")
    if enter == "":
        show_kit("Kit 1", kick1, snare1, hihat1)

    enter = input("Please press enter to hear kit 2.")
    if enter == "":
        show_kit("Kit 2", kick2, snare2, hihat2)

    enter = input("Please press enter to hear kit 3.")
    if enter == "":
        show_kit("Kit 3", kick3, snare3, hihat3)
    
    print("Which kit would you like to choose?:")
    print("- Kit 1")
    print("- Kit 2")
    print("- Kit 3")
    kit_choice = int(input("Choose 1/2/3: "))
    
    if kit_choice == 1:
        kick = kick1
        snare = snare1
        hh = hihat1
    elif kit_choice == 2:
        kick = kick2
        snare = snare2
        hh = hihat2
    else:
        kick = kick3
        snare = snare3
        hh = hihat3

    # Determine BPM
    bpm = 120
    print("Default BPM: ", bpm)

    #Credits voor .lower() naar Semuel Leijten.
    input_bpm = input("Would you like to change the BPM? yes/no: ").lower()
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
            print("That might be a bit fast. Please choose a BPM between 60 - 240.")
        else:
            new_bpm = True
            print("You've set the BPM to: ", int(bpm))
        

    # Determine time signature (give option between 5/4 (default) and 7/4)
    # I wrote 5 * 2 and 7 * 2 to remember the time signature (5 or 7 over 4) and than work with 8ths.
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
            try:
                repeats = int(input("How many times would you like to hear the rhythm? "))
            except ValueError:
                print("Please enter a number only")
            else:
                if repeats < 1 or repeats > 8:
                    print("Can't do that, sorry. Please choose a number between 1 - 8")
                else:
                    new_repeats = True
        else:
            new_repeats = True

    print(repeats)


    # ======== GENERATE RHYTHM ========

    # Make a sequence (source: Ciska Vriezenga)
    def gen_seq(max_steps):
        # Choose random pulses with minimum of 2, otherwise it might be a bit boring
        pulses = random.randint(2, max_steps)
        # Determine how long the notes (as integers) could be if equally divided.
        min_note_length = int(steps/pulses)
        seq = []

        for i in range(pulses):
            seq.append(min_note_length)
        
        # Add the remainings of the division we did above.
        rest = steps - (pulses * min_note_length)

        for i in range(rest):
            seq[i] += 1
        
        # Shuffle the seq randomly, which is (in a way) rotating
        random.shuffle(seq)
        
        return seq


    # Make 3 different sequences for the 3 instruments
     # /2 to make the kick and snare appair less often than the hh
    note_dur_kick = gen_seq(int(steps/2))
    note_dur_snare = gen_seq(int(steps/2))
    note_dur_hh = gen_seq(steps)

    # Make lists that won't be popped later, to use for MIDI at the end.
    def make_def_note_durs(note_durs):
        note_durs_def = []
        note_durs_def.extend(note_durs)
        
        # Note durs /2
        for dur in note_durs_def:
            note_durs_def.append(note_durs_def.pop(0)/2)
        
        return note_durs_def

    note_dur_kick_def = make_def_note_durs(note_dur_kick)
    note_dur_snare_def = make_def_note_durs(note_dur_snare)
    note_dur_hh_def = make_def_note_durs(note_dur_hh)

    # Note durations to time stamps, depending on BPM
    def durations_to_time_stamps8th(durations_list):
        # Change quarter note_durs to 8ths
        timestamps8th = []

        # A variable that will later help with adding up the times to make a list of time stamps (8ths).
        timestamp_current = 0   

        for note_dur in range(len(durations_list)):
            timestamp_new = durations_list.pop(0)
            # Adding up the current timestamp with the new timestamp and defining this as the "new current" stamp so they keep adding up.
            timestamp_current = timestamp_new + timestamp_current
            timestamps8th.append(timestamp_current)
    
        eighth_note_duration = (60.0 / float(bpm)) / 2.0

        # Create 8th time stamps
        # Note: Had to work with range(len(timestamps8ths)) because just timestamps8ths gave a float error.
        for i in range(len(timestamps8th)):
            timestamps8th[i] = timestamps8th[i] * eighth_note_duration

        return timestamps8th

    # Function per instrument
    ts_kick = durations_to_time_stamps8th(note_dur_kick)
    # Emptying the timestamps16th list before re-using the function: (Source: Semuel Leijten)
    timestamps8th = [0] 

    ts_snare = durations_to_time_stamps8th(note_dur_snare)
    timestamps8th = [0] 

    ts_hh = durations_to_time_stamps8th(note_dur_hh)
    timestamps8th = [0]

    # Make events (Source: Semuel Leijten: multi_sample_sequencer.py)
    def make_events(timestamps, instrument):
        events = []
        for i in timestamps:
            new_event = {
                'timestamp': i,
                'instrument': instrument
            }
            events.append(new_event)

        return events


    # (Source: Semuel Leijten: multi_sample_sequencer.py and Ciska Vriezenga: 4d_dictionary_sorting_function.py)
    def get_timestamps(event):
        return event['timestamp']

    # Sort events (Source: Semuel Leijten: multi_sample_sequencer.py)
    events = make_events(ts_kick, kick) + make_events(ts_snare, snare) + make_events(ts_hh, hh)
    events.sort(key=get_timestamps)
    #print(events)


    # ======== PLAY RHYTHM ========

    # Function to play (bron: Semuel: multi_sample_sequencer.py and Ciska Vriezenga: 4d_dictionary_sorting_function.py)
    def handle_event (event):
        event['instrument'].play()

    # List to temporarily store events
    temp_events = []

    # Keep repeating the loop untill user doesn't want to hear it anymore
    loop = True

    print("Rhythm playing...")

    while loop == True:
        # We will ask the user for extra repetition later.
        rep = True

        # Play according to timestamps
        start_time = time.time()

        for i in range(repeats):
            temp_events.extend(events)

            passed_time = 0

            if i != 0:
                passed_time = (steps/(bpm*(1/30)))

            for event in temp_events:
                event['timestamp'] = event['timestamp']  + passed_time

            # Read time and compare with timestamps
            # (Source: Once again partly Semuel Leijten: multi_sample_sequencer.py and Ciska: 4d_dictionary_sorting_function.py)
            while temp_events:
                current_time = time.time()
                current_timestamp = temp_events[0]['timestamp']

                if(current_time - start_time >= current_timestamp):
                    simultaneous_events = []

                    # Create a new list to make the samples play at the same time.
                    while temp_events and temp_events[0]['timestamp'] == current_timestamp:
                        simultaneous_events.append(temp_events.pop(0))
                    for event in simultaneous_events:
                        handle_event(event)
                    
                else:  
                    time.sleep(0.001)
        
        # Sleep, for the last note to 'ring out'.
        time.sleep(1)

        # Ask for repition of the loop.
        while rep == True:
            play_again = input("Would you like to hear the rhythm again? yes/no: ").lower()
            
            if play_again == "no" or play_again == "yes":
                if play_again == "no":
                    loop = False
                    break
                else:
                    rep = False
                    # I still have a bug that delays the beginning of the next loop. With this print I'll notify the user.
                    print("Here it comes...")
            else:
                print("I didn't quite catch that, please come again.")
        
        

    # ======== WRITING TO MIDI ======== (source: Ciska Vriezenga's Git and self)

    kick_midi_pitch = 35
    snare_midi_pitch = 38
    hh_midi_pitch = 42

    # set the necessary values for MIDI util
    velocity = 80
    track = 0
    channel = 9  # corresponds to channel 10 drums

    # create the MIDIfile object, to which we can add notes
    mf = MIDIFile(1)
    # Set tempo
    time_beginning = 0
    mf.addTempo(track, time_beginning, bpm)

    def make_midi (durations, bpm, midi_pitch, file_name):
        # ___ add the durations to the note
        time = 0

        # Add notes
        for dur in durations:
            mf.addNote(track, channel, midi_pitch, time, dur, velocity)
            # increment time based on the duration of the added note
            time = time + dur


    # User input: Does the user want to store?
    store = True

    while store == True:
        store_midi = input("Would you like to store this to a MIDI file? yes/no: ").lower()
        
        if store_midi == "no" or store_midi == "yes":
            if store_midi == "yes":
                print("How would you like to name the file? ")
                file_name = input("File name: ")

                make_midi(note_dur_kick_def, bpm, kick_midi_pitch, file_name)
                make_midi(note_dur_snare_def, bpm, snare_midi_pitch, file_name)
                make_midi(note_dur_hh_def, bpm, hh_midi_pitch, file_name)
        
                # Store the file in Downloads (Source: Cas Huurdeman)
                with open(os.path.expanduser('~') + f"/Downloads/{file_name}.midi", "wb") as outf:
                    mf.writeFile(outf)

                print("Thank you! Your MIDI file is now stored with the name  ", file_name, "  in your downloadfolder.")
                # Little pause for the user to read.
                time.sleep(2)
                store = False
            else:
                store = False
        else:
            print("I didn't quite catch that, please come again.")
    
    # Again or quit?
    another_round = True
    while another_round == True:
        print("Would you like to create another beat, or would you like to quit?: ")
        print("yes: another go please!")
        print("no: please quit")
        enthousiasm = input("yes/no: ").lower()
        
        if enthousiasm == "no" or enthousiasm == "yes":
            if enthousiasm == "no":
                print("Thanks for using the Euclidean Random Beat Generator.")
                time.sleep(1)
                print("Hope you enjoyed it. See you next time!")
                time.sleep(1)
                print("Program done.")
                run_program = False
                break
            else:
                another_round = False
        else:
            print("I didn't quite catch that, please come again.")