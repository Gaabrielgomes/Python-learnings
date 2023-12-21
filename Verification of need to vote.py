def vote(birth):
    from datetime import date
    year = date.today().year
    a = year - birth
    if a < 16:
        return f'With {a} years you cannot vote'
    elif 16 <= a < 18 or 65 < a < 100:
        return f'With {a} years, vote is optional'
    elif a >= 100:
        return f"You're still alive with {a} years of age? Ok, you can vote"
    else:
        return f'With {a} years you must vote'


print('~~ Vote query ~~')
print(vote(int(input("When were you born? "))))
