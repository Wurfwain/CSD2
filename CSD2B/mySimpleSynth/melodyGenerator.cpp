//
// Created by Aurelia Wurfbain on 13/03/2026.
//
#include <iostream>
#include "melodyGenerator.h"
#include <random>

MelodyGenerator::MelodyGenerator(){
  std::cout << "We're making a melody!!" << std::endl;
}


MelodyGenerator::~MelodyGenerator(){
  delete indexList;
  delete melodyList;
}

int MelodyGenerator::getMelodyList(){
  // Dit werkt niet, zo in en for loop. Tenzij ik de i meegeef in een argument en dan de for loop zet op de
  //plek waar ik de getMelodyLists() aanroep.
  for (int i = 0; i < indexListSize; i++){
    return melodyList[i];
  }
}

//TODO: naamgevingen

void MelodyGenerator::generateIndexList(bool goesUp, int range){
  std::cout << "========================" << std::endl;
  std::cout << "Generating index list..." << std::endl;
  std::cout << "========================" << std::endl;

  if (!goesUp){direction = -1;}
  range *= direction;

  //We maken een lijst waarmee we later uit een lijst die overeenkomt met een toonsoort elementen kunnen kiezen.
  //Deze mag in waardes niet over de grootte van de toonsoortlijst komen. Het grootst mogelijke getal is dus "sizeof",
  //ofwel "range".
  int listTemp[listSize];
  //Eerste waarde wordt de beginnoot
  curNote = 0;
  incr = 0;
  listTemp[incr] = curNote;

  while (listTemp[incr] <= range - 3){
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
    listTemp[incr] = curNote;

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
    listTemp[incr] = curNote;
  }
  std::cout << "Increment: " << incr << std::endl;
  std::cout << "Temp list: " << std::endl;
  for (int i = 0; i < (sizeof(listTemp)/sizeof(listTemp[0])); i++) {
    std::cout << "#" << i << " = " << listTemp[i] << std::endl;
  }

  //De lijst die hieruit komt is te lang en de lengte van de het bruikbare deel wordt random bepaald.
  //Daar halen we nu nog het onbruikbare deel vanaf.

  // Ik ben in de war want deze nieuwe lijst heeft ook trash als je meer print dan alleen de indexListSize...
  //?????????????????
  indexListSize = incr + 1;
  indexList = new int[indexListSize];
  std::cout << "indexListSize: " << indexListSize << std::endl;

  std::cout << "Indexlist: " << std::endl;
  for (int i = 0; i < 20; i++) {
    indexList[i] = listTemp[i];
    std::cout << "#" << i << " = " << *(indexList + i) << std::endl;
  }

}

void MelodyGenerator::generateMelodyList(){

  melodyList = new int[indexListSize];
  std::cout << "Generating melody list..." << std::endl;
    for (int i = 0; i < indexListSize; i++) {
      melodyList[i] = ladderList[indexList[i]];
      std::cout << melodyList[i] << std::endl;
    }
}