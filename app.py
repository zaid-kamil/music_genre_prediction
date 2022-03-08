import os
import soundfile as sf
import streamlit as st
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import librosa, librosa.display
from code import *
st.set_page_config(page_title="Audio", layout="wide")

st.title('Musicality: Know your music ')
st.header('An Ai application that can classify the genre of song by audio.')
options = ['💾Upload','Predict']
choice = st.radio('Select an option',options)

if choice == options[0]:
    with st.form('upload your audio'):
        st.title("💾Upload")
        audio = st.file_uploader("select an audio file",type=['wav'])
        record_audio = st.form_submit_button('Upload')
    if record_audio:
        if audio is not None:
            audio_file = save(audio,f'sounds/{audio.name}')
            st.success(f"upload uploaded to sounds/{audio.name}")
        else:
            st.error("please select an music file")

if choice == options[1]:
    with st.form('Spectrogram and Wavelet Generator'):
        st.title("🔨Process")
        st.write('Process music file and generate the spectrogram and wavelet graph')
        soundfiles= os.listdir('sounds')
        file = st.selectbox('Select a sound file',soundfiles)
        
        process_audio = st.form_submit_button('Process')
    if process_audio:
        if file is not None:
            st.audio(f'sounds/{file}')
            audio_file = 'sounds/'+file
            st.info(f"processing {audio_file}")
            y, sr = librosa.load(audio_file)
            
            fig,ax = plt.subplots(figsize=(12, 3))
            librosa.display.waveplot(y, sr=sr)
            ax.set_title('Wavelet')
            st.pyplot(fig)
           

            stft = librosa.stft(y)
            fig3,ax = plt.subplots(figsize=(12, 3))
            librosa.display.specshow(librosa.amplitude_to_db(stft, ref=np.max), x_axis='time', y_axis='log',ax=ax)
            ax.set_title('Spectrogram')
            spectogram_file = 'generated/'+file.split('.')[0]+"_spectrogram.png"
            wavelet_file = 'generated/'+file.split('.')[0]+"_wavelet.png"
            fig3.savefig(spectogram_file)
            fig.savefig(wavelet_file)
            st.pyplot(fig3)
            st.success(f"generated graph data")            

        else:
            st.error("please select a file")