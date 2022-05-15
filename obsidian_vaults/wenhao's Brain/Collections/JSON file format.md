# JSON format
Created: October 3, 2021 3:33 PM

### JSON's basic data types
Json is a format of string, not a file format
##### Numbers
In json, numbers can be signed decimal number that may contain a fractional part, and:
- may use exponential E notation, but cannot include non-numbers such as NaN.
- the format makes no distinction between integer and floating-point.

##### Strings
Strings can be a sequence of zero or more Unicode characters. They are delimited with double-quotation marks and support a backslash escaping syntax.

##### Boolean
Either of the values: true or false

##### Array
Array in json is an ordered list of zero or more values, each of which may be of any type. Arrays use square bracket notation with comma-separated elements.

##### Objects
Objects are collections of name–value pairs where the names (also called keys) are strings. Objects are intended to represent associative arrays where each key is unique within an object. 

Objects are delimited with curly brackets and use commas to separate each pair, within each pair the colon '`:`' character separates the key or name from its value.

##### Null
Null stand for an empty value, using the word null

##### Whitespace
White space are  ignored around or between syntactic elements (values and punctuation, but not within a string value).
- [ space, horizontal tab, line feed, carriage return ] are considered whitespace for this purpose.
- in particular, the byte order mark must not be generated by a conforming implementation

##### Comments
JSON does not provide syntax for comments

### Example of a JSON file
```json
{
	"firstName": "John",
	"lastName": "Smith",
	"isAlive": true,
	"age": 27,
	"address": {
		"streetAddress": "21 2nd Street",
		"city": "New York",
		"state": "NY",
		"postalCode": "10021-3100"
	},
	"phoneNumbers": [
		{
			"type": "home",
			"number": "212 555-1234"
		},
		{
			"type": "office",
			"number": "646 555-4567"
		}
	],
	"children": [],
	"spouse": null
}
```