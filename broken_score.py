"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    get_score(score)

def get_score(num1):
    if num1 < 0 or num1 > 100:
        return "Invalid score"
    elif num1 > 90:
        return "Excellent"
    elif num1 > 50:
        return "Passable"
    else:
        return "Bad"

main()



