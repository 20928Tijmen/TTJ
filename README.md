# RUSH HOUR

Voor 'Algoritmen en Heuristieken' focussen Thijs, Tijmen en Joost onder de teamnaam 'TTJ' op het oplossen van de case 'Rush Hour'.

# Uitleg van de CASE

De case die wij hebben gekozen heet **Rush Hour**.

**Rush Hour** is een spel waar men een rode auto heeft die in de richting van een uitgang is gepositioneerd. Eén probleem: er zijn allerlei auto's die de weg van de rode auto versperren. De auto's variëren in grootte en in richtingen. Sommige auto's kunnen alleen van boven naar beneden en vice versa, terwijl andere auto's alleen van links naar rechts en van rechts naar links kunnen. Geen van de auto's mag gedraaid worden. Ook mogen geen van de auto's over elkaar heen gaan.

**Het uiteindelijk doel** van het spel is dat de versperrende auto's op bepaalde manieren zo aan de kant worden geschoven, dat de rode auto naar de uitgang kan gaan.

**Het uiteindelijke doel** van de case is dat we een programma schrijven in *Python* die **Rush Hour** op zichzelf kan oplossen door middel van een algoritme.

# De ALGORITMEN

**Het eerste algoritme** betreft de baseline van dit project. Dit gaat om een **Random** algoritme.

De aanpak van het **Random** algoritme gaat als volgt:

Het programma kiest, op basis van *import random* in *Python* een willekeurige op het bord. Daarna kiest het een willekeurige beweging: de keuzes betreffen **-1** (een stap naar links bij horizontale auto's en een stap naar boven bij verticale auto's) en **1** (een stap naar rechts bij horizontale auto's en een stap naar benden bij verticale auto's). Het auto houdt *GEEN* rekening met bewegingen die niet zijn toegestaan. Als je auto A naar rechts wil laten gaan terwijl deze pal naast auto B staat, dan mag dat dus niet. Het algoritme houdt daar dus geen rekening mee, en herhaalt het script net zo lang totdat de rode auto (auto X) tegen de uitgang staat.
