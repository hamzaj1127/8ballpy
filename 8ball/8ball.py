import random

def eight_ball_responses():
    QUESTION = input('what do you wanna ask the 8 ball?')
    v10 =random.randint(1,9)
    if v10==1:
        print("Yes - definitely.")
    elif v10==2:
        print("It is decidedly so.")
    elif v10==3:
        print("Without a doubt.")
    elif v10==4:
        print("Reply hazy, try again.")
    elif v10==5:
        print("Ask again later.")
    elif v10==6:
        print("Better not tell you now.")
    elif v10==7:
        print("My sources say no.")
    elif v10==8:
        print("Outlook not so good.")
    elif v10==9:
        print("Very doubtful.")
    ask_again()

def ask_again():    
    x2 = input('Do you want to ask another question? Yes or no?')
    v11 =random.randint(1,9)
    if x2 == 'nah' or x2 == 'no' or x2 == 'n':
        print('goodbye!')
    elif x2 == 'yes' or x2 == 'y':
        print('what is your question')
        eight_ball_responses()
    else:
        print('have a good day!')
ask_again()