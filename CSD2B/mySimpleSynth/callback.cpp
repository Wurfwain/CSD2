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
}

void CustomCallback::process (AudioBuffer buffer) {
  auto [inputChannels,
        outputChannels,
        numInputChannels,
        numOutputChannels,
        numFrames] = buffer;

  for (int frame = 0u; frame < numFrames; ++frame) {
    for (int channel = 0u; channel < numOutputChannels; ++channel) {
      outputChannels[channel][frame] = organ.getSample();
    }

    organ.tick();

    // melody.tick returns true when a new note is reached
    if (melody.tick()) {
      Note note = melody.getCurrentNote();
      organ.setFrequencies(note.getPitch());
    }
  }
}
