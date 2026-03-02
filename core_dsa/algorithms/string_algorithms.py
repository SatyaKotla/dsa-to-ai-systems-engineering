"""
String manipulation and text-processing algorithms. 
"""

# Basic word frequency counter
"""
Problem: Given a string text, return a dictionary with
word counts.
Case-sensitive basic implementation.
"""
def word_frequency(text: str) -> dict[str, int]:
    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1 
        else:
            frequency[word] = 1
    return frequency

# Word frequency counter upgraded version
"""
Case-insensitive and removes punctuation
"""
import string

def word_frequency_2(text: str) -> dict[str, int]:
    
    # normalize the case in text input
    text = text.lower()

    # remove punctuation
    for char in string.punctuation:
        text = text.replace(char, "")
    
    words = text.split()

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

def main():
    text = "AI is powerful. AI is amazing!"
    print(word_frequency_2(text))

if __name__ == "__main__":
    main()