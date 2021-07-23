# Given a word, write a function to generate all of its unique generalized abbreviations.
# Generalized abbreviation of a word can be generated by 
# replacing each substring of the word by the count of characters in the substring.
# Take the example of “ab” which has four substrings: “”, “a”, “b”, and “ab”. 
# After replacing these substrings in the actual word by the count of characters 
# we get all the generalized abbreviations: “ab”, “1b”, “a1”, and “2”.

# Example 1:
# Input: "BAT"
# Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"

# O(N * 2^N) space: O(N * 2^N)
from collections import deque

class Abbrevations:
    def __init__(self, str, start, count) -> None:
        self.str = str
        self.start = start
        self.count = count

def unique_generalized_abbrevations(word):
    result = []
    queue = deque()
    queue.append(Abbrevations(list(), 0, 0))
    while queue:
        ab_word = queue.popleft()
        if ab_word.start == len(word):
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))
            result.append(''.join(ab_word.str))
        else:
            queue.append(Abbrevations(list(ab_word.str), ab_word.start + 1, ab_word.count + 1))
        
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))
            
            new_word = list(ab_word.str)
            
            new_word.append(word[ab_word.start])
            queue.append(Abbrevations(new_word, ab_word.start + 1, 0))
    
    return result

def unique_generalized_abbrevations_2(word):
    result = []
    unique_generalized_abbrevations_recursive(word, 0, 0, [], result)
    return result

def unique_generalized_abbrevations_recursive(word, start, count, current_str, result):
    if start == len(word):
        if count != 0:
            current_str.append(str(count))
        result.append(''.join(current_str))
    else:
        unique_generalized_abbrevations_recursive(word, start + 1, count + 1, list(current_str), result)
        
        if count != 0:
            current_str.append(str(count))
        new_word = list(current_str)
        new_word.append(word[start])
        unique_generalized_abbrevations_recursive(word, start + 1, 0, new_word, result)

print(unique_generalized_abbrevations("BAT"))
print(unique_generalized_abbrevations_2("BAT"))