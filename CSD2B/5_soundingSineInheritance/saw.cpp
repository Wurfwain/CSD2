#include "saw.h"
#include "math.h"

Saw::Saw(float frequency, float samplerate) : Oscillator(frequency, samplerate)
{
  std::cout << "Saw - constructor\n";
}

Saw::~Saw() {
  std::cout << "Saw - destructor\n";
}

void Saw::calculate() {
  sample = (1 - 2 *  phase) * amplitude;
}

