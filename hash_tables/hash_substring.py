# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def hash(pattern, p, x):
    val = 0
    for i in range(len(pattern)):
        val = val + (ord(pattern[i]) * pow(x, i))
    return val

def precompute_hashes(text, pattern, p, x):
    text_len = len(text)
    pattern_len = len(pattern)

    h = [None] * (text_len-pattern_len+1)
    s = text[(text_len-pattern_len):]

    h[text_len-pattern_len] = hash(s, p, x)

    y = 1
    for _ in range(pattern_len):
        y = (y*x)

    for i in range(text_len-pattern_len-1, -1, -1):
        h[i] = ((x*h[i+1]) + ord(text[i]) - (y*ord(text[i+pattern_len])))

    return h

def rabin_karp(pattern, text):
    p = 982451653
    x = random.randint(1, p-1)

    result = []

    p_hash = hash(pattern, p, x)
    h = precompute_hashes(text, pattern, p, x)

    for i in range(len(text)-len(pattern)+1):
        if p_hash != h[i]:
            continue
        if p_hash == h[i]:
            result.append(i)

    return result

# if __name__ == '__main__':
#     print_occurrences(rabin_karp(*read_input()))

class TextSearch:
    """Rabin–Karp’s algorithm for searching the given pattern in the given text.
    Samples:
    >>> ts = TextSearch("aba", "abacaba")
    >>> ts.find()
    [0, 4]
    >>> # Explanation:
    >>> # The pattern aba can be found in positions 0 (abacaba) and 4 (abacaba)
    >>> # of the text abacaba.
    >>>
    >>> ts = TextSearch("Test", "testTesttesT")
    >>> ts.find()
    [4]
    >>> # Explanation:
    >>> # Pattern and text are case-sensitive in this problem. Pattern “Test“
    >>> # can only be found in position 4 in the text “testTesttesT“.
    >>>
    >>> ts = TextSearch("aaaaa", "baaaaaaa")
    >>> ts.find()
    [1, 2, 3]
    >>> # Explanation:
    >>> # Note that the occurrences of the pattern in the text
    >>> # can be overlapping, and that’s ok, you still need to
    >>> # output all of them.
    """
    def __init__(self, pattern, text):
        self._pattern = pattern
        self._text = text
        self._window = len(pattern)
        self._scan_bound = len(text) - len(pattern) + 1
        self._checksums = []

    def checksum(self, string):
        """Returns hash of the string."""
        return sum([ord(string[i]) for i in range(len(string))])

    def precompute_hashes(self):
        """Precomputes hash values for the whole possible pattern entries
        in the text.
        """
        self._checksums = [self.checksum(self._text[:self._window])]

        for i in range(1, self._scan_bound):
            old_hash = self._checksums[i - 1]
            left_l_hash = ord(self._text[i - 1])
            right_l_hash = ord(self._text[i + self._window - 1])

            ith_hash = old_hash - left_l_hash + right_l_hash
            self._checksums.append(ith_hash)

    def find(self):
        """Returns all occurrences of pattern in the text."""
        pattern_checksum = self.checksum(self._pattern)
        self.precompute_hashes()

        results = []
        for i in range(self._scan_bound):
            if pattern_checksum == self._checksums[i]:
                if self._pattern == self._text[i:i + self._window]:
                    results.append(i)
        return results


if __name__ == "__main__":
    pattern, text = input().rstrip(), input().rstrip()

    ts = TextSearch(pattern, text)
    result = ts.find()

    print(" ".join(map(str, result)))


