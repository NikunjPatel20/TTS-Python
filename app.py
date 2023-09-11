from flask import Flask, request, render_template, send_file
from gtts import gTTS
import os,uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    language = request.form['language']  # Get the selected language
    
    # Generate a unique filename using uuid
    audio_filename = str(uuid.uuid4()) + '.mp3'
    audio_path = os.path.join('static', audio_filename)

    tts = gTTS(text, lang=language)  # Use the selected language
    tts.save(audio_path)
    os.system('mpg321 ' + audio_path)  # Play the generated audio file
    return render_template('result.html', audio_path=audio_filename)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join('static', filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
