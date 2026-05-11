#ifndef _Oscillator_H_
#define _Oscillator_H_

class Oscillator {
public:
  Oscillator (float frequency = 440, float samplerate = 44100);
  ~Oscillator();

  void setSamplerate (float samplerate);
  float getSample();

  void setFrequency (float frequency);
  float getFrequency();
  // go to next sample
  void tick();

protected:
  virtual void calculate() = 0;
  float frequency;
  float amplitude { 0.25f };
  float phase;
  float sample;
  float samplerate;
};

#endif
