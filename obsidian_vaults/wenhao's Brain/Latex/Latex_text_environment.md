# Words, Sentences and Paragraphs
### Horizontal spaces
##### Space character
The have the following rules about the space character: 
- Two or more space, end-of-line or a tab is the same as a single space
- A blank line or \par indicates the end of a paragraph
- Spaces at the begining of a line are ignored

*Note*: since end-of-line are treated as single space, we should not put punctuations at the beginning of the next line, which introduce a space between word and following punctuation

##### Adjusting horizontal space
Latex will place certain size space betweens words (interword space) and some larger space between sentences (intersentence space)

The following commands are often used to adjust horizontal space: 

| command | result | 
| --- | --- |
|  `\!` | negative thin space
|  `\,` | thin space
| `\-`   | interword space
| `\quad`  | larger space
| `\qquad`   | even larger space
| `\hspace{npt}` | take length as argument, but is ignored at the beginning of the line. `\hspace*{}` is the version that is not ignored at the begining of the line
| `\hfill`, `\dotfill`, `\hrulefill` | fill all available space within the line with spaces, dots or horizontal underline. (`A \hfill B` will produce A and B at the two end of the page)

##### Space after a period symbol
a period (`.`) after a capital letter are recognized as abbreviation or an initial, every other period signifies the end of a sentence.

If abbreviation does not end with a capital letter and is not at the end of a sentense, we should follow the period with a interword space \_ or tilt ~. Otherwise, latex will use intersentence space, which is larger. For initial, use thin space or no space, instead of interword space. For example, use: `W.H.Lampstone` or `W.\,H.\,Lampstone` instead of `W. H. Lampstone`.
    
If a capital letter followed by period is at the end of the sentence, precede that period with \@, which will require latex to use intersentence space.

### Vertical spaces
##### Line breaks
Controlling vertical spaces:
- `\\` and `\newline` break the line at the point of insertion but do not stretch it.
- `\linebreak` break the line at the insertion and stretches the line so it has normal width.
- The line following these command start with no indentation.

##### Paragraphs
Paragraphs are separated by blank lines or `\par` command. We can use `\noindent` or `\indent` command can be uesd to explicitly specifies indentation.

##### Pages
`\newpage` will finish the current page and start text on the next page.

`\pagebreak` will break the page at the point of insertion and stretch the current page to normal length.

##### Adjusting vertical position

| command | result | 
| --- | --- |
| `\\[length]` | can add specified interline space.
|`\vspace{}` | command also specifies vertical space and works similarly to `\hspace` command
| `\smallskip`, `\medskip`, `\bigskip` | provide standard amounts of vertical space (3, 6, 12 points)
| `\hfill` | fills the page with vertical space.

### Alignment
##### Boxes
`\text{}` command treat the enclosing text as if it were a single character

##### Alighment
flushright, flushright and enter environments are used to control the alignment of the paragraph. Within the flushright or center, we need to force new lines with \\

We can also use command declaration to achieve alignment: \centering \raggedright \raggedleft
    