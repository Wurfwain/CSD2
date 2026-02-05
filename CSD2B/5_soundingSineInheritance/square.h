#ifndef _SQUARE_H_
#define _SQUARE_H_
#include <iostream>
#include "oscillator.h"

class Square : public Oscillator
{
public:
  //Constructor and destructor
  Square(double frequency, double samplerate = 44100);
  ~Square();
  void calculate();
};

#endif
