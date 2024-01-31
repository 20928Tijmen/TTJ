# RUSH HOUR

**Rush Hour** is een spel waar men een rode auto heeft die in de richting van een uitgang is gepositioneerd. Eén probleem: er zijn allerlei auto's die de weg van de rode auto versperren. De auto's variëren in grootte en in richtingen. Sommige auto's kunnen alleen van boven naar beneden en vice versa, terwijl andere auto's alleen van links naar rechts en van rechts naar links kunnen. Geen van de auto's mag gedraaid worden. Ook mogen geen van de auto's over elkaar heen gaan.

**Het uiteindelijk doel** van het spel is dat de versperrende auto's op bepaalde manieren zo aan de kant worden geschoven, dat de rode auto naar de uitgang kan gaan. Daarvoor gebruikt men 'moves': bewegingen van 1 stap per keer, waarbij een auto of naar voor, of naar achter kan gaan.

**Het uiteindelijke doel** van de case is dat men met een programma in *Python* het spel **Rush Hour** kan oplossen door middel van algoritmen.

# DE ALGORITMEN

**Random**: Het programma kiest, op basis van *import random* in *Python* een willekeurige auto op het bord. Daarna kiest het een willekeurige beweging: de keuzes betreffen **-1** (een stap naar links bij horizontale auto's en een stap naar boven bij verticale auto's) en **1** (een stap naar rechts bij horizontale auto's en een stap naar beneden bij verticale auto's). Deze bewegingen worden ook wel 'zetten' (of *moves*) genoemd. De auto houdt *GEEN* rekening met bewegingen die niet zijn toegestaan. Als je auto A naar rechts wil laten gaan terwijl deze pal naast auto B staat, dan mag dat dus niet. Dit algoritme is dan ook bedoelt als een 'baseline'.

**RandomLegalMove**: bij dit algoritme wordt er op basis van *import random* in *Python* een willekeurige auto gekozen op het bord. Het verschil is dat de code er wel voor zorgt dat er alleen geldige moves kunnen worden gedaan: als de auto alleen naar links kan, gaat de auto naar links. Kan een auto alleen naar voren (omdat er links van de auto een andere auto staat), dan gaat die naar voren. Dit algoritme is bedoelt als experiment dat verder uitbouwt op het **Random** algoritme.

**RandomLegalRepeatMove**: Dit bouwt voort uit **RandomLegalMove** en fungeert als verbetering ervan. Bij **RandomLegalRepeatMove** kiest de code met *import random* een willekeurige auto op het bord. Het verschil met **RandomLegalMove** is dat er een geldige move wordt gekozen, waarna het algoritme deze geldige move blijft herhalen totdat deze niet meer geldig is. Als het algoritme een auto naar rechts wil schuiven, en er zijn rechts van die auto drie plekken vrij, dan zal de auto drie keer naar rechts worden geschoven.

**BFS**: Bij een **breadth_first_search**-algoritme begint het programma bij het startbord, waarna alle mogelijke zetten vanuit dat bord worden onderzocht, waarna het programma alle mogelijke borden vanuit die zetten onderzoekt. Bij elk nieuw bord wordt gecontroleerd of het al is bezocht, en zo zo niet, dan wordt het aan een queue toegevoegd. Deze queue bestaat om borden en paden bij te houden. Bij elk bord wordt gecontroleerd of de auto de uitgang heeft gevonden. Zo ja, dan wordt het pad teruggegeven. Dit algoritme zoekt altijd naar de kortste oplossing. Nadelig is wel dat het proces bij grote borden veel tijd en ruimte in beslag kan nemen.

**DFS**: Een **depth_first_search**-algoritme verschilt met BFS. In tegenstelling tot BFS gaat DFS zo diep mogelijk in op een bepaald pad voordat het naar andere paden gaat. Het algoritme begint met een startbord en genereert zoveel mogelijk zetten. De code implementeert DFS dan ook met een stack en een set om bezochte borden bij te houden, waarbij er voor elk nieuw bord wordt gecontroleerd of het al is bezocht. Zo niet, dan wordt het aan de stack toegevoegd. Wanneer de rode auto de uitgang bereikt, wordt het gevonden pad teruggegeven. Het algoritme eindigt zodra het een bord vind waar de rode auto de uitgang heeft bereikt. Hoewel het niet de kortste oplossing garandeert, is DFS efficiënter dan BFS op het gebied van ruimte en tijd.

**Astar**: Een **Astar**-algoritme komt in de buurt van BFS op gebied van werking, maar de volgorde van de verkenning van de bordconfiguraties (hier in nodes) wordt gebaseerd op een heuristieke score die elk bord krijgt. Deze score is berekend op basis van de hoeveelheid zetten die nodig zijn om naar een bepaald bord te gaan, de afstand van de auto naar de exit, en alle voertuigen die in de weg staan. Hoe lager de score, hoe meer prioriteit deze krijgt van het algoritme. Ook dit algoritme gaat voor de kortst mogelijke oplossing.

# OVERZICHT VAN DEZE REPOSITORY

**/code**: Hierin staat alle code die nodig is om het programma draaiende te krijgen.

**/data**: Hierin staat 'algoritmen_data.csv', een belangrijk bestand dat snelle statistieken bijhoud van algoritmische prestaties. Ook worden hier - bij het gebruik van de algoritmen DFS, BFS, en Astar - drie 'Results'-mappen aangemaakt via gebruik van de Main, die bijhouden hoeveel zetten een algoritme nodig had om in een Rush Hour-spel de finishlijn te halen.

**/docs**: Hierin staan kleine afbeeldingen, waaronder de grafieken die dit programma kan aanmaken met matplotlib.

*Main.py*: Het hoofdprogramma waarin alle belangrijke processen plaatsvinden.

*README.md*: Wat men nu leest. Dit bestand geeft uitleg die van belang is om de case, de algoritmen en het programma te begrijpen. 

*Requirements.txt*: Dit bestand bevat allerlei vereisten om het programma werkend te krijgen op andere computers.

# AAN DE SLAG!

Allereerst moet men deze repository en de bijbehorende afhankelijkheden downloaden. *Requirements.txt* legt uit hoe men dit moet doen.

Om de resultaten van de case te kunnen reproduceren, moet men allereerst de 'main' afspelen in de terminal.

Bij het starten van de 'main' krijgt men een startscherm te zien, waarbij de 'main' is voorzien van een interface dat de gebruiker goed op weg helpt. Het eerste scherm dat men ziet, noemen we het 'introductiescherm'.

![print](https://github.com/20928Tijmen/TTJ/assets/144214560/9953cba8-2e31-4f54-a187-9f7c68fc94b9)

Als men kiest voor 'v' (voor 'visualize-random'), wordt men eerst gevraagd of deze een willekeurig bord wil zien. Zo ja, dan krijgt men een bord met allemaal willekeurige auto's op willekeurige plaatsen. Zo nee, dan men kiezen tussen een reeks borden. Daarna kan je met behulp van de interface kiezen welke van de drie 'Random'-algoritmes moet worden afgespeeld.

Na het kiezen van een 'Random' algoritme, wordt een 'pygame'-venster geopend. Deze pygame vertoont elke zet van het random-algoritme als bewegingen van de auto's op het bord.

![screenshottwo](https://github.com/20928Tijmen/TTJ/assets/144214560/46081226-b8c5-4a16-ad35-b80dedd3e3c5)

Zodra het spel voorbij is, sluit pygame automatisch af, waarna de terminal uitlegt hoeveel zetten nodig waren. Je kan er ook voor kiezen om het spel vroegtijdig af te sluiten door te drukken op het kruisje in de rechterbovenzijde van het pygame-venster. Dit is wel aangeraden bij borden die heel lang duren (zoals **Random** borden van 9x9 en hoger) - als je het spel vroegtijdig afsluit, krijg je nog steeds te zien hoeveel moves nodig waren om het spel op te lossen.

In ieder geval krijgt men na het zien van de resultaten, de optie om óf door te gaan door 'c' in te drukken (waarna men gebruik kan maken van een andere functie in de main), of het spel af te sluiten. Als men het spel afsluit, krijgt men de mogelijkheid om de matplotlib-grafieken te zien voor de andere algoritmen uit deze case. Dit is echter voor later.

![screenshotthree](https://github.com/20928Tijmen/TTJ/assets/144214560/875c58da-7ba7-490a-ad16-ea198bd11924)

Als men op het introductiescherm kiest voor 'e', wordt er gevraagd hoe vaak je een spel wil laten afspelen. Daarna wordt gevraagd welk bord je wil gebruiken, waarna wordt gevraagd welk algoritme je wil gebruiken voor het experiment.

![screenshotfour](https://github.com/20928Tijmen/TTJ/assets/144214560/24a5fbd9-dff7-4663-b66e-1f722a6ffd08)

Na het klikken op 'Enter', speelt het programma meerdere spellen af, waarbij voor elk spel de hoeveelheid moves wordt vertoond op het scherm. Indien alle spellen zijn afgespeeld, krijgt men het eindresultaat met het gemiddeld aantal moves.

![screenshotfive](https://github.com/20928Tijmen/TTJ/assets/144214560/6b8a5f65-8663-4c12-8793-d5b80c03f353)

Als je in het introductiescherm voor 'algo' gaat, krijg je de mogelijkheid om algoritmen te testen en te vergelijken. In deze modus krijg je dan weer de mogelijkheid om te kiezen of je BFS, DFS of Astar wil laten afspelen. Als men voor 'b', 'd', of 'a', kiest dan wordt er respectievelijk gekozen voor BFS, DFS of Astar. In alle drie de gevallen krijgt men de vraag welk bord ze willen kiezen. Zodra dat is gedaan, wordt elke move die één van deze drie algoritmes aflegd, afgespeeld als bewegingen op een pygame-bord.

Zodra het algoritme en het bord zijn gekozen, wordt elke move die één van deze drie algoritmes aflegd, afgespeeld als bewegingen op een pygame-bord.

![itworks](https://github.com/20928Tijmen/TTJ/assets/144214560/f259db68-f935-4473-98fd-51b99028f42c)

Nadat de rode auto de exit heeft bereikt, ziet men een boodschap waarin staat dat bepaalde resultaten in twee 'output'-bestanden zijn opgeslagen. Het eerste 'output'-bestand bevat alle moves die zijn gezet om de auto de uitgang te laten bereiken. Deze moves kan men terugvinden in de bijbehorende 'results'-map die wordt aangemaakt in de 'data'-map.

Het andere output-bestand, 'data/algoritmen_data' geeft statistieken over hoe de algoritmen tot nu hebben gepresteert.

![itworks2](https://github.com/20928Tijmen/TTJ/assets/144214560/2ea04859-f608-4caf-a8f0-1acbf6c2b34e)

Als je hier op 'c' klikt, ga je niet terug naar introductiescherm. Bij 'manual_algo' krijg je dan juist de mogelijkheid om direct een ander algoritme en/of een ander bord te testen in dezelfde modus.

![print3](https://github.com/20928Tijmen/TTJ/assets/144214560/af0c3cf0-4c17-4d1c-856f-5bc6638f8b1b)

Als je bij 'manual_algo' op 'q' drukt wordt het programma niet meteen afgesloten - in plaats daarvan krijg je eerst een resultatenlijst waarin men ziet hoe elk algoritme in de 'algo'-modus heeft gepresteerd. Elk algoritme wordt beoordeeld op verscheidene attributen. Dit geeft mogelijkheid om elk algoritme te vergelijken. Wij hebben deze manual modes vooral gebruikt om de 9x9 borden te runnen, omdat die veel tijd en computer geheugen in beslag nemen.

![print2](https://github.com/20928Tijmen/TTJ/assets/144214560/5d4af9a1-5506-4b4d-8067-e585c47f1d47)

Als men in het introductiescherm voor 'auto' kiest, worden de algoritmen 'BFS', 'DFS' en 'Astar' opeenvolgend afgespeeld, waarbij elk algoritme drie keer wordt afgespeeld (één keer voor elk Grootte-bij-Grootte bord).

Na het kiezen van 'auto' krijg je dan ook de keuze tussen het afspelen van de 6x6, de 9x9, of de 12x12 borden.

Ook hiervoor wordt bij elke game het pygame-bord vertoond om elke move te vertonen als bewegingen op een spelbord.

Zodra het uitgespeeld is met de 6x6 borden is er een mogelijkheid om het te printen in twee matplotlib grafieken (bij 6x6 is dit geimplementeerd omdat bij 9x9 het te lang duurt om alle data te verzamelen). Om ervoor te zorgen dat dit werkt, moet je algoritmen_data.csv alleen de negen resultaten hebben die voortkomen uit het afspelen van 'auto'. Elk resultaat is een regel die met de naam van een algoritme begint. Als er onder de eerste regel (die met 'Algorithm' begint) meer dan negen individuele regels staat, moet je alle regels onder de eerste regel er handmatig uithalen.

![screeenshottty](https://github.com/20928Tijmen/TTJ/assets/144214560/34261ca0-cd65-4e0a-9472-99bb94b77911)

![hallo](https://github.com/20928Tijmen/TTJ/assets/144214560/99c5c4c1-2825-4c69-ba12-99ec504dd1a6)

De twee matplot-libgrafieken kan je op een mac systeem saven door middel van plt.show, maar anders hebben wij het voor windows users zo ingesteld dat je met plt.savefig de grafieken kan saven. De optie om de grafieken te zien krijg je als je quit drukt. Lukt dat niet? Dan moet je misschien het bestand 'data/algoritmen_data.csv' opschonen. Je kunt ook main.py runnen en p als input typen als je negen resultaten in het bestand hebt en (een extra) afbeelding van de resultaten wil laten maken.

![pictar](https://github.com/20928Tijmen/TTJ/assets/144214560/9d6c0355-c52e-40d7-9412-b3f33f0d2c85)

