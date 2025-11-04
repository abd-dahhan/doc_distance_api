# Find the algorithm stubs you need to complete the tasks
from collections import Counter


def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    input_text = input_text.replace(",", " , ")
    
    return input_text.lower().split()


def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return Counter(word)



def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
        **NOTE: Our API will send a list of strings**
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note:
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    return Counter(input_iterable)


def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    elements = set(freq_dict1.keys()) | set(freq_dict2.keys())

    total_delta = 0
    total_sigma = 0

    for element in elements:
        count1 = freq_dict1.get(element, 0)
        count2 = freq_dict2.get(element, 0)

        delta = abs(count1 - count2)
        sigma = count1 + count2

        total_delta += delta
        total_sigma += sigma
    
    if total_sigma == 0:
        return 1.0
    
    similarity = 1.0 - (total_delta / total_sigma)

    return round(similarity, 2)