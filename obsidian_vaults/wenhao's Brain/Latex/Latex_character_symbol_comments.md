# Keyboard, Document, Font and Comments
### General
##### keyboard
- The allowed characters for typing latex file are: `a-z A-Z 0-9 + = * / ( ) [ ]`
- Punctuation marks are `, ; . ? ! : ‘ ‘ -` as well as space tab and return.
- Special characters used in latex are `# $ % & ~ - ^ { } @ “ |`
- Quotation: single quotation: `this is single', double quotation ``this is double''. [Ref](https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/QuotDash.html)

##### Line numbers
To number the lines of the typeset file, we can use: `\usepackage{lineno}` and command: `\linenumbers`  in the preamble.

##### Structure of a document
*Preamble*: the part before `\begin{document}` is a preamble. The only required command in the preamble is the `\documentclass{}` command.

*Body*: from `\begin{document}` to `\end{document}` are the body of the document. 


### Special Symbols
The following characters are usually used and can be typed as follows:
- *Double quotes* is obtained by typing the single quote key twice. not by using the double quote key
- *Word hypenation* can be declared to be Hyphenation and hyphened correctly by using `\hypenation{data-base set-up}` in the preamble. [Hypenation are different from a dash](https://www.grammarly.com/blog/hyphens-and-dashes/)
- a *Dash* “-” is used to connect words.
- an *En dash* ”—” is used to indicate ranges and is typed as “--”, For example pages 23--25 as 23—25
- an *Em dash* (longer dash) is typed as “---” and is used to mark a change or to add emphasis, usuall used as `database---that contain data---is not a base for anything`
- *Nonbreakable spaces* is a tile `~` gives a interword non-breakable space that will not be separated by line break. For example, `Figure~\ref{}`
- *Ellipses* (...) are typed as \dots to have correct spacing, instead of three periods
- *Ligatures* are certain groups of characters are joined together when typeset automatically by latex. See [this](https://en.wikipedia.org/wiki/Ligature_(writing))
- `\today`, `\day`, `\month`, `\year` give the numbers related to current time

### Comments, Footnotes and Comments on page margins
##### Comments
Comments in a line follows `%`. To use precentage sign, escape it: `\%`.

For multiline comments, we the verbatim package:    
```latex
\usepackage{verbatim}
    
\begin{comment}
   ...
\end{comment}
```
    
##### Footnotes
Footnotes are typed as argument of a `\footnote{}` command. 

##### Comments at page margins
`\marginpar` command allows adding comments in the page margins (left or right depending on page number)

### Fonts
##### Different typesets
Text can be *upright*, *slanted*, *italic* or *small capital*. Slanted is in between upright and italic (italic is basically a different version of the font). Small capital typeset are captial letters that have the size of normal letter (i.e. `\textsc{a}` is A but with the size of a)

##### Font types
- *Monospaced* text are typeset as “typewriter style” (\texttt{}), other typeset are usually proportional.
- *Serifs*: serif font is the fonts which has a small horizontal stroke at the end of the vertical stroke of a letter.
- *Sans serif*: sans serif are fonts that does not have serifs.

##### Document Font family
- Each document class specifies a normal font family, which is the default font.
- It can be specified explicitly by \textnormal{} or {\normalfont ... }

##### Chaning fonts
Font change can be given by a command with a argument, such as \textbf{}, or it can be carried out in a command declaration, such as {\bfserise ...}. For long changes across paragraph, we need to use command declaration.
    
| Commands | declarations | meanings |
| --- | --- | --- |
| \textup | {\upshape ... } | upright font |
| \textit | {\itshape ...} | italic font |
| \textsl | {\slshape ...} | slanted version of the upright font |
| \textsc | {\scshape ...} | small capital, can be used for abbreviations |
| \emph | {\em ...} | emphasis |
| \textbf | {\bfseries ...} | bold text |
| \texttt |  | typewritter style |

Emphasis is italic or slanted depending on the document class, the difference—compared to italic environment—is that it will be upright if it is surrounded by italic text.

##### Italic corrections
To correct spacing after an italic font, we can use: `{\itshape serif\/}`, the `\/` command is called italic correction, which give some extra shape after an italic font. The command with argument version `\textit{}` treat the correction automatically.

##### Size changes
Normally, latex documents are typeset in 10 point type. Font size can be specified by optional argument in the document class. The title, subscripts etc. are adjusted automatically.

To explicitly change font size, we can use the following font declarations:
```latex
\Tiny \tiny \SMALL \Small \small \normalsize \large \Large \LARGE \huge \Huge
```
`\SMALL` is the size for subscript or superscript, `\Small` is the size for footnote.
    