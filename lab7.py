def is_palindrome(word):
    return word == word[::-1]

def find_shortest_palindrome(sentence):
    words = sentence.split()
    shortest_word = min(words, key=len)
    if is_palindrome(shortest_word):
        return f"Найкоротше слово '{shortest_word}' є паліндромом."
    else:
        return f"Найкоротше слово '{shortest_word}' не є паліндромом."

sentence = input("Введіть рядок слів, розділених пробілами: ")
result = find_shortest_palindrome(sentence)
print(result)
