# input score
score = float(input("Enter score in [0.0 , 1.0]: "))

# evaluate the score.
if score > 1 or score < 0 : 
    print("Invalid score")
elif score > 0.8 : 
    print("High-Confidence Positive")
elif score >= 0.5 :
    print("Positive")
else : print("Negative") 