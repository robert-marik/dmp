# Build book by sphinx. Jupyterbook does not (probably) work well with double dollas 
directory=../_build/pdf

sphinx-build ../ $directory -b latex

cp prednasky_definice.tex $directory/
cp cviceni_definice.tex $directory/
cp custom_preamble.tex $directory/
cp ukazky_definice.tex $directory/

sed -i 's/sphinxShadowBox/comment/' $directory/python.tex 
sed -i 's/documentclass\[/documentclass[twocolumn,/' $directory/python.tex
cd $directory

sed -i 's/\\chapter{Úvodní slovo}/\\chapter*{Úvodní slovo}/' python.tex

sed -i 's/\\chapter{První kroky}/\\end{document}\\part{Cvičení}\\input cviceni_definice.tex\n\\chapter{První kroky}/' python.tex
sed -i 's/\\chapter{Funkce a vlastnosti funkcí}/\\input prednasky_definice.tex\n\\chapter{Funkce a vlastnosti funkcí}/' python.tex
sed -i 's/\\chapter{Základní konstrukce}/\\part{Další materiály}\n\\input ukazky_definice.tex\\chapter{Základní konstrukce}/' python.tex


# sed -i 's/\\def\\sphinxdocclass{report}/\\def\\sphinxdocclass{book}/' python.tex


vlna python.tex

sed -i "s/title{Python}/title{Dynamické modely populací}/" python.tex
sed -i 's/Corollary/Důsledek/' python.tex
sed -i 's/Theorem/Věta/' python.tex
sed -i 's/Remark/Poznámka/' python.tex
sed -i 's/Definition/Definice/' python.tex
sed -i 's/Example/Příklad/' python.tex

xelatex python
xelatex python
cd -
cp $directory/python.pdf Dynamicke_modely_populaci_text.pdf

echo "Pro upload na server spustit nasledujici prikaz"
echo "scp Dynamicke_modely_populaci_text.pdf cornus.mendelu.cz:html/dmp/"


