#build .tex which depends on .png
paper.pdf: paper.tex figures/plot-data.png
	#pdflatex -interaction=nonstopmode -halt-on-error  paper.tex
	pdflatex paper.tex

#run .py with .dat and output as .png
figures/plot-data.png: figures/data.dat figures/plot.py
	cd $(<D);python plot.py -i data.dat -o plot-data.png
