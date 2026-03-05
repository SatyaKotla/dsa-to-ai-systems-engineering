"""
String manipulation and text-processing algorithms.
"""

import string
import heapq
from collections import deque

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


def top_k_frequent_words(text: str, k: int) -> list[tuple[str, int]]:
    """
    Returns top k frequent words by sorting the words
    descending based on frequency.
    Time complexity : O(n + m*logm) where m is number of
                    unique words
    """
    freq = word_frequency_2(text)

    # sort by frequency descending
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:k]


def top_k_frequent_words_heap(text: str, k: int) -> list[tuple[str, int]]:
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


# ------------------------------------------------------#
# ----------------BUILDING STREAMING COUNTER ---------- #
# ------------------------------------------------------#
"""
Goal: Build a class that
1. Accepts words one by one
2. Updates frequency
3. Can return top-k at anytime.
"""


# Basic Streaming Counter
class StreamingWordCounter:

    def __init__(self):
        self.frequency = {}

    def add_word(self, word: str) -> None:

        # Normalize the words
        word = word.lower()
        word = word.strip(string.punctuation)

        if not word:
            return

        self.frequency[word] = self.frequency.get(word, 0) + 1

    def add_text(self, text: str) -> None:
        words = text.split()
        for word in words:
            self.add_word(word)

    def get_top_k_frequent_words(self, k: int) -> list[tuple[str, int]]:
        heap = []

        for word, count in self.frequency.items():
            heapq.heappush(heap, (count, word))

            # heap size limited to k
            if len(heap) > k:
                heapq.heappop(heap)
        result = sorted(heap, reverse=True)
        return [(word, count) for count, word in result]


# Streaming Counter With Sliding Window


class SlidingWindowWordCounter:
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.window = deque()
        self.frequency = {}

    def add_word(self, word: int) -> None:
        word = word.lower()
        word = word.strip(string.punctuation)

        if not word:
            return

        # Add the new word
        self.window.append(word)
        self.frequency[word] = self.frequency.get(word, 0) + 1

        # Remove the last word if window > window_size
        if len(self.window) > self.window_size:
            old_word = self.window.popleft()
            self.frequency[old_word] -= 1
            if self.frequency[old_word] == 0:
                del self.frequency[old_word]

    def get_top_k_frequent_words(self, k: int) -> list[tuple[str, int]]:
        heap = []

        for word, count in self.frequency.items():
            heapq.heappush(heap, (count, word))
            if len(heap) > k:
                heapq.heappop(heap)

        result = sorted(heap, reverse=True)
        return [(word, count) for count, word in result]


def main():
    word_counter = SlidingWindowWordCounter(2)
    word_counter.add_word("AI")
    word_counter.add_word("Is")
    word_counter.add_word("AI")
    word_counter.add_word("Powerful")

    print(word_counter.get_top_k_frequent_words(2))


if __name__ == "__main__":
    main()
