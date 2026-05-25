#Interactive User Bot Project
name=input('enter your name:')
gender=input('are you woman/man:').lower()
if gender=='woman':
    print(f'Welcome,lady {name}')
elif gender=='man':
    print(f'welcome,Mr.{name}')
age=int(input('enter your age:'))
ro=['Am','Pm']
country=input('enter the name of your country: ').lower()
greetings={'china':'Ni Hao','algeria':'slm','saudi arabia':'ahlan wa sahlan','france':'bonjour'}
country_lower=country.lower()
if country_lower in greetings:
    print(f'{greetings[country_lower]}  In fact {country} is a beautiful  country')
else:
    print(f'hello,In fact {country} is a beautiful country')
city=input('enter the name of your city:')
print(f'{city}  one of the best cities in the world')
time=int(input('what time is it in your country:'))
status=input('enter the status in your country(night/Morning):').lower()
if status=='morning':
    print(f'the time in your country is {time}{ro[0]}')
    question=input('do you like to do activities?(yes/no):').lower()

    if question=='yes':
        print(f'have a productive morning in {city}, time to grab some coffee.')
    elif question=='no':
        print('you are lazy')
elif status=='night':    
    print(f'the time in your country is {time}{ro[1]}')
    print(f'good evening, it is a great time to relax in the beautiful city of {city}')
print(f'thank you {name} for subscribing to my program')      
