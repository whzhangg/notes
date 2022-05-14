# Dynamic Memory
### Using dynamic memory
##### Why
Program use dynamic memory for one of the three purposes**
1. they don't know how many objects they will need (we do not allocate if we do not need it)
2. don't know the type of objects they will need
3. share data between several objects

##### dynamic objects
c++ let us allocate objects dynamically, which exist *until freed explicitly*. There are three different kind of ways to allocate objects:
1. *static memory*: local static objects, variables defined outside any function
2. *stack memory*: nonstatic objects defined inside functions (in a block). Stack memory are automatically created and destoryed by compiler
3. *heap* (free store): dynamically allocated objects

##### manging memory directly
The language defines two operator that allocates memory:
- `new`: allocate memory;  
- `delete` : frees memory

##### new
Objects allocated on the free store are unnamed, new allocates the memory and returns a pointer to the object it allocates:
```cpp
int *pi = new int;
int *pi = new int();        // new with some initial value
auto p1 = new auto(obj);    // use auto to infer object type directly
```
    
#####  delete
We return the memory back through delete expression (*pointer itself is not destroyed*). `delete` destorys the object to which its given pointer points and frees the corresponding memory
    
`delete` do not check if the pointer points to a dynamically allocated memory, It is our responsibility to make sure it's correct.

##### memory management
Dynamically allocated objects exist until they are freed.
```cpp
void use(T arg){
	foo *p = new T(arg);
	... use p
}   
// p goes out of scope and is deleted but the allocated memory is not freed
```

On the other hand, when we free memory by deleting a pointer(for example, `delete p;`), *the pointer itself is not deleted*, but it become undefined until it goes out of scope. 
```cpp
auto q = p;
delete p;
q = nullptr;    // q point to the same place as p, so we should prevent it being used
```

### Dynamic arrays
##### Allocating dynamic arrays
We can ask new to allocate an array of objects by specifying a number
```cpp
int *pi_a = new int[size];
int *pi_a = new int[size]( initializer );
```

*Note*: `new` do not return a object of an array type, we get a *pointer to the element type* of the array as a consequence, we *cannot* use array member such as iterator or ranged for

It is possible to allocate an empty array, in which case the pointer act as a off-the-end pointer.

##### Freeing dynamic arrays
To free a dynamic array, we use delete that include an empty pair of square brackets
```cpp
delete p;
delete[] p_a;
// [] indicates to the compiler that pointer addresses the first element of an array objects
```

### smart pointer
##### Basics
A smart pointer act like a regular pointer *but it automatically deletes the object to which it points*. A smart pointer cannot convert with ordinary pointers.

There are three kinds of smart pointer:
1. shared_ptr: we can make multiple different pointer to point to the same object
2. unique_ptr: opposite to shared_ptr
3. weak_ptr: weakly related to an object managed by shared_ptr

##### shared_ptr class
Shared_ptr can be created using templates:
```cpp
shared_ptr<int> p1;
shared_ptr<list<int>> p2;
// default initialization create a smart pointer holds a null pointer
```

We can use smart pointer in the way similar to using a pointer. 

`make_shared()` is defined in the memory header. It allocates and initializes an object in dynamic memory and return a shared_ptr. we must specify the type of object we want to create.

Make_shared use argument to construct an object of the given type, like similar to `emplace()`.
```cpp
shared_ptr<int> p3 = make_shared<int>(42);
auto p4 = make_shared<vector<string>>();        // default initialized dynamic memory
// p3 points to an int with value 42
```
    
##### reference counter
Shared_ptr keep track of how much other shared_ptr point to the same object using the reference count:
1. Copy or assign shared_ptr: the count is incremented (more shared_ptr pointing to the object)
2. Assign new value to shared_ptr or when it is destroyed (eg. go out of scope): the count is decremented (less shared_ptr pointing to the object)

When reference_counter goes to zero, the ptr automatically frees the object
```cpp
void process(shared_ptr<int> ptr) {
    use ptr;
}
shared_ptr<int> p(new int(42));
process(p);
```

In this example, smart pointer p is passed to process by value (copy), ptr is a copy of p and the reference counter of ptr increase by 1. after function execution, ptr go out of scope and is destroyed, reference counter automatically decrement by 1
    
##### operation common to shared_ptr and unique_ptr
```cpp
shared_ptr<T> sp    // create shared_ptr
unique_ptr<T> up
p                   // using a smart pointer name as a condition, true if it points to an object
*p                  // dereference
p.get()             // return a normal pointer
swap(p,q)           // swap two pointers
make_shared<T>(args)// create a shared object initialized with args
shared_ptr<T> p(q)  // create a copy of shared_ptr
p = q               // assignment, decrement p's reference count 
                    // (for other shared pointers associated with p) and increment q's count
p.unique()          // if p is the only pointer pointing to its object
p.use_count()       // return reference count
```

##### shared_ptr with new
We can initialize a smart pointer from a pointer returned by new
```cpp
shared_ptr<double> p1;
shared_ptr<int> p2(new int(43));    // initialize the smart pointer with new
shared_ptr<int> p2 = new int(43);   // but this result in error because we cannot directly convert
```

By default, we need to supply a pointer to the dynamic memory to initialize *shared_ptr* because *shared_ptr* will free the object afterward. if we supple a pointer to other resourse we must supply our own deletion code.
    
Mixing shared_ptr with pointer may cause the memory to be deleted:
```cpp
int *x = new int(42);
process(shared_ptr<int>(x));    // we make a shared pointer and pass it to a function
int j = *x;            // x become undefined because shared_ptr deleted the memory
```

##### normal pointer from smart pointer
Smart pointer define a function named .get() which return a normal pointer to the object: 
```cpp
int *p = smart_p.get()
```

##### dynamic object with exception
If an exception happens between new and delete and is not caught by the code, this memory will never be freed and there is no pointer to this memory. But *smart pointer will still able to automatically deleter the memory in the case of exception*.

### other smart pointers
##### unique_ptr
A unique_ptr owns the object to which it points, only one unique_ptr can pointer to a given object

##### weak_ptr
Weak pointer does not control the lifetime of the object to which it points. weak_ptr can points to an object that is managed by shared_ptr, which does not change the reference count of that shared_ptr