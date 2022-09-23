def count_substring(word: str, subword: str):
    if len(subword) == 0:
        raise ValueError("Subword cannot be empty!")
    
    counter = 0
    
    while True:
        idx = word.find(subword)
        
        if idx >= 0:
            counter += 1
            word = word[(idx + 1):]
        else:
            break
    
    return counter


word = "BANANA"

print("You can write 0 if you want to exit program.")

total_score = 0
while True:
    user_subword = input("Enter your subword: ")
    
    if user_subword == "0":
        print(f"Your total score: {total_score}")
        break
    try:
        score = count_substring(word, user_subword)
        total_score += score 
    except ValueError:
        user_subword = input("You cannot write empty string! Enter your subword: ")
    
    print(f"Subword: {user_subword} | score: {score}")  

# 1. Перезапустити ВЕСЬ цикл
# 2. ЗРОБИТИ цикл функцією game()
# 3. Вводимо ANA, отримає тотал скор 2, якщо повторно запишу ANA, то воно вже не має враховуватися
# Тоді запросити в користувача ввести заново

open()