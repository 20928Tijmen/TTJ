# RUSH HOUR


**Rush Hour** is een spel waar men een rode auto heeft die in de richting van een uitgang is gepositioneerd. Eén probleem: er zijn allerlei auto's die de weg van de rode auto versperren. De auto's variëren in grootte en in richtingen. Sommige auto's kunnen alleen van boven naar beneden en vice versa, terwijl andere auto's alleen van links naar rechts en van rechts naar links kunnen. Geen van de auto's mag gedraaid worden. Ook mogen geen van de auto's over elkaar heen gaan.

**Het uiteindelijk doel** van het spel is dat de versperrende auto's op bepaalde manieren zo aan de kant worden geschoven, dat de rode auto naar de uitgang kan gaan. Daarvoor gebruikt men 'moves': bewegingen van 1 stap per keer, waarbij een auto of naar voor, of naar achter kan gaan.

**Het uiteindelijke doel** van de case is dat men met een programma in *Python* het spel **Rush Hour** kan oplossen door middel van algoritmen.

# De ALGORITMEN

**Het eerste algoritme** betreft de baseline van dit project. Dit gaat om een **Random** algoritme.

De aanpak van het **Random** algoritme gaat als volgt:

Het programma kiest, op basis van *import random* in *Python* een willekeurige auto op het bord. Daarna kiest het een willekeurige beweging: de keuzes betreffen **-1** (een stap naar links bij horizontale auto's en een stap naar boven bij verticale auto's) en **1** (een stap naar rechts bij horizontale auto's en een stap naar benden bij verticale auto's). De auto houdt *GEEN* rekening met bewegingen die niet zijn toegestaan. Als je auto A naar rechts wil laten gaan terwijl deze pal naast auto B staat, dan mag dat dus niet. Het algoritme houdt daar dus geen rekening mee, en herhaalt het script net zo lang totdat de rode auto (auto X) tegen de uitgang staat.

**Het tweede algoritme** betreft het **RandomLegalMove** algoritme. Dit is een vervolg van het **Random** algoritme.

Bij **RandomLegalMove** wordt er op basis van *import random* in *Python* een willekeurige auto gekozen op het bord. Het verschil is dat de code er wel voor zorgt dat er alleen geldige moves kunnen worden gedaan: als de auto alleen naar links kan, gaat de auto naar links. Kan een auto alleen naar voren (omdat er links van de auto een andere auto staat), dan gaat die naar voren,

**Het derde algoritme** betreft het **RandomLegalRepeatMove** algoritme. Dit bouwt voort uit **RandomLegalMove**.

Bij **RandomLegalRepeatMove** kiest de code met *import random* een willekeurige auto op het bord. Het verschil met **RandomLegalMove** is dat er een geldige move wordt gekozen, waarna het algoritme deze geldige move blijft herhalen totdat deze niet meer geldig is. Als het algoritme een auto naar rechts wil schuiven, en er zijn rechts van die auto drie plekken vrij, dan zal de auto drie keer naar rechts worden geschoven.