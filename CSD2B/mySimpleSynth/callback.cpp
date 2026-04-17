#include "callback.h"

CustomCallback::CustomCallback (float samplerate)
  : AudioCallback (samplerate){
}

void CustomCallback::prepare (int samplerate) {
  this->samplerate = samplerate;

  melody.prepare(samplerate);

  // set start frequency
  Note currentNote = melody.getCurrentNote();
  organ.setFrequencies(currentNote.getPitch());

  filter.setDryWet(0.9);

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
  float shapedFilteredSample = 0.0f;
  float delayedShapedSample = 0.0f;

  int incr = 0;
  int numDS = 0;

  for (int frame = 0u; frame < numFrames; ++frame) {
    float curSample = organ.getSample();
    vibrato.tick();

    vibrato.processFrame(curSample, vibSample);
    waveshaper.processFrame(vibSample, shapedSample);
    filter.processFrame(shapedSample, shapedFilteredSample);


    //if (incr <= 10) {std::cout << "numDelaySamples = " << delay2[1].getNumDelaySamples(numDS) << std::endl;}
    //if (incr < 10) {delay2[1].getReadH(rHead), std::cout << "readHead: " << rHead << "\n";}
    for (int channel = 0u; channel < numOutputChannels; ++channel) {
      //outputChannels[channel][frame] = 0.0f;
      delay[channel].processFrame(shapedFilteredSample, delayedShapedSample);
      sample = delayedShapedSample;
      outputChannels[channel][frame] = sample;

    }
    //if (incr <= 10 ) {std::cout << "sample: " << sample << std::endl;}
    organ.tick();
    incr++;

    // melody.tick returns true when a new note is reached
    if (melody.tick()) {
      /* NOTE: retrieving a copy of note, would be better to use a pointer,
       * but usage of pointers is out of scope for now.
       */
      Note note = melody.getCurrentNote();
      organ.setFrequencies(note.getPitch());
    }
  }
}
