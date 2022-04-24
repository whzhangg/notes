
# Sequential Containers

### sequential containers
##### Containers in standard library
The standard library provide several sequential containers. In general, each container is *defined in a header file with the same name as the type*, for example `#include <vector>`

They all provide sequential access to the elements, but offer different performance of:
1. cost to add or remove elements, 
2. cost to perform nonsequential access

##### Different sequential containers
Vector, String, list, deque and array are the basic sequential containers:
- vector: flexible size, fast access. elements are hold in contiguous memory, adding elements sometime require movement of the whole object
- string: similar to vector
- list, forward_list: fast add or remove anywhere in the container, do not support random access
- deque: fast random access; fast insert/delete at front or back, but not at middle
- array (this array type is different from the build in array)

##### Operations are provided by containers
The following operations are provided by all containers:
```cpp
types:
		iterator
		const_iterator
		size_type
		difference_type
		value_type
		reference
		const_reference
constructure:
		Container c;
		Container c1(c2);           <- copy construction
		Container c(begin,end);     <- constructe by iterators
Assignment and swap
		c1 = c2;
		a.swap(b);                  <- swap elements
		swap(a,b);
Size
		c.size()
		c.max_size()
		c.empty()                   <- true if container is empty
Adding elements
		( when we insert an object t, the object is copied, we do not insert the object itself )
		c.push_back(t)              <- create an element with value t (object) at the end
		c.emplace_back(args)        <- initialize a new element at the end of c
		c.push_front(t)
		c.emplace_front(args)
		c.insert(p,t)               <- create an element with value t before the iterator p,
																	 return an iterator of the element that is added
		c.emplace(p,args)           <- initialize new element by args before iterator p
		c.insert(p,il)              <- il is a { } list of element values, insert before iterator p
		c.insert(p,begin,end)       <- insert the elements given by a iterator range, before p
Accessing elements
		c.back()                    <- return a ***reference*** to the last elements in c
		c.front()                   <- return a reference to the first elements
		c[n]                        <- return a reference to element indexed by n
		c.at(n)                     <- return a reference to element indexed by n, check range
Erasing elements
		c.pop_back()                <- return void, remove the last element
		c.pop_front()
		c.erase(p)                  <- remove the element denoted by an iterator, or a range
		c.erase(begin, end)            return the location after the last element that is removed
		c.clear()
Resize
		c.resize(n)                 <- resize c to have n elements, discard excess elements
Manage capacity (vector and string)
		capacity -> how many elements we can hold in the current memory space
		c.shrink_to_fit()           <- reduce capacity to equal to current size
		c.capacity()                <- return number of elements c can have before reallocation is necessary
		c.reserve()                 <- allocate space for at least n elements
Obtain iterators
		c.begin(), c.end()          <- return iterators to the end and one pass end
		c.cbegin(), c.cend()        <- return const_iterator
```

##### iterator ranges
An iterator range is denoted by a pair of iterators refer to elements in the same container. Iterator range is left-inclusive : `[ begin, end )`.

##### Reverse iterators
Most container provide reverse iterators that go backward through a container `++` on a reverse iterator yields previous element.

##### Container initialization
Except array, most default constructor creates an empty container, we can create a container by copy initialize or passing an iterator range:
```cpp
 list<string> authors = {"A","B","C"};                       // list initialization
 list<string> list2(authors);                                // copy initialization
 forward_list<string> words(authors.begin(),authors.end());  // range initialization
 ```
    
Array must be fixed size, array elements will be default initialized.

##### Relational operators on containers
Two containers are compared as follows, similar to string comparsion:
1. if both container are the same size and all elements are equal, they are equal
2. container are of different size but all element of the smaller one is equal to the corresponding element of the larger container, then smaller one is smaller
3. if the smaller container is not the initial subsequence of the other, then comparsion depends on comparing the first unequal elements

##### Container adoptor
An adaptor is a mechanism for making one thing act like another, a contain adaptor take an existing container and make it act like a different type. Library define three adaptor: stack, queue and priority_queue
