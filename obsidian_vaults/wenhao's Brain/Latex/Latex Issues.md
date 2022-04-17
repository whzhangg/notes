# Latex Subproblems
Created: October 3, 2021 3:10 PM

### Installation
##### Install the texlive on Windows
Currently I install with the medium sized package + bibtex + addition.

##### Install packages from ctan
The following steps probably let you install packages on windows machine. But we should avoid it as much as possible. 
1. get packages: Download the packages from the website and unpack it in the folder `/texmf-local` in the latex install positions
2. After this you need to update the texlive distribution `mktexlsr /.././texmf-local`
If the library is distributed in the form of .dtx file, you can run `latex **.dtx` to get `.cls` file (macro)

As an example, to install `achemso` package
1. Unzip the zip file download from the internet
2. Run `latex achemso.dtx` to obtain all the files
3. Since they are not well organized file, I mannually put those files in the right place:
    ```
    .cfg           goes to /texmf-local/tex/local
    .cls, .sty     goes to /texmf-local/tex/achemso
    .bib .bst      goes to /texmf-local/bibtex/bib/achemso and /bst/achemso file
    .dtx           goes to the /texmf-local/source, but it is not needed
    ```
4. Update the directory: `mktexlsr /texmf-local`

For reference, see https://askubuntu.com/questions/1114302/how-to-use-revtex4-2-with-ubuntu-18-04,  http://tug.org/tds/tds.html#Local-additions](http://tug.org/tds/tds.html#Local-additions for directory structures

Following is from the installation note of a package
```
Installation:

Just run LaTeX on (package).ins, which generates (package).sty.  
If you want the documentation as a dvi, run LaTeX on (package).dtx, 
otherwise use the provided format.  

Move the .sty-files to a directory where LaTeX looks for the input files.  
Update your file name database and you're done.
```

### Compile with reference
The one that will work currently:
1. use the package **biblatex** which should come as installed with texlive if you choose the bibtex related package in the install.
2. Put the following part in the pereamble
    ```latex
    \usepackage[style=numeric,backend=bibtex,sorting=none]{biblatex}
    \addbibresource{reference.bib}
    # bibtex and biber can both work as backend, but bibtex seems to work better
    # sorting = none gives a normal sorted reference, (index of alphbet sorting)
    ```
3. In the end of the document, add `\printbibliography[title={Reference}]`, reference here is the title for the section
4. To compile, compile in the following order
    ```bash
    pdflatex doc.tex
    bibtex   doc
    pdflatex doc.tex
    pdflatex doc.tex
    ```
    
For more options, see this site https://www.overleaf.com/learn/latex/Articles/Getting_started_with_BibLaTeX, and https://tex.stackexchange.com/questions/51434/biblatex-citation-order
    
This is a list of citation styles that can be used in biblatex: https://www.overleaf.com/learn/latex/Biblatex_citation_styles. For example, chem-acs, phys, nature, science
