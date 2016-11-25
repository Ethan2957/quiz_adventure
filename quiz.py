# Our quiz!
score = 0
def quiz():
    question1()
    question2()
    question3()
    question4()
    question5()


def question1():
    global score
    print('Round 1/5')
    print('Which is the fastest?')
    print('A. Bugatti Veyron SS')
    print('B. Hennessey Venom GT Spyder')
    print('C. Koenigsegg One:1')
    answer = input('Choose an answer: ')
    if answer.lower() == 'b':
        print('Correct')
        score = score + 1   
    else:
        print('Wrong - It was B')

    

def question2():
    global score
    print('Round 2/5')
    print('What is ther most wheels on a car?')
    answer = input('Put your guess here: ')
    if answer == '72':
        print("You're Right!")
        score = score + 1
    else:
        print('Wrong, it was 72!')

def question3():
    global score
    print('Round 3/5')
    print('What was the first manifactured car?')
    print('A. Benz Patent-Motorwagen')
    print('B. Model T Ford')
    print("C. Gustave Trouvé's tricycle")
    answer = input('Choose an answer: ')
    if answer.upper() == 'C':
        print('Correct')
        score = score + 1
    else:
        print('Wrong, it was C!')

def question4():
    global score
    print('Round 4/5')
    print('What is the fastest 0-60?')
    print('A. 1.5 seconds')
    print('B. 2 seconds')
    print('C. 2.5 seconds')
    answer = input('Choose your answer: ')
    if answer == 'A':
        print('Correct')
        score = score + 1
    else:
        print('Wrong it was A!')

def question5():
    global score
    print('What is the most expensive car?')
    print('A. Ferrari 250 GTO')
    print('B. Ferrari 350 Scaglietti')
    print('C. Mercedes-Benz W196')
    answer = input('Choose an answer: ')
    if answer.lower() == 'a':
        print('Correct')
        score = score + 1
    elif answer.lower() != 'a':
        print('Wrong it was A!')
    else:
        print("That isn't an option")

    print(score, '/5 well done!')
    


    
# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
