import pyaudio
import io
import wave


def play(path, CHUNK = 1024):

    wf = wave.open(path, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
    data = wf.readframes(CHUNK)
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()

def save(bytes, filepath="audios/uploads/upload.wav"):

    with open(filepath,'wb') as f:
        f.write(bytes.read())
    return filepath