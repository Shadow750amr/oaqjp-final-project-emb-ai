import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy(self):
        resultado = emotion_detector("I am glad this happened")['dominant_emotion']
        self.assertEqual(resultado, "joy")
        
    def test_anger(self):
        resultado = emotion_detector("I am really mad about this")['dominant_emotion']
        self.assertEqual(resultado, "anger")
        
    def test_disgust(self):
        resultado = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        self.assertEqual(resultado, "disgust")
        
    def test_sadness(self):
        
        resultado = emotion_detector("I am so sad about this")['dominant_emotion']
        self.assertEqual(resultado, "sadness")
        
    def test_fear(self):
        resultado = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual(resultado, "fear")


if __name__ == "__main__":
    unittest.main()