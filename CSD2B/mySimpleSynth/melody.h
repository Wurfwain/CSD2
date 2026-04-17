#pragma once

#include <iostream>
#include "melodyGenerator.h"
#include "note.h"
#include <vector>

#define NUM_NOTES 6

class Melody
{
public:
  Melody();
  ~Melody();

  void prepare(int samplerate);
  // returns true if the melodyChanged
  // NOTE: this would be nicer with e.g. observer pattern, but out of scope.
  bool tick();

  // setters and getters
  void setMelody(std::vector<Note> newMelody);
  Note getCurrentNote();




private:
  MelodyGenerator melodyGenerator;

  std::vector<Note> notes;

  int currentNoteFrameDuration;

  // using a constant value 120 for now, can be made adaptable
  const float bpm = 120.0f;
  // the duration of a quarternote in frames given the bpm
  // using a float, rounding when transforming the note frame dur to integer
  float quarterNoteFrameDur;
  // the index of the current note - readIndex
  int noteIndex = 0;
  int frameCount = 0;
  int j = 0;
  int melodyLength;
};






