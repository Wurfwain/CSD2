//
// Created by Aurelia Wurfbain on 05/02/2026.
//

#ifndef OSCILLATOR_H
#define OSCILLATOR_H
#include <iostream>

class Oscillator
{
  public:
    Oscillator(float frequency, float samplerate = 44100);
    ~Oscillator();
    void setSamplerate(float samplerate);
    //return the current sample
    float getSample();
    // go to next sample
    void tick();

    //getters and setters
    void setFrequency(float frequency);
    float getFrequency();

  protected:
    virtual void calculate() = 0;
    float amplitude;
    float phase;
    // sample contains the current sample
    float sample;

  private:
    float frequency;
    float samplerate;
};

#endif //OSCILLATOR_H
