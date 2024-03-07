' Q1 A circular coil of radius 5 * 10-2 m and with 40 turns is carrying a current of 0.25 A. Determine the magnetic field of the circular coil at the centre.'
' Q2 Determine the magnetic field at the centre of the semicircular piece of wire with a radius 0.20 m. The current carried by the semicircular piece of wire is 150 A.'
' Q3 A circular loop with a radius of 0.1 m carries a current of 2 A. Calculate the magnetic field at the center of the loop.'
from scipy.constants import mu_0
import math
import time

def feedback():
    suggest=f"Enter your suggestion : {'\n'}{'\n'}"
    for i in range(len(suggest)):
        print(suggest[i],end='')
        time.sleep(0.02)
    data=str(input())
    #Here we will use SQL database to store the suggestion to resolve the issue further, and improve our program.


def solve_magnetism():
    s1=f"Enter all the values in SI Units {'\n'}"
    s2=f"Enter multiplication as * {'\n'}"
    for i in range(len(s1)):
        print(s1[i],end='')
        time.sleep(0.02)
    for i in range(len(s2)):
        print(s2[i],end='')
        time.sleep(0.02)
    N = I = a = None
    permeability_of_free_space = mu_0
    text=f"Enter the question : {'\n'}"
    for i in range(len(text)):
        print(text[i],end='')
        time.sleep(0.02)
    question=str(input())
    question=question.translate(question.maketrans("","","',?"))
    question=question.lower()  #Extracting the exact question
    question=question.split()

    if 'circular' in question:
        N=1
        for i in range(len(question)):
            if question[i] == 'radius' and '*'==question[i + 2]:
                a = float(int(question[i + 1]) * math.pow(10, int(question[i + 3][2:])))
            elif question[i] == 'radius' and question[i+1].isalpha():
                a = float(question[i + 2])
            elif question[i] == 'radius':
                a = float(question[i + 1])
            if question[i] == 'turns':
                N = float(question[i - 1])
            if question[i] == 'current':
                I = float(question[i + 1]) if question[i + 1].replace('.', '', 1).isdigit() else float(question[i + 2])
        if N is None or I is None or a is None:
            
            string=f"Something is wrong with the question! Sorry"
            for i in range(len(string)):
                time.sleep(0.02)
                print(string[i],end='')
        else:
            B = (permeability_of_free_space * N * I) / (2 * a)
            return B
    elif 'semicircular' in question:
        N=1
        for i in range(len(question)):
            if question[i] == 'radius' and '*' in question[i + 2]:
                a = float(int(question[i + 1]) * math.pow(10, int(question[i + 3])))
            elif question[i] == 'radius' and question[i+1].isalpha():
                a = float(question[i + 2])
            elif question[i] == 'radius':
                a = float(question[i + 1])
            if question[i] == 'turns':
                N = float(question[i - 1])
            if (question[i] == 'a' or question[i]=='a.' )and question[i-1].isdigit():
                I=float(question[i-1])
        
        if N is None or I is None or a is None:
            string=f"Something is wrong with the question! Sorry"
            for i in range(len(string)):
                time.sleep(0.02)
                print(string[i],end='')
        else:
            B = (permeability_of_free_space * N * I) / (4 * a)
            return B
    




result=solve_magnetism()
string_main=f"The resultant magnetic field is :{'\n'}{result} Tesla {'\n'}"
for i in range(len(string_main)):
            time.sleep(0.02)
            print(string_main[i],end='')
feed_text=f"Was the answer correct : {'\n'}"
for i in range(len(feed_text)):
    time.sleep(0.02)
    print(feed_text[i],end='')
feed=str(input()).strip().lower()
if(feed=='yes'):
    feed_positive=f"Thanks for using our software! We hope to see you again.{'\n'}"
    for i in range(len(feed_positive)):
        print(feed_positive[i],end="")
        time.sleep(0.02)
elif(feed=='no'):
    feed_negative=f"Please Give us your feedback.{'\n'}"
    for i in range(len(feed_negative)):
        print(feed_negative[i],end='')
        time.sleep(0.02)
    feedback()
