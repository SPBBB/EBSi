""" 
The program should compare input_id and input_pw with the correct values and print:
• “Access Granted” ➔ when both ID and password are correct.
• “Wrong ID” ➔ when only the ID is wrong
• “Wrong Password” ➔ when only the password is wrong.
• “Wrong ID and Password” ➔ when both are wrong.
"""
ID = "IamAdmin"
PW = "!admin123"


input_id = input("Enter your ID: ")
input_pw = input("Enter your pasword: ")

corr_id = (input_id == ID)
corr_pw = (input_pw == PW)

if corr_id and corr_pw : print("Access okay")
if not corr_id and corr_pw : print("ID issue")
if corr_id and not corr_pw : print("password issue")
if not corr_id and not corr_pw : print("denied.")