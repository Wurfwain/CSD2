#ifndef _SINE_H_
#define _SINE_H_
#include <iostream>
#include <cmath>
#include "oscillator.h"

class Sine : public Oscillator
{
public:
  //Constructor and destructor
  Sine(float frequency, float samplerate = 44100);
  ~Sine();
  void calculate();

private:
  const float pi = acos (-1);  //atan(1) * 4; <-- vak van Pieter.
};

#endif
