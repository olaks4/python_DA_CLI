score_input = input('Enter score: ')
score = int(score_input)
if 75 <= score <= 100:
    print("student garde is A1 for score 75 <= score <= 100")
elif 70 <= score <= 74:
    print("student grade is B2 for score 70 <= score <= 74")
elif 65 <= score <= 69:
    print("student grade is B3 for score 65 <= score <= 69")
elif 60 <= score <= 64:
    print("student grade is c4 for score 60 <= score <= 64") 
elif 55 <= score <= 59:
    print("student grade is c5 for score 55 <= score <= 59")  
elif 50 <= score <= 54:
    print("student grade is c6 for score 50 <= score <= 54")
elif 45 <= score <= 49:
    print("student grade is D7 for score 45 <= score <= 49") 
elif 40 <= score <= 44:
    print("student grade is E8 for score40 <= score <= 44")  
elif 0 <= score <= 39:
    print("student grade is F9 for score 0 <= score <= 39")  
else:
    print("Invalid score")
