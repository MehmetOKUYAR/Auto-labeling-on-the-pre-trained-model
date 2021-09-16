# auto-labeling-on-the-pre-trained-model
This function I wrote performs the image and txt saving process. You can also use this function on a model you have trained before. If your model works well enough, it will easily detect the images and record the labels. You can edit the recorded data and train with your new data quickly.

### How to use 

You need to run this script like that `python auto_label.py`

You need to edit the codes in `auto_label.py` line according to yourself.

specify the yolo weights and config files you trained before.
~~~~~~~~~~~~
7. weightsPath = "yolov4-obj_last.weights"
8. configPath = "yolov4-obj.cfg"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the video path you want to test.

~~~~~~~~~~
14. cap = cv2.VideoCapture('2.mp4')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

then you need to edit the following lines in `yolov4_pred.py` 
Edit them according to your class labels.

~~~~~~~~~~~~
13.  LABELS = [ 'class_name1',
                'class_name2',
                'class_name3',
                'class_name3',
                .
                .
                .
                ]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
that's all, if your model predicts well enough, it will predict and start labeling.
