# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
#adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
#don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
#tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

#this is a list of lists that has the key of correct answers for all three 
#sentences
correct_answers = [["blue", "green", "purple", "black"],["Art", "Painting", "oil", "canvas"],
                   ["Picasso", "Dali", "Seurat", "Monet"]]

# The following are some test strings to pass in to the execute_quiz function.
sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

#the following are the three sentences
easy =  '''The three primary colors are ___1___, red, and yellow. Blue and yellow make ___2___.
   Blue and red make ___3___.  The darkest color is ___4___.'''

medium = '''___1___ is the expression or application of human creative skill and imagination producing works 
to be appreciated primarily for their beauty or emotional power. ___2___ is the art of using a brush to
apply paints made of watercolor base, ___3___ base, acrylic base, etc. on a pre-prepared ___4___  or paper.'''

hard = '''Pablo ___1___ painted in the form of Cubism. Salvador ___2___ painted in the form of Surrealism.Georges ___3___ used pointillism to make the beautiful painting, "A Sunday on La Grande Jatte". 
Claude ___4___ was the leader of the Impressionist movement in France. '''


# Runs a fill in the blank quiz. A player is prompted to replace words in a sentence, 
# which appear in fill_in_numbers with their own words. 
# there is no input to this function
# output is final_sentence
def execute_quiz():    
    final_sentence = []
    user_words = []
    number = 1
    diff_int = get_difficulty()
    final_sentence = set_text(diff_int)
    user_words = get_user_input(diff_int, final_sentence, number)
    final_sentence = show_new_sentence(user_words, final_sentence, number)
    print "Congratulations. You won!"
    return final_sentence


def show_new_sentence(user_words, sentence, number_count):
    for user_word in user_words:
        sentence = sentence.replace("___" + str(number_count) + "___", user_word)
        number_count += 1
    return sentence

## this function obtains the user input and deals with the invalid response
## input is the difficulty in the form of an integer
## output is the list: Word_list that contains the correct user entries
def get_user_input(difficulty_int, new_sentence, num_count):
    word_list = []
    fi_number_count = 4  
    word_count = 0
    num_of_tries_allowed = 5
    try_count = 1
    ui_val = True
    while word_count < fi_number_count:
        while True:
            ui_val, word = get_word_instance(word_count + 1, difficulty_int)
            if ui_val is False:
                print "Invalid Response.  Please try again."
                check_try_count(try_count, num_of_tries_allowed)
                try_count += 1
            else:
                word_list.append(word)
                print show_new_sentence(word_list, new_sentence, num_count) 
                break	  
        word_count += 1
    return word_list

## this function checks the tries and if exceeded displays a message and exits the
## program
## the inputs are answer_count and tries_allowed
## there is not output 
def check_try_count(answer_count, tries_allowed):
    if answer_count >= tries_allowed:
        print "You have lost.  Too many tries.  Please play again. "
        exit() 

## This function gets prompts the user, accepts the raw input and validates
## the entries
## inputs are the num_of_word and the diff_integer
## outputs are the boolean user_input_val and the user_input string
def get_word_instance(num_of_word, diff_integer):
    user_input = raw_input("Please type in " + str(num_of_word) + " : ")
    user_input_val = validate(num_of_word, user_input, diff_integer)       
    return user_input_val, user_input 

## this code validates the user's entry
## this code has three inputs - the three parameters, fin_entry, user_entry, diff_rating
## this code has one output, a Boolean
def validate(fin_entry, user_entry, diff_rating):               
		if user_entry == correct_answers[diff_rating - 1][fin_entry - 1]:
			  return True
		else:
	 			return False	

## this code gets the difficulty entry from the user's raw input 
## there is no input to the function
## the output is the ret_diff which stands for return difficuty in numeric value
def get_difficulty():
    diff_input = ''
    print "Thank you for playing my fill in the blank game."
    diff_input = raw_input("Please choose difficulty as easy, medium, or hard :")  
    print "Thanks. You picked " + diff_input + " !"
    print "You get 5 chances to get the fill in the blank correctly."
    if diff_input == "easy":
      print easy
      ret_diff = 1
    elif diff_input == "medium":
      print medium
      ret_diff = 2
    else:
      print hard
      ret_diff = 3
    return ret_diff
 
## this code gets the appropriate sentence for the difficulty level
## input is the difficulty number
## output is the sentence that matches the difficulty
def set_text(diff_number):
    if diff_number == 1:
        return easy
    elif diff_number == 2:
        return medium
    else:
         return hard

 
print execute_quiz()      

