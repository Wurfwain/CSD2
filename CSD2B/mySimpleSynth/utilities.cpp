//
// Created by Aurelia Wurfbain on 05/05/2026.
//

#include "utilities.h"

Utilities::Utilities(){}

Utilities::~Utilities(){}

int Utilities::retrieveScaleTypeSelection(){
  std::cout << "Please choose a scale type:\n"
  << "1. Major\n"
  << "2. Mixolydian\n"
  << "Please enter 1 or 2 + Enter\n"
  << "---------------------------\n";

  scaleTypeSelection = validation(1, 2);
  return scaleTypeSelection;
}

int Utilities::retrieveScaleSelection(){
  std::cout << "Please choose a scale:\n";

  for (int i = 0; i < 12; i++){
    std::cout << i + 1 << ": " << scales[i] << "\n";
  }
  std::cout << "Please enter one of the numbers above\n"
            << "-------------------------------------\n";

  scaleSelection = validation(1, 12);
  return scaleSelection;
}

int Utilities::retrieveDirection(){
  std::cout << "Choose a direction: \n"
  << "1. Down\n"
  << "2. Up\n"
  << "Please enter 1 or 2 + Enter\n"
  << "---------------------------\n";

  directionSelection = validation(1, 2);
  return directionSelection - 1;

}

int Utilities::validation(int min, int max){
  correctSelection = false;
  while (!correctSelection){

    std::cin >> selection;

    if (selection >= min && selection <= max){
      correctSelection = true;
      std::cout << "\n";
      return selection;
    } else {
      std::cout << "\n\nReceived false input, try again.\n";
      std::cin.clear();
      std::cin.ignore(10000, '\n');
    }
  }
}