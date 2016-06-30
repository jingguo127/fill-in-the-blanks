def word_in_pos(word, parts_of_speech):
    '''
    This functions is used to exam whether there is a match between one of the parts_of_speech
    and word. If there is a match, then return the match part. Ohterwise return None
    '''
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def fill_blank(ml_string,ml_list,parts_of_speech,count,number,answer,blank_number,wrong_chances):
    '''
    This functions is to exam a list of words in order to find out which word is the blank.
    After it find out the blank, it let use fill the blank with their input.
    Then exam wheter the input match the responsive answer or not and calculate the right time and the wrong time.
    Also return the string of which blanks have been replaced by user's input
    '''
    for word in ml_list:
        replacement=word_in_pos(word,parts_of_speech)
        if replacement != None:
            user_input = raw_input('What is the answer in '+replacement+': ')
            if user_input == answer[number[0]]:
                ml_string = ml_string.replace(replacement,user_input)
                number[0] += 1
                print ml_string
                if number[0] == blank_number:
                    print 'you are awesome!'
                return  ml_string
            else:
                print  'Wrong x '+str(count[0]+1)
                count[0] += 1
                if count[0] == wrong_chances:
                    print 'you suck!'
                return  ml_string

def play_game(ml_string, parts_of_speech, count,number,wrong_chances,blank_number,answer_list):
    '''
    This functions start one round of game. In other words, it's to let user fill one blank
    '''
    choice_number = 4-wrong_chances
    answer=answer_list[choice_number]
    replaced = []
    ml_list = ml_string.split()
    return_string = fill_blank(ml_string,ml_list,parts_of_speech,count,number,answer,blank_number,wrong_chances)
    return return_string

content_of_levels = ['''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',
'''this is a different ___1___ content, which ___1___is the next level ___2___ separated by commas between the parentheses.
 ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated su___5___ch as objects and lambda functions.''',
'''This this even harder___1___ is created witputs a ___1___ takes by
adding ___2___ separae parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standardch as string, number, dictionary,
tuple, and ___4___ or can be more co___5___mplicated such ___6___as objects and lambda functions.''']

blank_parts = [["___1___", "___2___", "___3___", "___4___"],
["___1___", "___2___", "___3___", "___4___", "___5___"],
["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]]

answer_list = [['AAA','BBB','CCC','DDD'],['AAA','CCC','BBB','DDD','EEE'],['FFF','GGG','SSS','HHH','FFS','ADF']]

def game_process(choice_number,content_of_levels,blank_parts,answer_list):
    '''
    This function start the gameplay part. In other words, it start the fill_in_blank
    question and let user to answer it untill they finish it or make it all wrong
    '''
    parts_of_speech  = blank_parts[choice_number-1]
    ml_string = content_of_levels[choice_number-1]
    countA=[0]
    numberA=[0]
    wrong_chances = 5 - choice_number
    blank_number = len(parts_of_speech)
    print ml_string
    while (countA[0] != wrong_chances and numberA[0] != blank_number):
        ml_string = play_game(ml_string, parts_of_speech,countA,numberA,wrong_chances,blank_number,answer_list)

def start_game():
    'This function start the whole game process from the very beginning'
    print '3 levels, chose one.' # put it in to a funtion
    user_choice = raw_input('hard, super hard, magnificently hard:')
    choice_number = 0
    if user_choice == 'hard' :
        choice_number = 1
    elif user_choice == 'super hard':
        choice_number = 2
    elif user_choice == 'magnificently hard':
        choice_number = 3
    else:
        choice_number = 1
        print 'since you are too stupid to input the right choice, i chose the simplest for you'
    game_process(choice_number,content_of_levels,blank_parts,answer_list)

start_game()
