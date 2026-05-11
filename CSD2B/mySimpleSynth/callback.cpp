#include "callback.h"

CustomCallback::CustomCallback (float samplerate)
  : AudioCallback (samplerate){
}

void CustomCallback::prepare (int samplerate) {
  this->samplerate = samplerate;

  std::cout << "\n=====================================\n"
    << ">>> Welcome! Let's create an arp. <<<\n" <<
      "=====================================\n\n";

  int scaleType = utilities.retrieveScaleTypeSelection();
  int scale = utilities.retrieveScaleSelection();
  int direction = utilities.retrieveDirection();
  melody.prepare(samplerate, scaleType, scale, direction);

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

    if (melody.tick()) {
      Note note = melody.getCurrentNote();
      organ.setFrequencies(note.getPitch());
    }
  }
}
