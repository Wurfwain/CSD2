#pragma once

#include <juce_audio_processors/juce_audio_processors.h>
#include "waveShaper.h"
#include "delay.h"
#include "vibrato.h"
#include "filter.h"


class EffectsChain {
public:
    EffectsChain() {}
    void prepareToPlay(float sampleRate, int numSamplesPerBlock){
        // Your Prepare Goes Here
    }

    void getNextBlock(juce::AudioBuffer<float>& buffer){
        // Your DSP goes here
        float sample = 0.0f;
        float vibSample = 0.0f;
        float shapedSample = 0.0f;
        float shapedFilteredSample = 0.0f;
        float delayedShapedSample = 0.0f;


        for(int channel = 0; channel < buffer.getNumChannels(); ++channel){
            auto* inputChannel = buffer.getReadPointer(channel);
            auto* outputChannel = buffer.getWritePointer(channel);


            for (int sample = 0; sample < buffer.getNumSamples(); ++sample){
              vibrato[channel].processFrame(inputChannel[sample], vibSample);
              waveShaper.processFrame(vibSample, shapedSample);
              filter[channel].processFrame(shapedSample, shapedFilteredSample);
              delay[channel].processFrame(shapedFilteredSample, delayedShapedSample);
              outputChannel[sample] = delayedShapedSample;

              vibrato[channel].tick();
            }


        }

    }

    void setParameter(float parameter){
        // Your Code goes here
        //Filter
        filter[0].setDryWet(parameter);
        filter[1].setDryWet(parameter);

        //Vibrato dry/wet
        float vibDWParameter;
        if (parameter >= 0.5){
          vibDWParameter = 1.0;}
        else{
          vibDWParameter = parameter * 2;
        }
        vibrato[0].setDryWet(vibDWParameter);
        vibrato[1].setDryWet(vibDWParameter);

        //Vibrato LFO speed
        float vibLFOParameter;
        if (parameter < 0.5){
          vibLFOParameter = 5.0;
        } else {
          vibLFOParameter = parameter * 10;
        }
        vibrato[0].setLFO(vibLFOParameter);
        vibrato[1].setLFO(vibLFOParameter);

        //Waveshaper dry/wet (mapInRange)
        float waveShaperParameter;
        if (parameter < 0.2){
          waveShaperParameter = 0.0;
        } else if (parameter > 0.8){
          waveShaperParameter = 1.0;
        } else {
           waveShaperParameter = (parameter - 0.2) / (0.8 - 0.2);
        }
        waveShaper.setDryWet(waveShaperParameter);

        //Delay dry/wet (linMap)
        float delayDWParameter = parameter * 0.6;
        delay[0].setDryWet(delayDWParameter);
        delay[1].setDryWet(delayDWParameter);

        //Delay feedback (lihMap)
        float delayFBParameter;
        if (parameter < 0.5)
            {delayFBParameter = 0.0;
        } else {
            delayFBParameter = (parameter - 0.5) * 2 * 0.6;
        }
        delay[0].setFeedback(delayFBParameter);
        delay[1].setFeedback(delayFBParameter);
    }

private:
	WaveShaper waveShaper;
    Delay delay[2];
    Vibrato vibrato[2];
    Filter filter[2];
};
