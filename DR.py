import librosa
import numpy as np
import matplotlib.pyplot as plt

def calculate_decibels(audio_signal, reference_pressure=20e-6):
    rms = np.sqrt(np.mean(audio_signal**2))
    decibels = 20 * np.log10(rms / reference_pressure)
    return decibels

def plot_decibel_range(file_path):
    # Read audio file
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    
    # Calculate the decibels over a sliding window
    window_size = sample_rate  # 1 second window
    step_size = window_size // 2
    decibel_levels = []

    for start in range(0, len(audio_data) - window_size, step_size):
        window = audio_data[start:start + window_size]
        decibels = calculate_decibels(window)
        decibel_levels.append(decibels)

    # Plot the decibel levels
    plt.figure(figsize=(5, 3))
    plt.plot(decibel_levels, label='Decibel Level (dB)')
    plt.xlabel('Window Index')
    plt.ylabel('Decibel Level (dB)')
    plt.title('Decibel Range of Audio File')
    plt.legend()
    plt.grid(True)
    output_path = 'static/decibel_plot.png'
    plt.savefig(output_path)
    return output_path
