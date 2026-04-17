//
// Created by Aurelia Wurfbain on 13/04/2026.
//

#ifndef FILTER_H
#define FILTER_H

#include "effect.h"



class Filter : public Effect
{
public:
   Filter();
   ~Filter();

   void applyEffect(const float &input, float &output) override;
   void calculateCoefficients();
   void printCoefficients();
   void setCoefficients(float coefficient1, float coefficient2, float coefficient3,
      float coefficient4, float coefficient5);

private:
   //Coefficienten:
   float a0;
   float a1;
   float a2;
   float b1;
   float b2;
   //Geheugen:
   float y0 { 0.0 };
   float y1 { 0.0 };
   float y2 { 0.0 };
   float x1 { 0.0 };
   float x2 { 0.0 };

};



#endif //FILTER_H
