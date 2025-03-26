# Ovládání JupyterLab


Jedná se o překlad dokumentu publikovaného [zde](https://gist.github.com/discdiver/9e00618756d120a8c9fa344ac1c375ac).

V zápisníku jsou buňky několika druhů. Budeme používat Code pro kód v Pythonu a Markdown pro doprovodné texty.  
Můžete se nacházet buď v režimu editace obsahu buněk, tj. v takzvaném _editačním režimu_, nebo v _příkazovém režimu_.

V editačním režimu píšete příkazy nebo doprovodný text, v příkazovém režimu nastavujete typ buněk, spouštíte příkazy v buňkách, kopírujete či přesunujete buňky, vkládáte nové nebo mažete nepotřebné buňky a podobně.

Zkratky v _příkazovém režimu_ i v _editačním režimu_
---

(Znak plus znamená současný stisk kláves.)

|Zkratka|Akce|
|-|-|
`Shift` + `Enter` | spustit příkazy v buňce a posunout se na následující buňku, pokud nenásleduje žádná další buňka, vložit prázdnou 
`Ctrl` + `Enter` | spustit příkazy v buňce a zůstat na aktivní buňce
`Alt` + `Enter` | spustit příkazy v buňce, vložit práznou za ní a přesunout se na nově vloženou buňku
`Ctrl` + `B` | přepnutí zobrazení/skrytí levého panelu
`Ctrl` + `S` | uložit
`Ctrl` + `Shift` + `S` | uložit jako
`Ctrl` + `F` | najít nebo nebo najít a nahradit 


Zkratky v _příkazovém režimu_ 
---

|Zkratka|Akce|
|-|-|
`Enter` | vstoupit do _editačního režimu_ v aktivní buňce
Šipky nahoru a dolů|  Pohyb příslušným směrem. 
`A`| vložit buňku nad aktivní buňku (Above)
`B`| vložit buňku pod aktivní buňku (Below)
`M` |přepnout buňku na typ Markdown (doprovodný text)
`Y` |přepnout buňku na typ Code (kód Python)
`Shift` + `Up Arrow`| vybrat aktivní buňku a buňku nad
`Shift` + `Down Arrow`| vybrat aktivní buňku a buňku pod
`Ctrl` + `A`| vybrat všechny buňky
`X` |vystřihnout aktivní buňku nebo vybrané buňky
`C` |kopírovat aktivní buňku nebo vybrané buňky
`V` |vložit vykpírované nebo vystřižené buňky
`Shift + M` |spojit více buňek do jedné nebo spojit buňku s následující buňkou
`DD` (`D` dvakrát) |smazat aktivní buňku
`00` (nula dvakrát) |restartovat jádro interpretru
`Z` |undo pro většinu operací


Zkratky v _editačním režimu_
---

|Zkratka|Akce|
|-|-|
`Esc` |přejít do _příkazového režimu_
`Tab` |doplnit kód (pokud je za rozepsanou funkcí nebo proměnnou) nebo odsadit (pokud je na začátku řádku)
`Ctrl` + `Shift` + `-` |rozdělit buňku na dvě v místě kurzoru
`Ctrl` + `]` |odsadit, stejně funguje `Tab` na začátku řádku
`Ctrl` + `[` |zrušit odsazení, stejně funguje `Shift`+`Tab` na začátku řádku
`Ctrl` + `/` |zakomentovat nebo odkomentovat aktivní řádek nebo blok

Plus je možné používat obvyklé klávesové zkratky pro výběr, vyjmutí, kopírování, vložení, undo atd.

