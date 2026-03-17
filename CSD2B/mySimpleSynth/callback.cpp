#include "callback.h"

CustomCallback::CustomCallback (float samplerate)
  : AudioCallback (samplerate){
}

void CustomCallback::prepare (int samplerate) {
  this->samplerate = samplerate;
  std::cout << "\nsamplerate: " << samplerate << "\n";
  organ.setFrequencies();
  melodyGenerator.generateIndexList(true, 15);
  melodyGenerator.generateMelodyList();

  /*
  for (int i = 0; i < 2; i++) {
    delay2[i+1].setNumDelaySamples(33010);
    delay2[i+1].setFeedback(0.7);
  }
  */
}

void CustomCallback::process (AudioBuffer buffer) {
  auto [inputChannels,
        outputChannels,
        numInputChannels,
        numOutputChannels,
        numFrames] = buffer;

  //TODO: naamgevingen!!!
  float sample = 0.0f;
  float vibSample = 0.0f;
  float shapedSample = 0.0f;
  float delayedShapedSample = 0.0f;
  int incr = 0;
  int numDS = 0;

  for (int frame = 0u; frame < numFrames; ++frame) {
    float curSample = organ.getSample();
    vibrato.tick();

    vibrato.processFrame(curSample, vibSample);
    waveshaper.processFrame(vibSample, shapedSample);


    //if (incr <= 10) {std::cout << "numDelaySamples = " << delay2[1].getNumDelaySamples(numDS) << std::endl;}
    //if (incr < 10) {delay2[1].getReadH(rHead), std::cout << "readHead: " << rHead << "\n";}
    for (int channel = 0u; channel < numOutputChannels; ++channel) {
      //outputChannels[channel][frame] = 0.0f;
      delay[channel].processFrame(shapedSample, delayedShapedSample);
      sample = vibSample;
      outputChannels[channel][frame] = sample;

    }
    //if (incr <= 10 ) {std::cout << "sample: " << sample << std::endl;}
    organ.tick();
    incr++;
  }
}
