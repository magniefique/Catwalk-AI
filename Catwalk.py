import random

def main():
    state = 0
    decision = None
    rem_moves = 5
    decisions = ["gate", "catwalk", "obelisk", "pup wall entrance", "move forward"]
    valid_moves = []
    invalid_moves = []

    setting = int(input("Automatic (1) or Not (2): "))
    
    if setting not in [1, 2]:
        print("Invalid Choice.")
        exit(1)

    while rem_moves > 0:
        if setting == 1:
            decision = ai(state, decisions, valid_moves, invalid_moves)
            print(f"AI chose {decision}.")

        elif setting == 2:
            if state != 0:
                decision = input("Where do you wanna go, love?: ")

        state, rem_moves, valid_moves, invalid_moves = state_machine(state, decision, rem_moves, valid_moves, invalid_moves)
    
    print(f"After {len(invalid_moves)} invalid moves, you finally reached your destination!")
    print(f"Valid moves are: {valid_moves}")
    print(f"Invalid moves are: {invalid_moves}")

# Cat Machine
def state_machine(state, decision, moves, val, inv):
    match state:
        case 0:
            state = 1
            print("Welcome, Cat! You are now outside the PUP.\n")
        
        case 1:
            if decision == "gate":
                if [state, decision] not in val:
                    val.append([state, decision])

                state = 2
                moves -= 1
                print("You approached the gate.\n")
            
            else:
                state, moves, inv = reset(state, decision, inv)
                print("Invalid Move, you returned in the beginning.\n")
        
        case 2:
            if decision == "catwalk":
                if [state, decision] not in val:
                    val.append([state, decision])

                state = 3
                moves -= 1
                print("You catwalk-ed. (PUN INTENDED)\n")
            
            else:
                state, moves, inv = reset(state, decision, inv)
                print("Invalid Move, you returned in the beginning.\n")
        
        case 3:
            if decision == "obelisk":
                if [state, decision] not in val:
                    val.append([state, decision])

                state = 4
                moves -= 1
                print("You went to the obelisk.\n")
            
            else:
                state, moves, inv = reset(state, decision, inv)
                print("Invalid Move, you returned in the beginning.\n")
        
        case 4:
            if decision == "pup wall entrance":
                if [state, decision] not in val:
                    val.append([state, decision])

                state = 5
                moves -= 1
                print("You walked forward the PUP wall entrance\n")
            
            else:
                state, moves, inv = reset(state, decision, inv)
                print("Invalid Move, you returned in the beginning.\n")
        
        case 5:
            if decision == "move forward":
                if [state, decision] not in val:
                    val.append([state, decision])

                state = 6
                moves -= 1
                print("You walked forward the PUP wall entrance\n")
            
            else:
                state, moves, inv = reset(state, decision, inv)
                print("Invalid Move, you returned in the beginning.\n")
    
    return state, moves, val, inv

# Reset the remaining moves
def reset(last_state, last_move, inv):
    inv_move = [last_state, last_move]
    inv.append(inv_move)

    return 1, 5, inv

def ai(curr_state, decisions, val, inv):
    making_decision = True
    dec_ret = None

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
            if [curr_state, dec_ret] in inv:
                pass

            else:
                making_decision = False

    # Return the decision (dec)
    return dec_ret

if __name__ == "__main__":
    main()   