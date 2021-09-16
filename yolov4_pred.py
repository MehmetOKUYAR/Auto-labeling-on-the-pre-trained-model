
import cv2 
from save_image_and_txt import save_img_txt

def YOLOv4(model,image,count):
    
    model = cv2.dnn_DetectionModel(model)
    model.setInputParams(size=(608, 608), scale=1/255, swapRB=True)

    confThreshold= 0.5
    nmsThreshold = 0.4

    LABELS = [ 'girilmez',
                'tasit_trafigine_kapali',
                'duz_veya_sola',
                'duz_veya_saga',
                'yalnizca_sola',
                '20_hiz_limiti_sonu',
                '30_limit',
                '20_limit',
                'yalnizca_saga',
                'saga_donulmez',
                'sola_donulmez',
                'dur',
                'park_yapilmaz',
                'park',
                'durak',
                'kirmizi_isk',
                'sari_isik',
                'yesil_isik']
    COLORS = [[0, 0, 255]]

   
    classes, confidences, boxes = model.detect(image, confThreshold, nmsThreshold)
    
    # saved per frame 5
    if count%5 == 0:
        if len(boxes)>0:
            save_img_txt(image,boxes,classes)
  

    

    for cl, score, (left, top, width, height) in zip(classes, confidences, boxes):

        start_point = (int(left), int(top))
        end_point = (int(left + width), int(top + height))
        
        color = COLORS[0]
        img = cv2.rectangle(image, start_point, end_point, color, 3)  # draw class box
        text = f'{LABELS[cl[0]]}: {score[0]:0.2f}'

        cv2.putText(img, text, (int(left), int(top-7)), cv2.FONT_ITALIC, 1, COLORS[0], 2)  # print class type with
    
    return img
