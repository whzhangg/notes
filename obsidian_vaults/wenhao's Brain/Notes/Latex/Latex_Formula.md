# Formula
### General rules for inline formulas
No blank lines are premitted in a formula, and latex ignores spaces in math environment

##### Text
`\text{}` environment can type text in the formula environment. It will typeset its argument in the same size and shape of the surrounding text (especially for inline equation). If the surround text is italic, you need to use `\textnormal{}` in math environment

##### intertext
We can insert one or more lines of text in the middle of an aligned environment so that the equation before and after the text are aligned. The command is `\intertext`. For example:
```latex
\begin{align}
	f(x) &= x + yz & \qquad g(x) &= x + y + z\\ 
	\intertext{The reader may also find the followingpolynomials useful:}
	h(x) &= xy + xz + yz& \qquad k(x) &= (x + y)(x + z)(y + z)
\end{align}
```


##### Delimiter
Delimiters can be stratched to enclose the formula by specifying `\left` and `\right`. If you want to stretch a single delimiter, it need to be paired with a blank delimiter. We can also get a bigger version of the delimiter, without stratching them w.r.t the formula. We can use `\big(`, `\Big(`, `\bigg( `or `\Bigg(` to decorate a delimiter. If the stretching version result is not ideal. We should use the non-stretch version.

`|` symbol can be used as delimiter, but for binary relation, such as $\{x\in R\ |\ x^2 \leq 2\}$, it is typed as `\mid` to get a correct spacing.

Multiline subscript and superscripts. `\substack` command provides multiline limites for large operators. For example `\sum_{\substack{i<n \\ i \text{even}}}` is typeset as $\sum_{\substack{i<n \\ i \text{even}}}$. Substack can be used for subscript or superscript

##### Declare Operator
We can declare operator by: `\DeclareMathOperator{\Aut}{Aut}`

### Math symbols and fonts
##### Stretchable horizontal lines
Horizontal braces are typed as `\overbrace`: $\overbrace{a + a + \dots + a }$, A superscript adds a label to the brace: $\overbrace{a + a + \dots + a }^m$

`\overline` and `\underline` commands draw lines above or below a formula. For example 
$$
\overline{ \overline{X} \cup \overline{\overline{X}} } = \overline{ \overline{X} }
$$

`\overleftwrror` and `\overleftarrow` and `\overleftrightarrow` are typeset as: $\overleftarrow{a} \quad \overrightarrow{aa} \quad \overleftrightarrow{aaa}$. We similarly have underleftarrow and so on.

##### Spacing in math environment
In math environment, explicit spacing adjustments are very useful. `\,` and `\!` add or remove thinspace. `\quad` and `\qquad` are used to adjust aligned formulas or to add space before text.

##### Stacking symbols
Symbols can be stacked together using `\overset` commands. It take two arguments. The first argument is placed in a smaller size above the second argument. For example: $f(x) \overset{ \text{def}}{=} x^{2} - 1$ 

*sideset* commands set symbols at the 4 corners of large operator, which is shown as follows: `\sideset{ {ll}^{ul} }{{lr}^{ur}} }{\sum}`. The first two arguments are necessary and the third argument must be a large operator

##### Math symbol alphabets
The normal font in math is usually italic for letters and normal letter for digits. *Greek characters are treated as a math symbol*, Its bold version is preduced as \boldsymbol command $\boldsymbol{\alpha}$

The following alphabets are used in math:

| Greek | They are created by the corresponding math commands |
| --- | --- |
| Galligraphic | uppercase-only alphabet invoked by `\mathcal{}` |
| Euler Fraktur | invoked by `\mathfrak` command |
| Blackboard Bold | Uppercase-only alphabet, invoked by `\mathbb{}` |

##### Other type sets:
colon symbol in math should be typed as `\colon` command to have the correct spacing: $f\colon A \to B$.

$\|a\|$ double `|` are typed correctly by $\|a\|$, not $||a||$

### Display formula
##### General
Display formula can be called by `\[ \]`, equivalent to `\begin{equation*} \end{equation*}`

In general, in a display formula environment, lines are separated with `\\`, but we should not include `\\` at the end of the last line. No blank lines are permitted

Each line is numbered unless it has `\tag` or `\notag` on the line before line separate, or it is in a environment ended with `*`. Place \label command in each numbered line so that we can reference the equation

##### case
the cases construct is a specialized matrix that appear within a math environment such as equation and align. They are typed as follows, with `\begin{case}`. Inside the case environment, it’s basically aligned matrix with `&` and `\\`
$$
f(x)=\begin{cases}-x^{2}, &\text{if $x < 0$;}\\\alpha + x, &\text{if $0 \leq x \leq 1$;}\\x^{2}, &\text{otherwise.}\end{cases}
$$

##### Gather
Gather environment produce a group on one-line formulas, each centered on a separate line.


##### Matrices
`\begin{matrix}` environment will create a matrix inside a math environment. The matrix environment only provide a matrix up to 10 columns. For more columns, we need to declare: \setcounter{MaxMatrixCols}{12}

Dots span any number of columns can be given by `\hdotsfor{}` command
```latex
\begin{equation*}
	\left(                                 % add ( ) to the size
		\begin{matrix}
			a + b + c & uv & x - y & 27\\
			a + b & u + v & z & 1340
		\end{matrix}
	\right) =
	\begin{pmatrix}
		1   & 100 & 115 &  27\\
		201 & \hdotsfor{2}   & 1340
	\end{pmatrix}
\end{equation*}
```
produce the matrix: 
$$
\begin{equation*}\left(\begin{matrix}a + b + c & uv & x - y & 27\\a + b & u + v & z & 1340\end{matrix}\right) =\begin{pmatrix}1 &100& 115&27\\201 & 0 & 1 & 1340\end{pmatrix}\end{equation*}
$$

*Note*: matrix does not include ( ) at the side, which need to be given by `\left(` and `\right)`. *pmatrix* environment is a shorthand for `\left(\begin{matrix}` and the corresponding closing.

##### Inline matrix
Inline matrix can be typed as small matrix environment. For example $\left(\begin{smallmatrix}1 & 2 \\ 3 & 4\end{smallmatrix}\right)$ is typed as: `\left( \begin{smallmatrix} 1 & 2 \\ 3 & 4 \end{smallmatrix} \right)`
    

##### Array
Array is similar to matrix, but for an array, we have to specify the alignment of each column with option l, c, r for flush left, right and centered. The following array is typed as `\begin{array}{lccr}`
$$
\begin{equation*}\left(\begin{array}{lccr}
	a + b + c & uv & x - y & 27\\
	a + b & u + v & z & 134
\end{array}\right)\end{equation*}
$$

### Formula alignment

##### Simple alignment
In the align formula environment, insert `&` as the alignment point. There can only be one `&` per line, by convention, if the alignment point is adjacent to =, + and so on, the & should be placed before the symbol.

##### Aligned columns
In align environment, Lines of formula can be divied into columns. Multi-aligned columns can be implemented with the align environment. 

In an align environment, we can create multiple aligned columns. The number of columns are restricted by the width of the page. For example, a two columns formula can be created, with single line typed as `f(x) &= x + yz & g(x) &= x + y + z \\`:
$$
\begin{align} 
    f(x) &= x + yz       & g(x) &= x + y + z \\
    h(x) &= xy + xz + yz & k(x) &= (x + y)(x + z)(y + z) 
\end{align}
$$

The & symbol plays two different roles. For the second &, it is a *column separator*, and for the first and third &, it is a alignment point. In each column, there can only be a single alignment point. Therefore, *for n aligned columns, each line should have 2n - 1 & symbols*. The even-numbered & are column separators and the odd-numbered & are the alignment point.

##### Alignat environment
Alignat is a variant of the align environment. Align environment will automatically give appropriate separation between columns, the *alignat environment does not automatically separate columns*. Therefore, there are little difference between  & of column separation and & of alignment point.

Alignat environment require number of columns as arguments, `\begin{alignat}{2}` in the following case
$$
    \begin{alignat}{2}
    f(x) &= x + yz       & g(x) &= x + y + z \\
    h(x) &= xy + xz + yz & k(x) &= (x + y)(x + z)(y + z) 
    \end{alignat}
$$
Which leave no space between the column separation. We can maually specify space between the columns by `\quad`, for example.

This environment is important for multiply alignments in a single line. For example: (the `&` is before +, C and y)
$$
\begin{alignat}{2}
	(A + B C)x &+{} &C &y = 0,\\
	Ex &+{} &(F + G)&y = 23.
\end{alignat}
$$
In the alignat environment, the argument does not have to be precise. For two columns, the argument provided can be either 2, 3 or larger numbers
