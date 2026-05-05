#include "melody.h"
#include <vector>

Melody::Melody() {}

Melody::~Melody() {}

void Melody::prepare(int samplerate)
{
  quarterNoteFrameDur = 60.0f / bpm * samplerate;
  //voor nu doen we alleen 8e noten met bpm 120.
  currentNoteFrameDuration = 0.5f * quarterNoteFrameDur;
  //updateCurrentNoteFrameDur();     d-- en gebruiken we deze functie niet.

  //in deze prepare moet ik een melodie genereren en opslaan en num_notes instellen
  //met de lengte van de vector van de generator

  setMelody(melodyGenerator.generateMelodyList());
  melodyLength = melodyGenerator.getMelodyLength();
}
/*
 * NOTE - returning a copy of current note example,
 * instead, we could return a pointer to the current note.
 */
Note Melody::getCurrentNote()
{
  return notes[noteIndex];
}

bool Melody::tick()
{
  frameCount++;

  if (frameCount >= currentNoteFrameDuration)
  {
    // fetch a new notemake
    noteIndex++;
    // wrap note index back to the beginning if it exceeds the melody array
    if(noteIndex >= melodyLength) {
      noteIndex = 0;
    }

    // reset the frameCount
    frameCount = 0;
    return true;
  }
  return false;
}

void Melody::setMelody(std::vector<Note> newMelody) {
  notes = newMelody;
}