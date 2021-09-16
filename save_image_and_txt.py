import numpy as np
import os
from pathlib import Path
from datetime import datetime
import cv2

def save_img_txt(image,boxes,class_id):
    photo_path = "images and txt"
    photo_dir = Path(photo_path)
    photo_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%d.%m.%Y")
    photo_dir_today = Path(os.path.join(photo_path, today))
    photo_dir_today.mkdir(parents=True, exist_ok=True)
    image_name = 'Predict_' + datetime.now().strftime("%d.%m.%Y_%H.%M.%S") 
    cv2.imwrite(os.path.join(photo_dir_today, image_name + ".jpg"), image)

    height,width,channels = image.shape
    yolo_data =[]
    
    for cl,bb in zip(class_id,boxes):
        print('classs id : ',cl[0])
        x1, y1, w, h = bb[0], bb[1], bb[2], bb[3]
        x_center = (x1+((w)/2))/width
        y_center = (y1+((h)/2))/height
        w = (w)/width
        h = (h)/height
        yolo_data.append([cl[0],x_center,y_center,w,h])

    file_path = os.path.join(photo_dir_today,image_name+ ".txt")
    
    with open(file_path, 'w') as f:
        np.savetxt(
            f,
            yolo_data,
            fmt=["%d","%f","%f","%f","%f"]
        )

