//
// Created by Aurelia Wurfbain on 09/03/2026.
//

#include "vibrato.h"
#include <iostream>

Vibrato::Vibrato(float dryWet) : Effect(dryWet)
{
 std::cout << "Vibrato::Vibrato()\n" << std::endl;
    sine = new Sine(8.0, 44100.0);
    vibDelay = new Delay(0, 33010, 44100, 1.0);

    /*
    Delay delay2[2] {
        Delay{0.0, 1000, 44100, 1.0},
        Delay{ 0.0, 1000, 44100, 1.0}
    };
    */
}

Vibrato::~Vibrato()
{
    delete sine;
    delete vibDelay;
}

void Vibrato::applyEffect(const float &input, float &output) {
    //std::cout << "Vibrato::applyEffect()" << std::endl;
/*
    for (int i = 0; i < 2; i++) {
        delay2[i].setNumDelaySamples(getLfo());
    }
*/
    //del5ay2[1].processFrame(input, output);
    vibDelay->setNumDelaySamples(getLfo());
    vibDelay->processFrame(input, output);

}

void Vibrato::tick() {
    // increment the phase to allow calculation of next sample
    sine->tick();

    setLfo();
}

void Vibrato::setLfo(){
  //if (lfoSwitch) --- TODO: alleen berekenen als het nodig is:
    lfo = sine->getSample();

  //lfo = sin(M_PI * 2 * phase);
    //std::cout << "lfo: " << lfo << std::endl;

  lfo *= 21.0f;

    //bewegen rond een numDelaySamples van nu 500
    lfo += modDepthCenter;
    //dit is nog wel een float en numDelaySamples van Delay maakt het straks een int.


    //if (lfo == 1) {std::cout << "lfo: " << lfo << " and LFO freq = " << lfoFreq << std::endl;}
}

float Vibrato::getLfo() {
    return lfo;
}