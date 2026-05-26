This project uses a NLP system to perform emotion detection.
As an extension of sentiment analysis, emotional analysis attends "the finer emotions, like joy, sadness, anger, and so on, from statements rather than the simple polarity that sentiment analysis provides" (IBM,sf), not to mention that this is useful for recomendation systems, chatbots and customer management.

## Repo structure

```
├── EmotionDetection                             ----- main logic folder
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── emotion_detection.cpython-312.pyc
│   └── emotion_detection.py                     ----- main logic file  
├── LICENSE
├── README.md
├── __pycache__
│   └── server.cpython-312.pyc
├── server.py                                    ----- app logic
├── static
│   └── mywebscript.js                           ----- js used to frontend
├── templates
│   └── index.html                               ----- html used to frontend
└── test_emotion_detection.py                    ----- test file for unit tests
```

Example usages:

By typing "I think I am having fun" we received a sort of values as follows, indicating that the predominant emotion is joy:
<img width="1340" height="837" alt="6b" src="https://github.com/user-attachments/assets/19cba108-5d0d-4ef9-a603-93eaca8ec5ac" />





