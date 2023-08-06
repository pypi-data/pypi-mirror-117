def oddOrEven():
    import random

    comp_possiblities = [number for number in range(1, 7)]


    def select():
        inp = input('Do you wanna be odd or even(o/e): ')

        bat = False
        selection = random.choice(['o', 'e'])
        if inp == selection:
            inp=input('Do you wanna bat first y/n?: ')
            inp=inp.lower()
            if inp=='y':
                bat=True
        else:
          selection = random.choice(['bat', 'ball'])
          if selection=='ball':bat=True
          print('Computer won the toss and chose to',selection)


        return bat


    def bat_userFirst():
        state = True
        score = 0
        while state:
            computer = random.choice(comp_possiblities)
            try:
                inp = int(input('Enter the number: '))
                if inp <= 0 or inp >= 7:
                    print('Sorry,invalid number.You lose')
                    state=False

                else:
                    if computer == inp:
                        state = False
                        print('Bowled out!!!')
                    else:
                        print('Computer selected',computer)
                        score += inp
                        print('Total runs: ',score)
                        print('')

            except Exception as e:
                print('Invalid entry you lose')
                state = False

        return score
    def bat_userSecond(target):
        state = True
        score = 0

        while state:

                computer = random.choice(comp_possiblities)
                try:
                    inp = int(input('Enter the number: '))
                    if inp <= 0 or inp >= 7:
                        print('Sorry,invalid number.You lose')
                        state=False

                    else:
                        if computer == inp:
                            state = False
                            print('Bowled out!!!')
                        else:
                            print('Computer selected',computer)
                            score += inp
                            print('Total runs:',score,' Target to win',target+1)
                            print('')
                            if score>=target+1:
                                state=False

                except Exception as e:
                    print('Invalid entry you lose')
                    state = False
                    score=None

        return score




    def ball_userFirst():
        state = True
        score = 0
        while state:
            computer = random.choice(comp_possiblities)
            try:
                inp = int(input('Enter the number: '))
                if inp <= 0 or inp >= 7:
                    print('Sorry,invalid number.You lose')
                    state=False

                else:
                    if computer == inp:
                        state = False
                        print('You bowled out computer!!!')
                    else:
                        print('Computer selected',computer)
                        score += computer
                        print('Total runs for computer: ',score)
                        print('')

            except Exception as e:
                print('Invalid entry you lose')
                state = False
                score=None

        return score
    def ball_userSecond(target):
        state = True
        score = 0

        while state:

                computer = random.choice(comp_possiblities)
                try:
                    inp = int(input('Enter the number: '))
                    if inp <= 0 or inp >= 7:
                        print('Sorry,invalid number.You lose')
                        state=False

                    else:
                        if computer == inp:
                            state = False
                            print('You bowled out computer!!!')
                        else:
                            print('Computer selected',computer)
                            score += computer
                            print('Total runs for computer:',score,' Target for computer is ',target+1)
                            print('')
                            if score>=target+1:
                                state=False

                except Exception as e:
                    print('Invalid entry you lose')
                    state = False

        return score



    while True:
        print('''RULES
        -If invalid entry in batting or balling,you lose
        -If invalid entry for odd or even selection,Computer wins the toss''')
        win=select()
        if win==True:
            print('You are batting first....Atb...')
            score=bat_userFirst()
            if score is not None:
                print('')
                print('Now lets ball for computer.....')
                print('Target for computer', score)
                print('')
                score1=ball_userSecond(score)
                if score1 > score:
                    print('You lost')
                elif score1 < score:
                    print('You won')
                else:
                    print('You tied')
        else:
          print('You are balling first....Atb...')
          score=ball_userFirst()
          if score is not None:
              print('')
              print('Now lets bat....Atb...')
              print('Target for you',score)
              print('')
              score1=bat_userSecond(score)
              if score1<score:
                  print('You lost')
              elif score1>score:
                print('You won')
              else:
                print('You tied')

        print('')
