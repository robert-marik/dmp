# Build book by sphinx. Jupyterbook does not (probably) work well with double dollas 
directory=../_build/html

touch ../intro.md
sed -i 's/ipython3/ipython3\n:tags: ["hide-input"]/' ../prednaska/*.md 
sed -i ':a;N;$!ba;s/\(:tags: \["hide-input"\]\)\n\(:tags: \["hide-input"\]\)/\1/g' ../prednaska/*.md
sed -i ':a;N;$!ba;s/\(:tags: \["hide-input"\]\)\n\(:tags: \["hide-input"\]\)/\1/g' ../prednaska/*.md
#~/anaconda3/bin/sphinx-build ../ $directory -b html
sphinx-build ../ $directory -b html

# Loop over lectures do open ipynb files in Colab rather than md files.
echo "Fixing Colab links from md to ipynb."
for i in $directory/prednaska/*.html
do
    sed -i 's/colab.research.google.com\/github\/robert-marik\/dmp\/blob\/main\/prednaska\/\(..\)\.md/colab.research.google.com\/github\/robert-marik\/dmp\/blob\/gh-pages\/_sources\/prednaska\/\1.ipynb/' $i
done

sed -i 's/colab.research.google.com\/github\/robert-marik\/dmp\/blob\/main\/intro\.md/colab.research.google.com\/github\/robert-marik\/dmp\/blob\/gh-pages\/_sources\/intro.ipynb/' $directory/intro.html

sed -i 's/Corollary/Důsledek/' $directory/prednaska/*html
sed -i 's/Theorem/Věta/' $directory/prednaska/*html
sed -i 's/Remark/Poznámka/' $directory/prednaska/*html
sed -i 's/Definition/Definice/' $directory/prednaska/*html
sed -i 's/Example/Příklad/' $directory/prednaska/*html
sed -i 's/Podle Robert/Autor Robert/' $directory/*/*html

sed -i 's/\\begin{split}//' $directory/prednaska/*html
sed -i 's/\\end{split}//' $directory/prednaska/*html

# Copy custom css file
cp custom.css $directory/_static/styles/
cp custom.css $directory/_static/
cp custom.js $directory/_static/
