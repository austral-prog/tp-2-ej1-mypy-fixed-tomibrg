# Replace the "ANSWER HERE" for your answer
def is_leap_year() -> None:
    year: int = int(input('Ingrese un año: '))
    
    if (year % 100 == 0) and (year % 400 == 0):
        print(f'El año {year} es bisiesto')
    elif year % 4 == 0 and not (year % 100 == 0):
        print(f'El año {year} es bisiesto')
    else:
        print(f'El año {year} no es bisiesto')
    


is_leap_year()