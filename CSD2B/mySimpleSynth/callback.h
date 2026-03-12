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

class CustomCallback : public AudioCallback {
public:
  CustomCallback (float samplerate);
  void prepare (int rate) override;
  void process (AudioBuffer buffer) override;

private:
  AdditiveSynth organ;
  WaveShaper waveshaper;
  Delay delay[2];

  //Credits DAAN
  Delay delay2[2] {
    Delay{0.0, 1000, 44100, 1.0},
    Delay{ 0.0, 1000, 44100, 1.0}
  };
  Vibrato vibrato;
  double samplerate;
};

#endif  //CALLBACK_H
