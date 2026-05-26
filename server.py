from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def template():
    # html
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def return_data():
    # captura de l oque manda js
    texto_usuario = request.args.get('textToAnalyze')
    resultado = emotion_detector(texto_usuario)
    resultado_sin_emotion = resultado.pop('dominant_emotion')
    return f"For the given statement, the system response is {resultado}." f"The dominant emotion is {resultado_sin_emotion}"
if __name__ == "__main__":
    app.run(debug=True, port=5000) 