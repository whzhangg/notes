
# Chapter 8. The IO Library

### IO classes
##### IO libraries
IO library defines the IO type (3 header, defines the IO classes):
- iostream(istream, ostream) : basic io type
- fstream(ifstream, ofstream) : read and write from named files
- sstream(istringstream, ostringstream) : read and write from a string

Types defined in fstream and sstrean inherit from basic iostream, so the members of iostream are also fstream and sstream

In case of wide character, we add 'w' for the corresponding objects: `ifstream` -> `wifstream`  for wide char

We cannot copy or assign objects of the IO type, we can pass it with non const reference

### Basic iostream
##### iostate
Read or write operation change the IO states of the IO type, *the easiest way to check a string is OK to use is to use* is as follows: 
```cpp
while (cin >> word)
		...                 // if the operation succeeded
```

##### system dependent IOstate
IO class defines function and class to access IO state. *iostate* is a class type and is used as collection of bits: `iostream::iostate` a machine dependent integral type
    
We have 4 constexpr values of type iostate, eacg represent bit patterns, they are used to test or set flags:

| constexpr | meaning |
| --- | --- |
|    `iostream::badbit`   |  incidate if a stream is corrupted (machine specific value) 
|   `iostream::failbit`   |  IO operation failed
|   `iostream::eofbit`    |   stream hit end of file
|   `iostream::goodbit`   |  stream is not in an error state (guaranteed to be zero)
    
##### member methods
We have the following member functions for iostream
- `s.good()`  return true if stream is valid
- `s.fail()`  true if failbit or badbit is set
- `s.bad()`  true if badbit is set
- `s.eof()`  true if eof is set
- `s.clear()`  reset all condition so the stream will be in a valid state
- `s.clear(flags)`  reset the given flag, flag is a iostate type
- `s.setstate(flags)`  add condition to the string
- `s.rdstate()`  return the current condition as a s.iostate value
    
For example:
```cpp
auto old_state = cin.rdstate();     // get the previous state
cin.clear();                        // we clear state informations
process_input(cin);
cin.setstate(old_state);            // add back the IO state attached
```

##### flush the buffer
System manage a stream buffer to hold data that is read or write. There are several conditions that cause buffer to flush:
1. program complete (not when program crashes)
2. full buffer
3. flush the buffer explicitly
4. change the behavior of stream by "unitbuf"

Use the following to flushing the buffer explicitly:
```cpp
cout << "hi" << endl;   // write hi and newline, flush buffer
cout << "hi" << flush;  // write hi, and flush, nothing is added
cout << "hi" << ends;   // write hi and add a null, flush buffer
```

we can use *unitbuf* to modify stream to do a flush after every write by `cout << unitbuf;`:
```cpp
cout << unitbuf;    // 
cout << "ssss";     // flush immediately
cout << nounitbuf;  // return to normal buffering
```

##### tie IO stream
If istream is tied to an ostream, then any attempt to read will flush the output first, this is usefull in interactive IO. To tie stream: `cin.tie(&cout)`

### File IO
In addition to inherited method from iostream, *fstream* defines more operation:
- `ifstream input;` creates the file stream object (also for ofstream)
- `ifstream input(s);` create object and opens a file named s
- `ifstream input(s,mode);`  open in a given mode
- `input.open(s);`
- `input.open(s, mode);`  open a file in a given mode
- `input.close();`  close the file
- `input.is_open();`  return bool indicating if the file is open

For example:
```cpp
ifstream in(file);
ofstream out;
out.open(file+".copy");
if (out)                    // check if out is succeeded, out is converted to bool
in.close();
in.open(file2);             // associate it with another file
```

##### File IO in scope
When fstream object go out of scope, the file it associated is closed automatically:

```cpp
for (auto p = argv+1; p!= argv+argc; ++p) {
		ifstream input(*p);
		if (input) process(input);
		else cerr << "cannot open "+string(*p);
}   
// input is in the block, and is destroyed at each iteration
```

##### file open mode
| mode | meaning |
| --- | --- |
| `in` |  |
| `out` | by default, opening file as out will discard the contents of the file
| `app` | open to the output mode and append to last (seek the end first)
| `trunc` | truncate the file (discard the content of the file) out mode also truncate file by default
| `ate` | seek the end immediately after open
|  `binary` | binary mode

For example:
```cpp
ofstream out("f1", ofstream::out)
out.open("fo",ofstream::app)
```

### string streams
##### inherit from the basic iostream with additional members:
- `sstream strm;` : create an unbound stringstream object
- `sstream strm(s);` : object hold a string s
- `strm.str();` : return a copy of the string
- `strm.str(s);` : copy string s into strm

##### Example usage
`istringstream` is useful when we need to process strings line by line, For example:
```cpp
string line, word;
vector<personInfo> people;

while (getline(cin,line)) {
		personInfo info;
		istringstream record(line);
		record >> info.name;
		while (record >> word)
				info.phones.push_back(word);
		people.push_back(info);
}
```

`ostring` is useful to format without write:
```cpp
for (const auto &entry : people) {
		ostringstream formatted, badNums;
		for (const auto &nums : entry.phones) {
				if (!valid(nums))
						badNums << " " << nums;
				else
						formatted << " " << format(nums);
		}
		
		if (badNums.str().empty())
				os << entry.name << " " << formatted.str() << endl;
		else
				cerr << "input error:" << entry.name << "invalid: " << badNums.str() << endl;
}
```
