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

  void generateIndexList(int range, bool goesUp);
  std::vector<Note> generateMelodyList(int maj, int scale, bool goesUp);
  std::vector<Note> tempNotesVector;

  int getMelodyLength();

private:
  int direction = 1;
  int listSize = 20;
  int indexListSize = 0;
  int noteDelta;
  int incr = 0;
  int curNote;
  int ladderListMaj[15] = {48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72};
  int ladderListMix[15] = {48, 50, 52, 53, 55, 57, 58, 60, 62, 64, 65, 67, 69, 70, 72};
  std::vector<int> indexList;
  int melodyList;

};



#endif //MELODYGENERATOR_H