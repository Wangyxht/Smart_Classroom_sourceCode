import os
import numpy as np
import cv2 as cv
from ultralytics import YOLO


class VideoFaceDetector(object):
    """
    @:param model: YOLO 权重模型
    """

    def __init__(self, model: YOLO, pic_dir):
        self.__model = model
        self.__pic_dir = pic_dir

    def face_detect(self):
        pictures_names = os.listdir(self.__pic_dir)

        detect_pic_num = 0
        for picture_name in pictures_names:
            picture_path = self.__pic_dir + '\\' + picture_name
            results = self.__model.predict(picture_path)
            detect_pic_num += 1
            for result in results:
                # 结果的输出
                boxes = result.boxes  # Boxes object for bbox outputs

                # 访问目标坐标
                rect_results = boxes.xywh
                class_results = boxes.cls
                class_list = []
                rect_list = np.zeros((len(class_results), 4), dtype=np.int32)

                for class_result in class_results:
                    class_list.append(int(class_result.item()))
                i = 0
                for rect_result in rect_results:
                    rect_list[i, :] = rect_result.cpu().numpy()
                    i += 1

                picture = cv.imread(picture_path)
                for i in range(rect_list.shape[0]):
                    # 读取识别框坐标
                    [x, y, w, h] = rect_list[i, :]
                    point_left_up = (int(x - w / 2), int(y - h / 2))
                    point_right_bottom = (int(x + w / 2), int(y + h / 2))

                    # 切割目标
                    face_picture_name = "./face_detect_ans/face_target" + str(i) + ".jpg"
                    target_detect = picture[int(y - h / 2):int(y + h / 2), int(x - w / 2):int(x + w / 2)]

                    # 重新缩放
                    target_detect = cv.resize(target_detect, (500, 500), cv.INTER_AREA)

                    cv.imwrite(face_picture_name, target_detect)
                    i += 1

        # def face_recognize(self):
        #     cv.
