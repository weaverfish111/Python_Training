##Richard Weaver
##01/03/2022

def text_to_lines (text, max_length):
    total_count= 0
    output_text = ""
    space = "_"
    word_list = text.split()
    for word in word_list:
        # print(word)
        word_length = len(word)
        if total_count + word_length <= max_length: 
            output_text += word 
            output_text += space
            total_count += word_length +1     # +1 for the spaces after words?
        else:
            output_text = output_text.strip("_")
            output_text += "\n"
            output_text += word
            output_text += space
            total_count = 0
            spaces_count = 0
            total_count += len(word)
            # output_text = output_text.strip("_")
    output_text = output_text.strip("_")
    return(output_text)

test_text1 = "Row, row, row your boat. Gently down the stream. Row, row, row your boat. Gently down the stream."
separate_lines = text_to_lines(test_text1, 25)

# test_text2a = "Computer science is no more about computers than astronomy is about telescopes."
# test_text2b = "If debugging is the process of removing software bugs, then programming must be the process of putting them in."
# print(text_to_lines(test_text2a, 35))
# print(text_to_lines(test_text2b, 40))



for line in separate_lines.split("\n"):
    print(f"{len(line)}: {line}")


 # total_count += len(space)
            # total_count += output_text.count(space)
        # elif total_count + word_length + total_spaces < max_length:
        #     output_text.strip(" ")         #attempt at stripping the final space following the last word of each line

# source_text = "I really appreciate the help, thankyou! This will hopefully work, but who knows?"
# source_text = "ASDF is the sequence of letters that appear on the first four keys on the home row of a QWERTY or QWERTZ keyboard. They are often used as a sample or test case or as random, meaningless nonsense. It is also a common learning tool for keyboard classes, since all four keys are located on Home row." # from the wikipedia
# print(source_text)
# print()
# print(text_to_lines(source_text, 25))


    #create a variable (max_length) which specifies maximum number of characters
    #split up the string into seperate words
    #create a variable that holds the newly made list
    #consider each word to see whether a new line has to be added (\n)
    #if needed, add the new line FIRST! And then the word after.
    #Now that this is done, rejoin the string back together and return it as a string. (Transform Stategy)



    #create a for loop that cuts of the text as certain point
    #create if function which makes sure word is not cut in half
