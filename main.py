from flask import Flask, send_file
from size import get_file_size
from Bitrate import get_bitrate
from DR import plot_decibel_range
from harmonicity import plot_harmonicity
from loudness import plot_loudness
from peak_level import plot_waveform_with_peak
from silence_speech import plot_silence_speech_ratio_pie
from SR import plot_waveform_with_sampling_rate
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Audio Features API. Use specific endpoints to get audio features."

@app.route('/file-size')
def file_size():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "audio.mp3")

    file_size_in_mb = get_file_size(file_path)
    return f'File Size: {file_size_in_mb:.2f} MB'

@app.route('/bitrate')
def bitrate():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "audio.mp3")

    bitrate_value = get_bitrate(file_path)
    if bitrate_value:
        return f'Bitrate: {bitrate_value} bps'
    else:
        return 'Could not determine the bitrate'

@app.route('/decibel-range')
def decibel_range():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "audio.mp3")

    plot_path = plot_decibel_range(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/harmonicity')
def harmonicity():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "audio.mp3")

    plot_path = plot_harmonicity(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/loudness')
def loudness():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "audio.mp3")

    plot_path = plot_loudness(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/waveform-with-peak')
def waveform_with_peak():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "audio.mp3")

    plot_path = plot_waveform_with_peak(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/silence-speech-ratio')
def silence_speech_ratio():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "audio.mp3")

    plot_path = plot_silence_speech_ratio_pie(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/waveform-sampling-rate')
def waveform_sampling_rate():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "audio.mp3")

    plot_path = plot_waveform_with_sampling_rate(file_path)
    return send_file(plot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
