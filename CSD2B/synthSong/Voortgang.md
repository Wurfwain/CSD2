# Voortgang logboek synthSong

### Week 6 (totaal 8u)
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

_0.5 uur_ - learningGoals.md voor csd2c geschreven en git geüpdatet.

---

### Week 7 (totaal 8u)
##### Maandag: 
_2 uur_ - wiskunde D H1 herhalen en H2 beginnen.
_0.5 uur_ - License vernieuwen en wifi-problemen verhelpen (bijzonder frustrerend en gevoelsmatig onproductief)

---

##### Dinsdag:
###### Aantekeningen les Ciska:

Afspraak met Ciska: 2c custom focus met synth ipv controller oid. Om 2b en c te combineren.
**Volgende week playtest aftekenen** (Wizard Of Oz).

_underscore voor een variabele geeft aan dat het een private member is.
Ook m_hutsie of mHutsie, krijgt ook ander kleurtje in Clion.

Wat doet inline ook alweer? (optimaliseren)

incr is increment en betekent 1 groter maken.

new & delete, memset & free ??

unsigned int wordt niet negatief?

processFrame is write, read, tick

Wat doet een #DEFINE ook alweer?

Arrays van c++ bekijken

_1.5 uur_ - Wiskunde H2, geëindigd bij polair naar cartesisch, licht begrepen met dank aan Vida.

###### Aantekeningen les Pieter:
Wat is convolutie ook alweer?

Ringmodulatie??

----

##### Woensdag:

Idealerwijs doe ik 10+ uur per week aan zelfstudie. Met de side note dat ik oplet dat het niet te veel wordt.
Vooralsnog loop ik sterk tegen motivatieproblemen aan. Er is nauwelijks wat voor nodig om me te laten slacken.
Ik heb nu pomodoro aangezet (50m) en mezelf de laatste periode van USA - Canada ijshockey beloofd voor daarna.
Of, als ik toch in de flow kom, na een 2e ronde studie.

Het geeft wat lucht dat ik nu 2b en 2c mag combineren. Ik ga mijn focus omschrijving aanpassen aangezien ik nu custom
ga met melody generation als custom.

_2 uur_ - Voorbeeld maken in Logic van mijn design en in overallDesign parameters toelichting typen. 

Ik heb nu geleerd hoe je een afbeelding in .md krijgt! (Voorbeeld in overallDesign.md)

TODO voor morgen is: 
- FX na elkaar chainen. 
- Nog eens checken of er geen nieuwe assignments zijn.
- Interpolatie opdracht checken, of ik het begrijp. / schrijven.

---

##### Donderdag:

Staat van vandaag: luteale fase. Erg ongemotiveerd. Mood: 4,5/10.

Een TODO-lijstje maken aan het eind voor de volgende dag is wel heel handig en behulpzaam; ik heb iedere dag weer het
gevoel niet te weten waar te beginnen.

unsigned int (uint) is altijd positief en wordt (bovenaan) gedclareerd mbv: 

```typedef unsigned int uint;```

_1 uur_ - Poging gewaagd om de code van Plugin-Focus te begrijpen en FX eraan toe te voegen. Erg gefrustreerd geraakt.
Ik kijk er morgen nog eens naar en als ik het dan nog niet snap vraag ik hulp. Eerst maar weer eens naar 2b kijken, of
ik pointers enzo wel kan snappen uberhaupt.

_1 uur_ - 
- Hoe werkt de audioToFile (2b)? Wordt er een file geschreven? Zo ja, waar? Bij 4 in output.csv en bij 3..?

4_sineSquareSawFinal gedupliceerd, de writeToFile eruit gehaald en 2 squares eraan toegevoegd zoals in 3_sineSquareSaw
om er een orgelgeluid van te maken.
uiUtilities in _session4 map doorgelezen en geprobeerd te begrijpen. Het lukt redelijk maar ik vind het nog lastig voor
me zien hoe ik het goed ga toepassen. Ik denk dat ik gewoon ook moet oefenen om het meer "in de vingers" te krijgen
(ha... ha...). Ik type nog steeds niet met 10 vingers en ik merk dat ik me beperkt en trager voel. Gelukkig gaat het
steeds beter met de pijn!

Vandaag heb ik alles behalve bereikt wat ik wilde bereiken. Ik zie de dingen somber in en vind het lastig om in
oplossingen te denken. Hopelijk is het morgen beter. Mood: 4/10.

---

##### Vrijdag:

Ik heb matig geslapen. Rond 5 begin ik dan te denken over oplossingen voor waar ik gister niet uitkwam en dan lig ik
wakker. Erg frustrerend. Volgens mij kwam het ook een beetje langs in mijn dromen. Het irritante is ook dat ik niet
meer echt weet wat ik had bedacht als oplossingen.

_1 uur_ - 
- Ik ga Daan een Discord sturen om te vragen of het klopt dat er voor deze week geen assignment.md is.
- IK heb in de _02_session de 1_applyEffectExample_csdlib gevonden. Ik ga die bestuderen in de hoop dat ik het beter
begrijp en ook zelf kan gaan toepassen.

- uint kan je ook schrijven als: ```int = 0u;```
- Waarom wordt in de voorbeeldcode het effect aangemaakt in de private vd header? In 2b maakten we oscillators aan
in de .cpp file? Of misschien was er toen geen .cpp en was sws alles in de header.

Ik heb geprobeerd de voorbeeldcode op mijn code toe te passen maar nu komt er een piep uit m'n plugin. Ik ga proberen
de nested forloop ook na te maken, ipv de sampleIndex en channel berekening omgedraaid te houden tov het voorbeeld.

Bij het omdraaien komt er nog steeds een gekke buzz-piep uit, dus er gaat nog steeds iets mis.

Ik heb 1_applyEffectExample_csdlib geprobeerd te draaien maar die maakt helemaal geen component... Met welke input
werkt die? Ik krijg ook dit: ```zsh: segmentation fault  ./1_applyEffectExample_csdlib```.

Ik merk dat als ik vastloop dat ik ook niet zo goed weet waarop ik dan vastloop. Ik heb het gevoel dat ik basis mis en
niet weet waar ik mee bezig ben. Misschien moet ik nog wat meer terug naar de basis. Dit voelt chaotisch en frustrerend.

---

### Week 8 (totaal 5u)
##### Maandag:
Aantekeningen les:
- lineair interpoleren bij fdbk delay & waveshaper (+ andere golf als waveshape als laatste stap/tijd over)
- Misschien tape delay? Je maakt m wobbly/drunk.
- TODO: Blokdiagrammen opzoeken/maken vd effecten. Daarna class diagrammen, audio flow overzicht is fijn...
- low pass voor anti aliasing?
- reload cmake project (bij cmakelists.txt) om te bouwen in clion.
- blueprints: settings.h write_to_file_mode (verwijst naar audiocomponent.h), we hebben .csv files gemaakt maar hoe
krijg je dat dan in een python plot?
- "indent" is de tabs-structuur
- enum?? ; elegante if-statement leren lezen en gebruiken
- Heb ik matplotlib? ander pip3 install

_1 uur_ - 
Ik ga overstappen van met Plugin_Focus werken naar met PP_C_Focus werken.

Ik snap nu waarom clion niet wilde bouwen. JUCE moet in de map staan van waaruit ik bezig ben anders kan die het niet
vinden. Logisch. Het maken is me alleen nog niet gelukt met clion. Dan krijg ik een error met liblo en arm64. Heeft
Fabian dezelfde error?

IK heb nu de PP_C_Focus klinkend. Daar kan ik een orgel in bouwen. Of eerst effecten uitproberen??
Fabian heeft me geholpen om homebrew opnieuw te installeren op de juiste manier. Het was eerst geinstalleerd automatisch
alsof het voor intell was, maar ik heb silicon. Daardoor kan ik nu clion wel gebruiken om te bouwen en maken!

---

##### Dinsdag:
_1 uur_ - Met Fabian de biquad filter geschreven. In de spectrumanalyse code van Pieter gecheckt hoe de spectrums eruit
zouden zien en vergeleken met hoe het klinkt in de cc4_filters code. Ik hoor geen spectrale verschillen?? Wel amp
verschillen. Geen idee hoe dat komt, aan Daan vragen.

Heb nu filters (FIR en IIR) door te herhalen wel weer iets meer begrepen, was weggezakt.

---
##### Woensdag:
_0 uur_ - 10 min in de bieb gezeten en daarna naar huis gestrompeld en gevloerd geweest door menstruatie.
In die 10 min wel uitgevonden waarom ik niet uit opdracht 2.13 kwam: ik moet mijn rekenmachine op radialen zetten.

---
##### Donderdag:
_2 uur_ -  complexe wiskunde dsp. Note voor 2.13 (van cartesisch naar polair): als x < 0 dan moet je 
arctan(y/x) + pi doen.
---
##### Vrijdag:
Ik ben erg ontevreden over mijn werk van afgelopen week. Het gevoel van achterlopen achtervolgt me. Ik weet tegelijk
dat ik niet veel van mezelf heb kunnen verwachten ivm menstruatie, dus dat is een dubbel gevoel. Het is mijn voornemen
om in de komende roostervrije week ook wat meters te maken.

_1 uur_ - DSP in de bieb.

---

### Week 9 (totaal 8.5u)
##### Maandag: -

---
##### Dinsdag: 

Het is de roostervrije week. Ik zit in de bieb. Ik vind het wederom lastig om mezelf ergens toe te krijgen. Tot wat dan
ook. Maar ik ga ervoor.
Doel van vandaag (en deze week): 
- DSP H2 afronden (voor zover dat gaat)
- Werkboek van Pieter doornemen om up to speed te komen met het huidige onderwerp: Poles & zero's, filters, FFT.
- Systeemeigenschappen (DSP) weer doornemen en mee oefenen.
- Overzicht/planning creëren voor CSD. En daaraan beginnen.

_2 uur_ - H2 afgemaakt, samenvatting H2 doorgenomen, toets blok b gemaakt en nagekeken. Eerste korte blik op
systeemeigenschappen geworpen.
_0.5 uur_ - Systeemeigenschappen verder doorgenomen en oefenopgaven gemaakt.

---
##### Woensdag: 

De zon schijnt, het wordt 16 graden vandaag. Het is nu 11:00. Ik had eerder willen beginnen maar dit is in principe
genoeg tijd. Eigenlijk wil ik niet binnen zitten maar de beloning van sauna vanavond is heel mooi...
Wat overblijft van gisteren is:
- Werkboek Pieter doornemen 
- Overzicht/planning creëren voor CSD

Ik begin met Pieter.
_1.5_ - Werkboek t/m blz 15 doorgenomen en geoefend met overdrachtsfunctie, amplitudespectrum en fasespectrum van een
eerste orde LTI FIR systeem.

---
##### Donderdag: 

Het is tijd voor CSD. Ik moet blokdiagrammen maken of zoeken voor mijn effecten. Daarnaast moet ik oefenen met code
en wellicht kan ik al een effect bouwen.

_1.5 uur_ - Ik bekijk de vibrato in Pirkle's boek (blz 416-418). Daar is het hetzelfde als een flanger maar dan met 100% wet en 0% dry.
Dus ik hoef voor dat effect geen wet/dry te maken dan? Zo had ik het wel bedacht in mijn proefversie.
Ik kom er nu achter dat een vibrato is opgebouwd met een feedback delay, dus die heb ik dan al. Ik vraag me af waarom
een vibrato dan 1 punt waard is en een fbck delay 2?

Nvm ik lees net dat er geen feedback nodig is voor de vibrato... net helemaal een diagram gebouwd... Ik kan ze uit
elkaar trekken en dan heb ik ook die van de feedback delay. (C++ code blz. 422.)
Simple delays: blz. 390
Non-linear processing: blz. 535, 584pdf
Misschien kan ik voor asymmetrsche waveshaping gaan? (blz. 549, 598pdf)

_1 uur_ - Waveshaper diagram gemaakt (issie overtuigend..? idk) en de diagrams gecommit en gepusht.
Kleine blik op reverbs geworpen, zou evt nog kunnen later. Maar wel meer step up. Ik moet eerst C++ begrijpen...

Ik kijk naar de diagram van 2b. Moet ik ook een additive synth object aanmaken? Of is 3 squares in de callback priem?

___
##### Vrijdag:

Diagrams zijn gemaakt. Tijd om naar code te kijken om dat beter te leren begrijpen. Het klikt allemaal nog niet volledig.
Doel voor vandaag: PP_C_focus een square laten spelen en daarna er een synth (orgel) van maken.

_2 uur_ - 
In de prepare vd callback gebeurt: wave.prepare() en wave.setFrequency().
In de process vd callback gebeurt: wave.setFrequency() (alweer) en wave.getSample() en wave.tick()

Hier heb ik wave = sine veranderd naar wave = square in de hoop dat ik nu een square ga horen. Hopelijk kan ik er in de
toekomst wave = oscillator van maken.

Ik heb nu een uur geprobeerd die PP_C_Focus te begrijpen en aan te passen om er een orgel van te maken. Het lukte me at
some point wel om er een square uit te krijgen maar nu geen orgel. Ik raak erg gefrustreerd omdat ik het idee heb geen
overzicht te hebben. Ik weet echt niet waar ik mee bezig ben, voor m'n gevoel. Het komende uur wil ik even terug naar
blok b, naar de simpele synth. Om te begrijpen wat daar gebeurt. Misschien lees ik nog even wat code van Semuel of Vida.

Code lezen van anderen brengt me nog niet heel ver dus ik ben maar weer terug gegaan naar _session4 van blok b.
Ik denk dat ik pointers nu ietsje beter begrijp dan eerst? Ik snap nu ook dat de UI eigenlijk gebeurt via de Callback.cpp
van Semuel en Vida, mbv functies uit de UIUtils. Ik was daar erg lang naar aan het zoeken. Ik snap nog niet hoe en 
wanneer die Callback wordt aangeroepen om al die info te verzamelen.

---
### Week 10 (totaal 8.5u)
##### Maandag: 

CSD les
_0.5_ - 2_enum_choices gelezen. Nog niet echt begrepen. Slechte focus.
CodeClinic filters2: Ik heb een biquad filter 2nd order LPF gemaakt in Pieters spectrum analyser. Op pagina 272 (320pdf)
van Pirkle staan de formules die ik heb gebruikt en in dat hoofdstuk staan nog veel meer formules om coefficienten te
berekenen om specifieke filters mee te maken. Ik weet nu dus hoe ik filters moet maken, of in ieder geval de wiskunde
erachter. Het implementeren is een ander ding.

Het is me nu ook gelukt om de filter in de cc4 hoorbaar te krijgen. Dat is wel nice. Nu nog classes begrijpen...

---
##### Dinsdag:

_0.5_ - Nog eens 3_enum_choices doorgelezen en ik begrijp het eindelijk een beetje. Begonnen aan 1_melody doorlezen.
Ik snap nog niet waar het nou allemaal begint, waar het in gang wordt gezegd. Ik zie dat er een callback wordt aangemaakt
en van daaruit een square en een melody, maar waar gaan dan al die functies zoals prepare lopen? Die lijn heb ik nog niet
gevonden.

---
##### Woensdag:

_3.5 uur_ - Static members en functions herhaald, het landt nog niet mega. Ook weer naar pointers gekeken, nog niet overtuigd, maar
het lijkt langzaam te komen.

Het lukt me maar niet om squares toe te voegen aan files zoals 1_melody en PP_C_Focus... Ik snap nog niet waarom, maar
ik ga nu even kijken naar waarom PP_C_Focus wel stereo is en 1_melody niet.

In de nested forloop in de callback zijn de samples en de channels omgedraaid. Ik had dit ooit al geprobeerd en het lukte
me niet dus er moet meer zijn... Ik kan even niks anders vinden dus ik probeer deze truc nu bij 1_melody, kijken of het
me lukt. Niet gelukt. Het klinkt alsof er niks is veranderd... whyyyyy?

Okee nvm het is nu wel gelukt. Ik moest dus toch in de main.cpp ```juceModule.init (1, 1);``` veranderen in 
```  juceModule.init (1, 2);``` zodat er 2 outputs zijn voor JUCE. Ik dacht dat ik dit eerder ergens anders ook had
geprobeerd en dat dat niet lukte, maar nu iig wel hier. Even kijken of dit me ook bij mySimpleSynth lukt... Gelukt!

Stereo, check. Oscillatoren stapelen, niet zo check. Heb ik daar een synthobject voor nodig??
Ik gebruik dat niet in mySimpleSynth en daar lukt het stapelen wel..? Maar whyyyy...

Ik kom daar niet uit, dus ik ga even kijken naar 5_polymorphism. Dan heb ik session4 zo ongeveer gehad.
HAND UPDATE: ik type vandaag met 5 vingers aan de linker hand. En ik heb gebeld met het ziekenhuis en moet
misschien mijn rechter even laten checken daar.

Vraag over 5_polymorphism: waarom zou je een Oscillator pointer aan willen maken?
*Antwoord:* Omdat je met een class pointer makkelijker(?) kan switchen tussen in dit geval sine en saw; je verandert
alleen even het adres van de pointer en je hebt nieuwe info, of in dit geval voer je dan meteen een nieuwe functie uit.
NOTE: Ik weet nog steeds niet waarom dit de voorkeur verkrijgt boven de losse sine.calculate() en saw.calculate()...?

Ik lees weer over references en pointers en dit zijn belangrijke verschillen:
- You cannot have NULL references. You must always be able to assume that a reference is connected to a legitimate piece
of storage.
- Once a reference is initialized to an object, it cannot be changed to refer to another object. 
Pointers can be pointed to another object at any time. 
- A reference must be initialized when it is created. Pointers can be initialized at any time.

---
##### Donderdag:

Het is alweer donderdag. Ik heb net afgewassen en heb nu wat meer pijn rechts. We gaan het ermee doen.
Even overzichtelijk krijgen wat ik vandaag ga doen. Ik denk dat het nice zou zijn om effecten te gaan bouwen maar
daarvoor moet ik ook weten hoe ze te implementeren zodat ik weet wat ik moet returnen om het toe te kunnen passen.
Of ik bouw eerst een effect en kijk daarna hoe ik dat erin ga bouwen. Hmm...

_1.5 uur_ - 
Dit is nice:

_"Using Initialization Lists to Initialize Fields
In case of parameterized constructor, you can use following syntax to initialize the fields −"_
```
Line::Line( double len): length(len) {
   cout << "Object is being created, length = " << len << endl;
}
```

_"Above syntax is equal to the following syntax −"_

```
Line::Line( double len) {
   cout << "Object is being created, length = " << len << endl;
   length = len;
}
```

Want dit begreep ik maar niet! En nu maakt het meer sense.

Ik snap nu ook weer even opnieuw waarom je SIZE onderaan in je enum doet omdat je de elementen uit een enum
telt vanaf 0 dus als de laatste "size" heet is dat ook meteen gelijk aan het aantal elementen in je enum:

```angular2html
  enum Waveform{
    SINE, //0
    SAW   //1
    SIZE  //2
  };
```

Dat was ik weer even vergeten en snap ik nu weer :) goeie sessie.

Ik ben (mbv Vida's code) aan het proberen een additiveSynth class toe te voegen aan mijn code die straks alle
oscs bij elkaar optelt zodat ik dat straks weer kan bewerken met een waveshaper. Ik merk dat ik Vida's code nu
een stuk beter kan volgen en heel fijn en logisch vind. Thanks Vida <3

_0.5 uur_ - Nog in bieb Amersfoort gezeten om mijn AdditiveSynth class te schrijven voor mySimpleSynth.

---
##### Vrijdag:
_1 uur_ - Verder gewerkt aan de AdditiveSynth, getest, errors weggewerkt, alleen nog geen geluid... dat moet
ik nog fixen, maar eerst het probleem vinden...

Ik heb minder gedaan dan ik wilde vandaag maar ik heb kort geslapen en moest vroeg naar de tandarts. Daarna heb ik
geprobeerd een dutje te doen en toen heb ik hardgelopen. Vanavond heb ik ook een programma, dus ik moet morgenochtend
maar weer strijden dan. Misschien dat ik dan het geluidprobleem kan vinden. Zou nice zijn.

---
##### Zaterdag:

_1 uur_ - Tijd om overzicht te krijgen van wat er wanneer gebeurt of hoort te gebeuren in mijn code, voor trouble shooting.
Hand update: het typen met de linkerpink lijkt elke dag beter te gaan. Ik denk dat die weer sterker wordt.

- Stap 1 (main): programma wordt opgestart. Vanuit de main wordt de callback geactiveerd. 
- Stap 2 (callback.h): In de callback wordt een additiveSynth aangemaakt.
- Stap 3 (additiveSynth): Er worden 3 oscs pointers gemaakt naar 3 nieuw aangemaakte squares.
- Stap 4 (callback): Ik snap niet precies hoe en waar de prepare en de process van de callback worden aangeroepen, maar
het is nu de beurt aan de prepare. In de prepare wordt de samplerate ge-set vanuit de input vd main (44100).

Misschien dat het hier misgaat? Moet de samplerate van de Oscillator ook ge-set worden hier? Of erft die automatisch
van callback? Goed om te proberen misschien. Vida preparet naast de callback alleen de melody met samplerate zie ik.

...Gecheckt mbv cout, de samplerate klopt in de Oscillator. Hoe dat kan weet ik niet...

- Stap 5 (callback): de prepare activeert setFrequencies van additiveSynth.
- Stap 6 (additiveSynth): setFrequencies activeert setFrequency per oscs pointer. (cout bevestigt dit)
- Stap 7 (callback): organ.getSample() wordt geactiveerd
- Stap 8 (additiveSynth): activeert in getSample() alle getSample()s van de oscs pointers en telt ze bij elkaar op en
normaliseert het totaal. Dit is nu "sample".
- Stap 9 ...

---
### Week 11 (totaal 10u)

##### Maandag:
Les.

```
//Portamento van 500 naar 1000 delayInSamples in psuedo
int startValue = 500
int targetValue = 1000
int step = 5                //hoe snel je van start naar target wil
bool notDone = true
int value = startValue;

tick(){
  if (notDone)
    value ++;
    
    if (value == targetValue || value > targetValue) value = targetValue, notDone = false;
}
```

Totaal verkeerd begrepen hihaho.

_1 uur_ - Mijn mySimpleSynth geluid probleem is gefixt in de les. Ik vermenigvuldigde met 0 omdat ik een int door een int deelde.
0.3 wordt 0, ik had met floats moeten werken. We kunnen door.
Ik was daar bijna met mijn eigen trouble shooting, echt bijna.

Wat moeter nog allemaal gebeuren?
Misschien wordt het tijd dat ik mijn FX class ga maken. (maar hoe)

- FX class
- Circular Buffer begrijpen en toepassen
- FXs
- FXs koppelen aan macro
- Melody op het eind
- Tijd over? -> ADSR

Ik heb de Effect class en waveshaper toegevoegd! En het werkt, het orgel vervormt, dus dat is top.
Nu kan ik eigen *effecten bouwen*, *doorpiepen/testen* en *uitproberen* met het orgel!

Maar misschien eerst de circular buffer begrijpen, zodat ik delays kan bouwen. Ik ga het nodig hebben voor de feedback 
delay, vibrato en evt de biquad die ik evt kan gebruiken voor bijv een lopass.

---
##### Dinsdag:

_1 uur_ - Project methodes: (interesssant voor plannen)
SCRUM, agile methodiek, kanban

- trello
- asana
- jira

Ik wil dat mijn vibrato een LFO heeft: sample = sin(M_PI * 2 * phase);
Die moet de numDelaySamples aanpassen. Dit gebeurt binnen een bepaalde range: min - max
//INTERPOLEREN!!!!!!!!!! Meh

---
##### Woensdag:
Het is me niet gelukt om een vibrato te bouwen. Ik krijg steeds errors, zelfs al laat ik de class nog niks doen. Ik ga 
nu uitzoeken hoe dat zit.

Ik kwam er niet uit. Daan heeft me geholpen. Blijkbaar moet je een functie die in je header staat ook in je cpp laten
terugkomen anders kan je een linker error krijgen. Ik had:
```
Undefined symbols for architecture arm64:
  "Vibrato::applyEffect(float const&, float&)", referenced from:
      vtable for Vibrato in vibrato.cpp.o
ld: symbol(s) not found for architecture arm64
error: linker command failed with exit code 1 (use -v to see invocation)
```
_2 uur_ - Ik heb een lfo gecreëerd voor de vibrato. Die werkt. Ik heb wel nu een static samplerate meegegeven aan die
lfo. Misschien een TODO voor later om dat netter te maken.

Vibrato is werkend!! Het klinkt alleen voor geen meter.
Op dit moment heeft 'ie een lfo met een statische frequentie. Die moet later wel aanpasbaar zijn.

TODO's:
- LFO freq aanpasbaar maken
- Melodiegenerator maken
- Checken of de inheritance (OOP) nu klopt --> ik roep niet vibrato.processFrame aan maar delay2, kan dat via vib?
- Omzetten naar PP_C_Focus, met knop werken.
- Alle TODO's die ik in de code heb gezet
- Alle code doornemen om te cleanen

Oude todo's toevoegen?? Ik ben ze even kwijt.

---
##### Donderdag:
_2 uur_ - Waar had ik ook alweer staan wat de eisen zijn van een vibrato? Way back.
"Pirkle's boek (blz 416-418)"

Blz. 420 zegt: 
- min-delay = 0
- max-delay = 3-7 ms
- wet = 100%
- dry = 0%
- feedback = 0
- LFO = sine

Nu kan ik de delay preciezer gaan instellen, het klinkt namelijk nog niet als een vibrato. Ik kijk ook even naar de
dryWet. Die lijkt al goed te staan.

1 sec = 44100 samples;
1 ms = 44.1 samples;

?????? Ik heb de lfo in setLfo vermenigvuldigd met een nieuwe parameter genaamd modDepth. Ik krijg hele rare getallen
daaruit en als ik het een float maak krijg ik zelfs "nan", not a number. Als ik modDepth vervang voor gewoon 22.0f dan
gaat de berekening goed. Whyyyyyyy???

Rare clicks als lfo = 0; Dit gebeurt niet als we niet lager komen dan 1 dus ik maak de "modDepth" 21.0f. 

Het klinkt ook nog niet echt mooi, een beetje phasey, ik moet denk ik interpoleren en het evt stereo maken.

Wat er met modDepth gebeurt, gaat ook raar met parameter lfoFreq. Als ik die een waarde geef in de headerfile leest de
cpp 'm hoe dan ook uit als 0.7... Ik snap niet waarom. 

Okee ik heb de vibrato weer werkend, het was een boel gedoe en ik snap niet wat er mis ging steeds. Nu werkt het iig
weer en ik ga er niet meer aanzitten, tenzij ik 'm nog stereo wil maken of toch de modDepth en de lfoFreq wil kunnen 
aanpassen, wat wel het idee was. Maar dan heb ik echt Daans of iemands hulp nodig.

Side note: wat ik ook nog zou kunnen doen bij tijd over (delulu) is geen lelijke squares gebruiken maar squares maken
door sinussen te stapelen, wat vrij goed kan met al 3 sinussen.

Wat ik zou moeten doen is een wavetable voor de waveshaper, maar misschien kan ik beter gewoon een biquad bouwen?

Voordat ik ga proberen om de sinus berekening van de vibrato door de sine class te laten doen, ga ik eerst deze versie
van mySimpleSynth pushen naar git. Ik zie dit namelijk alweer helemaal fout gaan...

ik loop tegen een vergelijkbaar probleem aan als ik de vibrato de sine laat calculaten. De frequency wordt wel geset tot
6 in de constructor van Oscillator.

---
##### Vrijdag:
_1,5 uur_ -  Het is met gelukt door een pointer te maken van sine. Het klinkt alleen wel anders dan de vorige versie,
naar mijn idee. Het klinkt weer meer als een phaser dan een vibrato.

... ik moest de * amplitude uit sine calculate nog weghalen... NU DOET IE HET WEER NICE!!!

Nu wil ik:
- vibrato.processFrame() ipv delay2.processFrame().

Veel gedoe, Daan helpt me. vibrato.cpp zegt dat ik delay.h niet heb include maar dat heb ik wel en het build ook.
De feedback had ik per ongeluk even op 1 staan, dat ging mis, staat nu weer op 0!!!

Ik weet even niet wat nu belangrijker is, melodiegeneratie (grooooot onderdeel) of lfo aanpasbaar maken.
Ik moet ook nog alles overzetten in de PP_C_Focus... om die knop te checken.

_2,5 uur_ - 

---MELODIEGENERATIE---

- Melodie class
- Melodie generatie class
- Note class

Gebruiker kiest begin note en toonsoort (majeur, mixo).

Ik ben stap voor stap de pseudocode die ik met Ciska heb gemaakt aan het omzetten in echte code, als eerste versie.

Ik probeer mijn eerste stuk code uit in mijn try_outs file. Daar lijkt het eerst goed te gaan en vervolgens mis.
Dit is een voorbeeld van een lijst die gemaakt wordt:
```
0
3
2
4
5
8
7
9
8
10
11
14
146106280
2
15
2
146106280
2
-85243580
1070775398
146106280
2
146106280
2
-1889937825
1072106068
8
0
32
0
1829729488
1
```
Het zou moeten stoppen na 14.

NVM ik gaf de verkeerde opdracht om te printen, de lijst wordt wel juist aangemaakt!
Zo moet ik printen:
```
for (int i = 0; i < (sizeof(list)/sizeof(list[0])); i++) {
            std::cout << list[i] << std::endl;
        }
```
Op die manier bereken je de lengte vd lijst, niet met sizeof(list).

Ik dacht dat ik het had gefixt, maar dat is nog niet helemaal waar. De lengte van de indexlist moet het aantal keer zijn
dat er een curNote toegevoegd kan worden, maar dat wordt random bepaald en is pas bekend aan het einde van die cycle.
Tenzij ik zelf bepaal hoe lang die wordt, maar dan zou ik de kortst mogelijk combi moeten aanhouden en dat ik zonde.
Alle elementen van een lijst die ik niet aanpas zijn trash, dat moet ik verkomen. Kan ik die nog verwijderen als ze niet
meer nodig blijken? Want cpp kent geen append heb ik gezien. 

Ik zou de overige waarders negatief kunnen maken en dan later selecteren welke van pas komen. Ik kan al aan incr zien
hoeveel er is toegevoegd. Als incr = 10 dan zitten er 11 elementen in de lijst van waarde.
Dus als mijn maximale grootte bijv 20 is, moet ik 20 - (incr + 1) verwijderen.

Hoe ik dat doe, daar kom ik nog niet helemaal uit. Moet ik pointers gebruiken?
Ik bewaar het voor later.

---

### Week 12 (totaal 2u)

##### Maandag:
_0.5 u_ - Ik heb een test gedaan en bovenstaande klopt. Er moet een nieuwe list aangemaakt worden met de lengte van incr + 1.

De indexList is af. Volgende stap is met de indexList de waardes uit een ladderList aflezen.

Majeur 7 = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]

Huidige stand van zaken: ik heb een melodyGenerator die een melodielijst maakt met midi waardes.
Next step = mtof!!!!!!

---
##### Dinsdag:
TODO:
- mtof
- playTune met noteDur etc.

_1.5u_ - Gekeken naar Melody en Note uit voorbeeld. De voorbeeldmelodie getest, werkt! Nagedacht over hoe ik mijn eigen
melodie kan afspelen daarmee. Daar loop ik nog op vast.

---

### Week 13 (totaal 5u)
##### Maandag:
Tijd voor de eindsprint.
Ik ben er even een weekje ziek uitgeweest dus ik ben even kwijt waar ik was. I love deze documentatie.
___

##### Dinsdag:
_1 uur_ - Het schiet niet op. Ik heb bij elkaar opgeteld gister en vandaag een uurtje eraan kunnen concentreren, heel
gefragmenteerd.

___
##### Woensdag:
_2 uur_ - Ik loop nu aan tegen dat ik van de melodylist, wat gewoon een lijst met getallen is, een object list wil maken die ik
de waarde van de melodylist wil meegeven in de constructor. Dat lukt me nog niet zomaar.
---
##### Donderdag:
_1.5 uur_ - Aan het proberen m'n segmentation fault op te lossen samen met Daan maar ik kom er niet uit... HEEL
FRUSTREREND.
Uiteindelijke oplossing: int* indexList is nu geen pointerlist meer maar een vector. De int* melodyList is nu geen 
pointerlist meer maar gewoon een int! Super handig en fijn en beter. Het lijkt te werken.

Volgende stap: NUM_NOTES aanpassen naar indexListSize.

_0.5 uur_ - NUM_NOTES aanpassen is gelukt. Af en toe kwam er toch nog een 15 in de indexList die er niet in hoort dus 
ook dat heb ik gefixt (indexList[incr] < range - 3 ipv <=). Ik heb de waveshaper en de delay er ook weer op gezet.
Het liefst ga ik volgende keer aan de slag met mijn biquado. Daarna moet ik de parameters nog aanpasbaar maken in lijn
met het bewegen van de knop. Dan ben ik bijna klaar denk ik..?
___
##### Vrijdag:
Voor de biquad heb ik 4 delays nodig:
1x feedback = 0, numDelaySamples = 1, maxDelaySize = 2, dryWet = 1
1x feedback = 0, numDelaySamples = 2, maxDelaySize = 2, dryWet = 1
1x feedback = b1, numDelaySamples = 1, maxDelaySize = 2, dryWet = 1
1x feedback = b2, numDelaySamples = 2, maxDelaySize = 2, dryWet = 1

---

### Week 16 (totaal: 2u)
##### Maandag:
Ik heb weer 1 hand...

Midas raadt me af om delays aan te maken voor de biquado. Ik denk dat dat wel de meest nette manier zou zijn want een
filter is een delay. Maar het kost wel meer tijd want ik weet niet precies hoe ik dat zou kunnen fixen.

Ik ben in de les begonnen aan de biquado

---
##### Dinsdag:

---
##### Woensdag:

---
##### Donderdag:

---
##### Vrijdag:
_2 uur_ - Ik heb een vraag aan Daan. Want hoe kan het dat ik in een functie in een cpp, bijv een void, geen aanpassingen kan
maken aan variabelen in de header die ik vervolgens weer kan gebruiken in een andere functie in die cpp. Alleen met
een setter lijkt de variabele echt te veranderen. Ik schrijf even een proefschriftje om dit beter te leren begrijpen.


Na het zelf bouwen van dat voorbeeldje merk ik dat het toch niet nodig is om een setter te gebruiken. Ik denk dat dat
wellicht alleen geldt voor wanneer een waarde private staat..? Of nee, ik heb die waardes private staan en het lijkt
niks uit te maken. For some reason werkt het nu en deed ik eerder iets fout.

Ik heb de biquado werkend! Het is een 2e orde LPF van blz 271 van Pirkle.

Klopt het dat ik nu alleen nog UI moet toepassen, de knop moet koppelen en mijn code moet opschonen? Volgens mij wel.
Dan nog een presentatie! DUS:
- UI              (voelt medium groot 3/5)
- Knop koppelen   (voelt erg groot 5/5)
- Schone code     (voelt medium groot 3/5)
- Presentatie     (voelt redelijk groot 4/5)

Waar te beginnen?
Ik denk dat die knop koppelen het meest ingewikkeld is, misschien moet ik daar vragen over stellen.

---
### Week 17 (totaal: 3u)
##### Maandag: -

---
##### Dinsdag: 
_3 uur_ - Tijd om de knop te koppelen. Ik heb het met Daan gehad over hoe ik dat moet doen. Loopback lijkt de handigste tool.
Ik zou niet weten wat ik zonder Daan had gemoeten. Held.

Ik loop aan tegen het toepassen van mijn fx in de plugin.
Het lukt me om te beginnen al niet om het stereo te maken omdat ik die getNextBlock code niet helemaal begrijp. 
Dit zorgt voor een crash van Logic:

```
for (int sample = 0; sample < buffer.getNumSamples(); ++sample){
    sample = inputChannel[sample];
    filter.processFrame(sample, shapedFilteredSample);
    outputChannel[sample] = shapedFilteredSample;
}
```
En dit zorgt voor weirde noise ipv een werkend filter:
```
for (int sample = 0; sample < buffer.getNumSamples(); ++sample){
    filter.processFrame(inputChannel[sample], shapedFilteredSample);
    outputChannel[sample] = shapedFilteredSample;
}
```
En op de manier van Vida wordt ie ook weer "unstable":
```
for (int sample = 0; sample < buffer.getNumSamples(); ++sample){
  waveShaper[channel]->processFrame(inputChannel[sample], shapedSample[channel]);
   outputChannel[sample] = shapedSample[channel];
}
```
Samen met Daan opgelost, ik snepte het njet.

---

### Week 19 (totaal 9u)
##### Maandag: 
_1.5 uur_: Er zit een roostervrije week op. Een week waarin ik niet heb gewerkt in de hoop met nieuwe energie in schoolwerk te
kunnen duiken. Ik moet zeggen dat ik wel weer wat frisse motivatie voel, naast de immer aanwezige angst voor falen.

Als ik terugkijk naar mijn aantekeningen zie ik dat het nu tijd is voor het koppelen van de parameters.
Parameters die ik wil koppelen:
- Vibrato wet/dry (0-1 van 0-0.5 knob)
- Vibrato LFO speed (5-10 van 0.5-1.0 knob)
- Waveshaper wet/dry (0-1 van 0.2-0.8 knob)
- Delay wet/dry (0-0.6 van 0-1 knob) ???
- Delay feedback (0-0.8 van 0.5-1.0 knob) ???
- Filter wet/dry (0-1 van 0-1)

Wat de delay betreft is het nog maar kijken wat mooi klinkt qua parameters.

Het wordt in ieder geval belangrijk om **interpolatie** toe te passen!! De scaling interpolatie weliswaar.

Het koppelen van het filter is het makkelijkst omdat het 1 op 1 is met de parameter. En dat ik gelukt!!!!!
Nu even dat code clinic documentje van interpolatie erbij pakken.

Ik ga linMap maar eens proberen, ik werk toch alleen met lineaire veranderingen.

Vibrato wet/dry.
if parameter => 0.5; parameter = 0.5
parameter 0-0.5 * 2 = 0-1.0
GELUKT! (nog zonder linMap)

Die van de vib speed lijkt ook niet zo lastig. Maar dat heb ik verkeerd zie ik want ik heb nog geen functie voor het
aanpassen van de LFO speed in de vib class zelf. Dit heeft wel net iets minder prio en voor de overige 3 heb ik wel
interpolatie nodig dus misschien dat ik daar eerst aan ga.

Waveshaper 0.2 - 0.8
if parameter < 0.2 ; waveShaperParameter = 0;
else if parameter > 0.8 ; waveShaperParameter = 1;
else linMap

Nee ik kom er nu achter dat linMap bij deze niet werkt. Ik moet waarschijnlijk mapInRange hebben.

  	float partial = (value - fromLow) / (fromHigh - fromLow);
		float delta = toHigh - toLow;

  	return toLow + delta * partial;

float partial = (parameter - 0.2) / (0.8 - 0.2);
float delta = 1 - 0;
waveShaperParameter = 0 + (delta * partial);

GELUKT!!

Op naar de delay. Daarvan zou de dry/wet wel met de linMap moeten kunnen?
Yessss gelukt!!!
Nu de feedback van de delay.
Ook gelukt en meteen de vorige code iets opgeschoond. Ik vind deze functie alleen niet zo mooi klinken.

Voor de volgende stap: Vibrato speed!

##### Dinsdag: 
_2 uur_: Het is me nu ook gelukt om de vibratospeed aan te passen. Het bleek niet heel ingewikkeld te zijn.
Next step: melodiegeneratie UI geven en de FX eruit halen.

Welke UI wilde ik ook alweer hebben...:
- Key selection
- Scale selection
- Direction selection (up/down)

Ga ik die allemaal doen? Wie weet.

De scale selection is misschien nog wel het simpelst. Ik kan het in dit stukje code denk ik wel aanpassen:

```  
for (int i = 0; i < indexListSize; i++) {
    melodyList = ladderList[indexList[i]];
    tempNotesVector.emplace_back(melodyList);
  }
```
Door er het volgende van te maken: (pseudo)

```  
if (scaleSelection == maj){
  for (int i = 0; i < indexListSize; i++) {
      tempNotesVector.emplace_back(ladderListMaj[indexList[i]]);
    }
  } else {
  for (int i = 0; i < indexListSize; i++) {
      tempNotesVector.emplace_back(ladderListMix[indexList[i]]);
    }
  }
```

Met ladderListMaj[] = majeur toonladder en ladderListMix[] = mixo toonladder in de .h file.

Dit ga ik morgen toepassen.

---
##### Woensdag:
_1.5 uur_ - Het is met in 1.5u gelukt om de gebruiker een scale te laten kiezen, maj of mixo.
Of ik dat nu netjes aan het doen ben is de vraag maar ik kan het altijd nog opschonen. Voor nu moet het gewoon werken.

_1 uur_ - Next: Toonsoort laten kiezen.

Ik werk momenteel in toonsoort D. Ik ga dat veranderen naar C, vanaf midinoot 48. Dan geef ik de gebruiker de volgende 
opties:
1: C
2: C#/Db
3: D
enzv.

Dit is nu ook gelukt!
Voor de volgende keer: 
- Direction selection
- Clean up utilities.cpp / make more efficient

_0.5 uur_ - Het lukt met niet om te reversen. Ik blijf tegen dingen aanlopen. Wat ik morgen wil proberen:
om duplicate code te verkomen in de while loop niet indexList[i] < range - 3 te gebruiken maar misschien werken met een verschil.
Het mag bij omlaag niet onder -14 komen. Dus dan zou het eiglk > range + 3 moeten zijn maar je kan die pijl niet 
zomaar flippen. Daar moet ik iets op vinden morgen.

---
##### Woensdag:
_0.5 uur_ -
indexList[incr] - range <= -3 || indexList[incr] - range >= 3;

Het is me eindelijk gelukt om een reversed lijst te maken. Het resultaat is wel funny!
Straks ga ik de UI hiervoor aanmaken.

_1 uur_ - Ik heb de keuzes werkend! Het lijkt er alleen wel op dat er nog wat tijd gaat zitten in de validation op
orde krijgen. Die tript 'm nu bij het invullen van een woord ipv getal en ik heb nog duplicate code. Verder werkt
het nice! Ik denk dat ik daar vanavond nog wel een uurtje aan zit misschien. Misschien valt het mee.

_0.5 uur_ - Het is me gelukt om de validatie apart te doen en om te checken dat er geen andere dingen binnenkomen dan
ints!
In principe is het af. Mijn huisgenoot heeft geplaytest.
---
##### Donderdag:
_0.5 uur_ - Extra aanpassingen na playtests en begin presentatie.