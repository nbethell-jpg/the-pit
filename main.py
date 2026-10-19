from map import locations
import subprocess
import textwrap

run = True
menu = True
play = False
rules = False


# prints box around text

def print_box(lines, width=60):
    
    longest = max(len(line) for line in lines)
    inner_width = min(width - 4, longest)
       
    
    print("┌" + "─" * (inner_width+2) + "┐")

    for line in lines:
        wrapped_lines = textwrap.wrap(line, width=inner_width)

        for wrapped in wrapped_lines:
            print("│ " + wrapped.ljust(inner_width) + " │")

    print("└" + "─" * (inner_width+2) + "┘")


# clears terminal

def clear():
    subprocess.run('clear', check=False)

#gest stats for chosen role

def get_stats(role):

    if role == 'fighter':
        strength = 15
        cun = 10
        wis = 5

    elif role == 'thief':
        strength = 10
        cun = 15
        wis = 15

    elif role == 'arcanist':
        strength = 5
        cun = 10
        wis = 15
 
    return strength, cun, wis

#gets resources stats based on str,cun,wis

def get_resources(strength, cun, wis):
    maxhp = int(strength)*5 +50
    maxfocus = int(cun)*5
    maxmana = int(wis)*5
    return maxhp, maxfocus, maxmana

#saves game

def save():
    list = [
        str(name),
        str(role),
        str(hp),
        str(focus),
        str(mana),
        str(strength),
        str(cun),
        str(wis),
        current_location
    ]
    f = open("load.txt", 'w')
    
    for item in list:
        f.write(item + ' \n')
    f.close()

#offers player yes or no option

def get_yes_no():
    yesno=''
    while yesno not in ['Y', 'N']:
        yesno = input('#').upper()

        if yesno not in ['Y','N']:
            print ('invalid selection')
    return yesno




while run:
    while menu:
        clear()
        print_box ([
        '1. NEW GAME',
        '2. LOAD GAME',
        '3. RULES',
        '4. EXIT GAME'
        ])

        choice = input ('# ')

        if choice == '1':
            clear()
            print_box(['What is your name faceless one?'])
            name = input ("#")
            clear()
            print_box([
                'In life, what was your profession?',
                '1. Fighter 2. Thief 3. Arcanist'
            ])
            role =''
            while role not in ['1','2','3']:
                role = input ('#')
                if role not in ['1','2','3']:
                    print('Invalid selection')
            if role == '1':
                role = 'fighter'
            elif role == '2':
                role = 'thief'
            elif role == '3':
                role = 'arcanist'
            strength, cun, wis = get_stats(role)
            maxhp, maxfocus, maxmana = get_resources(strength, cun, wis)
            hp = maxhp
            focus = maxfocus
            mana = maxmana    
            clear()
            print_box([
                'Are you ready to enter the pit? Y/N'
            ])

            dest=get_yes_no()

            if dest == 'Y':
                play = True
                menu = False
                current_location ='Front Gate'
            elif dest == 'N':            
                save()            
                menu = True
                play = False

        elif choice == '2':
            clear()
            try:
                f = open("load.txt", 'r')
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    role =  load_list[1][:-1]
                    hp =  int(load_list[2][:-1])
                    focus =  int(load_list[3][:-1])
                    mana =  int(load_list[4][:-1])
                    strength =  int(load_list[5][:-1])
                    cun =  int(load_list[6][:-1])
                    wis =  int(load_list[7][:-1])
                    current_location = load_list[8].strip()
                    maxhp, maxfocus, maxmana = get_resources(strength, cun, wis)
                    maxhp=int(maxhp)
                    maxfocus=int(maxfocus)
                    maxmana=int(maxmana)
                else:
                    print(['Corrupt save file, press enter to return to menu'])
                    input('#')
                    break
            except OSError:
                print_box(['Save file not found, press enter to return to menu'])
                input('#')
                break

            print_box([
                'Welcome back, are you ready to return to.. The pit?'
            ])
            dest =''
            dest = get_yes_no()
            if dest == 'Y':
                play = True
                menu = False
            elif dest == 'N':
                play = False
                menu = True

        elif choice == '3':
            clear()
            print('rules to be added later')
            input ('press enter to return to the menu')
            choice = ''
        elif choice == '4':
            quit()




    while play:
        clear()
        print_box([
            name.capitalize(),
            role.capitalize(),
            f'HP: {hp}/{maxhp}',
            f'Mana: {mana}/{maxmana}',
            f'Focus: {focus}/{maxfocus}',
            f'strength: {strength}',
            f'Cunning: {cun}',
            f'Wisdom: {wis}'
        ])    
        save()
        
        room = locations[current_location]
        paths = room.get('paths', {})
        print_box([room['description']])
        # if paths:
        #     print_box([
        #         f"{number}. {path['description']}"
        #         for number, path in room.get('paths,{}').items() 
        #         ])
        # else:
        #     print_box([
        #         'There is no way foward'
        #     ])
        paths = room.get('paths', {})

        print_box([
            f"{number}. {path['description']}"
            for number, path in paths.items()
        ] if paths else ["There are no obvious ways forward."])
        print_box(['Where do you go?'])
        choice = input('#')
        if choice in room['paths']:
            previous_location = current_location
            current_location = room['paths'][choice]['destination']
        else:
            print('That is not a valid option')
