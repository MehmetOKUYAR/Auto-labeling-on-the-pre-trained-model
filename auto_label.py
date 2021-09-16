import cv2 
import time 
import numpy as np
from yolov4_pred import YOLOv4

#======= Yolov4 ağırlıkları  yüklenmektedir ========================
weightsPath = "yolov4-obj_last.weights"
configPath = "yolov4-obj.cfg"
        
net = cv2.dnn.readNet(weightsPath, configPath)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

cap = cv2.VideoCapture('2.mp4')

if cap.isOpened() == 0:
    exit(-1)


cnt=0
frames_to_count=20
st=0
count=0

#============ kamera açıldıysa görüntüyü aktar ===========
while(cap.isOpened()):
    ret,frame = cap.read()
    count +=1


    frame = YOLOv4(net,frame,count)

    if cnt == frames_to_count:
        try:
            print(frames_to_count/(time.time()-st),'FPS')
            fps = round(frames_to_count/(time.time()-st)) 
            st = time.time()
            cnt=0
        except:
            pass
    cnt+=1

    cv2.namedWindow('predict_video',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('predict_video',1650,750)
    cv2.imshow("predict_video",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows()