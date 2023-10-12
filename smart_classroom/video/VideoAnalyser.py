from ultralytics import YOLO

from smart_classroom.video.VideoFaceDetector import VideoFaceDetector
from smart_classroom.video.VideoRaiseHeadDetector import VideoRaiseHeadDetector

class VideoAnalyser(object):

    """
    @
    """

    def __init__(self, model_dir):
        self._detect_model = YOLO(model_dir)
        self._face_detector = VideoFaceDetector(self._detect_model, "./face_detect_test")
        self._raise_head_detector = VideoRaiseHeadDetector(self._detect_model, "./test/test.mp4")

    def raise_head_analyse(self):
        self._raise_head_detector.raise_head_detect()

    def face_anaylse(self):
        self._face_detector.face_detect()


