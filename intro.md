---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Dynamické modely populací

```{code-cell} ipython
:tags: ["hide-input"]
from datetime import datetime
from babel.dates import format_datetime
now = datetime.now()
print ("Poslední aktualizace: ", format_datetime(now, locale='cs'))
```

```{figure} ./pics/lotka-volterra.jpg

Lotkův-Volterrův model dvoudruhové populace dravce a kořisti byl v první polovině dvacátého století jedním z prvních počinů při snaze využít matematické modelování k objasnění přírodních fenoménů spojených s velikostmi populací živočichů. Model vysvětlil vznik pozorovaných oscilací ve společenstvu dravce a kořisti a také poněkud překvapivou skutečnost, že omezení lovu způsobí posun rovnováhy ve prospěch dravců.
```
## O předmětu

Předmět je přednášen na oboru Myslivost. Obsahuje matematický aparát používaný v
matematické biologii k popisu vývoje populací, jejich vzájemné interakce a
schopnosti přežívat. [Webová stránka](https://robert-marik.github.io/pages/dmp/) předmětu s popisem požadavků na ukončení je
na webu vyučujícího. 

Budeme používat matematické postupy a zkoumat matematické modely, ale předmět
není matematikou. Nemá tedy ambice všechny pojmy definovat přesným způsobem v
matematice obvyklým. Přesné definice těchto pojmů je snadné najít v literatuře,
například {cite}`liska`.



## Motivace 1, záchrana Lišky ostrovní 

```{figure} ./pics/Urocyon_littoralis_santacruzae.jpg  
*Liška ostrovní, poddruh žijící na ostrově Santa Cruz, foto: <https://wikimedia.org>*
``` 
Na úvod jako motivaci uveďme jeden optimistický příběh.

[Liška ostrovní](https://cs.wikipedia.org/wiki/Li%C5%A1ka_ostrovn%C3%AD)
(*Urocyon littoralis*) je jedinečný živočišný druh, endemit žijící jenom na
ostrůvcích okolo Kalifornie. Velká jako kočka, důvěřivá (díky absenci
přirozených nepřátel), jako druh citlivá a zranitelná (malá genetická
variabilita, malá odolnost vůči nemocem zavlečeným z pevniny). Jedna z
nejmenších psovitých šelem. Umí šplhat po stromech. Vlivem činnosti člověka se
dostala do velkých potíží. Na ostrově San Miguel klesla populace z 450 dospělých
jedinců v roce 1994 na 15 v roce 1999
([odkaz](https://www.iucnredlist.org/species/22781/13985603)). Podobná situace
byla i na ostatních ostrovech, z nichž každý je osídlen samostatným poddruhem
lišky ostrovní. Příčinou úhynu by celý řetězec událostí: produkce insekticidu
DDT, farmaření a rozmnožení zdivočelých prasat, vytlačení orla bělohlavého
(*Haliaeetus leucocephalus*) orlem skalním (*Aquila chrysaetos*). Dříve vrcholný
predátor na ostrově se stal najednou kořistí a byl těsně před vyhubením.
Naštěstí se podařilo situaci pro lišku zachránit, zajistit podmínky ve kterých
je populace stabilní a populaci lišek opětovně rozmnožit. Nyní je liška ostrovní
"pouze" téměř ohrožená. Jedná se o jeden z nejúspěšnějších záchranných programů
pro savce. Komplexní program zahrnoval vybití divokých prasat, přesídlení orlů
skalních, návrat orlů bělohlavých, umělé rozmnožení lišek, jejich návrat do
přírody a jejich vakcinaci proti zavlečeným chorobám. To vše za jednu dekádu.

* [Článek na idnes.cz](https://www.idnes.cz/cestovani/kolem-sveta/ostrovnim-liskam-kalifornske-rarite-hrozi-vyhynuti.A000706153420igsvet_cha)  z roku 2000 o hrozícím vyhubení.
* [Youtube video](https://youtu.be/2AVRSGkartg) z roku 2018 o záchraně ostrovních lišek.
* [Matematický model](https://www.pnas.org/doi/10.1073/pnas.012422499#F3)
  interakce mezi liškami, orly, skunkem a zdivočelými prasaty.
* [Řešení modelu v prostředí Jupyter notebooku](https://gist.github.com/robert-marik/b1466473f485e7218efda491064765a6)

> Specifika ostrovní biogeografie si představíme ve [třetí přednášce](/prednaska/03). Modelům interakce živočišných druhů ve vztahu [konkurence](/prednaska/09) nebo [predace](/prednaska/10) se budeme věnovat koncem semestru. Jednoduchý Jupyter zápisník, ukazující, že umíte zkombinovat text s výpočty a umíte spustit model a nějakým způsobem vizualizovat řešení bude obsahem seminární práce, nutné pro ukončení předmětu. 

## Motivace 2, záchrana populace želv

```{figure} ./pics/Sea_turtles.jpg 

*Kareta obecná, foto: <https://wikimedia.org>*
``` 

Mořské želvy obecně mají poměrně komplikovaný životní cyklus. Vylíhnutí
z vajíček probíhá na souši, další vývoj v moři. Ochrana se tradičně
soustřeďovala na ochranu pláží pro kladení vajíček a umožnění vylíhnutým
želvičkám dostat se k vodě. To je efektní a snadno proveditelná činnost. Je to
ale i efektivní? Je to opravdu účinná strategie pro podporu populace želv? 

Matematický
rozbor přínosu jednotlivých životních fází k celkovému růstu populace ukázal, že
pro udržení druhu ochrana vajíček a čerstvě vylíhnutých mláďat nestačí. Ukázal,
že tato
činnost má malý vliv. Želva se o svá mláďata nestará a jenom malý zlomek se
dožije dospělosti. Ukázalo se, že pro podporu populace je důležité chránit
dospělé jedince, na kterých stojí břímě rozmnožování. Je nutné snížit riziko, že
tyto jedince z populace odstraníme například jako vedlejší efekt rybolovu.
Protože se ukazuje, že tato aktivita je pro populaci podstatná (dospělí jedinci
mají velkou takzvanou *reprodukční hodnotu*), má smysl hledat cesty a řešení. V
případě rybářských sítí je to například zařízení zvané TED, [Turtle Excluder
Device](https://www.worldwildlife.org/magazine/issues/summer-2016/articles/how-a-simple-technology-is-saving-turtles), které umožní dospělým želvám (a velkým rybám), na nichž závisí přežití
druhu, uniknout z rybářských sítí. Protože se jedná se o poměrně jednoduché a
levné zařízení, je poměr cena/užitek obrovský. 

> Model populace s různými životními etapami si představíme na [šesté přednášce](prednaska/06.html#zobecneni-leslieho-modelu).
> Na [sedmé přednášce](prednaska/07.html#sensitivita-a-elasticita-projekcni-matice) si ukážeme nástroj na analýzu vlivu parametrů na celkový
> růst populace a v [jednom ze cvičení](cviceni/cviceni_07.html#kareta-obecna-loggerhead-sea-turtle) se budeme blíže věnovat zmíněnému modelu populace karety. 

## Co budeme dělat

V předmětu si představíme základní metody modelování jevů a efektů známých z
ekologie a populační biologie. Z těchto oblastí máme celou řadu poznatků. 

* Populace nerostou neomezeně, ale jenom do nosné kapacity prostředí (Verhulst, 1838).
* Větší územní celky mají pestřejší druhové složení. (Mac Arthur, Wilson, 1967).
* Malé populace mohou mít malou nebo zápornou rychlost růstu per capita (Allee, cca 1930–1940).
* Věkově strukturovaná společenstva konvergují ke stabilní věkové skladbě (Leslie, 1945).
* Při konkurenci dvou a více druhů dojde za určitých podmínek ke konkurenčnímu
  vyloučení některých druhů (Gause, 1934).
* Ve fragmentovaném prostředí je nutno chránit i migrační trasy mezi fragmenty a
  také fragmenty, kde se daná populace nenachází (Levins, 1969).
* V přírodě dochází k oscilacím, například ve společenstvech dravce a kořisti
  (Lotka, Volterra, 1920), u dlouhověkých cikád, při některých chemických
  reakcích (Bělousov, Žabotinski, 1951), při periodickém přemnožování obaleče v
  kanadských lesích (Ludwig, Jones, Holling, 1978).
* Organismy produkují enzymy a bílkoviny a jejich fungování je závislé na
  rychlosti, s jakou dokáží syntetizovat potřebný enzym a na tom, jak dokáží
  udržet jeho stabilní hladinu. Výhodnější než jednoduchá konstantní produkce
  enzymu je, pokud si organismus vytvoří evolucí taktiku směřující ke zrychlení
  syntézy a zvýšení robustnosti stacionárního stavu, tj. zvýšení odolnosti proti
  narušení rovnováhy (viz {cite}`alon`). 

Ukážeme si, že uvedené efekty nejsou ničím jiným, než nevyhnutelným důsledkem
principů, podle kterých funguje dané společenství. Matematickým modelováním
převedeme představy o vztazích v populacích na pozorovatelná data. Zpravidla
budeme sledovat velikost populace a její vývoj v čase. 

Pokud matematický model vykazuje shodu s pozorovanou skutečností, máme všechny
důvody domnívat se, že naše představy o principech fungování společenství jsou
správné a to nám umožní sledovat, jak se situace bude měnit při změně parametrů
jako jsou změna prostředí nebo lov či sběr členů této populace. Matematika
umožní levné, snadné, etické a bezpečné experimenty s danou populací. 


## O metodách výuky

Cvičení jsou z výpočetního hlediska zaměřeny na využití jazyka Python. To je
moderní a perspektivní skriptovací jazyk,  vhodný pro manipulaci s daty a
přístupný i neprogramátorům.

```{margin} 
![](./pics/ovladaci_prvky.png)

Ovládací prvky v horní části stránky umožňují přístup k různým formátům textu. Nejdůležitější je raketa, ikona pro otevření textu v nástrojích umožňujících interaktivní práci a spouštění výpočtů.
```

* Díky Pythonu zpřístupníme možnosti řešení matematických modelů i
  nematematikům. Vyhneme se obtížným výpočtům, kvůli kterým bychom se museli
  naučit používat netriviální matematický aparát, jako jsou derivace a
  integrály. 
* Nebojte se, nebudete programovat. Měli byste pasivně rozumět kódu z přednášek
  a cvičení a umět jej přizpůsobit jinému modelu nebo jiné situaci.
* Příklady pro **cvičení** jsou zápisníky prostředí Jupyter, ve kterém Python
  budeme spouštět. Je možné otevřít v online prostředí nebo na svém lokálním PC.
  Online možnosti jsou přístupné přes horní lištu pod ikonkou rakety. 
    * JupyterHub je volba, kterou budeme používat během cvičení. Touto volbou se
      vám naklonují materiály do vlastního adresáře a budete moci s touto jejich
      kopií pracovat. Co se přesně stane a jaké jsou možnosti je popsáno v
      dokumentaci k
      [nbgitpuller](https://tljh.jupyter.org/en/latest/howto/content/nbgitpuller.html).
      Budete pracovat na serveru univerzity, abychom měli všichni stejné
      prostředí. Zde se také bude pracovat na zápočtovém projektu. Účet na
      [jupyter.mendelu.cz](https://jupyter.mendelu.cz) mají studenti předmětu.
      Login je stejný jako do UIS (například `xnovak65`), přednastavené heslo
      máte v UIS, návod jak heslo najít je na přihlašovací stránce JupyterHubu.
    * Binder založí dočasně server  na službě mybinder.org a umožní Vám
      experimentovat s kódem, spouštět příkazy. Práce je dočasná, pokud po
      ukončení nechcete o práci přijít, musíte si zápisník stáhnout na lokální
      PC. Je možné doinstalovat balíčky, například knihovnu intersect příkazem
      `! pip install intersect` (vykřičník na začátku informuje o tom, že se
      jedná o příkaz operačního systému a ne příkaz jazyka Python).
    * Colab vám po přihlášení ke Google účtu uloží zápisník na Google disk.
      Prostředí je trochu jiné, ale práce je zpravidla svižnější na odezvu.
      Zápisník se ukládá a je možné sledovat změny a ukládat verze. Výsledek
      práce je možno uložit na [GitHub](https://cs.wikipedia.org/wiki/GitHub) do
      svého repozitáře nebo jako Gist. Je možné doinstalovat chybějící balíčky
      stejně jako v předchozím bodě pro Binder.
    * Live Code umožní spouštět příklady přímo na stránce, kterou čtete. Volba
      je nejméně svižná, ale použitelná. 
    * Offline práce je možná, pokud máte nainstalovaný Python, Jupyter a s tím
      spojený ekosystém. Doporučenou volbou pro nejběžnější operační systémy
      (Linux, Windows) je
      [Anaconda](https://www.anaconda.com/products/distribution) a jako editor
      buď Jupyter zápisník v prohlížeči nebo editor [Visual Studio
      Code](https://code.visualstudio.com/) a pluginy Python, Pylance, Python
      for VSCode, Jupyter.
* **Přednášky** jsou psány jazykem [MyST](https://myst-parser.readthedocs.io/en/latest/) a je možné je otevřít v online prostředí, které tento jazyk podporuje. To je v zimě 2022 částečně Binder a JupyterHub z online služeb a Jupyter Notebook jako offline volba. (Nejsou renderovány definice, věty a některá další prostředí, ty se zobrazují jako programový kód.) Vývoj však jde rychle dopředu...

```{warning}
Pokud pracujete na lokálním počítači, máte data pod kontrolou a nikdo jiný je nevidí. Při práci na JupyterHubu na Mendelově univerzitě data může vidět i admin serveru. (Toho budeme využívat při práci na zápočtovém projektu.) Při práci na serverech jako Colab či Binder jdou data přes servery dalších vlastníků a nemáte data plně pod kontrolou. Proto není vhodné pracovat s osobními daty a citlivým obsahem. 
```

## Troubleshooting


### V příkazech je chyba a je těžké ji najít

Příkazy pište po malých krůčcích a teprve poté vše spojte. Pokud vidíte dlouhou 
chybovou hlášku, je zpravidla nejinformativnější její konec. Pokud nevíte o co
jde, můžete část chybového hlášení nakopírovat do vyhledávacího políčka google
a pátrat po radách k uvedenému problému.

### Učební text se zasekává při otevírání na jupyter.mendelu.cz

Pokud si naklonujete učební text k sobě a něco v něm upravíte, může při
dalších verzích dojít ke kolizi a nestáhne se vám aktuální verze.
Nejrychlejší řešení je přepnout se do konzole (v seznamu souborů použít New, 
Terminal) a tam zadat příkazy OS Linux. Můžete použít `mv dmp dmp_kopie` pro
přejmenování. Zůstanou Vám i upravené soubory v adresáři dm_kopie. Pokud
svou práci ukládáte jinam (doporučeno do hlavního adresáře nebo do svého
podadresáře), můžete adresář smazat příkazem `yes | rm -r dmp` a poté se při
otevření souboru z učebního textu naklonuje celá nová verze. 

