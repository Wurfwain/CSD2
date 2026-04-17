#ifndef CALLBACK_H
#define CALLBACK_H

#include "audiocomponent.h"
#include "oscillator.h"
#include "sine.h"
#include "square.h"
#include "additiveSynth.h"
#include "waveShaper.h"
#include "delay.h"
#include "vibrato.h"
#include "melodyGenerator.h"
#include "melody.h"
#include "filter.h"

class CustomCallback : public AudioCallback {
public:
  CustomCallback (float samplerate);
  void prepare (int rate) override;
  void process (AudioBuffer buffer) override;

private:
  AdditiveSynth organ;
  Melody melody;

  WaveShaper waveshaper;
  Delay delay[2];
  Vibrato vibrato;
  Filter filter;

  double samplerate;
};

#endif  //CALLBACK_H
