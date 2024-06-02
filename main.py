from flask import Flask, request, send_file, jsonify
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI environments
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

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return "Welcome to the Audio Features API. Use specific endpoints to get audio features."

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            return jsonify({'file_path': file_path})
    return '''
    <!doctype html>
    <title>Upload an audio file</title>
    <h1>Upload an audio file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/file-size', methods=['POST'])
def file_size():
    file_path = request.json['file_path']
    file_size_in_mb = get_file_size(file_path)
    return f'File Size: {file_size_in_mb:.2f} MB'

@app.route('/bitrate', methods=['POST'])
def bitrate():
    file_path = request.json['file_path']
    bitrate_value = get_bitrate(file_path)
    if bitrate_value:
        return f'Bitrate: {bitrate_value} bps'
    else:
        return 'Could not determine the bitrate'

@app.route('/decibel-range', methods=['POST'])
def decibel_range():
    file_path = request.json['file_path']
    plot_path = plot_decibel_range(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/harmonicity', methods=['POST'])
def harmonicity():
    file_path = request.json['file_path']
    plot_path = plot_harmonicity(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/loudness', methods=['POST'])
def loudness():
    file_path = request.json['file_path']
    plot_path = plot_loudness(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/waveform-with-peak', methods=['POST'])
def waveform_with_peak():
    file_path = request.json['file_path']
    plot_path = plot_waveform_with_peak(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/silence-speech-ratio', methods=['POST'])
def silence_speech_ratio():
    file_path = request.json['file_path']
    plot_path = plot_silence_speech_ratio_pie(file_path)
    return send_file(plot_path, mimetype='image/png')

@app.route('/waveform-sampling-rate', methods=['POST'])
def waveform_sampling_rate():
    file_path = request.json['file_path']
    plot_path = plot_waveform_with_sampling_rate(file_path)
    return send_file(plot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
