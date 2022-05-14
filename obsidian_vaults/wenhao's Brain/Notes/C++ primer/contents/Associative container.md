# Associative Containers
### associative containers
##### Basics
Elements in an associative container are stored and retrieved by a key, instead by positions. They *support efficient lookup and retrival* by key.

There are 8 associative containers, as a combination of:
1. set or key
2. unique keys or duplicate keys
3. order or unorder
    
##### associative container defined in library
```cpp
map             multimap            // map header
set             multiset            // set header
unordered_map   unordered_multimap  // unordered_map header
unordered_set   unordered_multiset  // unordered_set header
```

##### Define a map or set
The following example defines the container:
`map<string, size_t> word_count;` Define two types as a pair
`set<string> exclude = {"the","and"};` Define type
`map<string, string> authors = { {"joyce","james"}, {"Austen","Jane"} };` List initialize the defined map, A key value pair is given inside curly braces { }

##### Requirement on key type
Key type of ordered type must be able to compare using operator `<`

##### pair type
A type "pair" is defined in the utility header, which hold two public data member:
```cpp
pair<string, size_t> word_count;                // a pair
pair<string, string> author{"James", "Joyce"};  // pair with initialization
author.first    // "James"
author.second   // "second"
```
`make_pair(v1,v2)` return a pair initialized from v1 and v2, type is inferred from v1 and v2

### operations on associative containers
##### iterators
Iterator of a map point to a pair: 
```cpp
auto map_it = word_count.begin(); 
cout << map_it->first
```

Iterator of a set are const. we cannot change the key in a set

##### adding elements
Insert only when the element with the given key is not already in c
```cpp
c.insert(v)             // insert an elements
c.emplace(args)         // insert by initialization
c.insert(b,e)           // insert by iterators
c.insert(il)            // insert by list
c.insert(p,v)
c.emplace(p,argus)
    
// For example   
word_count.insert({word,1});        // insert a pair
word_count.insert(make_pair(word,1));
```
The return of insert is a pair, the first member is an iterator to that element inserted, or where is already is. The second member is a bool indicating whether the element was inserted.

Adding elements to a multiset or multimap keys in multi-container is not unique, insert always insert an element so they act like a vector of pairs

##### Removing elements
`c.erase(k)`: remove every element with key k from c, return the number of elements removed
`c.erase(p)`: remove the element denoted by the iterator
`c.erase(begin,end)`: remove element in the range

##### Accessing elements
Map contain subscript operator and a "at" function:
```cpp
c[key] 
c.at(key) // access the element with key k;
```
    
If the key is not already present, a new element is created and inserted for that key. `word_count["Anna"] = 1`: create a default initialized element with key "Anna" and assign 1 to its value
    
The following method do not add elements automatically
```cpp
c.find(key)             // return off-the-end if not found
c.count(key)            // number of elements with key k
c.lower_bound(key)      // iterator to first element with key not less than k
c.upper_bound(key)      // iterator to first element with key greater than k
c.equal_range(key)
```

When a multiset has multiple elements of a given key, *those elements will be adjacent*, we can use find and count to get all elements

##### Unordered containers
unordered containers use has function and == operator of the keys to find elements which is useful when we can not give order to the keys
