//
// Created by Aurelia Wurfbain on 09/03/2026.
//

#include "vibrato.h"
#include <iostream>

Vibrato::Vibrato(float dryWet) : Effect(dryWet)
{
 std::cout << "Vibrato::Vibrato()" << std::endl;
}

Vibrato::~Vibrato()
{

}

void Vibrato::applyEffect(const float &input, float &output) {
    //std::cout << "Vibrato::applyEffect()" << std::endl;


}

void Vibrato::tick() {
    // increment the phase to allow calculation of next sample
    lfoFreq = 6.0;
    phase += lfoFreq / samplerate;
    if (phase > 1) phase -= 1.0f;

    setLfo();
}

void Vibrato::setLfo(){
  //if (lfoSwitch) --- TODO: alleen berekenen als het nodig is:

  lfo = sin(M_PI * 2 * phase);

  lfo *= 21.0f;

    //bewegen rond een numDelaySamples van nu 500
    lfo += modDepthCenter;
    //dit is nog wel een float en numDelaySamples van Delay maakt het straks een int.
    //
    //std::cout << "lfo: " << lfo << std::endl;
    if (lfo == 1) {std::cout << "lfo: " << lfo << " and LFO freq = " << lfoFreq << std::endl;}
}

float Vibrato::getLfo() {
    return lfo;
}