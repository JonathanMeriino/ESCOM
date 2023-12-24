import librosa
import librosa.display
import matplotlib.pyplot as pyplot
import numpy
import os
import glob
import sys
import subprocess

# Ruta al archivo audio
if len(sys.argv) == 1:
    try:
        FILE_NAME_WAV = glob.glob("*.wav")[0]
    except:
        raise ValueError("No .wav file in the root directory")
elif len(sys.argv) == 2:
    FILE_NAME_WAV = list(sys.argv)[1]
    if FILE_NAME_WAV[-4:] != ".wav":
        raise ValueError("Provided filename does not end in '.wav'")
else:
    raise ValueError("Too many arguments provided. Aborting")

FILE_NAME = FILE_NAME_WAV[:-4]

ORIGINAL_DIRECTORY = os.getcwd()

audio_file_path = (ORIGINAL_DIRECTORY + "/" + FILE_NAME_WAV)

# Cargar el archivo de audio y obtener la forma de onda y la tasa de muestreo

audio_embeding_vector, sampling_rate = librosa.load(audio_file_path, sr=None)
print("Audio embeding vector: {}".format(audio_embeding_vector))
print("Longitud del vector de audio: {}".format(len(audio_embeding_vector)))
print("Frecuencia de muestreo: {}".format(sampling_rate))

# Identify sample rate in the .wav file
bash_out = subprocess.run("soxi {0}".format(FILE_NAME_WAV), stdout=subprocess.PIPE, text=True, shell=True)
cleaned_list = bash_out.stdout.replace(" ","").split('\n')
print("Información del audio mediante SOX: {}".format(cleaned_list))

# Calcular el espectrograma utilizando la transformada de Fourier de tiempo corto (STFT)
n_fft = 2048 # Tamaño de la ventana para la STFT
hop_length = 552 # Paso entre ventanas
audio_spectrogram = numpy.abs(librosa.stft(audio_embeding_vector, n_fft=n_fft, hop_length=hop_length))

# Conversión a decibeles del espectrograma
audio_spectrogram_db = librosa.amplitude_to_db(audio_spectrogram, ref=numpy.max)

# Calcular los coeficientes cepstrales de frecuencia Mel (MFCC)
n_mfcc = 13 # Número de coeficientes MFCC
mfccs = librosa.feature.mfcc(y=audio_embeding_vector, sr=sampling_rate)

# Calcular el tono promedio
chroma = librosa.feature.chroma_stft(y=audio_embeding_vector, sr=sampling_rate)
chroma_mean = numpy.mean(chroma, axis=1)

# Calcular el ritmo utilizando el método tempogram
tempogram = librosa.feature.tempogram(y=audio_embeding_vector, sr=sampling_rate)

# Calcular la función de tonalidad
tonnetz = librosa.feature.tonnetz(y=audio_embeding_vector, sr=sampling_rate)

# Calcular la envolvente espectral
spectral_centroids = librosa.feature.spectral_centroid(y=audio_embeding_vector, sr=sampling_rate)[0]

# Calcular el contraste espectral
spectral_contrast = librosa.feature.spectral_contrast(y=audio_embeding_vector, sr=sampling_rate)

# Visualización del análisis
pyplot.figure(figsize=(12, 10))

pyplot.subplot(4, 2, 1)
librosa.display.waveshow(y=audio_embeding_vector, sr=sampling_rate)
pyplot.title("Forma de onda")

pyplot.subplot(4, 2, 2)
librosa.display.specshow(audio_spectrogram_db, sr=sampling_rate, hop_length=hop_length, x_axis="time", y_axis="log")
pyplot.colorbar(format="%+2.0f dB")
pyplot.title("Espectrograma")

pyplot.subplot(4, 2, 3)
librosa.display.specshow(mfccs, sr=sampling_rate, x_axis="time")
pyplot.colorbar()
pyplot.title("MFCCs")

pyplot.subplot(4, 2, 4)
librosa.display.specshow(chroma, y_axis="chroma", x_axis="time")
pyplot.title("Tono")

pyplot.subplot(4, 2, 5)
librosa.display.specshow(tempogram, sr=sampling_rate, hop_length=hop_length, x_axis="time", y_axis="tempo")
pyplot.colorbar()
pyplot.title("Ritmo")

pyplot.subplot(4, 2, 6)
librosa.display.specshow(tonnetz, y_axis="tonnetz", x_axis="time")
pyplot.colorbar()
pyplot.title("Tonalidad")

pyplot.subplot(4, 2, 7)
frames = range(len(spectral_centroids))
frames_to_time = librosa.frames_to_time(frames, sr=sampling_rate, hop_length=hop_length)
pyplot.semilogy(frames_to_time, spectral_centroids, label="Centroides espectrales")
pyplot.ylabel("Hz")
pyplot.xticks([])
pyplot.xlim([frames_to_time.min(), frames_to_time.max()])
pyplot.legend()
pyplot.title("Centroides espectrales")

pyplot.subplot(4, 2, 8)
librosa.display.specshow(spectral_contrast, sr=sampling_rate, hop_length=hop_length, x_axis="time")
pyplot.colorbar()
pyplot.title("Contraste espectral")

pyplot.show()

