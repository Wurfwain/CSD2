#include "oscillator.h"
#include "math.h"

Oscillator::Oscillator (float frequency, float samplerate)
  : frequency (frequency),
    amplitude (0.25f),
    phase (0),
    sample (0),
    samplerate (samplerate) {
  std::cout << "Oscillator - constructor\n" << "Samplerate: " << samplerate << "\n";
  std::cout << "Frequency: " << frequency << "\n";
}


Oscillator::~Oscillator() { std::cout << "Oscillator - destructor\n"; }

void Oscillator::setSamplerate (float samplerate) {
  this->samplerate = samplerate;
}

float Oscillator::getSample() {
  //if (phase == 0.0) std::cout << "Sample: " << sample << " and frequency : " << frequency << std::endl;
  return sample; }


//getters and setters
void Oscillator::setFrequency (float frequency) {
  // TODO
  // add check to see if parameter is valid
  this->frequency = frequency;
  std::cout << "Frequency is set to: " << frequency << std::endl;
}

float Oscillator::getFrequency() { return frequency; }

void Oscillator::tick() {
  // increment the phase to allow calculation of next sample
  phase += frequency / samplerate;
  // wrap the phase to interval [0, 1]
  if (phase > 1) phase -= 1.0f;
  //std::cout << "Phase: " << phase << " and freq: " << frequency << std::endl;

  // calculate sample for the incremented phase
  calculate();
}