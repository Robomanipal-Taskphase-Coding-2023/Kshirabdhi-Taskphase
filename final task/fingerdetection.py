import torch
import numpy as np
import cv2
from time import time

class FingerDetection:

    def __init__(self, capture_index, model_path):

        self.capture_index = capture_index
        self.model = self.load_model(model_path)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)

    def get_video_capture(self):
        return cv2.VideoCapture(self.capture_index)

    def load_model(self, model_path):
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
        return model

    def score_frame(self, frame):
        self.model.to(self.device)
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def plot_boxes(self, results, frame):
        labels, cord = results
       # print(cord)
        #print(labels)
        n = len(labels)
        cord2 = cord*415
        print(cord2)
        for i in range(n):
            row = cord2[i]
            x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
            bgr = (0, 255, 0)  # Green color for box
            cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
        return frame

    def __call__(self):
 
        cap = self.get_video_capture()
        assert cap.isOpened()

        while True:
            ret, frame = cap.read()
            assert ret
            
            # Resize the frame to match the input size expected by the YOLOv5 model
            frame = cv2.resize(frame, (416 ,416))
            
            start_time = time()
            results = self.score_frame(frame)
            #print(results)
            frame = self.plot_boxes(results, frame)
            end_time = time()

            fps = 1 / np.round(end_time - start_time, 2)
            cv2.putText(frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
            cv2.imshow('Finger Tip Detection', frame)

            if cv2.waitKey(5) & 0xFF == 27:
                break

        cap.release()


# Create a new object and execute.
detector = FingerDetection(capture_index=0, model_path='/home/prachi/Downloads/besttt.pt')
detector()
