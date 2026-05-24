#building a Calculator
number1=input('enter the firste number: ')
number2=input('enter the secend number:')
operation=input('choose operation(+,-,*,/):')
if operation=='+':
    result=float(number1)+float(number2) 
    print(f'the result is{result}')

elif operation=='-':
    result=float(number1)-float(number2)
    print(f'the result is{result}')
    
elif operation=='*':
    result=float(number1)*float(number2)
    print(f'the result is{result}')
    
elif operation=='/':
    result=float(number1)/float(number2)
    print(f'the result is{result}')
