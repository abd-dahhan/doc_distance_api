from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from distance.algo import calculate_similarity_score, get_letter_frequencies



class TestWordFrequencies(TestCase):
    def test_frequency(self):
        client = APIClient()
        res = client.post(reverse('word-frequencies'), {"payload": ["h", "e", "l", "l", "o"]})
        self.assertDictEqual({'response': {'h': 1, 'e': 1, 'l': 2, 'o': 1}}, res.json())
        self.assertEqual(res.status_code, 200)


class TestTextToList(TestCase):
    def test_words_to_list(self):
        client = APIClient()
        res = client.post(reverse('text-to-list'), {"text": "Hello world, you are awesome"})
        # result is converted to lower case
        self.assertDictEqual({'response': ["hello", "world", "," "you", "are", "awesome"]}, res.json())
        self.assertEqual(res.status_code, 200)


class UnitTest(TestCase):
    def test_similarity(self):
        word = get_letter_frequencies('hello')
        self.assertEqual(calculate_similarity_score(word, word), 1)
        
        word = get_letter_frequencies('hello world, hello')
        word_2 = get_letter_frequencies('hello friends')
        # Test will be refined at a future date
        self.assertTrue(calculate_similarity_score(word, word_2) < 1)

