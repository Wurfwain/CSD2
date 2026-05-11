# Overall design deliverable
### Chosen focus:
In overleg met Ciska kies ik voor de custom focus, waarbij mijn custom de melody generation van 2b is die ik nog moet 
inhalen. Zo kan ik 2b en 2c combineren zonder al te veel achter te blijven lopen.

### Chosen effects:
De custom focus betekent 3 FX punten minimaal. Voor 2b maak ik een simpele organ synth mbv square waves, dus ik kies
voor effecten die ik leuk aan vind sluiten bij dit geluid.
- Het lijkt me tof (en haalbaar) om en een __vibrato__(1) te maken, omdat het 1 van mijn favoriete effecten
is en omdat het mooi samengaat met een organ. I like it dreamy!
- De __waveshaper__(1) is voorbij gekomen in de les en spreekt me ook aan.
Door zowel de simpliciteit als het karakter. Overstuurde orgels zijn niet ongebruikelijk maar wel heel vet.
- Een mooie derde toevoeging lijkt me een __feedback delay__(2). Enerzijds om het extra dreamy en groots te maken en
anderzijds omdat ik denk dat het bouwen daarvan haalbaar moet zijn voor mij met de tijd die ik heb. Als ik tijd
overhoud kan ik altijd nog naar nieuwe FX kijken maar voor nu: KISS.


### Parameters:
In de afbeelding hieronder is weergegeven hoe de parameters veranderen met het aanpassen van de macroknop.
- De onderste lijn (groen) is de __macro__ en die loopt van 0 naar 1.0. Bij 0 staat het effect uit, bij 1.0 is die 
volledig aan.
- De bovenste lijn (paars) is de __wet van de delay__. In het voorbeeld loopt deze tot 64% maar ik zal zien hoe dat
in mijn ontwerp uitpakt. De stijging loopt in ieder geval gelijk met de macro.
- De 2e lijn van boven (lichtblauw) is de __snelheid van de vibrato__ in Hz. Deze neemt toe vanaf ongeveer 0.5
van de macro.
- De 3e lijn van boven (oranje) is de __vibrato diepte__. Deze bereikt de 100% al rond de 0.6 van de macro.
- De 4e lijn van boven (ook groen) is de __vervorming van de waveshaper__. In het voorbeeld is een drive gebruikt maar
het idee is vergelijkbaar. De vervorming is op de max (de max die ik wil, misschien niet het maximaal mogelijke) rond
de 0.8 van de macro. Je ziet ook dat de vervorming pas vanaf ongeveer 0.1 van de macro begint.
Misschien laat ik die in mijn ontwerp wel gewoon van 0 tot 1 lopen ipv 0.1 tot 0.8, we gaan het zien.
- De 5e (roze/paars) is de __feedback__ van de delay. Deze komt pas in op 0.5 van de macro en ik zal moeten playtesten
om te zien tot hoe hoog ik die daadwerkelijk ga laten lopen. In het voorbeeld vond ik 84% goed werken.

![parameters](parameters.png "parameters")