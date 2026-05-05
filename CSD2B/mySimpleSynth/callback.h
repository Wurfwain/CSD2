#ifndef CALLBACK_H
#define CALLBACK_H

#include "audiocomponent.h"
#include "additiveSynth.h"
#include "melody.h"


class CustomCallback : public AudioCallback {
public:
  CustomCallback (float samplerate);
  void prepare (int rate) override;
  void process (AudioBuffer buffer) override;

private:
  double samplerate;

  AdditiveSynth organ;
  Melody melody;
};

#endif  //CALLBACK_H
