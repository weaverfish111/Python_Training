# from cgitb import text

# python list_words.py

original = "The apple  doesn't fall far from the  tree."
'''
apple
doesn't
fall
far
from
the
tree
'''
# original = input("What do you want to say? -> ")
"""
I like how you provided an example, the goal, right at the start
You made a much broader clean up than me hahah
I like the change between the initial (commented out) code and the current,
I still have a bunch of functions, I prefer how you went about it

"""
def cleanup(string):
    lowercase = string.lower()
    punct = lowercase.strip("!.,!?;:()[]")
    clean_text = punct
    return(clean_text)

def text_to_unique_words(string):
    unique_words = []
    cleanwords_list = string.split()
    for word in cleanwords_list:
        word = cleanup(word)
        if word not in unique_words:
            unique_words.append(word)
    sorted_unique_words = sorted(unique_words)
    print(*sorted_unique_words, sep="\n")
    return(sorted_unique_words)

text_to_unique_words(original)



    # print(cleanwords_list)
    # return(cleanwords_list)
    #     if cleanwords not in unique_words:
    #         unique_words.extend(cleanwords_list)
    #     sorted_unique_words = sorted(unique_words)
    # print(*sorted_unique_words, sep = "\n")
    # return(sorted_unique_words)

    
    
    # cleanup(text)
    # words = text.split(" ")
    # unique_words = []
    # for words in text:
    #     unique_words.append(words)
    # # cleanup(words)
    # print(unique_words)

    # return(unique_words)

    # for words in text:
    #     for line in words:
    #         if line.isalpha():
    #             words = text.split(" ")
    #             print(line)
    #         break
    #     break
    # return(line)

# cleanup(text)
# print(text)


    # if lowercase in ".":
    #     lowercase = lowercase.replace(".","")
    # print(lowercase)
    # return(lowercase)




    
#     print(words)
#     for word in words:
#         word = words.split()
#         print(word)
#     return(word)


    
# text_to_unique_words(original)





    # for words in text:
    #     # words = text.split(" ")
    #     lower_case = words.lower()
    #     print(lower_case)
    # # print(lower_case)
    # return(lower_case)


# def cleanup(text):
#     sorted(text)
    
    
    
    
    # words_list = text.split(" ")
    # lines = words_list.splitlines()
    # print(lines)
    # return(lines)
    



# def cleanup(word):
#     str.casefold(text)
#     for word in text:



# def text_to_unique_words(text):
#     words = text.split(" ")
    # lower_case = words.lower(words)