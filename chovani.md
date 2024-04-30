# Model soupeření jestřábí a holubičí povahy


Cílem tohoto modelu je studovat typy chování živočichů a rostlin a
zjistit, zda některý typ chování přináší jeho nositelům evoluční
výhodu.

Nechť se v populaci vyskytují dva vzorce chování -- jedince
používající první z nich budeme nazývat *jestřábi* a druhý
*holubice*. Chování se projeví, pokud se dva jedinci setkají
u téhož zdroje (potrava, hnízdiště, apod). 

* Jestřáb o zdroj bojuje a ustoupí pouze po prohraném boji.
* Holubice o zdroje nebojuje. Pokud protivník ustoupí bez boje,
  holubice zdroj zkonzumuje. V opačném případě zdroj zkonzumuje
  protivník.
* Předpokládejme, že každý jedinec v populaci si zkonzumováním
  zdroje může svou evoluční zdatnost posílit o hodnotu $V$. Pokud
  je nucen a ochoten o zdroj bojovat, je jeho evoluční zdatnost naopak
  snížena o hodnotu $D$. 
* Setkají-li se u zdroje dvě holubice, jedna z nich ustoupí bez boje
  a druhá zkonzumuje zdroj. Předpokládejme, že po častých setkáních
  tohoto typu každá holubice zkonzumuje průměrně polovinu zdrojů.
* Setká-li se u zdroje holubice s jestřábem, zkonzumuje celý zdroj
  jestřáb.
* Setkají-li se u zdroje dva jestřábi, ani jeden z nich neustoupí
  a bojují o zdroj. Předpokládejme, že všichni jestřábi jsou stejně
  silní a po boji je pravděpodobnost zkonzumování zdroje poloviční pro
  každého jestřába.

Matematický rozbor (J. Kalas, Z. Pospíšil, Spojité modely v biologii)
ukazuje, že četnost $x$ výskytu jestřábů v populaci se řídí
diferenciální rovnicí
$$x'=x(1-x)\left(\frac V2-\frac D2 x\right).$$
Jediné realistické hodnoty $x$ jsou z intervalu $[0,1]$.  Stacionární
body rovnice jsou nulové body pravé strany rovnice a to jsou $x=0$,
$x=1$ a $x=\frac VD$. Poslední stacionární bod v závislosti na hodnotě
parametrů může a nemusí ležet v intervalu $[0,1]$. Pokud leží mimo
tento interval, nezajímá nás.


**Úkol:** Namodelujte vývoj procentuálního zastoupení jestřábů pro dva případy, kdy $V<D$ a $V>D$. V každém z případů simulujte několik počátečních podmínek rozložených na intervalu $[0,1]$ a sledujte, zda všechna řešení konvergují ke stejné stacionární hodnotě a pokud ano, k jaké.
