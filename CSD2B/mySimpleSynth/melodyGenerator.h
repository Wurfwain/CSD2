//
// Created by Aurelia Wurfbain on 13/03/2026.
//

#ifndef MELODYGENERATOR_H
#define MELODYGENERATOR_H
#include "note.h"
#include <vector>

class MelodyGenerator {
public:
  MelodyGenerator();
  ~MelodyGenerator();

  void generateIndexList(bool goesUp, int range);
  std::vector<Note> generateMelodyList();
  std::vector<Note> tempNotesVector;

  int getMelodyLength();

private:
  int direction = 1;
  int listSize = 20;
  int indexListSize = 0;
  int noteDelta;
  int incr = 0;
  int curNote;
  int ladderList[15] = {50, 52, 54, 55, 57, 59, 61, 62, 64, 66, 67, 69, 71, 73, 74};
  std::vector<int> indexList;
  int melodyList;


};



#endif //MELODYGENERATOR_H