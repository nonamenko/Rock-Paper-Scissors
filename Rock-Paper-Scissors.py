import random

def rock_paper_scissors():
    options = ["Камінь", "Ножиці", "Папір"]
    print("Ласкаво просимо до гри 'Камінь-ножиці-папір'!")

    while True:
        user_choice = input("Виберіть Камінь, Ножиці або Папір (або 'вихід' для завершення): ").capitalize()
        if user_choice == "Вихід":
            print("Гра завершена!")
            break

        if user_choice not in options:
            print("Некоректний вибір. Спробуйте ще раз.")
            continue

        computer_choice = random.choice(options)
        print(f"Комп'ютер вибрав: {computer_choice}")

        if user_choice == computer_choice:
            print("Нічия!")
        elif (user_choice == "Камінь" and computer_choice == "Ножиці") or \
             (user_choice == "Ножиці" and computer_choice == "Папір") or \
             (user_choice == "Папір" and computer_choice == "Камінь"):
            print("Ви перемогли!")
        else:
            print("Комп'ютер переміг!")

if __name__ == "__main__":
    rock_paper_scissors()
