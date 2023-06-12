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
while(cap.isOpened()):
    fps = FPS()
    with SharedMemoryBridge(shared_memory_file, shared_memory_size, file_changed) as bridge:  
        while True:
            ret, img = cap.read()
            if(ret):
                fps.update()
                data=dict()
                data["ret"]=ret
                data["img"]=img
                bridge.write(data)

            if cv2.waitKey(30) & 0xff == ord('q'):
                break
    cap.release()
else:
    print("Alert ! Camera disconnected")