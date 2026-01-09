# // PYTHON PROJECT #001 \\
# DAY 01
# PROJECT NAME: GREETING AND AGE CALCULATOR

name = input("What is your name? ")
print(f"Hello, {name}")
year_of_birth = int(input("What year were you born? "))
year_of_age = int(input("In which year do you want to know your age? "))
age = year_of_age - year_of_birth
print(f"{name}, you will be {age} years old in the year {year_of_age}.")
