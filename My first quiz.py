print('Hello, welcome to my very first quiz in python. Hope you enjoy!')
import time
time.sleep(2)
a=0
b=0
while (a<1):
    print('Choose a difficulty:')
    print('Easy = 1')
    print('Medium = 2')
    print('Hard = 3')
    dif=input()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
    if dif == '1':
        print('Difficulty set to easy.')
        time.sleep(1)
        a=(a+1)
        while (b<1):
            print('Choose a topic you would like your questions to be about:')
            print('__________________________')
            print('|Maths = 1               |')
            print('|Geography = 2           |')
            print('|English = 3             |')
            print('|General knowledge = 4   |')
            print('|________________________|')
            question=input()

            if question == '1':
                b=1
                point=0
                print('I\'m going to ask you 3 questions about maths, get them right and you earn a point.')
                print('What is 246 x 100?')
                q1=input()
                print('What is the square root of 81?')
                q2=input()
                print('What is 456 + 544?')
                q3=input()
                if q1 == '24600': point=(point+1)
                if q2 == '9': point=(point+1)
                if q3 == '1000': point=(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('Great job! You got all 3 questions correct.')
                
            elif question == '2':
                b=1
                point=0
                print('I\'m going to ask you 3 questions about geography, get them right and you earn a point.')
                print('What is the capital city of england?')
                q1=input()
                print('In what city is the Eiffel tower located?')
                q2=input()
                print('How many continents are there?')
                q3=input()
                if q1.lower() == 'london':
                    point=(point+1)
                if q2.lower() == 'paris':
                    point=(point+1)
                if q3 == '7':
                    point=(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('Great job! You got all 3 questions correct.')
                
            elif question == '3':
                b=1
                point=0
                print('I\'m going to ask you 3 questions about english, get them right and you earn a point.')
                print('Which is the correct spelling;  something, somethink or sumthing.')
                q1=input()
                print('How many letters are their in the english alphabet?')
                q2=input()
                print('What is the third vowel?')
                q3=input()
                if q1.lower() == 'something': point=(point+1)
                if q2 == '26': point=(point+1)
                if q3.lower() == 'i': point=(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('Great job! You got all 3 questions correct.')

            elif question == '4':
                b=1
                point=0
                print('I\'m going to ask you 3 questions on general knowledge, get them right and you earn a point.')
                print('How many rings are on the Olympic flag?')
                q1=input()
                print('What was given on the fourth day of christmas?')
                q2=input()
                print('Whose nose grew when he told a lie?')
                q3=input()
                if q1 == '5': point=(point+1)
                if q2.lower() == 'calling birds': point=(point+1)
                if q3.lower() == 'pinocchio': point=(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('Great job! You got all 3 questions correct.')

            else:
                print('Invalid input! Please try again.')
                print(' ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif dif == '2':
        print('Difficulty set to medium, good luck!')
        time.sleep(1)
        a=(a+1)
        
        while (b<1):
            print('Choose a topic you would like your questions to be about:')
            print('__________________________')
            print('|Maths = 1               |')
            print('|Geography = 2           |')
            print('|English = 3             |')
            print('|General knowledge = 4   |')
            print('|________________________|')
            question=input()

            if question == '1':
                b=1
                point=0
                print('I\'m going to ask you 4 questions about maths, get them right and you earn a point.')
                print('What shape do you need to times diameter and pie together to get the circumference(perimeter)?')
                q1=input()
                print('How do you work out the area of a rectangle? (Hint: Use symbols)')
                q2=input()
                print('Fill in the missing number. 172 - ___ = 60 ')
                q3=input()
                print('Calculate 3/4 of 840')
                q4=input()
                if q1.lower() == 'circle': point=(point+1)
                if q2.lower() == 'l * w' or q2.lower()=='l * h' or q2.lower()=='h * w': point=(point+1)
                if q3 == '112': point=(point+1)
                if q4 == '630': point=(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('Almost there! You got 3 questions correct.')
                if point == 4: print('Amazing job! You got all 4 questions correct.')
            
            elif question == '2':
                b=1
                point=0
                print('I\'m going to ask you 4 questions about geography, get them right and you earn a point.')
                print('Which country is the capital city \'Canberra\' located?')
                q1=input()
                print('What is the largest country in the world?')
                q2=input()
                print('Which country has the largest population?')
                q3=input()
                print('What is the capital city of Spain?')
                q4=input()
                if q1.lower() == 'australia': point=(point+1)
                if q2.lower() == 'rusia': point=(point+1)
                if q3.lower() == 'china': point=(point+1)
                if q4.lower() == 'madrid': point=(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('Almost there! You got 3 questions correct.')
                if point == 4: print('Amazing job! You got all 4 questions correct.')
            
            elif question == '3':
                b=1
                point=0
                print('I\'m going to ask you 4 questions about english, get them right and you earn a point.')
                print('What are doing words known as?')
                q1=input()
                print('Which is the the correct spelling. Chocolot, chocolate or choclate.')
                q2=input()
                print('What punctuation mark is put after a show of strong feelings or high volume?')
                q3=input()
                print('What was the famous poet "Shakespeare\'s" first name?')
                q4=input()
                if q1.lower() == 'verbs': point=(point+1)
                if q2.lower() == 'chocolate': point=(point+1)
                if q3 == '!' or q3.lower()=='exclamation mark': point=(point+1)
                if q4.lower() == 'william': point=(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('Almost there! You got 3 questions correct.')
                if point == 4: print('Amazing job! You got all 4 questions correct.')
                  
            elif question == '4':
                b=1
                point=0
                print('I\'m going to ask you 4 questions about general knowledge, get them right and you earn a point.')
                print('Which company is owned by Bill Gates?')
                q1=input()
                print('Which planet is the smallest in the solar system?')
                q2=input()
                print('What fish is composed of more than 90% of water?')
                q3=input()
                print('How many seconds are there in an hour?')
                q4=input()
                if q1.lower() == 'microsoft': point=(point+1)
                if q2.lower() == 'pluto': point=(point+1)
                if q3.lower() == 'jellyfish' or q3.lower()=='jelly fish': point=(point+1)
                if q4 == '3600': point=(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('Almost there! You got 3 questions correct.')
                if point == 4: print('Amazing job! You got all 4 questions correct.')
            
            else:
                print('Invalid input! Please try again.')
                print(' ')       
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif dif == '3':
        print('Difficult set to hard,good luck! You\'ll need it.')
        time.sleep(1)
        point=0
        a=(a+1)
        while (b<1):
            print('Choose a topic you would like your questions to be about:')
            print('__________________________')
            print('|Maths = 1               |')
            print('|Geography = 2           |')
            print('|English = 3             |')
            print('|General knowledge = 4   |')
            print('|________________________|')
            question=input()

            if question == '1':
               b=1
               print('I\'m going to ask you 5 questions about maths, get them right and you earn a point.')
               print('What is 24+35*2-44*2 using \'bidmas\'.')
               q1=input()
               print('What is \'PIE\' rounded up to 3 decimal places')
               q2=input()
               print('What is the volume of a cube when one side is 5cm (don\'t forget the units.)')
               q3=input()
               print('What is the circumference of a circle with a radius of 5m, where pie is 3.14(don\'t forget the units.)')
               q4=input()
               print('What\'s the missing angle from a triangle when one angle is 75 and the otheer is 45')
               q5=input()
               if q1 == '6': point=(point+1)
               if q2 == '3.142': point=(point+1)
               if q3 == '125cm3': point=(point+1)
               if q4 == '31.4m': point=(point+1)
               if q5 == '60': point=(point+1)
               if point == 0: print('You didn\'t get any questions right. You should revise more! ')
               if point == 1: print('You only got 1 question right, better luck next time!')
               if point == 2: print('You got 2 questions right. Good try!')
               if point == 3: print('You got 3 questions correct! Half way there.')
               if point == 4: print('Almost got it! You got 4 questions correct.')
               if point == 5: print('Brilliant job! All 5 questions were correct!')
               
            elif question == '2':
                b=1
                print('I\'m going to ask you 5 questions about geography, get them right and you earn a point.')
                print('What is the largest continent?')
                q1=input()
                print('What is the smallest continent?')
                q2=input()
                print('When was the lates Japan earthquake and tsunami?')
                q3=input()
                print('What is the capital city of Brazil?')
                q4=input()
                print('What is the richest country in the world?')
                q5=input()
                if q1.lower() == 'asia': point =(point+1)
                if q2.lower() == 'australia': point =(point+1)
                if q3 == '2011': point =(point+1)
                if q4.lower() == 'brazilia': point =(point+1)
                if q5.lower() == 'qatar': point =(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions correct. Good try!')
                if point == 3: print('You got 3 questions correct! Half way there.')
                if point == 4: print('Almost got it! You got 4 questions correct.')
                if point == 5: print('Brilliant job! All 5 questions were correct!')
                
            elif question == '3':
                b=1
                print('I\'m going to ask you 5 questions about english, get them right and you earn a point.')
                print('What do you call a figure of speach that compares two things using words such as "like", "as" or "than"?')
                q1=input()
                print('Which is the correct spelling?  Embarrass, embares or embarres.')
                q2=input()
                print('What is a \'describing word\' also known as?')
                q3=input()
                print('what is the word for the occurrence of the same letter or sound at the beginning of adjacent?')
                q4=input()
                print('What are all the vowels?(use spaces between each one.)')
                q5=input()
                if q1.lower() == 'simile': point =(point+1)
                if q2.lower() == 'embarrass': point =(point+1)
                if q3.lower() == 'adjective': point =(point+1)
                if q4.lower() == 'alliteration': point =(point+1)
                if q5.lower() == 'a e i o u': point =(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('You got 3 questions correct! Half way there.')
                if point == 4: print('Almost got it! You got 4 questions correct.')
                if point == 5: print('Brilliant job! All 5 questions were correct!')
               
            elif question == '4':
                b=1
                print('I\'m going to ask you 5 questions about general knowledge, get them right and you earn a point.')
                print('What does 3D stand for?')
                q1=input()
                print('Who was the first non-royal to appear on a UK postage stamp?')
                q2=input()
                print('What is the legal age to drive in the UK?')
                q3=input()
                print('At what age does a woman become a pensioner in the UK?')
                q4=input()
                print('Who found out about gravity?')
                q5=input()
                if q1.lower() == 'three-dimensional'or q1.lower()=='three dimensional': point =(point+1)
                if q2.lower() == 'william shakespeare': point =(point+1)
                if q3 == '17': point =(point+1)
                if q4 == '60': point =(point+1)
                if q5.lower() == 'issac newton': point =(point+1)
                if point == 0: print('You didn\'t get any questions right. You should revise more! ')
                if point == 1: print('You only got 1 question right, better luck next time!')
                if point == 2: print('You got 2 questions right. Good try!')
                if point == 3: print('You got 3 questions correct! Half way there.')
                if point == 4: print('Almost got it! You got 4 questions correct.')
                if point == 5: print('Brilliant job! All 5 questions were correct!')
               
            else:
                print('Invalid input! Please try again.')
                print(' ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
    else:
        print('Invalid input! Please try again.')
        print(' ')
time.sleep(1)
print(' ')
print('Thanks for playing my quiz. Hope you enjoyed!')
