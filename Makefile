#build .tex which depends on .png
paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

#run .py with .dat and output as .png
plot-%.png: %.dat plot.py
	./plot.py -i $*.dat -o $@
