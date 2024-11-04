import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertIn('domination_emotion', result)
        self.assertEqual(result['domination_emotion'], 'joy')

    def test_anger(self):
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertIn('domination_emotion', result)
        self.assertEqual(result['domination_emotion'], 'anger')

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertIn('domination_emotion', result)
        self.assertEqual(result['domination_emotion'], 'disgust')

    def test_sadness(self):
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertIn('domination_emotion', result)
        self.assertEqual(result['domination_emotion'], 'sadness')

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertIn('domination_emotion', result)
        self.assertEqual(result['domination_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()