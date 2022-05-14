# Documents
### Referencing
##### Labeling and referring
`\label` command gives equation, figure, table etc. a symbolic label. One of the convention for labeling is that: Equations start with E:, Table start with T: and so on. For example: `\label{E:eq1}`

`\ref` give reference for the equations. It is important that before `\ref`, a tile `~` is included: `Figure~\ref` so that Figure (1) will not break on linebreak

`\eqref` provide reference number in parenthesis.

##### Tagging
Equations can be tagged by attaching a name with `\tag{name}`.
$$ \begin{equation}\int_{0}^{\pi} \sin x \, dx = 2 \tag{Int}\end{equation} $$
*Tags are absolute*. This equation will always be referred to by the tag. which will be used to label the equation instead of equation number. As compared to equation number, which will change when the file is edited.

### Sectioning
A `\section` can be subdivided into `\subsections`, which can themselves be divided into `\subsubsections`, `\paragraphs`, and `\subparagraphs`.
- Any sectioning command can be followed by a `\label` command so that they can be referenced.
- Arguments for sections are titles, which are used for table of contents and therefore the command inside should be protected by \protect command.
- If a section are is not numbered (not `\section*{}`), then its subsections should also be unnumbered to avoid bugs

### Floating
##### Floating objects
Tables and illustrations are treated in a special way so that they do not break across pages - called floating objects - and are moved by latex to top, bottom of the current page or next page.

Latex provide *table* and *figure* environment for typesetting floats. The two are identical except that figure environments are captioned “Figure” and table environments are numbered as Table. 

For table environment, the `\caption{}` command is optional and should precede the table. A table environment can include multiply table, each with its own caption.

##### Position control
Table and Figure environment can have optional arguments, which influence latex’s placement of the typeset table. It can be one of the four letters: **b** (bottom), **h** (here), **t** (top of the pages) and **p** (a separate page).

They can be combined, for example: [ht]. The default option is [tbp]. [!h] requests this table to be placed where it is in the source file. Similar [t] or [b] can also be prefixed by !

### Simple bibliographies
The simplest way to add bibliographies is to use the bibliography environment, as follows:
- The *thebibliography* environment takes one argument, giving the widest reference number it must generate. For example, {9} means one digit wide reference index. {99} means two digit space for reference number.
- Each item is introduced with `\bibitem{}`, which is cited using `\cite{}`. The argument gives the name of the citation in the source file. They are similar to `\label` and `\ref`.
- The bibliography of the document itself is automatically numbered. However, in this environment, the bibliographic list is printed as the order in the source file

For example: 
```latex
% no other things are needed, for amsart environment.
\cite{gC13}
...
\begin{thebibliography}{9}
\bibitem{gC13}
	G. Cz\’edli, \emph{Patch extensions of slim lattices}, Algebra Universalis \textbf{88} (2013), 255--280.
\bibitem{sF98}
	Soo-Key Foo, \emph{Lattice constructions}, Ph.D. thesis, University of Winnebago, 1998.
\end{thebibliography}
```

### Table of contents
To add table of contents,use command `\tableofcontens`. The command will generate a file filename.toc which lists all the sectioning, as well as page numbers.