#include "callback.h"
#include <iostream>
#include <thread>


int main () {
  ScopedMessageThreadEnabler scopedMessageThreadEnabler;
  CustomCallback audioSource (44100);

  JUCEModule juceModule (audioSource);
  juceModule.init (2, 2);

  std::cout << "Press q + Enter to quit..." << std::endl;
  bool running = true;
  while (running) {
    switch (std::cin.get()) {
      case 'q':
        running = false;
    }
  }
  //end the program
  return 0;
}  // main()
