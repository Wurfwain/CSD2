//
// Created by Aurelia Wurfbain on 26/02/2025.
//
#include <iostream>

int main(){
  // User enters 3 lenghts of sides of a triangle (float)
  // Out decision whether the triangle is equilateral, isosceles or scalene

  float a, b, c;
  std::cout << "Please enter 3 side lenghts of a triangle: ";
  std::cin >> a >> b >> c;

  if (a == b && b == c)
    std::cout << "Your triangle is equilateral";
  else if (a!=b && b!=c && c!=a)
    std::cout << "Your triangle is scalene";
  else
    std::cout << "Your triangle is isosceles";



}