# OpenMP

Created: November 10, 2021 6:09 PM
Description: using the OpenMP library
Tags: Programming

This note is based on [Guide into OpenMP](https://bisqwit.iki.fi/story/howto/openmp/), but parts that include complex usage is not included here

## Compiling C++ with openMP
On linux installed with gcc package, openMP is automatically included with the compiler. To compile program with openMP enabled, compile with:
```bash
g++-9 -fopenmp -o open.x openmp.cpp
```

To check the version of openMP, use `echo |cpp -fopenmp -dM |grep -i open` [ref](https://www.geeksforgeeks.org/openmp-introduction-with-installation-guide/)

All openMP constructs in C and C++ start with `#pragma omp` followed by parameters, ending with a newline.

## Multithread excution
### Parallel
a parallel construct creates N threads (N determined at runtime), all execute the next statement (or statement block). All threads join after the statement is finished. We can explicitly determine the number of threads by: `#pragma omp parallel num_threads(4)`
For example: 
```cpp
#include <iostream>
int main()
{
	#pragma omp parallel
	std::cout << "hello" << std::endl;
	std::cout << "Join !" << std::endl;
}

>>> g++-9 -fopenmp -o print.x print.cpp
hellohellohellohellohello
hello
hello
  

hello
  

join
# this output shows that the printing all happen at once, "hello"
# and std::endl are not necessarily printed at the same time.
```

### Loop construct: for
**Team**
A team of the group of threads execute the program. At the program start, the team only consists of a single thread.

`#pragma omp for` split the for loops so that each thread *in the current team* handles a different portion of the lop. Note `#pragma omp for` only divide the loops and dispatch dfferent portions to different threads available but it does not create the threads. `#pragma omp parallel` creates the threads. Therefore, the correct way to run for loop on multiply threads is:

```cpp
#pragma omp parallel
{
	#pragma omp for
	for(int n=0; n<10; ++n) printf(" %d", n);
}

// or simply
#pragma omp parallel for
for(int n=0; n<10; ++n) printf(" %d", n);

// The above is which is equivalent to running
int this_thread = omp_get_thread_num();
num_threads = omp_get_num_threads();
int my_start = (this_thread ) * 10 / num_threads; // 10 is the range of for loop
int my_end = (this_thread+1) * 10 / num_threads;
for(int n=my_start; n<my_end; ++n)
	printf(" %d", n);
```

**Scheduling for the for loop**
Scheduling determines how a for construct divide the portion of the for loop. Default is *static*, as shown in the above example, which calculate my_start and my_end for each thread before starting the loop

Other scheduling for for-loop include dynamic, guided or auto. With the *dynamic* schedule, each thread asks the runtime OpenMP library for an iteration number, handles it and then asks for another. It is useful to combine with the `ordered` loop

**Ordered clause in a for loop**
Ordered specifier make sure that in a multithread for loop, the specified statement is executed in the iteration order
- There can only be one ordered block in an ordered for loop
- an `ordered` clause must be enclosed in an ordered loop `#pragma omp parallel for ordered`

```cpp
#pragma omp parallel for ordered schedule(dynamic) // we use a dynamic scheduler
for(int n=0; n<100; ++n)
{
	files[n].compress(); // compression happens in parallel
	#pragma omp ordered
	send(files[n]); // send operation is ensured to send in sequential order 0 ~ 99
}

```
If the thread assigned to compress file 7 is finished but file 6 is not yet been sent. The thread will wait before sending and before compressing another file.

  
**Collapse clause**
In a nested for loop, we can use collapse to apply the threading for multiple iterations

```cpp

#pragma omp parallel for collapse(2)
for(int y=0; y<25; ++y)
{
	for(int x=0; x<80; ++x)
	{
		tick(x,y);
	}
}
```

### Sections
We can define sections that will run parallel, instead of for loops. In a sections block, we use `#progma omp section` to divide code into sections. For example:
```cpp
#pragma omp parallel sections // every work functions are run exactly once
{
	{ Work1(); }
	#pragma omp section // section split the sections
	{ Work2();
	  Work3(); }
	#pragma omp section // Work1, Work2 + Work3 and Work4 will run in parallel
	{ Work4(); } // Work2 + Work3 will run in sequence on a threads
}

```
Similar to `for`, sections do not create threads, therefore, `#pragma omp parallel sections` will only use the existing threads without `parallel`.

## Thread Safety
#### Atomic
We can specify the following statement to be atomic, which will either happen completely or not happen at all. 
```cpp
#pragma omp atomic
counter += value;
```
Atomic only support a few operators, for example `<<` operator is not supported: `error: invalid operator for ‘#pragma omp atomic’ before ‘<<’ token`
There are other types of atomic expression, called `atomic read`, `atomic write`, `atomic update` and `atomic capture` giving different behaviors

#### Critical construct
critical construct restricts the execution of the statment to a single thread at a time. We can supply a name to the critical statement and *no two threads can execute critical construct of the same name*. (Default name is used if omitted). The name of the critical constructs are global to the entire program.
```cpp
#pragma omp critical(dataupdate)
{
	datastructure.reorganize();
}
...
#pragma omp critical(dataupdate) // function reorganize() and reorganize_again() cannot
{                                // be invoked at the same time
	datastructure.reorganize_again();
}

```

#### Flush
flush modifier can be used to ensure that the variables observed in one thread is also the value observed by the other threads. For example: `#pragma omp flush(a, b)`. Usually, we use to use flush when we need to read and write variables from different threads.

  

## Data sharing
#### Data types
There are different types of data sharing we can specify:
- **Shared**: All thread access the same variable
- **Private**: If a variable specified as private, each thread will create a copy of the variable uninitialized with the same name and the same type as the original variable.
- **Firstprivate**: Each thread create a copy of the firstprivate variable similarly as private but initialize it with the original value
- **Lastprivate**: Lastprivate modifier will create a private copy of the variable uninitialized and copy back the value of the variable of the last task back to the original variable. For example, in a loop construct, the last value is the value assigned by the thread that handles the last iteration of the loop. [Pitfall of lastprivate](https://www.notion.so/Pitfall-of-lastprivate-dabe679e16424a7f94a7e01fa4f0d305)

```cpp
#include <string>
#include <iostream>
int main()
{
	std::string a = "x", b = "y";
	int c = 3;
	#pragma omp parallel private(a) firstprivate(b) shared(c) num_threads(2)
	{
		a += "k"; // uninitialized
		b += "k"; // initialized with "y"
		c += 7; // shared
		#pragma omp critical
		std::cout << "A becomes (" << a << "), b is (" << b << "), c is (" 
			      << c << ")" << std::endl; ;
	}
}

>>> A becomes (k), b is (yk), c is (17)
>>> A becomes (k), b is (yk), c is (17)
```
#### Reduction
Reduction clause allow accumulation of a shared variable. We need to specifiy the type of the accumulation. 
A Reduction is defined by: `reduction(operator:variables)` which can include a list of variables:
1. At the begining or a parallel excution, a private copy of the variable is made and initialized automatically to a specific value with respect to the given operation
2. At the end of the excution, the private copies are atomically merged into the shared variables using the defined operation
In addition, variables are initialzed to 0. For multiplication, default value is 1. Other operations such as min, max will initialized to suitable values, such as the largest or smallest representable number (for min and max).
```cpp
# The following three code work in the same way:
int factorial(int number) // with reduction
{
	int fac = 1;
	#pragma omp parallel for reduction(*:fac)
	for(int n=2; n<=number; ++n)
		fac *= n;
	return fac;
}

int factorial(int number) // using atomic multiplication
{
	int fac = 1;
	#pragma omp parallel for
	for(int n=2; n<=number; ++n) // note that this verion will be slower than
	{                            // the other two version because of the wait time
		#pragma omp atomic       // needed to visit the shared variable
		fac *= n;
	}
	return fac;
}

int factorial(int number) // use a priviate variable for parallel summation
{ 						  // nowait prevent any implicit barrier
	int fac = 1;
	#pragma omp parallel
	{
		int omp_priv = 1; /* This value comes from the table shown above */
		#pragma omp for nowait
		for(int n=2; n<=number; ++n)
			omp_priv *= n;
		#pragma omp atomic
		fac *= omp_priv;
	}
	return fac;
}

```

  
## Synchronization
#### Barrier
Barrier directive causes all threads to wait until all other threads have encountered the barrier

```cpp
#pragma omp parallel
{
	// All threads execute this
	SomeCode();
	#pragma omp barrier
	// All threads execute this, but not before all threads have finished somecode()
	SomeMoreCode();
}

```

There are also *implicit barriers at the end of each paralle block and sections block*, unless nowait modifier is used:
```cpp
#pragma omp parallel
{
	#pragma omp for nowait // nowait
	for(int n=0; n<10; ++n) Work();
	
	// This line may be reached while some threads are still executing the for-loop.
	SomeMoreCode();
}

```

#### Thread cancellation
We can cancell threads (for example, when the results are found by one of the thread) by defining `#pragma omp cancel for`.  
- If one thread called cancellation, all other threads will also finish by checking at the **cancellation points**, which is one of the following: implicit and explicit barriers, cancell and cancellation point. 
- To enable checking for cancellation, we need to set global variable OMP_CANCELLATION (becase checking for cancellation is introduce large overhead in performance)

```cpp
#include <stdio.h> // For printf
#include <string.h> // For strlen
#include <stdlib.h> // For putenv
#include <unistd.h> // For execv
#include <omp.h> // For omp_get_cancellation, omp_get_thread_num()

static const char* FindAnyNeedle(const char* haystack, size_t size, char needle)
{
	const char* result = haystack+size;
	#pragma omp parallel
	{
		unsigned num_iterations=0;
		#pragma omp for
		for(size_t p = 0; p < size; ++p)
		{
			++num_iterations;
			if(haystack[p] == needle)
			{
				#pragma omp atomic write
				result = haystack+p;
				// Signal cancellation.
				#pragma omp cancel for
			}
			// Check for cancellations signalled by other threads:
			#pragma omp cancellation point for
		}
		// All threads reach here eventually; sooner if the cancellation was signalled.
		printf("Thread %u: %u iterations completed\n", omp_get_thread_num(), num_iterations);
	}
	return result;
}

int main(int argc, char** argv)
{
	if(!omp_get_cancellation())
	{
		printf("Cancellations were not enabled, enabling cancellation and rerunning program\n");
		putenv("OMP_CANCELLATION=true");
		execv(argv[0], argv);
	}
	printf("%s\n%*s\n", argv[1], FindAnyNeedle(argv[1],strlen(argv[1]),argv[2][0])-argv[1]+1, "^");
}

```