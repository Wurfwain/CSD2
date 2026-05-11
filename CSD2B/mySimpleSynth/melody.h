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

  void prepare(int samplerate, int scaleType, int scale, int direction);
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
  const float bpm = 120.0f;
  float quarterNoteFrameDur;
  int noteIndex = 0;
  int frameCount = 0;
  int j = 0;
  int melodyLength;
};






