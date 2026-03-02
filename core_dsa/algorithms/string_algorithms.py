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

# Return Top-K Frequent Words
"""
Problem: Given text and k, return the k most frequent words. 
"""
def top_k_frequent_words(text: str, 
                         k: int)-> list[tuple[str, int]]:
    """
    Returns top k frequent words by sorting the words
    descending based on frequency.
    Time complexity : O(n + m*logm) where m is number of 
                    unique words
    """
    freq = word_frequency_2(text)

    # sort by frequency descending
    sorted_words = sorted(freq.items()
                          , key=lambda x:x[1],
                            reverse=True)
    return sorted_words[:k]


import heapq
def top_k_frequent_words_heap(text: str,
                              k: int) -> list[tuple[str, int]]:
    """
    Returns top k frequent words using a min-heap.
    Time complexity : O(n + m*logk) where m is number of 
                    unique words
    """
    freq = word_frequency_2(text)

    heap = []

    for word, count in freq.items():
        heapq.heappush(heap, (count, word))

        # heap size limited to k
        if len(heap) > k:
            heapq.heappop(heap)
    
    # convert heap to descending order
    result = sorted(heap, reverse=True)

    return [(word, count) for count, word in result]


def main():
    text = "AI is powerful. AI is amazing and AI is evovling."
    print(top_k_frequent_words_heap(text, k=2))

if __name__ == "__main__":
    main()