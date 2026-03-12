//
// Created by Aurelia Wurfbain on 09/03/2026.
//

#ifndef VIBRATO_H
#define VIBRATO_H

#include "effect.h"


class Vibrato : public Effect
{
public:
  Vibrato(float dryWet = 1.0);
  ~Vibrato();

  void applyEffect(const float& input, float& output) override;
  void setLfo();
  void tick();
  float getLfo();


private:
    float lfoFreq = 5.0;
    float phase;
    //TODO: samplerate setten in prepare van callback?
    float samplerate = 44100;
    float lfo;
    unsigned int modDepthCenter = 22;
    float modDepth = 21.0;

};



#endif //VIBRATO_H
