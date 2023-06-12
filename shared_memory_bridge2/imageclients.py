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
            if (img is not None):
                cv2.imshow('img', img)
                fps.update()
                img = None
            if cv2.waitKey(10) & 0xff == ord('q'):
                break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()