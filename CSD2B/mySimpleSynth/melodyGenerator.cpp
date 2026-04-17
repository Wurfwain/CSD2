//
// Created by Aurelia Wurfbain on 13/03/2026.
//
#include <iostream>
#include "melodyGenerator.h"
#include <random>
#include <vector>

MelodyGenerator::MelodyGenerator(){
}


MelodyGenerator::~MelodyGenerator(){
  //delete[] indexList;
  std::cout << "MelodyGenerator::~MelodyGenerator()" << std::endl;
  //delete melodyList;
}


//TODO: naamgevingen


std::vector<Note> MelodyGenerator::generateMelodyList(){
  //Eerst maken we een index list, die we om kunnen zetten naar een melody list
  generateIndexList(true, 14);

  //veel ruzie gehad met pointers, dus ik gebruik vectors
  //melodyList = new int[indexListSize];
  std::cout << "\nGenerating melody list..." << std::endl;

  for (int i = 0; i < indexListSize; i++) {
    melodyList = ladderList[indexList[i]];
    std::cout << melodyList << std::endl;
    tempNotesVector.emplace_back(melodyList);
  }

  return tempNotesVector;
}


void MelodyGenerator::generateIndexList(bool goesUp, int range){
  std::cout << "========================" << std::endl;
  std::cout << "Generating index list..." << std::endl;
  std::cout << "========================" << std::endl;
  std::cout << "Range: " << range << std::endl;

  if (!goesUp){direction = -1;}
  range *= direction;

  //We maken een lijst waarmee we later uit een lijst die overeenkomt met een toonsoort elementen kunnen kiezen.
  //Deze mag in waardes niet over de grootte van de toonsoortlijst komen. Het grootst mogelijke getal is dus "sizeof",
  //ofwel "range".
  //Eerste waarde wordt de beginnoot
  curNote = 0;
  incr = 0;
  indexList.push_back(curNote);

  while (indexList[incr] < range - 3){
    //Random #1
    std::random_device rd;
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    float randomValue = dist(rd);

    //Stap 1 van generatie
    if (randomValue < 0.5){
      noteDelta = 2;
    } else {
      noteDelta = 3;
    }

    //Nieuwe waarde "curNote" toevoegen aan de lijst op de juiste plek mbv "incr".
    curNote += noteDelta;
    incr++;
    indexList.push_back(curNote);

    //Random #2
    randomValue = dist(rd);

    //Stap 2 van generatie
    if (randomValue < 0.5){
      noteDelta = -1;
    } else {
      noteDelta = 1;
    }

    //Nieuwe waarde weer toevoegen.
    curNote += noteDelta;
    incr++;
    indexList.push_back(curNote);
  }
  indexListSize = incr + 1;
  std::cout << "Increment: " << incr << std::endl;
  std::cout << "Temp list: " << std::endl;
  for (int i = 0; i < indexListSize; i++) {
    std::cout << "#" << i << " = " << indexList[i] << std::endl;
  }
  std::cout << "indexListSize = " << indexList.size() << std::endl;

  //De lijst die hieruit komt is langer dan indexListSize en bevat trash, is dat erg??
}

int MelodyGenerator::getMelodyLength() {
  return indexListSize;
}
