import random

def main():
    state = 0
    rem_moves = 5
    valid_moves = []
    invalid_moves = []

    title()
    print("\033[0;32m[INSTRUCTIONS]:\033[0m Choose your setting:")
    # For the Automatic and Manual Setting
    setting = int(input("Automatic (1) or Not (2) \033[1;33m->\033[0m "))

    if setting not in [1, 2]:
        print("\033[0;31m[ERROR]:\033[0m Invalid Choice.")
        exit(1)

    while rem_moves > 0:
        state, rem_moves, valid_moves, invalid_moves = state_machine(state, setting, rem_moves, valid_moves, invalid_moves)

    # Congratulatory Messages & Additional Information
    print(f"After \033[0;33m{len(invalid_moves)}\033[0m invalid moves, you finally reached your destination!")
    print(f"Valid moves are: {valid_moves}")
    print(f"Invalid moves are: {invalid_moves}")


def state_machine(state, setting, moves, val, inv):
    match state:
        case 0:
            state = 1
            print("\nWelcome! You are now outside the PUP.\n")
        
        case 1:
            success_mes(state-1, 2)
            choices = "1 - Enter Entrance Gate | 2 - Go Another Way"
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
            choices = "1 - Move Forward to Obelisk | 2 - Go Another Way"
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
            choices = "1 - Follow Curbside of the Obelisk | 2 - Go Another Way"
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
            choices = "1 - Walk Forward | 2 - Go Another Way"
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
        print(f"AI chose {decision}.")

    # If false, manually input decision.
    elif setting == 2:
        decision = int(input(f"\033[0;32mWhat do you want to do?\033[0m\n{choices}\nEnter Here \033[1;33m->\033[0m "))

    return decision

# Display success message
def success_mes(state, mess_type):
    mess = ["You entered the Entrance Gate.\n", "You moved forward to reach the Obelisk.\n", "You followed the Curbside of the Obelisk.\n", 
            "You walked forward.\n"]

    succ_mess = ["You arrived at PUP Main Gate!", "You arrived at the Catwalk!", "You arrived at the Obelisk!", 
                 "You arrived at the PUP Wall Entrance!", "You arrived at the PUP Lagoon!"]

    if mess_type == 1:
        print(f"\033[0;32m[ACTION]:\033[0m {mess[state]}")
    
    elif mess_type == 2:
        print(f"\033[0;34m[SUCCESS]:\033[0m {succ_mess[state]}")

# Reset the remaining moves
def reset(last_state, last_move, inv):
    inv_move = [last_state, last_move]
    inv.append(inv_move)
    print("\033[0;31m[WARNING]:\033[0m Invalid Move. You got lost. You returned to the beginning.\n")

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

main()