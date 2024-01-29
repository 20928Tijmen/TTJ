# RUSH HOUR


**Rush Hour** is een spel waar men een rode auto heeft die in de richting van een uitgang is gepositioneerd. Eén probleem: er zijn allerlei auto's die de weg van de rode auto versperren. De auto's variëren in grootte en in richtingen. Sommige auto's kunnen alleen van boven naar beneden en vice versa, terwijl andere auto's alleen van links naar rechts en van rechts naar links kunnen. Geen van de auto's mag gedraaid worden. Ook mogen geen van de auto's over elkaar heen gaan.

**Het uiteindelijk doel** van het spel is dat de versperrende auto's op bepaalde manieren zo aan de kant worden geschoven, dat de rode auto naar de uitgang kan gaan. Daarvoor gebruikt men 'moves': bewegingen van 1 stap per keer, waarbij een auto of naar voor, of naar achter kan gaan.

**Het uiteindelijke doel** van de case is dat men met een programma in *Python* het spel **Rush Hour** kan oplossen door middel van algoritmen.

# DE ALGORITMEN

**Random**: Het programma kiest, op basis van *import random* in *Python* een willekeurige auto op het bord. Daarna kiest het een willekeurige beweging: de keuzes betreffen **-1** (een stap naar links bij horizontale auto's en een stap naar boven bij verticale auto's) en **1** (een stap naar rechts bij horizontale auto's en een stap naar beneden bij verticale auto's). Deze bewegingen worden ook wel 'zetten' (of *moves*) genoemd. De auto houdt *GEEN* rekening met bewegingen die niet zijn toegestaan. Als je auto A naar rechts wil laten gaan terwijl deze pal naast auto B staat, dan mag dat dus niet. Dit algoritme is dan ook bedoelt als een 'baseline'.

**RandomLegalMove**: bij dit algoritme wordt er op basis van *import random* in *Python* een willekeurige auto gekozen op het bord. Het verschil is dat de code er wel voor zorgt dat er alleen geldige moves kunnen worden gedaan: als de auto alleen naar links kan, gaat de auto naar links. Kan een auto alleen naar voren (omdat er links van de auto een andere auto staat), dan gaat die naar voren. Dit algoritme is bedoelt als experiment dat verder uitbouwt op het **Random** algoritme.

**RandomLegalRepeatMove**: Dit bouwt voort uit **RandomLegalMove** en fungeert als verbetering ervan. Bij **RandomLegalRepeatMove** kiest de code met *import random* een willekeurige auto op het bord. Het verschil met **RandomLegalMove** is dat er een geldige move wordt gekozen, waarna het algoritme deze geldige move blijft herhalen totdat deze niet meer geldig is. Als het algoritme een auto naar rechts wil schuiven, en er zijn rechts van die auto drie plekken vrij, dan zal de auto drie keer naar rechts worden geschoven.

**BFS**: Bij een **breadth_first_search**-algoritme begint het programma bij het startbord, waarna alle mogelijke zetten vanuit dat bord worden onderzocht, waarna het programma alle mogelijke zetten van die zetten onderzoekt. Bij elk nieuw bord wordt gecontroleerd of het al is bezocht, en zo nee, dan wordt het aan een queue toegevoegd. Deze queue bestaat om borden en paden bij te houden. Bij elk bord wordt gecontroleerd of de auto de uitgang heeft gevonden. Zo ja, dan wordt het pad teruggegeven. Dit algoritme zoekt altijd naar de kortste oplossing. Nadelig is wel dat het proces bij grote borden veel tijd en ruimte in beslag kan nemen.

**DFS**: Een **depth_first_search**-algoritme verschilt met BFS: terwijl BFS alle mogelijke zetten op een bepaald niveau verkent, gaat DFS zo diep mogelijk in op een bepaald pad voordat er een ander pad wordt verkend. In dit geval begint het algoritme met een startbord, waarna deze zoveel mogelijk zetten genereert en verkent. Voor elk nieuw bord wordt gekeken of het al is bezocht, en zo nee, dan wordt het aan een 'stack' toegevoegd. Als er een bord is gevonden waar de rode auto tegen de uitgang staat, wordt er een pad teruggeven. Het nadeel is dat dit algoritme niet de kortste route garandeert, maar het neemt wel minder ruimte en tijd in beslag.

# AAN DE SLAG!

Om de resultaten van de case te kunnen reproduceren, moet men allereerst de 'main' afspelen in de terminal.

Bij het starten van de 'main' krijgt men een startscherm te zien, waarbij de 'main' is voorzien van een interface dat de gebruiker goed op weg helpt.



