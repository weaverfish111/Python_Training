from cmath import e


source_text = "ASDF is the sequence of letters that appear on the first four keys on the home row of a QWERTY or QWERTZ keyboard. They are often used as a sample or test case or as random, meaningless nonsense. It is also a common learning tool for keyboard classes, since all four keys are located on Home row." # from the wikipedia

def number_of_letters_in(text):
    letter_count = 0
    for letters in text:
        if letters.isalpha():
            letter_count += 1
    return(letter_count)

def number_of_words_in(text):
    word_count = 0
    words = text.split(" ")
    word_count = len(words)
    return(word_count)

def number_of_sentences_in(text):
    sent_count = 0
    sentences = text.split(". ")
    sent_count = len(sentences)
    return(sent_count)

def average_word_length(text):
    letter_count = 0
    word_a = text.split(" ")
    word_a_count = len(word_a)
    for letter_a in text:
        if letter_a.isalpha():
            letter_count += 1
    average = letter_count / word_a_count
    return(average)


print(number_of_letters_in(source_text))
print(number_of_words_in(source_text))
print(number_of_sentences_in(source_text))
print(average_word_length(source_text))