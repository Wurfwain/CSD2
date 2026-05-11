#include "melody.h"
#include <vector>

Melody::Melody() {}

Melody::~Melody() {}

void Melody::prepare(int samplerate, int scaleType, int scale, int direction)
{
  quarterNoteFrameDur = 60.0f / bpm * samplerate;
  currentNoteFrameDuration = 0.5f * quarterNoteFrameDur;

  setMelody(melodyGenerator.generateMelodyList(scaleType, scale, direction));
  melodyLength = melodyGenerator.getMelodyLength();
}

Note Melody::getCurrentNote()
{
  return notes[noteIndex];
}

bool Melody::tick()
{
  frameCount++;

  if (frameCount >= currentNoteFrameDuration)
  {
    noteIndex++;

    if(noteIndex >= melodyLength) {
      noteIndex = 0;
    }

    frameCount = 0;
    return true;
  }
  return false;
}

void Melody::setMelody(std::vector<Note> newMelody) {
  notes = newMelody;
}