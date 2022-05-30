# Latex packages
### AMS-latex
If we are using document class, then all the ams packages are implicitly loaded.

If we are using other document class, this [webpage](https://tex.stackexchange.com/questions/32100/what-does-each-ams-package-do) says that to basically obtain all ams-utilities, *we should import amsmath, amssymb and amsthm* package:
```latex
\\usepackage{amssymb}
\\usepackage{amsmath}
\\usepackage{amsthm}
% or 
\\usepackage{amssymb, amsmath, amsthm}
```

### IEEE style
IEEE style webpage can be found here: https://www.ieee.org/conferences/publishing/templates.html

### achemso packages
https://github.com/josephwright/achemso/blob/main/achemso-demo.tex
https://qiita.com/swakamoto/items/579a6b537d58b82b078b
(https://pubs.acs.org/page/4authors/submission/tex.html