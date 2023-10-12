from smart_classroom.sound.SpeakTextAnalyser import SpeakTextAnalyser

class SpeakAnalyser(object):

    def __init__(self):
        self._speak_text_analyser = SpeakTextAnalyser(r"D:\PycharmProjects\Classroom_Project\smart_classroom\test\test.mp4", "./sound/")

    def speak_text_analyse(self):
        data = self._speak_text_analyser.speak_text_analyse()
        print(data)
