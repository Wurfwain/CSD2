# Voortgang logboek synthSong

### Week 6 (totaal 7.5u)
##### Maandag: 
_2 uur_ - inkomen. Waar was ik? Herhaling delegating constructors en overloading.
Hoeveel kan ik met mijn handen? - Vastlopen met JUCE en om hulp vragen. Gestrand bij 5_soundingSine niet kunnen builden.

---

##### Dinsdag:
###### Ochtend
_0.5 uur_ - Geprobeerd tips toe te passen. Nieuwe vragen gesteld, nog niet gelukt.
Hoe werkt .md? Logboek begonnen.
#### Errors:
- CMake Error at JuceTest/CMakeLists.txt:2 (juce_add_console_app):
  Unknown CMake command "juce_add_console_app". 
- CMake Error in CMakeLists.txt:
No cmake_minimum_required command is present.  A line of code such as

  cmake_minimum_required(VERSION 4.1)
  
    should be added at the top of the file.  The version specified may be lower
  if you wish to support older CMake versions for this project.  For more
  information run "cmake --help-policy CMP0000"

Daan to the rescue.

###### Middag
_1.5 uur_ - Probleem opgelost met Daan. Kan nu ook Clion gebruiken.
Ik moet builden vanuit de juiste map!!!! --> csd2/build/csd2b/"mapnaam waar hetgeen in zit wat ik wil builden"

5_soundingSine bekeken. Square.cpp en .h in dezelfde map gezet (nog niet ge-include).
Square code met sine vergeleken, kleine verschillen. Code doorgelezen en gerund om te leren begrijpen wat waar gebeurt.
Ik snap het voor misschien 40%.

TODO voor later:
- square includen en runnen
- saw maken en runnen
- verder de inheritance opdracht van week 2 afmaken

Ik hoop dat morgen af te krijgen, dan kan ik daarna kijken naar de opdracht van blok c en/of
beginnen aan week 3 van blok b.
Het voelt al wel alsof ik er langzaam aan weer in kom, heeel voorzichtig. 

---

##### Woensdag:
_1.5 uur_ - Ruzie maken met Clion, square proberen te runnen, errors daarvan begrijpen en wegwerken,
saw schrijven en runnen.

Clion wil niet meer maken, ik snap niet waarom. Heb geprobeerd er wat over op te zoeken maar ik raak
gefrustreerd en laat het even bij maken en builden in de terminal, wat heel leerzaam is! Stiekem hoop ik dat
Clion bij een volgend project wel weer meewerkt, magically.

Bij het runnen van de square heb ik een aantal errors weggewerkt.
Eerst kreeg ik errors omdat ik square{440} had getypt - zoals dat ging met sine{440} - maar bij square werkte
het bepalen van de frequentie anders (wat ik nog niet volledig snap) dus met square() werkte het gelukkig wel.

Daarna kreeg ik de error:

````
ld: symbol(s) not found for architecture x86_64
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
````
Met Stack Overflow
(https://stackoverflow.com/questions/10143784/c-cant-compile-symbols-not-found-for-architecture-x86-64)
to the rescue begreep ik dat ik square.cpp moest toevoegen aan de CMakeLists.txt.
Om te voorkomen dat het nog eens gebeurt schrijf ik het hier op.

Ik had gehoopt verder te komen en meer te doen (meer tijd te besteden) vandaag maar ik liep aan tegen afleiding
en een motivatieprobleem. Mede dankzij vermoeidheid door paniekaanvallen van afgelopen nacht en meer pijn
aan mijn gebroken handen dan afgelopen 2 dagen. Ik ervaar lichte stress over mijn algehele achterstand.
Hopelijk kan ik morgen verder met de inheritance van opdracht 2. Het zou fijn zijn om deze week op z'n minst week 2
af te ronden en door te kunnen.

---

##### Donderdag:

_2 uur_ - 5_soundingSine afgemaakt met de inheritance stap. Wel een beetje afgekeken bij sessie 3, simple organ.
Ik snap het overriden met virtual af en toe en dan weer eventjes niet. Want waarom zet je die in
de base class als je 'm vervolgens ook in alle derived classes zet? Wellicht omdat je 'm in de base class
gelijk aan 0 stelt, ipv dat je dat steeds in elke sub doet.

Volgende stap: sessie 3
OrganSynth maken en MelodyGenerator beginnen.

Voor nu ga ik even kijken naar blok c, of ik daar iets voor kan doen om niet ook daar helemaal
achter te blijven en dan besteed ik nog wat tijd aan dsp.

---

##### Vrijdag:


---

