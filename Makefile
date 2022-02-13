# make file for all the notes that I have created over the time

all: grouptheory statistical mechanics general electrons phonon

general: steerable_cnn.pdf atomicunits.pdf
statistical: part1.pdf part2.pdf
grouptheory: group_theory.pdf
mechanics: classic_mechanics.pdf linear_response_theory.pdf quantum_condition.pdf

electrons: defect.pdf effectivemass.band.model.pdf phonondrag.short.pdf TB_by_MLWF.pdf transport.in.anisotropic.parabolic.bands.pdf wavepacket.pdf
phonon: adaptive.smearing.pdf green.kubo.pdf interpolate_phonon.pdf quantization.pdf unified.transport.pdf

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
VPATH += physics/electron
VPATH += physics/phonon
VPATH += general
