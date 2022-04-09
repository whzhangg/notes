# Regular Expression
Created: October 21, 2021 11:38 AM

### Method
https://docs.python.org/3/library/re.html
To import the module: `import re`

`re.compile(pattern)`
Return a regular expression object
`re.search(parttern, string)`
Find the first location where the RE give a match, and return a matchobject
`re.findall(pattern, string)`
Return all match of pattern in string, as a list of strings
`re.finditer(pattern, string)`
Return the matched string in an iterator
`re.sub(pattern, replace, string, count=0)`
Replace the pattern in the string by "replace"
`re.match(pattern, string)` 
Match only the begining of a string, return a matched matchobject, otherwise return None
`re.split(pattern, string, maxsplit=0)`
Split the string by occurences of a pattern

Regular expression objects may also be useful, see [regular-expression-objects](https://docs.python.org/3/library/re.html#regular-expression-objects)
For example, `pattern.search(string)` where `pattern` is a regular expression object.

### Special Characters
`.` match any character except a new line
`^` match the start of the string
`$` match the end of the string or just before the newline at the end of the string
`*` cause the resulting RE to match 0 or more repetitions of the preceding RE
`+` cause the resulting RE to match 1 or more repetitions of the preceding RE
`?` cause the resulting RE to match 0 or 1 repetitions of the preceding RE
`*?, +?. ??` the above qualifiers are greedy and match the longest string possible, adding ? will match the minimum string
`{m}` specifies exact m copy of the string, eg. a{6}
`{m,n}` specifies RE to match from m to n repetitions of the preceding RE
`{m,n}?` as the previous one, but now it attemp to match as few repetition as possible
`\` escape special characters
`[ ]` incidate a set of characters eg. `[amk], [a-zA-Z]`
`[^ ]` Adding ^ as the first character (only if the first) will match anything but the included character
`A|B` where A B are REs, will match either A or B from left to right
Specific points related to `[ ]`
- If we place - at the begining or end, it will match literal "-" [a-]. special characters will lose their special meaning

### Other Special Characters
`\A` match the start of the string
`\b` match the empty string, at the beginning or end of a word
`\B` match the empty string, but only when it is not at the begining or end of the word
`\d` match decimal digits, equivalent to [0-9]
`\D` match non digit characters, equivalent to [^0-9]
`\s` match any whitespace character, [ \t\n\r\f\v] (first character is white space)
`\S` match non whitespace character
`\Z` match the end of a string