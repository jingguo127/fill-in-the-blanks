def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech, count,number,n):


    answer=['AAA','BBB','CCC','DDD']

    replaced = []
    ml_list = ml_string.split()
    for word in ml_list:
        replacement=word_in_pos(word,parts_of_speech)

        if replacement != None:
            user_input = raw_input('What is the answer in '+replacement+': ')

            if user_input == answer[number[0]]:
                ml_string = ml_string.replace(replacement,user_input)
                number[0] += 1
                print ml_string
                if number[0] == 4:
                    print 'you are awesome!'

                return  ml_string
            else:
                print  'Wrong x '+str(count[0]+1)
                count[0] += 1
                if count[0] == n:
                    print 'you suck!'

                return ml_string




def game_process(n):
    parts_of_speech  = ["___1___", "___2___", "___3___", "___4___"]
    ml_string = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
    adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
    don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
    tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
    countA=[0]
    numberA=[0]
    print ml_string
    while (countA[0] != 4 and numberA[0] != n):
        ml_string = play_game(ml_string, parts_of_speech,countA,numberA,n)

    #print countA[0]
    #print numberA[0]

print '3 levels, chose one.'
user_choice = raw_input('hard, super hard, magnificently hard:')
choice_number = 0
if user_choice == 'hard' :
    choice_number = 4
if user_choice == 'super hard':
    choice_number = 3
if user_choice == 'magnificently hard':
    choice_number = 2
else:
    choice_number = 4
    print 'since you are too stupid to input the right choice, i chose the simplest for you'

game_process(choice_number)
