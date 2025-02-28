import wave
from pyaudio import PyAudio,paInt16

# 设置采样参数
NUM_SAMPLES = 2000
TIME = 2
chunk = 1024

# read wav file from filename 
def read_wave_file(filename):
    fp = wave.open(filename,'rb')
    nf = fp.getnframes()     #获取采样点数量
    print('sampwidth:',fp.getsampwidth())  
    print('framerate:',fp.getframerate())
    print('channels:',fp.getnchannels())
    f_len = nf*2
    audio_data = fp.readframes(nf)

# save wav file to filename 
def save_wave_file(filename,data):
    wf = wave.open(filename,'wb')
    wf.setnchannels(1)      # set channels  1 or 2
    wf.setsampwidth(2)      # set sampwidth 1 or 2
    wf.setframerate(16000)  # set framerate 8K or 16K
    wf.writeframes(b"".join(data))  # write data
    wf.close()

#recode audio to audio.wav
def record():
    pa = PyAudio()     # 实例化 pyaudio
    # 打开输入流并设置音频采样参数 1 channel 16K framerate 
    stream = pa.open(format = paInt16,
                     channels=1,
                     rate=16000,
                     input=True,
                     frames_per_buffer=NUM_SAMPLES)

    audioBuffer = []   # 录音缓存数组
    count = 0

    # 录制40s语音
    while count<TIME*20:
        string_audio_data = stream.read(NUM_SAMPLES) #一次性录音采样字节的大小
        audioBuffer.append(string_audio_data)
        count +=1
        print('.'),  #加逗号不换行输出

    # 保存录制的语音文件到audio.wav中并关闭流
    save_wave_file('test.wav',audioBuffer)
    stream.close()


# main函数 录制5s音频并播放
if __name__ == '__main__':
    print('record ready...')
    record()
    print('record over!') 


