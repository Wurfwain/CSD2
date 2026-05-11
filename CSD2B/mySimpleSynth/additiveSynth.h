//
// Created by Aurelia Wurfbain on 05/03/2026.
//

#ifndef ADDITIVESYNTH_H
#define ADDITIVESYNTH_H
#include "oscillator.h"


class AdditiveSynth {
    public:
    AdditiveSynth();
    ~AdditiveSynth();


    void tick();
    float getSample();

    void setFrequencies(float freq);

    protected:
    //From Vida's code
    int numOscs = 3;
    //make an empty list of oscillator pointers, for all 3 squares of the organ.
    Oscillator* oscs[3];


    private:
    float baseFreq = 220.0;

};



#endif //ADDITIVESYNTH_H
