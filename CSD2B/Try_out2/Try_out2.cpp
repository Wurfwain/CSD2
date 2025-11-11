//
// Created by Aurelia Wurfbain on 04/03/2025.
//

#include <iostream>

int main() {
  int num1, num2;

  std::cout << "Please enter a number: ";
  std::cin >> num1;
  std::cout << "Please enter a number: ";
  std::cin >> num2;

  (num1 == num2)? std::cout << "Correct": std::cout << "Wrong";

  }