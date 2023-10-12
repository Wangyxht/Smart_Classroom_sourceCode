import wave
from aip import AipSpeech
from moviepy.editor import AudioFileClip

def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


class SpeakTextAnalyser(object):

    def __init__(self, video_path, sound_path):
        _APP_ID = '38873030'
        _API_KEY = '2GM5mtiWNFjIm7m89Ovq91qp'
        _SECRET_KEY = 'veudyUoz1qwKGhMWkLzcH0rnp4nysZtw'

        self._client = AipSpeech(_APP_ID, _API_KEY, _SECRET_KEY)
        self._video_path = video_path
        self._sound_path = sound_path
        self._audio_clip = AudioFileClip(self._video_path)

    def _get_sound(self):
        self._audio_clip.write_audiofile(self._sound_path + "audio.wav")

    #def _resample_wave(self):

    def speak_text_analyse(self):
        self._get_sound()
        self._resample_wave()
        return self._client.asr(get_file_content(self._sound_path + 'audio_resample.wav'), 'wav', 16000, {'dev_pid': 1537, })

