VPATH = electron phonon physics

default: group_theory.pdf

%.pdf: %.tex
	cd $(<D)
	pdflatex $(<F)
	pdflatex $(<F)
	cd -
	$(clean)


define clean
	rm $*.out
    rm $*.log
    rm $*.aux
endef

#pdflatex $*.tex
#pdflatex $*.tex
