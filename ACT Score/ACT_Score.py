print("Calculate your ACT score\n")

def calc_ACT_score(english, math, reading, science):
    # Scores must be within the valid range: 1 - 36
    valid_range = range(1, 37)
    if not all(score in valid_range for score in [english, math, reading, science]):
        return "Invalid. Your score must be between 1 and 36.\nPlease check your entry and try again."

    # Calculate the composite score
    composite_score = (english + math + reading + science) / 4
    rounded_composite_score = round(composite_score)

    return rounded_composite_score

english_score = int(input("Enter English score (1 to 36): "))
math_score = int(input("\nEnter Math score (1 to 36): "))
reading_score = int(input("\nEnter Reading score (1 to 36): "))
science_score = int(input("\nEnter Science score (1 to 36): "))

result = calc_ACT_score(english_score, math_score, reading_score, science_score)
print("\nYour composite ACT score is:", result)

print("\n")

# 2024, August

# This program is NOT affiliated with ACT, Inc.