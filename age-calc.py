import datetime

def age_calc(age, target_year):
    current_year = datetime.datetime.now().year
    age_in_target = (target_year - current_year) + age
    return age_in_target

user_age = 0
while user_age > 100 or user_age <= 0:
    user_age = int(input("How old are you?\n"))

target_year = 0
while target_year < datetime.datetime.now().year:
    target_year = int(input("In what future year would you like me to tell you your age?\n"))

age_in_target = age_calc(user_age, target_year)

print(f"\nYou will be {age_in_target} in {target_year}!")

