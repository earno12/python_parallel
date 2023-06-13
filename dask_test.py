# dask-scheduler
# dask-worker tcp://192.168.1.100:8786
# dask-worker tcp://192.168.1.100:8786
# ```

# This will launch a Dask cluster with a scheduler node listening on port `8786` of the machine with IP address `192.168.1.100`, and two worker nodes connected to the scheduler.

from dask.distributed import Client

client = Client('tcp://192.168.1.65:8786')

# This creates a client object that connects to the [Dask scheduler](poe://www.poe.com/_api/key_phrase?phrase=Dask%20scheduler&prompt=Tell%20me%20more%20about%20Dask%20scheduler.) running on the machine with IP address `192.168.1.100` on port `8786`.

from dask import delayed

@delayed
def square(x):
    return x**2

# Create a list of values to square
values = [1, 2, 3, 4, 5]

# Square the values in parallel using Dask
results = []
for value in values:
    result = square(value)
    results.append(result)

# Compute the final result by summing the squared values
final_result = delayed(sum)(results)

# Submit the computation to the Dask client
final_result.compute()

# In this example, the `square` function is decorated with the `@delayed` decorator, which tells Dask to execute the function in parallel when it is called. The `values` list is processed in a loop, with each value squared using the `square` function and the resulting delayed objects appended to a list. Finally, the `sum` function is applied to the delayed objects using the `delayed` function, resulting in a [delayed object](poe://www.poe.com/_api/key_phrase?phrase=delayed%20object&prompt=Tell%20me%20more%20about%20delayed%20object.) representing the sum of the squared values. The computation is submitted to the Dask client using the `compute` method of the delayed object, which executes the computation in parallel on the Dask cluster.
print(final_result.compute())