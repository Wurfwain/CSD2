//
// Created by Aurelia Wurfbain on 05/05/2026.
//

#ifndef UTILITIES_H
#define UTILITIES_H

#include <iostream>

class Utilities {
public:
  Utilities();
  ~Utilities();

  int retrieveScaleTypeSelection();
  int retrieveScaleSelection();
    int retrieveDirection();
    int validation(int min, int max);

  int scaleTypeSelection;
  int scaleSelection;
  int directionSelection;
  int scaleInt;
  int selection;

  bool correctScaleType = false;
  bool correctScale = false;
  bool correctDirection = false;
  bool correctSelection = false;

  std::string scales[12] = {"C", "C#/Db", "D", "D#/Eb", "E", "F",
                                "F#/Gb", "G","G#/Ab", "A", "A#/Bb", "B"};
};



#endif //UTILITIES_H
