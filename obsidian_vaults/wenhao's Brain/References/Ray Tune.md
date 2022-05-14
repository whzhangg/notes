# Ray Tune
### Ray
Ray is a library for parallel and distributed python calculations. It provide an infrustructure to run functions on different process. See this page for a [short introduction](https://towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8) 

### Ray Tune Basics
Ray tune is a library for tunning hyperparameters of some target function that is build on top of Ray and uses ray’s ability to run parallel executions. https://docs.ray.io/en/latest/tune/user-guide.html

##### Tune.run()
Parameters:
- num_sample: the number of runs that a grid will be repeated
- stop: a dictionary or function argument that terminate the trials. 
- resume = True will resume a stopped run.
- local_dir

We can pass a dictionary, trail will stop when the reported value is *above* the given value. 
```python
stop={"training_iteration": 10, "mean_accuracy": 0.98}
``````
or a function:
```python
def stopper(trial_id, result):
    return result["mean_accuracy"] > 0.98 or result["training_iteration"] > 10
```

##### Logging
Tune will output results in CSV, JSON format. It will log the results of each trail to a subfolder of a specific local folder, default will be `~/ray_results`

We can specific `local_dir` and `name`(the name given to this tunning process) in `tune.run()`:
```python
tune.run(local_dir = 'ray', name = 'simple') 
# will create a folder as ray and a subfolder 'simple', and then write all the results
```

##### Output log
By passing `log_to_file` parameter to `tune.run()`, we can redirect the output to distinct files. These output are the outputs of the trainables. Therefore, they are pre-trial.

If we pass boolean, it will default log to `trial_logdir/stdout` and `trial_logdir/stderr`. If we pass files names, the output will be redirected to the given file: one file name will combine the error to a single file, passing two filenames will redirect the output separately. `trial_logdir` is the subdirectory of each trail in local_dir/name/training_function...

##### Trainable
Each trainable function will be executed on a separate process underneath the hood. `tune.report()` communicate the result of each process with the main control. 

`tune.report()` log all the input parameters. It seems that tune accept python type of floats, therefore we should not pass tensors

### Early stopping with scheduler
If some trial run goes bad or are “less promising”, we can use a scheduler to terminate such runs. For example a `aha` scheduler:
```python
asha_scheduler = ASHAScheduler(
    time_attr='training_iteration',      # a training result attributes to measure time or iterations
    metric='episode_reward_mean',        # target value attributes
    mode='max',                          # or 'min' if we want to minimize target value
    max_t=100,                           # max time per trial
    grace_period=10,                     # only stop trial at least after grace_period
    reduction_factor=3,
    brackets=1)
tune.run( ... , scheduler=asha_scheduler)
```

Some sechedulars are as follows:
##### Median Stopping Rule
This rule implement the simple strategy of stopping a trial if its performance falls below the median of other trials at similar points in time. The performance is measured by “the running average”, see Section 3.2 Golovin et al. 2017 
##### ASHA schedular
##### Population based training

### Search algorithms
##### Discrete space
Searching in discrete space, most of them take a list as input:
| Method | Description |
| --- | --- |
| tune.grid_search([1,2]) | If grid search is included, the same grid will be repeated N times |
| tune.choice([1,2]) |  |
| tune.randn([1,2]) |  |
| tune.sample_from(func) | take a custom callable functions for generating a search sace. Not that this is not supported by every search algorithms |

##### Continuous space
For Continuous search space, most search option take two parameters start and end. If a *q* parameter is added in the front, we can further specify an increment. For example, *tune.uniform(-5,-1)* and *tune.quniform(-5, -1, 0.2)*

The other ones are
| Continuous | With interval | Description |
| --- | --- | --- |
| tune.uniform() | tune.quniform() | float uniformly between -5.0 and -1.0 |
| tune.loguniform() | tune.qloguniform() | uniform in log scale, we can pass parameter base to the search |
| tune.randn() | tune.qrandn() | random float |
| tune.randint() | tune.qrandint() | random int |
| tune.lograndint() | tune.qlograndint() | random linear log space |

##### Tip: 
To loguniform, lograndint give rounded result of continuous choice, the base parameter only give the density at each values. 
To generate a sampling such as [2, 4, 8, 16, 32], use: `tune.sample_from(lambda _: 2**np.random.randint(1, 6))`

### Others
Disable tensorboard logging in windows, use:
`$env:TUNE_DISABLE_AUTO_CALLBACK_LOGGERS=1` in powershell