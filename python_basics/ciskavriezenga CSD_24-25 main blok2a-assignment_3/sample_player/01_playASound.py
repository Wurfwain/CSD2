"""
An example project in which three wav files are used.

------ EXERCISES ------

- What does the function wait_done() do?

- Answer the following question before running the code:
  Do you expect to hear the samples played simultaneously or one after the other?
  Why?

- Alter the code:
  Play the sounds one after the other and then simultaneously.

- Alter the code:
  Ask the user to choice which one of the three samples should be played and
  only play the chosen sample.

- Give yourself a couple of assignments, like playing one of the samples ten
  times before the others are played, playing all samples a given number
  of times or playing the samples one after the other with 1 second between
  them.

"""
import time

# simpleaudio is imported as sa -> shorter name
import simpleaudio as sa

# load audio files
sampleHigh = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Pop.wav")
sampleMid = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Laser1.wav")
sampleLow = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/ciskavriezenga_CSD_24-25_main_blok2a-assignment_3/audioFiles/Dog2.wav")

input("You can choose a sample. Press Enter to hear your options.")

print("1: Pop")
# play high sample
sampleHighPlay = sampleHigh.play()
# wait till sample is done playing
sampleHighPlay.wait_done()
time.sleep(0.5)

print("2: Laser")
# play mid sample
sampleMidPlay = sampleMid.play()
# wait till sample is done playing
sampleMidPlay.wait_done()
time.sleep(0.5)

print("3: Dog")
# play low sample
sampleLowPlay = sampleLow.play()
# wait till sample is done playing
sampleLowPlay.wait_done()
time.sleep(0.5)


sampleChoice = input("Which sample do you want to choose to hear again? Pop, Laser or Dog: ")

if sampleChoice == "Pop" or sampleChoice == "pop":
   print("Let's pop it!")
   sampleHighPlay = sampleHigh.play()
   sampleHighPlay.wait_done()
   

if sampleChoice == "Laser" or sampleChoice == "laser":
   print("Let's laser it!")
   sampleMidPlay = sampleMid.play()
   sampleMidPlay.wait_done()

if sampleChoice == "Dog" or sampleChoice == "dog":
   print("Doggo!")
   sampleLowPlay = sampleLow.play()
   sampleLowPlay.wait_done()

comp = input("Would you like to hear a small composition?: ")

if comp == "Yes" or comp == "yes" or comp == "yes please" or comp == "Yes please" or comp == "Yeah" or comp == "yeah":
   for i in range(10):
    sampleHighPlay = sampleHigh.play()
    sampleHighPlay.wait_done()


#sampleHighPlay = sampleHigh.play()
#sampleMidPlay = sampleMid.play()
#sampleLowPlay = sampleLow.play()
#sampleHighPlay.wait_done()
#sampleMidPlay.wait_done()
#sampleLowPlay.wait_done()


