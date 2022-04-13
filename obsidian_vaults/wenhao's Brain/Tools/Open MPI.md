# OpenMPI

Created: September 28, 2021 9:08 PM
Description: open MPI nodes for fortran and C++
Tags: Programming

The following are the reference for this note:
This is a reference for all MPI functions: https://www.mpich.org/static/docs/latest/www3/
An Introduction tutorial: https://mpitutorial.com/tutorials/
mpi_constants: https://www.mpich.org/static/docs/v3.2.x/www3/Constants.html

Quick Links:
[[Open MPI#mpi_init]]
[[Open MPI#mpi_finalize]]
[[Open MPI#mpi_comm_rank]]
[[Open MPI#mpi_comm_size]]
[[Open MPI#mpi_comm_split]]
[[Open MPI#mpi_reduce]]
[[Open MPI#mpi_allreduce]]
[[Open MPI#mpi_send]]
[[Open MPI#mpi_receive]]
[[Open MPI#mpi_bcast]]
[[Open MPI#mpi_barrier]]
[[Open MPI#mpi_scatter]]
[[Open MPI#mpi_gather]]
[[Open MPI#mpi_allgather]]

### Data Types
Open MPI contains build-in variables that specifies data type, In the case of *Fortran*, we have:
- MPI_REAL
- MPI_INTEGER
- MPI_LOGICAL
- MPI_DOUBLE_PRECISION
- MPI_COMPLEX
- MPI_DOUBLE_COMPLEX

### Communicator
**MPI_COMM_WORLD** is a pre-defined communicator, which do not require variable definition. Other communicators can be created by `mpi_comm_split` method, which give new communicators.

### MPI methods
##### mpi_init
`mpi_init(ierr)` initial the MPI execution environment

##### mpi_finalize
`mpi_finalize(ierr)` finish the MPI environment. Calling `mpi_init` without calling `mpi_finalize` will cause error in the program. Therefore, we meed to makesure to exit properly with `mpi_finalize(ierr)`

##### mpi_comm_rank
`mpi_comm_rank(comm_world, rank, ierr)` returns the rank of the current processes

| parameters  |  |
| --- | --- |
|comm_world | communicator
|rank       | the rank of the calling process

##### mpi_comm_size
`mpi_comm_size(comm_world, size, ierr)` returns the number of processes in the mpi environment.

| parameters  |  |
| --- | --- |
|comm_world | communicator
|size       | number of the processes

##### mpi_comm_split
Create subgroups and return their communicator
```c
mpi_comm_split(comm, color, key, new_comm, ierr)
```

| parameters  |  |
| --- | --- |
|color | control of subset assignment (nonnegative integer). Processes with the same color are in the same new communicator
|key | control of rank assignment
|new_comm | new communicator to return

##### mpi_reduce
mpi_reduce gather data to the root note.
```c
mpi_reduce(send_data, receive_data, size, type, op, root_id, comm_world, ierr)
```

| parameters  |  |
| --- | --- |
| send_data | data array as inputs from each process
| receive_data | contains the reduced resuld, only available to the root, should be the same size of send data
|size | number of elements in the array
|data_type | the mpi specific data_type
|op | the mpi specific operation
|root | integer number of the root node
|comm_world | the communicator
|ierror | specific to fortran, error code

*Note:* the receive_data is only written to the memory of the root node.
*Note:* send_data should be the starting position of the data array_v(1,1) <- starting elements

| reduce operations | |
| --- | --- |
|MPI_MAX, MPI_MIN | maximum and minimum elements
|MPI_SUM, MPI_PROD | summation and produce
|MPI_LAND, MPI_LOR | logical
|MPI_BAND, MPI_BOR | bit wise operation

Operations are element wise in the array

##### mpi_allreduce
`allreduce` will reduce the values and distribute the results to all processes. All processes will get a copy of result in receive_data.
```c
mpi_allreduce(send_data, receive_data, size, type, op, comm_world, ierr)
```
Parameters are the same as `mpi_reduce` expect *that it does not require root id*

##### mpi_send
Send the given data to a destination. 
```c
mpi_send(data, size, type, destination, tag, comm_world, ierr)
```

| parameters  |  |
| --- | --- |
|data | address of the send data (data buffer)
|size | number of elements to send
|type | mpi specific data_type
|destination | rank of the destination
|tag | message tag
|comm_world | communicator

*Note:* tag is an arbitrary integer to identify the message

##### mpi_receive
Receive data from a given source:
```c
mpi_receive(data, size, type, source, tag, comm_world, status, ierr)
```

status parameter
- We have one additional parameters compared to send: `status`. Status can be ignored by setting `status = MPI_STATUS_IGNORE`
- On the other hand, If we pass `status` to `MPI_receive`, it will contain additional information, for example, the rank of the source, the tag of the message (see [here](https://www.mcs.anl.gov/research/projects/mpi/mpi-standard/mpi-report-1.1/node35.htm))
- In Fortran, status is an array of INTEGERs of size MPI_STATUS_SIZE. The constants MPI_SOURCE, MPI_TAG and MPI_ERROR are the indices of the entries that store the source, tag and error fields. Thus, status(MPI_SOURCE), status(MPI_TAG) and status(MPI_ERROR) contain, respectively, the source, tag and error code of the received message
	For example:
	```fortran

	integer :: status(MPI_status_size) ! an integer array with size MPI_STATUS_SIZE
	call MPI_recv(array, size, MPI_integer, from, &
						mpi_send_tag, mpi_comm_world, status, error)
	```

##### mpi_bcast
Boardcast is only done by the root, which boardcast a copy of the data to every other process.
```c
mpi_Bcast(data, size, type, root, comm_world, ierr)
```
Boardcast can also be done using send and recv, see https://mpitutorial.com/tutorials/mpi-broadcast-and-collective-communication/

| parameters  |  |
| --- | --- |
|data | the starting address of the data
|count | size of the data to send
|type | data_type
|root | rank for the root
|comm_world | communicator

##### mpi_barrier
`mpi_barrier(comm_world, ierr)`
No process can pass the barrier until all of them call the function. Therefore, mpi_barrier synchronize all the processes. Barrier is implemented by a token, which is passed around processes. processes can only procede when the token goes around all processes.

##### mpi_scatter 
Root process distribute the data to all processes, *the root process itself also receive a part of the data*
```c
mpi_scatter(send_data, send_size, type, recv_data, recv_size, recv_type, root, comm_world, ierr)
```
One important parameter is `send_size`, specifying how much element to be distribute to one process. if `send_size=2`, process 0 will get 2 element, process 1 will get next 2 element
*Note:* Which element a process get depends on how array is stored in memory

##### mpi_gather
The root proecss receive the data from different processes, so it is the reverse of the scatter function.
```c
mpi_gather(send_data, send_size, type, recv_data, recv_size, recv_type, root, comm_world, ierr)
```

There parameters `recv_data`, `recv_size` and `recv_type` specifies how data is received on the root processes
 
##### mpi_allgather
As with allreduce, `root_id` is not needed as parameter and data is distributed to all process.
```c
mpi_allgather(send_data, send_size, type, recv_data, recv_size, recv_type, comm_world, ierr)
```

