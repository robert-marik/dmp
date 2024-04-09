# Enzymy

Procesy v živých organismech řídí proteiny (hormony, enzymy,
...). Tyto látky se v tělech živých organismů sytetizují, ale nejsou
stabilní a podléhají degradaci. Přitom přežití organismu úzce souvisí
se schopností umět syntetizovat dostatečně rychle potřebné látky a
udžovat jejich množsví na optimální hladině.

Předpokládejme, že degradace enzymu probíhá rychlostí úměrnou množství
enzymu a syntéza probíhá rychlostí, která klesá lineárně s množstvím
enzymu. Proces je tedy možné modelovat rovnicí $$\frac{\mathrm
dx}{\mathrm dt}=1-b(x-1) - x, $$ kde $x$ je množství enzymu a vhodnou
volbou jednotek je minimalizován počet parametrů na jediný parametr
$b$ vystupující v rychlosti syntézy ($1-b(x-1)$).

Vyřešte tuto rovnici pro tři různé hodnoty parametru $b$: pro nulovou
hodnotu (konstantní produkce) a pro dvě nenulové hodnoty (záporná
zpětná vazba, produkce klesá s množstvím syntetizované
látky). Zjistěte, která varianta vede k nejrychlejší syntéze proteinu
z nulové hodnoty.

Zjistěte, zda stejná varianta zajistí i nejrychlejší zotavení se po
rozkolísání rovnovážného stavu. Zopakujte model s jinou počáteční
podmínkou, kdy nevycházíme z nulového stavu, ale ze stavu o 20 procent
nad rovnovážnou hodnotou, tj. ze stavu 1.2.

Výstup bude obsahovat následující

* Nadpis, jméno autora
* Popis, jakou rovnici studujeme, co rovnice vyjadřuje.
* Vizualizaci řešení z nulové počáteční podmínky pro tři hodnoty
  parametru $b$, jedna z hodnot parametru $b$ bude nula.
* Okomentování obrázku. Co v něm vidíme? V které situaci roste řešení
  ke stacionárnímu stavu nejrychleji?
* Vizualizaci řešení pro počáteční podmínku 1.2. Je možné v maximální
  míře recyklovat kód z předchozí vizualizace.
* Okomentování obrázku. V které situaci se obnoví
  rovnovážný stav nejrychleji?
* Obrázky budou obsahovat popisky os a legendu. Rozsahy pro osy a hodnoty
  parametrů budou zvoleny tak, aby z obrázků bylo jasně patrné, kdy je
  syntéza nebo zotavení se nejrychlejší. Všechny textové komentáře
  budou dodržovat obvyklá typografická pravidla.


Model by měl vysvětlit, proč příroda nešla v evoluci nejjednoduší
cestou (konstantní produkce), ale cestou záporné zpětné vazby, kdy
rychlost syntézy souvisí s koncentrací syntetizované látky. Zařídit
zpětnou vazbu je evolučně složitější, vyžaduje to zpravidla souhru
dalších chemických reakcí, ale nositeli to dává evoluční výhodu.

