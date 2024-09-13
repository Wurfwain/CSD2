import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("/Users/aureliawurfbain/Documents/HKU/Jaar_2/CSD2/python_basics/Drum1.wav")
play_obj = wave_obj.play()
play_obj.wait_done()