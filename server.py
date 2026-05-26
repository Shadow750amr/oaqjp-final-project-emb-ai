from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def template():
    # html
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def return_data():
    texto_usuario = request.args.get('textToAnalyze')
    resultado = emotion_detector(texto_usuario)
    resultado_sin_emotion = resultado.pop('dominant_emotion')
    if resultado_sin_emotion == None:
        return "Invalid text! Please try again!."
    else:
        return f"For the given statement, the system response is {resultado}." f"The dominant emotion is {resultado_sin_emotion}"
if __name__ == "__main__":
    app.run(debug=True, port=5000) 