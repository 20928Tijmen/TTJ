# RUSH HOUR


**Rush Hour** is een spel waar men een rode auto heeft die in de richting van een uitgang is gepositioneerd. Eén probleem: er zijn allerlei auto's die de weg van de rode auto versperren. De auto's variëren in grootte en in richtingen. Sommige auto's kunnen alleen van boven naar beneden en vice versa, terwijl andere auto's alleen van links naar rechts en van rechts naar links kunnen. Geen van de auto's mag gedraaid worden. Ook mogen geen van de auto's over elkaar heen gaan.

**Het uiteindelijk doel** van het spel is dat de versperrende auto's op bepaalde manieren zo aan de kant worden geschoven, dat de rode auto naar de uitgang kan gaan. Daarvoor gebruikt men 'moves': bewegingen van 1 stap per keer, waarbij een auto of naar voor, of naar achter kan gaan.

**Het uiteindelijke doel** van de case is dat men met een programma in *Python* het spel **Rush Hour** kan oplossen door middel van algoritmen.

# DE ALGORITMEN

**Random**: Het programma kiest, op basis van *import random* in *Python* een willekeurige auto op het bord. Daarna kiest het een willekeurige beweging: de keuzes betreffen **-1** (een stap naar links bij horizontale auto's en een stap naar boven bij verticale auto's) en **1** (een stap naar rechts bij horizontale auto's en een stap naar beneden bij verticale auto's). Deze bewegingen worden ook wel 'zetten' (of *moves*) genoemd. De auto houdt *GEEN* rekening met bewegingen die niet zijn toegestaan. Als je auto A naar rechts wil laten gaan terwijl deze pal naast auto B staat, dan mag dat dus niet. Dit algoritme is dan ook bedoelt als een 'baseline'.

**RandomLegalMove**: bij dit algoritme wordt er op basis van *import random* in *Python* een willekeurige auto gekozen op het bord. Het verschil is dat de code er wel voor zorgt dat er alleen geldige moves kunnen worden gedaan: als de auto alleen naar links kan, gaat de auto naar links. Kan een auto alleen naar voren (omdat er links van de auto een andere auto staat), dan gaat die naar voren. Dit algoritme is bedoelt als experiment dat verder uitbouwt op het **Random** algoritme.

**RandomLegalRepeatMove**: Dit bouwt voort uit **RandomLegalMove** en fungeert als verbetering ervan. Bij **RandomLegalRepeatMove** kiest de code met *import random* een willekeurige auto op het bord. Het verschil met **RandomLegalMove** is dat er een geldige move wordt gekozen, waarna het algoritme deze geldige move blijft herhalen totdat deze niet meer geldig is. Als het algoritme een auto naar rechts wil schuiven, en er zijn rechts van die auto drie plekken vrij, dan zal de auto drie keer naar rechts worden geschoven.

**BFS**: Bij een **breadth_first_search**-algoritme begint het programma bij het startbord, waarna alle mogelijke zetten vanuit dat bord worden onderzocht, waarna het programma alle mogelijke borden vanuit die zetten onderzoekt. Bij elk nieuw bord wordt gecontroleerd of het al is bezocht, en zo nee, dan wordt het aan een queue toegevoegd. Deze queue bestaat om borden en paden bij te houden. Bij elk bord wordt gecontroleerd of de auto de uitgang heeft gevonden. Zo ja, dan wordt het pad teruggegeven. Dit algoritme zoekt altijd naar de kortste oplossing. Nadelig is wel dat het proces bij grote borden veel tijd en ruimte in beslag kan nemen.

**DFS**: Een **depth_first_search**-algoritme verschilt met BFS: terwijl BFS alle mogelijke zetten op een bepaald niveau verkent, gaat DFS zo diep mogelijk in op een bepaald pad voordat er een ander pad wordt verkend. In dit geval begint het algoritme met een startbord, waarna deze zoveel mogelijk zetten genereert en verkent. Voor elk nieuw bord wordt gekeken of het al is bezocht, en zo nee, dan wordt het aan een 'stack' toegevoegd. Als er een bord is gevonden waar de rode auto tegen de uitgang staat, wordt er een pad teruggeven. Het nadeel is dat dit algoritme niet de kortste route garandeert, maar het neemt wel minder ruimte en tijd in beslag.

**Astar**: Een **Astar**-algoritme komt in de buurt van BFS op gebied van werking, maar de volgorde van de verkenning van de bordconfiguraties (hier in nodes) wordt gebaseerd op een heuristieke score die elk bord krijgt. Deze score is berekend op basis van de hoeveelheid zetten die nodig zijn om naar een bepaald bord te gaan, de afstand van de auto naar de exit, en alle voertuigen die in de weg staan. Hoe lager de score, hoe meer prioriteit deze krijgt van het algoritme. Ook dit algoritme gaat voor de kortst mogelijke oplossing.

# AAN DE SLAG!

Allereerst moet men deze repository en de bijbehorende afhankelijkheden downloaden. *Requirements.txt* legt uit hoe men dit moet doen.

Om de resultaten van de case te kunnen reproduceren, moet men allereerst de 'main' afspelen in de terminal.

Bij het starten van de 'main' krijgt men een startscherm te zien, waarbij de 'main' is voorzien van een interface dat de gebruiker goed op weg helpt. Het eerste scherm dat men ziet, noemen we het 'introductiescherm'.

![screenshotone](https://github.com/20928Tijmen/TTJ/assets/144214560/2b06d5fc-b2e3-4937-be8f-4a0010683a37)

Als men kiest voor 'v' (voor 'Visual'), kan men kiezen tussen een reeks borden. Daarna kan men met behulp van de interface kiezen welke van de drie 'Random'-algoritmes moet worden afgespeeld.

Na het kiezen van een 'Random' algoritme, wordt een 'pygame'-venster geopend. Deze pygame vertoont elke zet van het random-algoritme als bewegingen van de auto's op het bord.

![screenshottwo](https://github.com/20928Tijmen/TTJ/assets/144214560/46081226-b8c5-4a16-ad35-b80dedd3e3c5)

Zodra het spel voorbij is, sluit pygame automatisch af, waarna de terminal uitlegt hoeveel zetten nodig waren. Hierna krijgt men de optie om óf door te gaan door 'c' in te drukken (waarna men gebruik kan maken van een andere functie in de main), of het spel af te sluiten.

![screenshotthree](https://github.com/20928Tijmen/TTJ/assets/144214560/875c58da-7ba7-490a-ad16-ea198bd11924)

Als men op het introductiescherm kiest voor 'e', wordt er gevraagd hoe vaak je een spel wil laten afspelen. Daarna wordt gevraagd welk bord je wil gebruiken, waarna wordt gevraagd welk algoritme je wil gebruiken voor het experiment.

![screenshotfour](https://github.com/20928Tijmen/TTJ/assets/144214560/24a5fbd9-dff7-4663-b66e-1f722a6ffd08)

Na het klikken op 'Enter', speelt het programma meerdere spellen af, waarbij voor elk spel de hoeveelheid moves wordt vertoond op het scherm. Indien alle spellen zijn afgespeeld, krijgt men het eindresultaat met het gemiddeld aantal moves.

![screenshotfive](https://github.com/20928Tijmen/TTJ/assets/144214560/6b8a5f65-8663-4c12-8793-d5b80c03f353)

Als men voor 'b', 'd', of 'a', kiest op het introductiescherm, wordt respectievelijk gekozen voor BFS, DFS of Astar. In alle drie de gevallen krijgt men de vraag welk bord ze willen kiezen. Zodra dat is gedaan, wordt elke move die één van deze drie algoritmes aflegd, afgespeeld als bewegingen op een pygame-bord.

![itworks](https://github.com/20928Tijmen/TTJ/assets/144214560/f0795c54-595d-4bac-85e3-96190e8f22d8)

Nadat de rode auto de exit heeft bereikt, ziet men een boodschap waarin staat dat de resultaten in een bepaald 'output'-bestand zijn opgeslagen. Dit 'output'-bestand bevat alle moves die zijn gezet om de auto de uitgang te laten bereiken. Deze moves kan men terugvinden in de bijbehorende 'results'-map in de 'data'-map.

![itworks2](https://github.com/20928Tijmen/TTJ/assets/144214560/2ea04859-f608-4caf-a8f0-1acbf6c2b34e)

Als je in het introductiescherm voor 'algo' gaat, krijg je de mogelijkheid om algoritmen te testen en te vergelijken. In deze modus krijg je dan weer de mogelijkheid om te kiezen of je BFS, DFS of Astar wil laten afspelen. Nadat je dat hebt gedaan, kun je weer op 'c' of 'q' indrukken. Als je hier op 'q' drukt wordt het programma niet meteen afgesloten - in plaats daarvan krijg je eerst een resultatenlijst waarin men ziet hoe elk algoritme in de 'algo'-modus heeft gepresteerd. Elk algoritme wordt beoordeeld op verscheidene attributen. Dit geeft mogelijkheid om elk algoritme te vergelijken.

![screenshotsix](https://github.com/20928Tijmen/TTJ/assets/144214560/f691ad9d-b695-48b5-af10-0c9a6b8c6f66)

Als men in het introductiescherm voor 'auto' kiest, spelen alledrie de algoritmen 'BFS', 'DFS' en 'Astar' opeenvolgend af, waarbij elk algoritme drie keer wordt afgespeeld (één keer voor elk 6x6 bord). Ook hiervoor wordt bij elke game het pygame-bord vertoond om elke move te vertonen als bewegingen op een spelbord.
