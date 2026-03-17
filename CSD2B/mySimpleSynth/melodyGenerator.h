//
// Created by Aurelia Wurfbain on 13/03/2026.
//

#ifndef MELODYGENERATOR_H
#define MELODYGENERATOR_H



class MelodyGenerator {
public:
  MelodyGenerator();
  ~MelodyGenerator();

  void generateIndexList(bool goesUp, int range);
  void generateMelodyList();
  int getMelodyList();

private:
  int direction = 1;
  int listSize = 20;
  int indexListSize = 0;
  int noteDelta;
  int incr = 0;
  int curNote;
  int ladderList[15] = {60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84};
  int* indexList;
  int* melodyList;

};



#endif //MELODYGENERATOR_H