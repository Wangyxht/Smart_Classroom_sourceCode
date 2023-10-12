from aip import AipSpeech

APP_ID = '38873030'  # 请填写你的APP_ID
API_KEY = '2GM5mtiWNFjIm7m89Ovq91qp'  # 请填写你的API_KEY
SECRET_KEY = 'veudyUoz1qwKGhMWkLzcH0rnp4nysZtw'  # 请填写你的SECRET_KEY

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# filePath = r'D:\Wisdom\Speech-to-text\pcm\audio.pcm'

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


data = client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {'dev_pid': 1537, })

print(data)
