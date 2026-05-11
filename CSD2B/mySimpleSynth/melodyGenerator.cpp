//
// Created by Aurelia Wurfbain on 13/03/2026.
//
#include <iostream>
#include "melodyGenerator.h"
#include <random>
#include <vector>

MelodyGenerator::MelodyGenerator(){}

MelodyGenerator::~MelodyGenerator(){}

//TODO: naamgevingen en opmerkingen


std::vector<Note> MelodyGenerator::generateMelodyList(int maj, int scale, bool goesUp){
  //First we make an index list, which we can transform into a melody list
  generateIndexList(14, goesUp);

  if (maj == 1) {
    for (int i = 0; i < indexListSize; i++) {
      tempNotesVector.emplace_back(ladderListMaj[indexList[i]] + scale);
    }
  } else {
    for (int i = 0; i < indexListSize; i++) {
      tempNotesVector.emplace_back(ladderListMix[indexList[i]] + scale);
    }
  }
  return tempNotesVector;
}


void MelodyGenerator::generateIndexList(int range, bool goesUp){
  if (!goesUp) {direction = -1;}
  range *= direction;

  //Creating index list (with root note as first note)
  curNote = 0;
  incr = 0;
  indexList.push_back(curNote);

  while ((indexList[incr] * direction) - range >= 3 || (indexList[incr] * direction) - range <= -3){
    //Random #1
    std::random_device rd;
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    float randomValue = dist(rd);

    //Step 1 of generation
    if (randomValue < 0.5){
      noteDelta = 2;
    } else {
      noteDelta = 3;
    }

    curNote += noteDelta;
    incr++;
    indexList.push_back(curNote);

    //Random #2
    randomValue = dist(rd);

    //Step 2 of generation
    if (randomValue < 0.5){
      noteDelta = -1;
    } else {
      noteDelta = 1;
    }

    curNote += noteDelta;
    incr++;
    indexList.push_back(curNote);
  }

  indexListSize = incr + 1;

  if (!goesUp) {
    for (int i = 0; i < indexListSize; i++) {
      indexList[i] = -indexList[i] + indexList[indexListSize - 1] + 1;
    }
  }

  //Add the high root note to the list if it wasn't created by chance
  if (!goesUp && indexList[0] != 14) {
    indexList.insert(indexList.begin(), 14);
    indexListSize++;
  }
}

int MelodyGenerator::getMelodyLength() {
  return indexListSize;
}
