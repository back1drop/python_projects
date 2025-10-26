import re
def passworder(password):
    score=0
    feedback_lis=[]
    password_lower=password.lower()

    if len(password)>=8:
        score+=1
    else:
        feedback="Password too short (minimum 8 characters)"
        feedback_lis.append(feedback)

    if re.search(r"[A-Z]",password):
        score+=1
    else:
        feedback="Add at least one uppercase letter"
        feedback_lis.append(feedback)

    if re.search(r"[a-z]",password):
        score+=1
    else:
        feedback="Add at least one lowercase letter"
        feedback_lis.append(feedback)

    if re.search(r"[0-9]",password):
        score+=1
    else:
        feedback="Add at least one number"
        feedback_lis.append(feedback)

    special_characters=re.findall(r"[^A-Za-z0-9]",password)

    if len(special_characters)>=1:
        score+=1
    else:
        feedback="Add at least one special character"
        feedback_lis.append(feedback)
    if len(set(special_characters))>=2:
        score+=1
    if len(set(password))==1:
        score-=1
        feedback="Avoid repeating the same character."
        feedback_lis.append(feedback)

    common_words=["password", "12345", "qwerty", "abc123"]
    if any(word in password_lower for word in common_words):
        score-=1
        feedback="Avoid using common or predictable words"
        feedback_lis.append(feedback)
    
    if(re.search(r"[A-Z]",password)and re.search(r"[a-z]",password) and re.search(r"[^A-Za-z0-9]",password)):
        score+=1
    else:
        feedback.append("Try mixing letters, numbers, and symbols.")

    max_score=6
    if score < 0:
        score = 0
    strength_percentage = int((score / max_score) * 100)

    # 8️⃣ Strength levels
    if strength_percentage <= 20:
        strength = "Very Weak"
        comment = "Too short or predictable. Avoid common patterns."
    elif strength_percentage <= 40:
        strength = "Weak"
        comment = "Needs more variety. Add digits and symbols."
    elif strength_percentage <= 60:
        strength = "Medium"
        comment = "Good start. Mix cases and extend the length."
    elif strength_percentage <= 80:
        strength = "Strong"
        comment = "Secure. Keep it unique and memorable."
    else:
        strength = "Very Strong"
        comment = "Excellent! Very difficult to crack."


    print("\n--- PASSWORD ANALYSIS ---")
    print(f"Password strength: {strength}  ({strength_percentage}%)")
    print(f"\n{comment}")
    if feedback_lis:
        print("Suggestions to improve: \n")
        for item in feedback_lis:
            print(f"- {item}\n")


        

password=input("Enter your password: ").strip()
passworder(password)
