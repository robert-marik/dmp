# Build book by sphinx. Jupyterbook does not (probably) work well with double dollas 
directory=../_build/pdf

sphinx-build ../ $directory -b latex

sed -i 's/sphinxShadowBox/comment/' $directory/python.tex 
sed -i 's/documentclass\[/documentclass[twocolumn,/' $directory/python.tex
cd $directory

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


