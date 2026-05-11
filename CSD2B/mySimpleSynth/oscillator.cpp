#include "oscillator.h"

Oscillator::Oscillator (float frequency, float samplerate)
  : frequency (frequency),
    amplitude (0.25f),
    phase (0),
    sample (0),
    samplerate (samplerate) {
}


Oscillator::~Oscillator() {}

void Oscillator::setSamplerate (float samplerate) {
  this->samplerate = samplerate;
}

float Oscillator::getSample() {
  return sample;
}


void Oscillator::setFrequency (float frequency) {
  this->frequency = frequency;
}

float Oscillator::getFrequency() { return frequency; }

void Oscillator::tick() {
  phase += frequency / samplerate;
  if (phase > 1) phase -= 1.0f;

  calculate();
}