import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from ultralytics import YOLO

class VideoRaiseHeadDetector(object):

    def __init__(self, model: YOLO, video_dir):
        self._model = model
        self._video_dir = video_dir

    def raise_head_detect(self):
        video_capture = cv.VideoCapture(self._video_dir)
        # 获取视频帧率
        fps = video_capture.get(cv.CAP_PROP_FPS)
        nums_fps = int(fps)
        # 获取视频总帧数
        frame = video_capture.get(cv.CAP_PROP_FRAME_COUNT)
        nums_frames = int(frame)
        nums_second = int(nums_frames / nums_fps)

        # 初始化数组
        raise_head = np.zeros(nums_second)
        lower_head = np.zeros(nums_second)
        turn_head = np.zeros(nums_second)
        raise_rate = np.zeros(nums_second)

        # 获取一帧的预测结果
        detect_results = (self._model.predict(self._video_dir,
                                              stream=True,
                                              vid_stride=nums_fps,
                                              conf=0.3,
                                              save=True,
                                              name='D:\PycharmProjects\Classroom_Project\smart_classroom\\detect_ans\\ans'
                                              ))

        i = 0
        for result in detect_results:
            # 访问预测结果
            boxes = result.boxes  # Boxes object for bbox outputs
            class_results = boxes.cls
            class_list = []
            for class_result in class_results:
                class_list.append(int(class_result.item()))

            # 统计抬头低头与转头总人数
            raise_head_sum = 0
            lower_head_sum = 0
            turn_head_sum = 0
            for head_condition in class_list:
                if head_condition == 0:
                    raise_head_sum += 1
                elif head_condition == 1:
                    lower_head_sum += 1
                elif head_condition == 2:
                    turn_head_sum += 1
            raise_head[i] = raise_head_sum
            lower_head[i] = lower_head_sum
            turn_head[i] = turn_head_sum
            raise_rate[i] \
                = raise_head_sum * 1.0 / (raise_head_sum + lower_head_sum + turn_head_sum)
            i += 1
        time_axis = np.array([i for i in range(0, nums_second)])

        # 结果绘图
        fig = plt.figure()
        fig.add_subplot(1, 2, 1)
        plt.plot(time_axis, raise_rate, label='raise_rate')
        plt.legend()
        fig.add_subplot(1, 2, 2)
        plt.plot(time_axis, raise_head, label='raise_head')
        plt.plot(time_axis, lower_head, label='lower_head')
        plt.plot(time_axis, turn_head, label='turn_head')
        plt.legend()
        plt.savefig("./detect_ans/fig.jpg")
        plt.show()



