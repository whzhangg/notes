# make file for all the notes that I have created over the time

all: grouptheory statistical mechanics

statistical: part1.pdf part2.pdf
grouptheory: group_theory.pdf
mechanics: classic_mechanics.pdf linear_response_theory.pdf quantum_condition.pdf

%.pdf: %.tex
	cd $(<D); \
	pdflatex $(<F); \
	pdflatex $(<F); \
	$(clean); \
	cd -

# -f does not produce error message if file does not exist
define clean
	rm -f *.aux;\
	rm -f *.out;\
	rm -f *.log;\
	rm -f *.toc
endef

VPATH = electron phonon physics mathematics
 
VPATH += physics/statistical_physics
VPATH += physics/mechanics