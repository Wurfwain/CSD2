//
// Created by Aurelia Wurfbain on 13/04/2026.
//

#include "filter.h"
#include <iostream>

Filter::Filter(){
  calculateCoefficients();
  }

Filter::~Filter(){}

void Filter::calculateCoefficients(){
  //Berekeningen voor een 2e orde LPF met een lage Q (weinig resonance)
  float Q = 0.707;
  float freq = 200;
  float d = 0.0;
  float beta = 0.0;
  float gamma = 0.0;
  float theta = 0.0;

  theta = 2.0 * M_PI * freq / 44100.0;
  d = 1.0/Q;
  beta = 0.5 * (1.0 - ((d/2.0) * sin(theta)))/(1.0 + ((d/2.0) * sin(theta)));
  gamma = (0.5 + beta)*cos(theta);

  a0 = (0.5 + beta - gamma)/2.0;
  a1 = (0.5 + beta - gamma);
  a2 = (0.5 + beta - gamma)/2.0;
  b1 = -2.0 * gamma;
  b2 = 2 * beta;

  std::cout << "a0: " << a0 << std::endl;
  std::cout << "a1: " << a1 << std::endl;
  std::cout << "a2: " << a2 << std::endl;
  std::cout << "b1: " << b1 << std::endl;
  std::cout << "b2: " << b2 << std::endl;

  std::cout << "\n" << "===== calculated coefficients =====\n\n";
  //setCoefficients(a0,a1,a2,b1,b2);
  //printCoefficients();
}

void Filter::applyEffect(const float &input, float &output){
  y0 = (a0 * input) + (a1 * x1) + (a2 * x2) - (b1 * y1) - (b2 * y2);
  y2 = y1;
  y1 = y0;
  x2 = x1;
  x1 = input;
  output = y0;
}

void Filter::printCoefficients(){
  std::cout << "a0: " << a0 << "\n"
      << "a1: " << a1 << "\n"
      << "a2: " << a2 << "\n"
      << "b1: " << b1 << "\n"
      << "b2: " << b2 << "\n\n";
}


//Dit was om te testen
void Filter::setCoefficients(float coefficient1, float coefficient2, float coefficient3,
      float coefficient4, float coefficient5){
  a0 = coefficient1;
  a1 = coefficient2;
  a2 = coefficient3;
  b1 = coefficient4;
  b2 = coefficient5;

  printCoefficients();
}