password=input("Enter your password: ").strip()
score=0
feedback_lis=[]
if len(password)>=8:
    score+=1
else:
    feedback="Password too short (minimum 8 characters)"
    feedback_lis.append(feedback)

if any(p.isupper() for p in password):
    score+=1
else:
    feedback="Add at least one uppercase letter"
    feedback_lis.append(feedback)

if any(p.islower() for p in password):
    score+=1
else:
    feedback="Add at least one lowercase letter"
    feedback_lis.append(feedback)

if any (p.isdigit() for p in password):
    score+=1
else:
    feedback="Add at least one number"
    feedback_lis.append(feedback)

special_characters=['!', '@', '#', '$', '%', '^', '&', '*',]
if any(p in special_characters for p in password):
    score+=1
else:
    feedback="Add at least one special character"
    feedback_lis.append(feedback)

common_characters=["password", "12345", "qwerty", "abc123"]
if any(p in common_characters for p in password.lower()):
    score-=1
    feedback="Avoid using common or predictable words"
    feedback_lis.append(feedback)

strength=''
if score<=2:
    strength="weak"
elif 3<=score<=4:
    strength="Medium"
elif score==5:
    strength="strong"

print(f"Password strength: {strength}")
if feedback_lis:
    print("Suggestions to improve: \n")
    for item in feedback_lis:
        print(f"- {item}\n")
        


