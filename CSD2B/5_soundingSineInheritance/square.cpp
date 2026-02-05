#include "square.h"
#include "math.h"


Square::Square(double frequency, double samplerate) : Oscillator(frequency, samplerate)
{
  std::cout << "Square - constructor\n";
}

Square::~Square() {
  std::cout << "Square - destructor\n";
}

void Square::calculate() {
  // use the phase to calculate the next value of the square wave
  if(phase < 0.5) {
    sample = 1.0;
  } else {
    sample = -1.0;
  }
  sample *= amplitude;
}
