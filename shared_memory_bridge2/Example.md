# Example

## OpenCV Server Process

The OpenCV server process captures images from the camera and writes them to a shared memory block. Multiple clients can then read the same shared memory to access the captured images.

```python
import numpy as np
import cv2
from shared_memory_bridge2.bridge import SharedMemoryBridge
from FPS import FPS

shared_memory_file = "shared_memory"
shared_memory_size = 2000000
lock_file = "lockfile"

def file_changed(fileobject):
    print(f"filechanged: the data:{fileobject}")

cap = cv2.VideoCapture(0)
while cap.isOpened():
    fps = FPS()
    with SharedMemoryBridge(shared_memory_file, shared_memory_size, file_changed) as bridge:
        while True:
            ret, img = cap.read()
            if ret:
                fps.update()
                data = {"ret": ret, "img": img}
                bridge.write(data)

            if cv2.waitKey(30) & 0xff == ord('q'):
                break
    cap.release()
else:
    print("Alert! Camera disconnected")
```

## OpenCV Client Process

The OpenCV client process reads the images from the shared memory block and displays them using OpenCV.

```python
import numpy as np
import cv2
from shared_memory_bridge2.bridge import SharedMemoryBridge
from FPS import FPS

shared_memory_file = "shared_memory"
shared_memory_size = 2000000
lock_file = "lockfile"

global img

def file_changed(fileobject):
    global img
    img = fileobject["img"]

def main():
    global img
    img = None
    with SharedMemoryBridge(shared_memory_file, shared_memory_size, file_changed) as bridge:
        fps = FPS()
        while True:
            if img is not None:
                cv2.imshow('img', img)
                fps.update()
                img = None
            if cv2.waitKey(10) & 0xff == ord('q'):
                break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

Make sure to adjust the file paths and customize the code according to your requirements.

## FPS Module

The `FPS` module mentioned in the code above is used to calculate and display the frames per second. You can find the implementation of the `FPS` class in the `FPS.py` file.

Please note that you need to have the `shared_memory_bridge2` module and the `FPS` module available in your project directory or installed in your Python environment for the example code to work properly.

Remember to adjust the file paths and customize the code according to your specific setup and requirements.

## License

This module is licensed under the [MIT License](LICENSE).
