//
// Created by Aurelia Wurfbain on 05/03/2026.
//

#include "additiveSynth.h"
#include "square.h"

AdditiveSynth::AdditiveSynth() {
    for (int i = 0; i < numOscs; i++) {
        oscs[i] = new Square();
        std::cout << "Square " << i + 1 << " was created\n";
    }
}

AdditiveSynth::~AdditiveSynth() {
    for (int i = 0; i < numOscs; i++) {
      delete oscs[i];
    }
}

//Stolen from Vida's code
void AdditiveSynth::tick() {
    for (int i = 0; i < numOscs; i++) {
        oscs[i]->tick();
    }
}

float AdditiveSynth::getSample() {
    float sample = 0;

    //sum the oscillators
    for (int i = 0; i < numOscs; i++) {
      sample += oscs[i]->getSample();
    }

    /*static int debug = 0;
    if(debug < 10) {
        std::cout << "***DEBUG***: " << numOscs << "\n";
        debug++;
    }*/

    //normalize amplitude
    //TODO: factor berekenen (1x) waarmee we kunnen vermenigvuldigen, zodat we niet hoeven te delen steeds.
    sample *= (1.00f/numOscs); //OMGGGGGGGGGGGGG heftie berekening, niet meer doen, foei


    return sample;
}

void AdditiveSynth::setFrequencies(){
  //TODO: duplicated code, miss oplossen met forloop en list
  oscs[0]->setFrequency(baseFreq);
  //apparently 440.0*(3/2) doesn't give 660, but 440. Donno why but in this order it works though:
  oscs[1]->setFrequency((3.0/2.0) * baseFreq);
  oscs[2]->setFrequency((3.01/2.0) * baseFreq);
}

