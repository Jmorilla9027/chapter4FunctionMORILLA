try:
    score = float(input('Enter Grade: '))

    if score <0 and score > 100:
        print('Please enter a valid Numerical Score')
except ValueError:
    print('Enter a Numerical grade')
    score = -1

if not score == -1:
    if score <101 and score >= 90:
        print('Grade A')
    elif score >= 80:
        print('Grade B')
    elif score >= 70:
        print('Grade C')
    elif score <= 70:
        print('Need Improvements')
