# Shared Memory Module

This module provides a shared memory implementation in Python for communication between separate processes. It allows multiple processes to read and write data to a shared memory block.

## Usage

To use the shared memory module, follow these steps:

1. Install the module:

```shell
Please note that you need to have the `shared_memory_bridge2` module available in your project directory or installed in your Python environment for the example code to work properly.
```

2. Import the `SharedMemoryBridge` class from the module:

```python
from shared_memory_bridge2.bridge import SharedMemoryBridge
```

3. Create an instance of the `SharedMemoryBridge` class by providing the shared memory path and optional parameters:

```python
shared_memory_file = "shared_memory"
shared_memory_size = 4096

def file_changed(fileobject):
    print(f"filechanged: the data:{fileobject}")

def main():
    with SharedMemoryBridge(shared_memory_file, shared_memory_size, file_changed) as bridge:
        # Your code here
```

- `shared_memory_file` (str): The path to the shared memory block. If the shared memory block doesn't exist, it will be created.
- `shared_memory_size` (int, optional): The size of the shared memory block in bytes. Default is 4096.

4. Write data to the shared memory:

```python
data = {'message': 'Hello, shared memory!'}
bridge.write(data)
```

- `data` (object): The data to be written to the shared memory. The data must be serializable using the `pickle` module.

5. Access the shared data:

The shared data can be accessed through the `data_dict` attribute of the `SharedMemoryBridge` instance.

```python
shared_data = bridge.data_dict
```

6. Close the shared memory:

```python
bridge.close()
```

## Test

Here's test usage of the shared memory module:

```python
from shared_memory_bridge2.bridge import SharedMemoryBridge
import time
import random

shared_memory_file = "shared_memory"
shared_memory_size = 4096

def file_changed(fileobject):
    print(f"filechanged: the data:{fileobject}")

def main():
    with SharedMemoryBridge(shared_memory_file, shared_memory_size, file_changed) as bridge:
        random_process_id = random.randint(0, 100)
        print(random_process_id)
        for i in range(0, 50):
            time.sleep(0.1)
            data = dict()
            data["name"] = "mustafa"
            data["data"] = random_process_id
            bridge.write(data)

if __name__ == "__main__":
    main()
```

[Example](example.md)

## License

This module is licensed under the [MIT License](LICENSE).
