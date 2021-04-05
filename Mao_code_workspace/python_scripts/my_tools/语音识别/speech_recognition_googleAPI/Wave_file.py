# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'
from pyaudio import PyAudio, paInt16
import wave

class Wave_file:
    NUM_SAMPLES = 2000
    framerate = 8000
    channels = 1
    sampwidth = 2
    TIME = 10# record time
    def __init__(self):
        self.pa = PyAudio()
    def create_wav(self,filename):
        stream = self.pa.open(format=paInt16, channels=self.channels,rate=self.framerate, input=True,frames_per_buffer=self.NUM_SAMPLES)
        save_buffer = []
        for count in range(self.TIME * 4):
            string_audio_data = stream.read(self.NUM_SAMPLES)
            save_buffer.append(string_audio_data)
        # filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
        with wave.open(self.filename, 'wb') as f:
            f.setnchannels(self.channels)
            f.setsampwidth(self.sampwidth)
            f.setframerate(self.framerate)
            f.writeframes(b"".join(save_buffer))
        print("[ %s ] saved successfully"%filename)

    def play_wav(self,path,size=1024):
        with wave.open(path, "rb") as f:
            stream =self.pa.open(format=self.pa.get_format_from_width(f.getsampwidth()),  # open stream
                            channels=f.getnchannels(),rate=f.getframerate(),output=True)
            data = f.readframes(size)
            while data != '':
                stream.write(data)# paly stream
                data = f.readframes(size)
            stream.stop_stream()# stop stream
            stream.close()
        self.pa.terminate()


if __name__ == "__main__":
    # record_wave()
    wv=Wave_file()
    path="voice/18012345678.wav"
    wv.play_wav(path)
