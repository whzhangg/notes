# Deep Learning with PyTorch
This note contain part 1 of the book [Deep Learning with PyTorch](https://pytorch.org/assets/deep-learning/Deep-Learning-with-PyTorch.pdf) hosted on PyTorch website. 

### Introduction
At its core, PyTorch is a library that 
- provides multidimensional arrarys called tensors
- ability of tensors to keep track of the operations performed on tem and to analytically compute derivatives of an output with respect to any of its inputs
- PyTorch can serialize a model into a set of instructions that can be invoked independently from Python, for example, be called from C programs

### Torch Hub
Using *Torch Hub*, it is possible to load pretrained model from GitHub without cloning the repository.

##### Publish
To publish a trained model (on github), we need a file named hubconf.py should be placed in the root directory of the GitHub repository, listing the dependencies and entry points (functions). For examle, A hubconf.py should have the following format
```python
dependencies = ['torch', 'math']
    
def some_entry_fn(*args, **kwargs):              # entry point
    model = build_some_model(*args, **kwargs)
    return model
```

##### Obtain trained model
To *obtain* a trained model from a github repository without cloning, we can load a model with hub from a specific github repository and branch
```python
from torch import hub
resnet18_model = hub.load('pytorch/vision:main', 'resnet18', pretrained = True)
# The first argument specifies the name and the branch of the github repository
# https://github.com/pytorch/vision in main branch
# the second argument specifies the entry point function, which would return a model
```
    
### Tensor
##### Essence of tensors
PyTorch tensors (as well numpy arrays) are *views over contiguous memory blocks containing C numeric types*. PyTorch tensor has the same indexing and slicing as numpy arrays. 

##### Named tensors
Names can be given to each dimension by passing `names =` parameters. For example:
```python
>>> torch.zeros(2, 3, names=('N', 'C'))
tensor([[0., 0., 0.],
        [0., 0., 0.]], names=('N', 'C'))
```
For more detail, see [here](https://pytorch.org/docs/stable/named_tensor.html)

##### Tensor element types
*dtype* argument to tensor constructors specifies the numerical data types.
- The default data type for tensors is 32-bit floating points
- If tensors are used to index other tensor, the indexing tensors are expected to be `torch.long`

Data types in torch is listed below:

| dtype | short name | description |
| -- | -- | -- |
|torch.float32 | torch.float | 32-bit floating-point |
|torch.float64 | torch.double| 64-bit, double-precision floating-point 
|torch.float16 | torch.half |16-bit, half-precision floating-point
|torch.int8 | | signed 8-bit integers
|torch.uint8| | unsigned 8-bit integers
|torch.int16 | torch.short| signed 16-bit integers
|torch.int32 | torch.int| signed 32-bit integers
|torch.int64 | torch.long| signed 64-bit integers
|torch.bool|| Boolean

We can specify dtype as argument to constructor: `short = torch.tensor([1, 2], dtype=torch.short)`. We can also casting the output using *.to()*: `double_points = torch.zeros(10, 2).to(torch.double)`

##### Views of storage
Data of Tensors are allocated in *contiguous memory (1D) managed by torch.storage instance*. A tensor instance is a view of such a storage instance. The underlying memory is allocated only once, but *different tensor views of the data can be created* (quickly).
```python
points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])  # 3 * 2 array
points.storage()
>>> 4.0 1.0 5.0 3.0 2.0 1.0               # 1 dimension contiguous memory
>>> [torch.FloatStorage of size 6]
```

##### Inplace operation
*Tensor methods with trailing underscore* indicates that the operations are inplace. Any method without the trailing underscore leaves the source tensor unchanged and return a new tensor.

##### Tensor view from tensor storage
Stride specified the number of elements in the storage that have to be skipped when the index is increased by 1 in the given dimension. For example, accessing an element `[i,j]` in an 2D elements is equivalent to accessing the position `storage_offset + stride[0] * i + stride[1] * j` in the storage. Storage offset will be non-zero if the tensor is a slice of a larger tensor. 

```python
# example showing tensor as separate from its storage
points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
points_t = points.t()

print( id(points) == id(points_t) )
>>> False
print( id(points.storage()) == id(points_t.storage()) )   
>>> True
print( points.stride(), points_t.stride() )
(2,1), (1,2)
```

##### Contiguous tensors
When we create a tensor, its storage in memory match its shape (in a given order) and this is called contiguous. However, other view, such as transpose, of the same storage is not contiguous.

*tensor.contiguous()* method will create a *clone of the original data shuffled so that its storage in memory is consistent with its shape*. i.e. The same as if it had been created from scratch with the same data. 
```python
points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
points_t = points.t()

points_t.stride()
>>> (1, 2)   # not contiguous
points_t.is_contiguous() 
>>> False

points_t_c = points_t.contiguous()
points_t_c.stride()
>>> (3, 1)   # contiguous, stride[0] > stride[1]

```

##### Tensor on GPU
Tensors can be constructed on GPU by specifying in the construction: `device = 'cuda'`

To move a tensor from CPU to GPU, we can use `.to(device = 'cude')` which will *return a new tensor* that is stored on GPU. Result of any operation performed on the tensor in GPU will also be stored in GPU

##### Numpy interoperability
Numpy objects that is returned from tensor by: `tensor.numpy()` *share the same underlying storage*.
```python
>>> a = torch.tensor([1.0,2.0])
>>> b = a.numpy()
>>> b[0] = 5
>>> a
tensor([5., 2.])     # storage are shared
```

To build a tensor from a numpy object, we use: `torch.from_numpy()` if the tensor is on CPU. To build a GPU tensor from a numpy object, a copy will be made as a numpy array on CPU

Numpy default datatype is 64 bit floats, while tensor default for 32 bit floats. Therefore, date conversion is sometimes necessary.

##### Real-world data representation using tensors
Here example of basis usage of tensor to represent data is shown:

Loading data from text files   
```python
import csv
wine_path = "../data/p1ch4/tabular-wine/winequality-white.csv" 
wineq_numpy = np.loadtxt(wine_path, dtype=np.float32, delimiter=";",skiprows=1)
    
wineq = torch.from_numpy(wineq_numpy)  # we explicitly use np.float32
```
    
normalization    
```python
data_mean = torch.mean(data, dim=0)
data_var = torch.var(data, dim=0)
data_normalized = (data - data_mean) / torch.sqrt(data_var)
```

### The Mechanics of Learning
##### Pytorch's autograd
Pytorch tensor remember where they come from, in terms of operations and parent tensors. They can *automatically provide the chain of derivatives* of such operations w.r.t their inputs

To enable autograd, we can create tensor using with the *requires_grad* parameter:
```python
params = torch.tensor([1.0, 0.0], requires_grad=True)
```
Pytorch track the entire family tree of tensor results with `requires_grad` enabled. The value of the derivative will automatically updated to `.grad` attribute.

##### Updating the gradients
Calling `.backward()` method on a resulting tensor will *compute the gradients*. 

`backward()` will *accumulate* all derivatives on the leaf nodes (parameters in the usual case). We can zero the gradient explicitly by `params.grad.zero_()`

With autograd, a simple training loop can be written:
```python
def training_loop(n_epochs, learning_rate, params, t_u, t_c):
	for epoch in range(1, n_epochs + 1):
		if params.grad is not None:
			params.grad.zero_()
		
		t_p = model(t_u, *params)
		loss = loss_fn(t_p, t_c) # loss_fn returns ((t_p - t_c)**2).mean()
		loss.backward()                  # loss is simply a resulting tensor
		
		with torch.no_grad():
			params -= learning_rate * params.grad      
			# prevent creating a loop in the forward graph

		if epoch % 500 == 0:
			print('Epoch %d, Loss %f' % (epoch, float(loss)))
	return params
```

When we do not need to build the forward graph, we should also use `torch.no_grad()` context, for example, when evaulating the validation loss. This will reduce the memory consumption and improve speed. On the other hand, `torch.set_grad_enabled()` enables the autograd function.

##### PyTorch optimizer
Different optimization algorithms are implemented in the *optimizer module*.

Every optimizers are constructed with pytorch tensors, with `requires_grad = True` as first input parameters. Every optmizers exposed two method
1. *zero_grad* zeros the gradient attribute of all the parameters passed upton construction
2. *step* updates the value of the parameters according to the optimization strategy

with an optimizer, the traning loop can be reduced:
```python
def training_loop(n_epochs, optimizer, params, t_u, t_c):
	for epoch in range(1, n_epochs + 1):
		t_p = model(t_u, *params)
		loss = loss_fn(t_p, t_c)

		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

		if epoch % 500 == 0:
			print('Epoch %d, Loss %f' % (epoch, float(loss)))
	return params
```

##### Overfitting and training
We usually have two simple rules with respect of overfitting:
1. If training loss is not decreasing, it's likely that the model is too simple for the data
2. If the training loss and validation loss diverge, it's likely that we are overfitting

If training and validation loss decrease exactly in tandem, we can perhaps increase the performance by go slightly underfitting

##### Splitting data into training and validating sets
```python
n_samples = t_u.shape[0]
n_val = int(0.2 * n_samples)

shuffled_indices = torch.randperm(n_samples)   # created a shuffled indices
train_indices = shuffled_indices[:-n_val]
val_indices = shuffled_indices[-n_val:]

train_t_u = t_u[train_indices]                 # splited data
val_t_u = t_u[val_indices] 
```

### Using a neural network to fit the data
`torch.nn` define the submodules that is related to neural networks. All the building blocks in torch.nn are called *modules*.

*All pyTorch subclasses of nn.Module* defines `__call__` method and therefore is callable. `__call__` will set up all the necessary preparation before calling the `forward()` method with the same arguments. Therefore, a `forward()` by itself is not equivalent to `__call__` method.

Some further points for torch modules:
- Modules *expect the zeroth dimension of the inputs to be the number of samples* in the batch
- `nn.Sequential` return a module that concatenate provided module
- Calling `model.parameters()` collect weight and bias

### Learning from images data
##### Dataset class
PyTorch dataset is required to implement two methods `__len__` and `__getitem__`
##### DataLoader
Dataloader help us organize and shuffle the data.

At minimum, the DataLoader constructor takes a *Dataset* object as input, along with *batch_size* parameter and a *shuffle* boolean option parameter

### Building a Convolution network
##### Some introductions
(Discrete) convolution produce a scalar product of the (local) region of the input data with a kernal matrix.

In convolution network, the kernel size typically is small and local. The consequences of using a discreate convolution are:
1. Operations are local
2. Translation invariance for images
3. Reduce model parameters

##### Kernel size
We should typically choose small kernel size. If we try to use a large kernel, such as $20\times20$ for a pixel image of $60\times60$ dimension, we loose the locality of the convolution methods. Therefore, typically small kernel size such as $3\times3$ and $5\times5$ are used.

To detect features larger than the kernel size, we can increase the depth of the convolutional neural networks by stacking one convolution after the other and at the same time downsampling the image between successive convolutions

##### Downsampling (Pooling)
Usual options for the downsampling is:
1. average pooling 
2. max pooling: is currently commonly used approach, but discard large amount of information
3. strided convoluton: more recently methods

##### Subclassing nn.Module
Subclassing nn.Module enable us to *build our own modules*.
- At a minimum, we need to define a **forward()** function, which takes the input and returns the output
- To include submodules, we define them in the constructor `__init__` and assign them to self, after calling `super().__init__()`.
- submodules must be top-level attributes, not inside contains, in order that the optimizer can locate them

Assigning an instance of `nn.Module` to an attribute in a nn.Module class, automatically register that module as a submodule. When we call `parameters()`, the class method go into all submodules assigned as attributes in the constructor and recursively call `parameters()` on those submodules. 

For example, a Module that treat image inputs and perform classification is then:
```python
class Net(nn.Module):
	def __init__(self):
		super().__init__()
		self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
		self.act1 = nn.Tanh()
		self.pool1 = nn.MaxPool2d(2)
		self.conv2 = nn.Conv2d(16, 8, kernel_size=3, padding=1)
		self.act2 = nn.Tanh()
		self.pool2 = nn.MaxPool2d(2)
		self.fc1 = nn.Linear(8 * 8 * 8, 32)
		self.act3 = nn.Tanh()
		self.fc2 = nn.Linear(32, 2)

	def forward(self, x):
		out = self.pool1(self.act1(self.conv1(x)))
		out = self.pool2(self.act2(self.conv2(out)))
		out = out.view(-1, 8 * 8 * 8)
		out = self.act3(self.fc1(out))
		out = self.fc2(out)
		return out
```

##### Saving and Loading model
To save a model:
```python
torch.save(model.state_dict(), data_path + 'birds_vs_airplanes.pt')
# the second part is the filename
```

To load from a model, *we first need to create an instance*, which should be exactly the same as the saved model, and then we can load the trained model:
```python
loaded_model = Net()
loaded_model.load_state_dict(torch.load(data_path + 'birds_vs_airplanes.pt'))

>> <All keys matched successfully>
```

##### Training on GPU
`nn.Module` provide a `.to()` function to will move all it parameters to the GPU. `Module.to()` is inplace: the module itself is modified. Compare to tensor.to(), which always return a new tensor (view).

To train a model on GPU, use:
```python
def training_loop(n_epochs, optimizer, model, loss_fn, train_loader):
	for epoch in range(1, n_epochs + 1):
		loss_train = 0.0
		for imgs, labels in train_loader:
			imgs = imgs.to(device=device)       # move the data to GPU
			labels = labels.to(device=device)
			outputs = model(imgs)

			loss = loss_fn(outputs, labels)
			optimizer.zero_grad()
			loss.backward()
			optimizer.step()
			loss_train += loss.item()
		if epoch == 1 or epoch % 10 == 0:
			print('{} Epoch {}, Training loss {}'.format(
				datetime.datetime.now(), epoch, loss_train / len(train_loader))
			)

train_loader = torch.utils.data.DataLoader(cifar2, batch_size=64, shuffle=True)

model = Net().to(device=device)
optimizer = optim.SGD(model.parameters(), lr=1e-2)
loss_fn = nn.CrossEntropyLoss()

training_loop(n_epochs = 100,
			optimizer = optimizer,
			model = model,
			loss_fn = loss_fn,
			train_loader = train_loader,
		)
```

##### Improving our model
The following are some basic method to improve our models:
1. adding width to the convolution model by increasing the number of channels per convolution. Increasing the number of channels increase the capacity of the model.
2. Regularization: regularization can be implemented in the network by adding penalties to the loss functions
3. Dropouts prevent overfitting by zeroing out a random fraction of outputs from neurons across the network, different randomization happens at each training iteration.
4. Batch normalization: batch normalization rescale the inputs in a minibatch to avoid the inputs of the activation function to be too far away from the activation regions nn.BatchNorm provide the batch normalization

An example of using Dropout module:
```python
class NetDropout(nn.Module):
    def __init__(self, n_chans1=32):
    	super().__init__()
    	self.n_chans1 = n_chans1
    	self.conv1 = nn.Conv2d(3, n_chans1, kernel_size=3, padding=1)
    	self.conv1_dropout = nn.Dropout2d(p=0.4)     # drop out layer
    	self.conv2 = nn.Conv2d(n_chans1, n_chans1 // 2, kernel_size=3, padding=1)
    	self.conv2_dropout = nn.Dropout2d(p=0.4)
    	self.fc1 = nn.Linear(8 * 8 * n_chans1 // 2, 32)
    	self.fc2 = nn.Linear(32, 2)
    
    def forward(self, x):
    	out = F.max_pool2d(torch.tanh(self.conv1(x)), 2)
    	out = self.conv1_dropout(out)
    	out = F.max_pool2d(torch.tanh(self.conv2(out)), 2)
    	out = self.conv2_dropout(out)
    	out = out.view(-1, 8 * 8 * self.n_chans1 // 2)
    	out = torch.tanh(self.fc1(out))
    	out = self.fc2(out)
    	return out
```

##### Deep networks
Deep networks: adding depth to the network increase the model complexity and make convergence slow (derivative to a specific weight become small). *Skip connection* can help training a deep network

This example define a module with *skip connection*:
```python
def forward(self, x):
    out = F.max_pool2d(torch.relu(self.conv1(x)), 2)
    out = F.max_pool2d(torch.relu(self.conv2(out)), 2)
    out1 = out                  # skipped connection 
    out = F.max_pool2d(torch.relu(self.conv3(out)) + out1, 2)    
	# use the output from previous two layers
    out = out.view(-1, 4 * 4 * self.n_chans1 // 2)
    out = torch.relu(self.fc1(out))
    out = self.fc2(out)
    return out
```
        
Very deep network: To build a very deep network, a standard strategy is to define a building block, such as:
```python
( Conv3d, ReLU, Conv2d ) + skip connection (combining the inputs)
```

They should have the same size of input and output, and then use a for loop to append the blocks in a *Sequential*.