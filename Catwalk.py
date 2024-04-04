import random

# Main Function
def main():
    state = 0
    decision = None
    rem_moves = 6
    valid_moves = []
    invalid_moves = []

    print("\n\033[1;34m| | ~ The pathway to PUP Lagoon ~ | |\n\033[0m")
    print("\033[0;32m[INSTRUCTIONS]:\033[0m Choose your setting:")
    # For the Automatic and Manual Setting
    setting = int(input("Automatic (1) or Not (2) \033[1;33m->\033[0m "))
    
    if setting not in [1, 2]:
        print("\033[0;31m[ERROR]:\033[0m Invalid Choice.")
        exit(1)

    while rem_moves > 0:
        # If true, let the computer decide.
        if setting == 1:
            if state not in [0, 6]:
                decision = ai(state, valid_moves, invalid_moves)
                print(f"AI chose {decision}.")

        # If false, manually input decision.
        elif setting == 2:
            if state not in [0, 6]:
                decision = input(f"\033[0;32mWhich direction do you want to go?\033[0m\n[gate, catwalk, obelisk, pup wall entrance, move forward]\nEnter Here \033[1;33m->\033[0m ")

        state, rem_moves, valid_moves, invalid_moves = state_machine(state, decision, rem_moves, valid_moves, invalid_moves)
    
    # Congratulatory Messages & Statistics
    print(f"After \033[0;33m{len(invalid_moves)}\033[0m invalid moves, you finally reached your destination!")
    print(f"Valid moves are: {valid_moves}")
    print(f"Invalid moves are: {invalid_moves}")

# State Machine
def state_machine(state, decision, moves, val, inv):
    match state:
        case 0:
            state = 1
            print("\nWelcome! You are now outside the PUP.\n")
        
        case 1:
            if decision == "gate":
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1)
                state = 2
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)
        
        case 2:
            if decision == "catwalk":
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1)
                state = 3
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)
        
        case 3:
            if decision == "obelisk":
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1)
                state = 4
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)
        
        case 4:
            if decision == "pup wall entrance":
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1)
                state = 5
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)
        
        case 5:
            if decision == "move forward":
                if [state, decision] not in val:
                    val.append([state, decision])

                success_mes(state-1)
                state = 6
                moves -= 1
            
            else:
                state, moves, inv = reset(state, decision, inv)
        
        case 6:
            success_mes(state-1)
            moves -= 1
    
    return state, moves, val, inv

# Display success message
def success_mes(state):
    mess = ["You approached the gate.\n","You traversed through the catwalk.\n", "You went to the obelisk.\n",
            "You walked forward the PUP wall entrance.\n", "You moved forward.\n", "You arrived at the PUP Lagoon!"]

    print(f"\033[0;32m[ACTION]:\033[0m {mess[state]}")

# Reset the remaining moves
def reset(last_state, last_move, inv):
    inv_move = [last_state, last_move]
    inv.append(inv_move)
    print("\033[0;31m[WARNING]:\033[0m Invalid Move. You got lost. You returned to the beginning.\n")

    return 1, 5, inv

def ai(curr_state, val, inv):
    making_decision = True
    dec_ret = None
    decisions = ["gate", "catwalk", "obelisk", "pup wall entrance", "move forward"]

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