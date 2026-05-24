#hero stats system:the-Novel-of-Viloria shadow
#1/inputs
#1. To enter the character's name
heroname=input('enter the name of hero:')
#2. To introduce the power of the chosen hero
powerofhero=int(input('enter heros strength level:'))
#3.to enter the power of the personal weapon
energyofweapon=float(input('enter the energy level of the weapon it carries:'))
#2/Numbers&Variables
#1. Calculate the total energy of the champion
totalenergy=powerofhero+energyofweapon
#2.Super Attack Strike Energy Calculation
superAttackBlowEnergy=totalenergy*2
#3/print  message for the user showing the results
print(f'power of the hero{heroname} is{powerofhero} energy of the weapon is{energyofweapon}')
print(f'SUPER ATTACK BLOW ENERGY IS {superAttackBlowEnergy}')
print('congratulations, you beat the enemy')
