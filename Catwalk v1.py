import random, os

def main():
    valid_moves = []
    invalid_moves = []
    
    while True:
        os.system('cls')
        title()
        print("\033[0;32m[INSTRUCTIONS]:\033[0m Choose your setting:")
        # For the Automatic and Manual Setting
        setting = int(input("Automatic (1) or Not (2) \033[1;33m->\033[0m "))

        if setting not in [1, 2]:
            print("\033[0;31m[ERROR]:\033[0m Invalid Choice.")
            exit(1)

        
        valid_moves, invalid_moves = traverse(setting, valid_moves, invalid_moves)

def traverse(setting, valid_moves, invalid_moves):
    state = 0
    rem_moves = 5
    separator = "-"

    while rem_moves > 0:
        print(f"{separator * 35}\n")
        state, rem_moves, valid_moves, invalid_moves = state_machine(state, setting, rem_moves, valid_moves, invalid_moves)

    # Congratulatory Messages & Additional Information
    print(f"After \033[0;33m{len(invalid_moves)}\033[0m invalid moves, you finally reached your destination!")
    print(f"Valid moves are: {valid_moves}")
    print(f"Invalid moves are: {invalid_moves}\n")
    
    retry = int(input("Do you want to try again? (With Updated Data Set)\n1 - YES | 2 - NO \033[1;33m->\033[0m "))
    if retry != 1:
        exit(0)

    return valid_moves, []

def state_machine(state, setting, moves, val, inv):
    match state:
        case 0:
            state = 1
            print("Welcome! You are now outside the PUP.\n")
        
        case 1:
            success_mes(state-1, 2)
            choices = ["Entrance Gate", "Go Another Way"]
            decision = dir_input(setting, state, choices, val, inv)
            if  decision == 1:
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1, 1)
                state = 2
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)
        
        case 2:
            success_mes(state-1, 2)
            choices = ["Move Forward to Obelisk", "Go Another Way"]
            decision = dir_input(setting, state, choices, val, inv)
            if  decision == 1:
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1, 1)
                state = 3
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)
        
        case 3:
            success_mes(state-1, 2)
            choices = ["Follow Curbside of the Obelisk", "Go Another Way"]
            decision = dir_input(setting, state, choices, val, inv)
            if  decision == 1:
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1, 1)
                state = 4
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)
        
        case 4:
            success_mes(state-1, 2)
            choices  = ["Walk Forward", "Go Another Way"]
            decision = dir_input(setting, state, choices, val, inv)
            if  decision == 1:
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1, 1)
                state = 5
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)

        case 5:
            success_mes(state-1, 2)
            moves -= 1

    return state, moves, val, inv

# Title Image
def title():
    print(f"----------------------------------------------| ~ The pathway to ~ |-------------------------------------------------------")
    print(f"                                               ,--,                                                                        ")
    print(f",-.----.                 ,-.----.           ,---.'|                                  ,----..       ,----..            ,--. ")
    print(f"\    /  \                \    /  \          |   | :      ,---,         ,----..      /   /   \     /   /   \         ,--.'| ")
    print(f"|   :    \          ,--, |   :    \         :   : |     '  .' \       /   /   \    /   .     :   /   .     :    ,--,:  : | ")
    print(f"|   |  .\ :       ,'_ /| |   |  .\ :        |   ' :    /  ;    '.    |   :     :  .   /   ;.  \ .   /   ;.  \,`--.'`|  ' : ")
    print(f".   :  |: |  .--. |  | : .   :  |: |        ;   ; '   :  :       \   .   |  ;. / .   ;   /  ` ;.   ;   /  ` ;|   :  :  | | ")
    print(f"|   |   \ :,'_ /| :  . | |   |   \ :        '   | |__ :  |   /\   \  .   ; /--`  ;   |  ; \ ; |;   |  ; \ ; |:   |   \ | : ")
    print(f"|   : .   /|  ' | |  . . |   : .   /        |   | :.'||  :  ' ;.   : ;   | ;  __ |   :  | ; | '|   :  | ; | '|   : '  '; | ")
    print(f";   | |`-' |  | ' |  | | ;   | |`-'         '   :    ;|  |  ;/  \   \|   : |.' .'.   |  ' ' ' :.   |  ' ' ' :'   ' ;.    ; ")
    print(f"|   | ;    :  | | :  ' ; |   | ;            |   |  ./ '  :  | \  \ ,'.   | '_.' :'   ;  \; /  |'   ;  \; /  ||   | | \   | ")
    print(f":   ' |    |  ; ' |  | ' :   ' |            ;   : ;   |  |  '  '--'  '   ; : \  | \   \  ',  /  \   \  ',  / '   : |  ; .' ")
    print(f":   : :    :  | : ;  ; | :   : :            |   ,/    |  :  :        '   | '/  .'  ;   :    /    ;   :    /  |   | '`--'   ")
    print(f"|   | :    '  :  `--'   \|   | :            '---'     |  | ,'        |   :    /     \   \ .'      \   \ .'   '   : |       ")
    print(f"`---'.|    :  ,      .-./`---'.|                      `--''           \   \ .'       `---`         `---`     ;   |.'       ")
    print("  `---`     `--`----'      `---`                                       `---`                                 '---'          ")
    print(f"---------------------------------------------------------------------------------------------------------------------------")

# Direction Input
def dir_input(setting, state, choices, valid, invalid):
    # If true, let the computer decide.
    if setting == 1:
        decision = ai(state, valid, invalid)
        print(f"[CHOICES]: 1 - {choices[0]} | 2 - {choices[1]}")
        print(f"AI chose {decision} - {choices[decision-1]}.")

    # If false, manually input decision.
    elif setting == 2:
        decision = int(input(f"\033[0;32mWhat do you want to do?\033[0m\n1 - {choices[0]} | 2 - {choices[1]}\nEnter Here \033[1;33m->\033[0m "))

    return decision

# Display success message
def success_mes(state, mess_type):
    mess = ["You entered the Entrance Gate.", "You moved forward to reach the Obelisk.", "You followed the Curbside of the Obelisk.", 
            "You walked forward."]
    
    percept = ["Catwalk", "Obelisk", "PUP Wall Entrance", "Garden"]

    succ_mess = ["You arrived at PUP Main Gate!", "You arrived at the Catwalk!", "You arrived at the Obelisk!", 
                 "You arrived at the PUP Wall Entrance!", "You arrived at the PUP Lagoon!"]

    if mess_type == 1:
        print(f"\033[0;32m[ACTION]:\033[0m {mess[state]}")
        print(f"\033[0;33m[PERCEPT]:\033[0m {percept[state]}\n")
    
    elif mess_type == 2:
        print(f"\033[0;34m[SUCCESS]:\033[0m {succ_mess[state]}")

# Reset the remaining moves
def reset(last_state, last_move, inv):
    inv_move = [last_state, last_move]
    inv.append(inv_move)
    print("\033[0;31m[WARNING]:\033[0m Invalid Move. You got lost. You returned to the beginning.")
    print(f"\033[0;33m[PERCEPT]:\033[0m Lost\n")

    return 1, 5, inv

# Automatic Mode
def ai(curr_state, val, inv):
    making_decision = True
    dec_ret = None
    decisions = [1, 2]

    # Checks for previously valid moves
    if len(val) > 0:
        for i in val:
            if curr_state in i:
                dec_ret = i[1]
    
    # Thinks for the next right move
    if dec_ret == None:
        while making_decision:
            dec_idx = random.randint(0, len(decisions)-1)
            dec_ret = decisions[dec_idx]

            # If the next move is in invalid move, think again.
            if [curr_state, dec_ret] not in inv:
                making_decision = False
            
            else:
                decisions.remove(dec_ret)

    # Return the decision (dec)
    return dec_ret

if __name__ == "__main__":
    main()