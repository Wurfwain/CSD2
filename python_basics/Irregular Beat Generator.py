""" 
The irregular beat generator

step 1: user input (BPM, maatsoort)
step 2: generate rhythm (note seq)
step 2.1: note dur to timestamps
step 3: transform timestamps to events
step 4: play events
step 5: store to MIDI? (user input)
step 6: store and/or loop
- netjes maken: alles van tags voorzien
- netjes maken: alle onzin weghalen
- User path netjes afwerken

TO DO:
- MIDI fixen

Wan tijd over:
- work with off set?
- keuze uit kits
- kan het nog efficiënter?

- Er gaat iets fout bij het maken van timestamps. Ik zou eiglk overal moeten beginnen met 0 en dan met off set moeten werken maar dat heb ik niet.
"""
# ======== PREPARATION ========
import simpleaudio  as sa
import time
import random
from midiutil import MIDIFile

# Load samples
kick = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Kick1.wav")
snare = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Snare1.wav")
hihat = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Hihat1.wav")

# ======== INTRODUCTION ========
print("Hi! Welcome to the Euclidean Random Beat Generator")
print("You're going to create a beat. Please set the settings first.")

run_program = True

while run_program == True:

    # ======== USER INPUT ========
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

    # Note durations to time stamps, depending on BPM
    def durations_to_time_stamps8th(durations_list):
        # Change quarter note_durs to 8ths
        # A 0 to start with for the kick so that this is the first timestamp of the first note we'll hear.
        if durations_list == note_dur_kick:
            timestamps8th = [0]     
        else:
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
    events = make_events(ts_kick, kick) + make_events(ts_snare, snare) + make_events(ts_hh, hihat)
    events.sort(key=get_timestamps)
    #print(events)

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

    kick_qnote_offset = 0
    snare_qnote_offset = 0
    hh_qnote_offset = 0
    kick_midi_pitch = 35
    snare_midi_pitch = 38
    hh_midi_pitch = 41

    # set the necessary values for MIDI util
    velocity = 80
    track = 0
    channel = 9  # corresponds to channel 10 drums

    # create the MIDIfile object, to which we can add notes
    mf = MIDIFile(1)
    # Set tempo
    time_beginning = 0
    mf.addTempo(track, time_beginning, bpm)

    def make_midi (durations, offset, bpm, midi_pitch, file_name):
        # ___ add the durations to the note
        # set the time to offset in case the sample does not start at the beginning
        time = offset

        # Add notes
        for dur in durations:
            mf.addNote(track, channel, midi_pitch, time, dur, velocity)
            # increment time based on the duration of the added note
            time = time + dur

        with open(f"/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/MIDI_files/{file_name}.midi",'wb') as outf:     # TO DO: file path maken en documentnaam
                mf.writeFile(outf)

    # User input: Does the user want to store?
    store = True

    while store == True:
        store_midi = input("Would you like to store this to a MIDI file? yes/no: ").lower()
        
        if store_midi == "no" or store_midi == "yes":
            if store_midi == "yes":
                print("How would you like to name the file? ")
                file_name = input("File name: ")

                make_midi(note_dur_kick, kick_qnote_offset, bpm, kick_midi_pitch, file_name)
                make_midi(note_dur_snare, snare_qnote_offset, bpm, snare_midi_pitch, file_name)
                make_midi(note_dur_hh, hh_qnote_offset, bpm, hh_midi_pitch, file_name)

                print("Thank you! Your MIDI file is now stored with the name: ", file_name)
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
                print("Hope you enjoyed it. See you next time!")
                print("Program done.")
                run_program = False
                break
            else:
                another_round = False
        else:
            print("I didn't quite catch that, please come again.")