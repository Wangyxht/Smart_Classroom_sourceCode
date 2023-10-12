from smart_classroom.video.VideoAnalyser import VideoAnalyser
from smart_classroom.sound.SpeakAnalyser import SpeakAnalyser

if __name__ == '__main__':
    video_analyser = VideoAnalyser("./model/class_detect_model.pt")
    speak_analyser = SpeakAnalyser()
    speak_analyser.speak_text_analyse()

    # video_analyser.raise_head_analyse()
    # video_analyser.face_anaylse()
