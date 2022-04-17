# Text vs. Byte
### String and encoding
##### Unicode
`str` in Python 3 store Unicode characters. A *character* is defined by its code point according to the unicode standard U+Num, where num is a 4 - 6 hexadecimal digits reranging from 0 to 1114111. For example, the letter A has a Unicode U+0041 (hexadecimal)
![[python string encoding.png|500]]
    
The *actual bytes* that represent a character, however, depend on the encoding used. Encoding converts the code pointed into actual byte that represent characters (in a text documents). 'uft-8' is the most common encoding method

##### Encoding and decoding
In short, a character can have different byte representations. We can *create bytes by encoding a string*, similarly, we can decode a bytes object to recover the string As an example, we can encode str:
```python
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t') 

>>> latin_1 b'El Ni\xf1o'
>>> utf_8   b'El Ni\xc3\xb1o'
>>> utf_16  b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'

#To recover string from bytes
b.decode('utf_8')
```

##### Detecting the encoding of a Byte Sequence
It is not possible to tell apart what coding is used to parse the bytes in a text file. In some protocols or file formats, text file contain *header information* on how the content is encoded. 

For a string of plain text without encoding information, we can usually only gauss, for example, using statistics. Python package *Chardet* provide such utility to identify encoding. It also provide a command line tool:
```bash
which chardetect
>>> /Users/wenhao/myapp/miniconda3/envs/pymat/bin/chardetect

chardetect make.sh
>>> make.sh: ascii with confidence 1.0
```

### Handling Text files
##### Best practice
The best practice of handling text files is to handle text exclusively on str objects. 

Python's file reading and writing perform necessary decoding and encoding. *However, we should take care to use the same encoding for writting and reading file*.
```python
>>> open('cafe.txt', 'w', encoding='utf_8').write('café') 4
>>> open('cafe.txt').read()
'cafÃ©'
```

If no encoding arguments are specific, `read()` and `write()` use default encoding that vary across systems. *We should not rely on default encoding*. Therefore, we should use 
```python
open(filename, 'w', encoding = 'utf_8')
```

##### Points touched in the book but not included here in this note
- String normalization for comparsion (Unicode provide different ways to represent the same characters, See page 117)
- Sorting unicode with non-ASCII characters
- str vs. bytes in functions and regular expressions
    
