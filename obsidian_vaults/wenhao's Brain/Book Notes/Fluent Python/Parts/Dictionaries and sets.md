# Chapter 3. Dictionaries and Sets

### Dictionaries and sets
python dictionaries are highly optimized. The mapping type in python are mutable
![[class diagram dictionary.png|500]]

##### Hashable
An object is hashable if it has a hash value `hash()` ( from `__hash__()` method ), which is unique and comparable by `__eq__()` method. 

Most of the python (atomic) immutable build-in objects are hashable.

### Dictionary
##### Dictionary comprehensions
A *dictcomp* builds a dictionary instance by producing `{key:value}` pair from iterable
```python
>>> DIAL_CODES = [
... (86, 'China'),
... (91, 'India'),
... (1, 'United States'),
... (62, 'Indonesia'),
... (55, 'Brazil'),
... (92, 'Pakistan')
... ]
>>> country_code = {country: code for code, country in DIAL_CODES}
# which build a dictionary with country as key and code as values
```

##### Missing keys with setdefault()
There are several methods to get default value from a dictionary
1. `dict.get(key, default)` is a method to obtain values with an default values, however, **it does not give this default value to key if the key does not exist**
2. `dict.setdefault(key, default)`: if key in dict, return dict[key], otherwise, set dict[key] = default and return it
3. `defaultdict`: we can **instantiate a defaultdict by provide a callable** that will produce a default value as default value, whenever `__getitem__()` is passed a non-existent key (similar to an implicit `getdefault()` method)
    ```python
    from collections import defaultdict
    
    index = defaultdict(list)
    index[word].append(location)
    # if word not in index, defaultdict create a list as value to the key
    ```

##### collections.OrderedDict
Note: from python 3.7, the build in dict class is able to remember insertion order. See [here](https://docs.python.org/3/library/collections.html#collections.OrderedDict)
    
The keys in ordered dict will be maintained in insertion order, ensuring iteration over items in a certain order. `popitem()` method can pop the first item (`popitem(last = True)` pop the last item)
    
##### Counter
Counter accept a multiset and count the instances of hashable objects. It provide some method related to counting.
 ```python
ct = collections.Counter('abracadabra')
print(ct)
>>> Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}) 
ct.update('aaaaazzz')
print(ct)
>>> Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1}) 
print(ct.most_common(2))
>>> [('a', 10), ('z', 3)]
# it also implemented "+" and "-" operators to combine counters
 ```

### Set
##### Set operation
Set type implement the essential set operations
```python
a |  b   # return union of a and b
a |= b   # update a with union of a and b 
a &  b   # return intersection of a and b
a &= b   # update a with intersection of a and b
a -  b   # return a substract b
a -= b   # update a by substracting b from a
    
e in b   # element e is in set b
a <  b   # a is a proper subset of b
a <= b   # a is a subset of b
a >  b   # a is a proper superset of b
a >= b   # a is a superset of b
```
    
Using set operation, some operation become straight forward, For example:
```python
found = len( set(smaller_set) & set(larger_set) )
```
    
Class diagram of set
![[class diagram set.png|500]]

### Mechanism of fast searching for dict and set (hash)
##### Set operation is fast
![[speed of set operation.png]]

##### Hash table method
Dictionary and set use a *hash table* to implement searching: https://en.wikipedia.org/wiki/Hash_table

A hash table is a sparse array that is mostly empty. Each datapoint in the sparse array "buckets" contains two fields: a reference to the key and a reference to the value of the item ( in terms of set, it only keep a single reference to the key ). The procedure of hashing is as follows:
- For each key, the dictionary calculate the hash value (`hash()` function)
- To find a value of a key, python first obtain the hash value and use the least significant bits (first bits) of that number to find the position of the point in the sparse array.
- If the founded position is empty, keyerror is raised. If the key of founded point in the sparse array but does not match the input key, a hash collision happens. In such case, python check the next bits in the hash value and use the result to look up again a point in the sparse array, until the keys match. Then the item value is returned.
- Python will automatically manage the sparseness of the hash table, so that the size in memory of mapping object is dynamic

![[hash method.png|500]]

For a sparse hash table, most search happen with no collisions, and average number of collision is very few ( one or two )

##### Consequences of hashing for mapping types
1. keys must be hashable objects
2. dictionarys and sets have large memory overhead
3. key search is very fast with a sparse array
4. key ordering will depends on insertion order, and adding items to a dict or set may change the key order, since python will rebuild the hashtable when the size grow.
