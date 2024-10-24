""" 
The irregular beat generator

DONE:
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
- MIDI fixen
- keuze uit kits

TO DO:

Wan tijd over:
- work with off set?

- kan het nog efficiënter?

- Er gaat iets fout bij het maken van timestamps. Ik zou eiglk overal moeten beginnen met 0 en dan met off set moeten werken maar dat heb ik niet.
- Lijkt goed te gaan met de MIDI though.
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
    note_dur_kick = gen_seq(int(steps/2))
    note_dur_snare = gen_seq(int(steps/2))
    note_dur_hh = gen_seq(steps)

    # Make 3 lists to store durations even after popping those 3 above for the making of timestamps
    note_dur_kick_def = []
    note_dur_kick_def.extend(note_dur_kick)
    note_dur_snare_def = []
    note_dur_snare_def.extend(note_dur_snare)
    note_dur_hh_def = []
    note_dur_hh_def.extend(note_dur_hh)

    # Note durations to time stamps, depending on BPM
    def durations_to_time_stamps8th(durations_list):
    # Change quarter note_durs to 8ths
        if durations_list == note_dur_kick:
            timestamps8th = [0]                                      # a 0 to start with because this is the first timestamp of the first note we'll hear.
        else:
            timestamps8th = []

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
    events = make_events(ts_kick, kick) + make_events(ts_snare, snare) + make_events(ts_hh, hh)
    events.sort(key=get_timestamps)
    #print(events)

    # Function to play (bron: Semuel: multi_sample_sequencer.py and Ciska: 4d_dictionary_sorting_function.py)
    def handle_event (event):
        #print("play!!")
        event['instrument'].play()

    # List to temporarily store events
    temp_events = []

    # Keep repeating the loop untill user doesn't want to hear it anymore
    loop = True

    print("Rhythm playing...")

    while loop == True:
        # We will ask the user for extra repetition later.
        rep = True

        ######### Play according to timestamps
        start_time = time.time()

        for i in range(repeats):
            temp_events.extend(events)

            passed_time = 0

            if i != 0:
                passed_time = (steps/(bpm*(1/30)))           # bpm afhankelijk

            for event in temp_events:
                event['timestamp'] = event['timestamp']  + passed_time
            
            #print("Passed time: ", passed_time)

            ##print(i, steps, temp_events)

            
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
        
        

    # ======== WRITING TO MIDI ======== (source: Ciska's Git and self)

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

    # NOTE: DUPLICATE CODE below, would be better to place stuff below in a function

    def make_midi (durations, offset, bpm, midi_pitch, file_name):
        # ___ add the kick durations to the note
        # set the time to kick offset in case the kick does not start at the beginning
        time = offset         # bijv: kick_qnote_offset


        # add the notes for the kick
        
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


                print("Note dur kick: ",note_dur_kick_def)
                print("Note dur snare: ",note_dur_snare_def)
                print("Note dur hh: ", note_dur_hh_def)
                make_midi(note_dur_kick_def, kick_qnote_offset, bpm, kick_midi_pitch, file_name)
                make_midi(note_dur_snare_def, snare_qnote_offset, bpm, snare_midi_pitch, file_name)
                make_midi(note_dur_hh_def, hh_qnote_offset, bpm, hh_midi_pitch, file_name)

                with open(f"/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/MIDI_files/{file_name}.midi",'wb') as outf:     # TO DO: file path maken en documentnaam
                #with open(os.path.expanduser('~') + f"/Downloads/{file_name}.midi", "wb") as outf:
                    mf.writeFile(outf)

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