 # An adventure game
health = 5
from random import randint
boss_damage = randint(1,3)
health_loss = randint(1,2)
boss_health = 10
health = 5
inventory = ''
def status():
    print('')
    print('==========================================================================')
    print('    Health:',health,'    Boss Health:', boss_health)
    print('==========================================================================')
    print('')
def room1():
    global health_loss,health,inventory
    status()
    print('You are getting shot at do you: ')
    print('A. Run to cover')
    print('B. Battle the shooter')
    answer = input('Choose an option: ')
    if answer.lower() == 'b':
        print('You lose the battle, you lost', health_loss, 'health')
        health = health - health_loss
        inventory = inventory + 'Empty gun'
        room2()        
    elif answer.lower() == 'a':
        print('You win the battle, you move on!')
        print('You pick up his weapon on the way past aswell')
        inventory = inventory + 'Gun'
        room2()
    else:
        print("That isn't an option.")
        room1()

def room2():
    global health, inventory
    status()
    print('There is a guard, do you: ')
    print('A. Sneak past him')
    print('B. Assassinate him')
    answer_room2 = input('Choose you answer: ')
    if answer_room2.lower() == 'a':
        print("You move on and he doesn't notice you.")
        room3()
    elif answer_room2.lower() == 'b':
        print('You sneak up to him and assassinate him.')
        print("Do you want the guard's sword or keep the shooter's gun?")
        weapon = input('Which do you want?: ')
        if weapon.lower() in 'the shooters gun':
            print('You keep the gun and move on')
            room3()
        elif weapon.lower() in 'the guards sword':
            inventory = inventory.lower() - 'gun'
            inventory = inventory + 'Sword'
            room3()
        else:
            print('You leave both behind')
            print('You go into a fight bare fisted and get killed')
            room2()
    else:
        print("You don't move and he turns and sees you")
        print('He picks up his gun and shoots')
        print('You have died')
        room2()



def room3():
    global health_loss, health, boss_health, boss_damage ,inventory
    status()
    print('You have reached the boss battle')
    print('The boss lifts his sword, what do you do?')
    print('A. Run Left')
    print('B. Run Right')
    answer = input('Choose a direction: ')
    if answer.lower() == 'a':
        print('You are hit with his sword you lose', health_loss,'health')
        health = health - health_loss
        if health <= 0:
            print('You are dead.')
            room4()
        else:
            room4()
    elif answer.lower() == 'b':
        print('You avoid his swing')
        if inventory == 'Empty Gun':
            print('You go to shoot but the magazine is empty')
            print('He swings and kills you')
            room3()
        elif inventory == 'Gun':
            print('You pull out you gun and deal 5 damage')
            boss_health = boss_health - 5
            if boss_health == 0:
                print('You have killed the boss and won!!')
        else:
            print('You swing back and deal 3 damage')
            boss_health = boss_health - 3
    else:
        print("You Didn't move, he swings and kills you")
        room3()

def room4():
    global health_loss, boss_health, boss_damage, health, inventory
    status()
    print('You are going to attack to the troll: ')
    print("A. Aim for the leg")
    print("B. Aim for the the head")
    print('C. Aim for the waist')
    answer = input('Choose somewhere to attack: ')
    if answer.lower() == 'a':
        print('You slash his leg and deal', boss_damage, 'damage to him')
        boss_health = boss_health - boss_damage
        print('The boss has', boss_health, 'health left')
    elif answer.lower() == 'b':
        print("You hit his side but it doesn't phase him")
    elif answer.lower() == 'c':
        print('You hit him in his waist but his armour protects him')
    else:
        print("That isn't an option, he swings and kills you")
        room4()
    room5()


def room5():
    global health_loss, boss_health, boss_damage, health, inventory
    status()
    print('Where do you run to?')
    print('A. A pile of boxes.')
    print('B. Stay and fight.')
    print('C. Keep running')
    answer5 = input('What do you choose?: ')
    if answer5.lower() == 'a':
        print('He sees you turn the corner he swings at the boxes and takes', health_loss,'health off you')
        health = health - health_loss
        if health <= 0:
            print('You have died')
            room5()            

    elif answer5.lower() == 'b':
        print('You choose to fight... and succeed, you deal',boss_damage,'damage')
        boss_health= boss_health - boss_damage
        if boss_health == 0:
            print('You killed the boss well done!')
            print('You have won with',health,'health left!')
        else:
            print('The boss has',boss_health,'health left!')

    elif answer5.lower() == 'c':
        print('He sees you running and tries to swing but misses')
        print('You swing back and deal 2 damage to the boss')
        boss_health = boss_health - 2
        if boss_health <= 0:
            print('You have killed the Boss!!')
            print('You have won!')

    else:
        print('You have taken too long he kills you')
        room1()        
    
    

    

    
    
    




    
# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
