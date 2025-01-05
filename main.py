import sys

# Display function
def display():
    for y in range(1, 9):

        for x in range(1, 9):

            global v_display_new

            # Displays chess symbol if there is a chess piece
            if str(l_x_trans[x]) + str(l_y_trans[y]) in l_white_pos:
                v_display_new = l_white_pos[str(l_x_trans[x]) + str(l_y_trans[y])]
                print(l_white_symbols[v_display_new] + " ", end = "")
            elif str(l_x_trans[x]) + str(l_y_trans[y]) in l_black_pos:
                v_display_new = l_black_pos[str(l_x_trans[x]) + str(l_y_trans[y])]
                print(l_black_symbols[v_display_new] + " ", end = "")
            else:
                v_display_new = "none"


            # If blank space dose checkerboard pattern
            if v_display_new == "none":
                if x % 2 == 0:
                    if y % 2 == 0:
                        print ("▱ ", end = "")
                    else:
                        print("▰ ", end="")
                else:
                    if y % 2 == 0:
                        print ("▰ ", end = "")
                    else:
                        print("▱ ", end="")


        print (end = "\n")

def check_valid(x, team):
    if len(x) == 2:
        if not x[0].isdigit() and x[1].isdigit():
            if str(x[0]) in ["a", "b", "c", "d", "e", "f", "g", "h"]:
                if int(str(x[1])) >= 1 and int(str(x[1])) <= 8:
                    if x in team:
                        return "valid"
                    else:
                        #print("error.001")
                        return "false"
                else:
                    #print("error.002")
                    return "false"
            else:
                #print("error.003")
                return "false"
        else:
            #print("error.004")
            return "false"
    else:
        #print("error.005")
        return "false"

# Transfers chess coords (a1) into coords (18) function
def transfer(xy, target):
    if xy == "x":
        for a, b in l_x_trans.items():
            if b == target:
                return a
    if xy == "y":
        for a, b in l_y_trans.items():
            if b == target:
                return a

# Finds all positions a chess piece can move to function
def check_position(new, type, pos, team, enemy):

    global l_white_pos
    global l_black_pos
    global a_valid_positions
    global v_checkenemy
    global v_bool
    global v_counter
    global v_position
    global empty

    a_valid_positions = []
    v_checkenemy = ""
    v_bool = False
    v_counter = 0
    v_position = ""

    # Gets chess piece
    if type == "Pawn":
        if team == l_white_pos:

            # Adds a valid position in front of it if there are no other chess pieces
            if not (str(pos[0]) + str(int(pos[1]) + 1)) in enemy and not (str(pos[0]) + str(int(pos[1]) + 1)) in team:
                if int(pos[1]) + 1 < 9:
                    a_valid_positions.append(str(pos[0]) + str(int(pos[1]) + 1))

            # Transfers the letter into a coord
            v_checkenemy = transfer("x", str(pos[0]))

            # Checks if enemy is in a position diagonal right to the chess piece
            if v_checkenemy + 1 < 9:
                if str(l_x_trans[int(v_checkenemy + 1)]) + str(int(pos[1]) + 1) in enemy:
                    a_valid_positions.append(str(l_x_trans[int(v_checkenemy + 1)]) + str(int(pos[1]) + 1))

            # Checks if enemy is in a position diagonal left to the chess piece
            if v_checkenemy - 1 > 0:
                if str(l_x_trans[int(v_checkenemy - 1)]) + str(int(pos[1]) + 1) in enemy:
                    a_valid_positions.append(str(l_x_trans[int(v_checkenemy - 1)]) + str(int(pos[1]) + 1))

            # If the new position is in the valid positions the function returns true
            if len(a_valid_positions) == 0:
                v_position = "None"

            if new in a_valid_positions:
                return "valid"
            else:
                return "false"

        elif team == l_black_pos:

            # Adds a valid position in front of it if there are no other chess pieces
            if not (str(pos[0]) + str(int(pos[1]) - 1)) in enemy and not (str(pos[0]) + str(int(pos[1]) - 1)) in team:
                if int(pos[1]) - 1 > 0:
                    a_valid_positions.append(str(pos[0]) + str(int(pos[1]) - 1))

            # Transfers the letter into a coord
            v_checkenemy = transfer("x", str(pos[0]))

            # Checks if enemy is in a position diagonal right to the chess piece
            if v_checkenemy + 1 < 9:
                if str(l_x_trans[int(v_checkenemy + 1)]) + str(int(pos[1]) - 1) in enemy:
                    a_valid_positions.append(str(l_x_trans[int(v_checkenemy + 1)]) + str(int(pos[1]) - 1))

            # Checks if enemy is in a position diagonal left to the chess piece
            if v_checkenemy - 1 > 0:
                if str(l_x_trans[int(v_checkenemy - 1)]) + str(int(pos[1]) - 1) in enemy:
                    a_valid_positions.append(str(l_x_trans[int(v_checkenemy - 1)]) + str(int(pos[1]) - 1))

            if len(a_valid_positions) == 0:
                v_position = "None"
            # If the new position is in the valid positions the function returns true
            if new in a_valid_positions:
                return "valid"
            else:
                return "false"

    if type == "Rook":


        # Checks in up direction
        while v_bool == False:
            v_counter += 1
            v_checkenemy = str(int(pos[1]) + v_counter)
            if not str(pos[0]) + str(v_checkenemy) in team and int(v_checkenemy) < 9:
                if not str(pos[0]) + str(v_checkenemy) in enemy:
                    a_valid_positions.append((str(pos[0]) + str(v_checkenemy)))
                else:
                    a_valid_positions.append((str(pos[0]) + str(v_checkenemy)))
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks in down direction
        while v_bool == False:
            v_counter += 1
            v_checkenemy = str(int(pos[1]) - v_counter)
            if not str(pos[0]) + str(v_checkenemy) in team and int(v_checkenemy) > 0:
                if not str(pos[0]) + str(v_checkenemy) in enemy:
                    a_valid_positions.append((str(pos[0]) + str(v_checkenemy)))
                else:
                    a_valid_positions.append((str(pos[0]) + str(v_checkenemy)))
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks in right direction
        while v_bool == False:
            v_counter +=1
            v_checkenemy = transfer("x", pos[0])
            v_checkenemy += v_counter
            if int(v_checkenemy) < 9:
                if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks in left direction
        while v_bool == False:
            v_counter += 1
            v_checkenemy = transfer("x", pos[0])
            v_checkenemy -= v_counter
            if int(v_checkenemy) > 0:
                if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        if len(a_valid_positions) == 0:
            v_position = "None"

        # If the new position is in the valid positions the function returns true
        if new in a_valid_positions:
            return "valid"
        else:
            return "false"

    if type == "Knight":

        # Checks upwards
        for counter in range(1, 3):
            v_checkenemy = int(pos[1]) + counter
            if v_checkenemy < 9:
                if not str(pos[0]) + str(v_checkenemy) in team:
                    empty = empty
                if counter == 2:
                    # Checks right
                    v_checkenemy = transfer("x", pos[0]) + 1
                    if v_checkenemy < 9:
                        v_checkenemy = l_x_trans[v_checkenemy]
                        if not str(v_checkenemy) + str(int(pos[1]) + counter) in team:
                            a_valid_positions.append(str(v_checkenemy) + str(int(pos[1]) + counter))
                    # Checks left
                    v_checkenemy = transfer("x", pos[0]) - 1
                    if v_checkenemy > 0:
                        v_checkenemy = l_x_trans[v_checkenemy]
                        if not str(v_checkenemy) + str(int(pos[1]) + counter) in team:
                            a_valid_positions.append(str(v_checkenemy) + str(int(pos[1]) + counter))

        # Checks downwards
        for counter in range(1,3):
            v_checkenemy = int(pos[1]) - counter
            if v_checkenemy > 0:
                if not str(pos[0]) + str(v_checkenemy) in team:
                    empty = empty
                if counter == 2:
                    # Checks right
                    v_checkenemy = transfer("x", pos[0]) + 1
                    if v_checkenemy < 9:
                        v_checkenemy = l_x_trans[v_checkenemy]
                        if not str(v_checkenemy) + str(int(pos[1]) - counter) in team:
                            a_valid_positions.append(str(v_checkenemy) + str(int(pos[1]) - counter))
                    # Checks left
                    v_checkenemy = transfer("x", pos[0]) - 1
                    if v_checkenemy > 0:
                        v_checkenemy = l_x_trans[v_checkenemy]
                        if not str(v_checkenemy) + str(int(pos[1]) - counter) in team:
                            a_valid_positions.append(str(v_checkenemy) + str(int(pos[1]) - counter))

        # Checks right
        for counter in range(1,3):
            v_checkenemy = transfer("x", pos[0]) + counter
            if v_checkenemy < 9:
                if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in team:
                    empty = empty
                if counter == 2:
                    # Checks up
                    if int(pos[1]) + 1 < 9:
                        if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + 1) in team:
                            a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + 1))
                    # Checks down
                    if int(pos[1]) - 1 > 0:
                        if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) - 1) in team:
                            a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) - 1))

        # Checks left
        for counter in range(1, 3):
            v_checkenemy = transfer("x", pos[0]) - counter
            if v_checkenemy > 0:
                if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in team:
                    empty = empty
                if counter == 2:
                    # Checks up
                    if int(pos[1]) + 1 < 9:
                        if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + 1) in team:
                            a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + 1))
                    # Checks down
                    if int(pos[1]) - 1 > 0:
                        if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) - 1) in team:
                            a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) - 1))


        if len(a_valid_positions) == 0:
            v_position = "None"

        # If the new position is in the valid positions the function returns true
        if new in a_valid_positions:
            return "valid"
        else:
            return "false"

    if type == "Bishop":

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks diagonal up right
        while v_bool == False:
            v_counter +=1
            v_checkenemy = transfer("x", pos[0]) + v_counter
            if v_checkenemy < 9 and int(pos[1]) + v_counter < 9:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks diagonal up left
        while v_bool == False:
            v_counter += 1
            v_checkenemy = transfer("x", pos[0]) - v_counter
            if v_checkenemy > 0 and int(pos[1]) + v_counter < 9:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks diagonal down right
        while v_bool == False:
            v_counter -= 1
            v_checkenemy = transfer("x", pos[0]) - v_counter
            if v_checkenemy < 9 and int(pos[1]) + v_counter > 0:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks diagonal down left
        while v_bool == False:
            v_counter -= 1
            v_checkenemy = transfer("x", pos[0]) + v_counter
            if v_checkenemy > 0 and int(pos[1]) + v_counter > 0:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        if len(a_valid_positions) == 0:
            v_position = "None"
        # If the new position is in the valid positions the function returns true
        if new in a_valid_positions:
            return "valid"
        else:
            return "false"

    if type == "Queen":

        # Checks in up direction
        while v_bool == False:
            v_counter += 1
            v_checkenemy = str(int(pos[1]) + v_counter)
            if not str(pos[0]) + str(v_checkenemy) in team and int(v_checkenemy) < 9:
                if not str(pos[0]) + str(v_checkenemy) in enemy:
                    a_valid_positions.append((str(pos[0]) + str(v_checkenemy)))
                else:
                    a_valid_positions.append((str(pos[0]) + str(v_checkenemy)))
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks in down direction
        while v_bool == False:
            v_counter += 1
            v_checkenemy = str(int(pos[1]) - v_counter)
            if not str(pos[0]) + str(v_checkenemy) in team and int(v_checkenemy) > 0:
                if not str(pos[0]) + str(v_checkenemy) in enemy:
                    a_valid_positions.append((str(pos[0]) + str(v_checkenemy)))
                else:
                    a_valid_positions.append((str(pos[0]) + str(v_checkenemy)))
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks in right direction
        while v_bool == False:
            v_counter += 1
            v_checkenemy = transfer("x", pos[0])
            v_checkenemy += v_counter
            if int(v_checkenemy) < 9:
                if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks in left direction
        while v_bool == False:
            v_counter += 1
            v_checkenemy = transfer("x", pos[0])
            v_checkenemy -= v_counter
            if int(v_checkenemy) > 0:
                if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks diagonal up right
        while v_bool == False:
            v_counter += 1
            v_checkenemy = transfer("x", pos[0]) + v_counter
            if v_checkenemy < 9 and int(pos[1]) + v_counter < 9:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks diagonal up left
        while v_bool == False:
            v_counter += 1
            v_checkenemy = transfer("x", pos[0]) - v_counter
            if v_checkenemy > 0 and int(pos[1]) + v_counter < 9:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks diagonal down right
        while v_bool == False:
            v_counter -= 1
            v_checkenemy = transfer("x", pos[0]) - v_counter
            if v_checkenemy < 9 and int(pos[1]) + v_counter > 0:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        v_bool = False
        v_counter = 0
        v_checkenemy = ""

        # Checks diagonal down left
        while v_bool == False:
            v_counter -= 1
            v_checkenemy = transfer("x", pos[0]) + v_counter
            if v_checkenemy > 0 and int(pos[1]) + v_counter > 0:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in team:
                    if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter) in enemy:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                    else:
                        a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + v_counter))
                        v_bool = True
                else:
                    v_bool = True
            else:
                v_bool = True

        if len(a_valid_positions) == 0:
            v_position = "None"

        # If the new position is in the valid positions the function returns true
        if new in a_valid_positions:
            return "valid"
        else:
            return "false"

    if type == "King":

        # Checks upwards
        if int(pos[1]) + 1 < 9:
            if not str(pos[0]) + str(int(pos[1]) + 1) in team:
                a_valid_positions.append(str(pos[0]) + str(int(pos[1]) + 1))

       # Checks downwards
        if int(pos[1]) - 1 > 0:
            if not str(pos[0]) + str(int(pos[1]) - 1) in team:
                a_valid_positions.append(str(pos[0]) + str(int(pos[1]) - 1))

        # Checks right
        v_checkenemy = transfer("x", pos[0]) + 1
        if v_checkenemy < 9:
            if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in team:
                a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))

        # Checks left
        v_checkenemy = transfer("x", pos[0]) - 1
        if v_checkenemy > 0:
            if not str(l_x_trans[v_checkenemy]) + str(pos[1]) in team:
                a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(pos[1]))

        # Checks up right
        v_checkenemy = transfer("x", pos[0]) + 1
        if int(pos[1]) + 1 < 9 and v_checkenemy < 9:
                if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + 1) in team:
                    a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + 1))

        # Checks down right
        v_checkenemy = transfer("x", pos[0]) + 1
        if int(pos[1]) - 1 > 0 and v_checkenemy < 9:
            if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) - 1) in team:
                a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) - 1))

        # Checks up left
        v_checkenemy = transfer("x", pos[0]) - 1
        if int(pos[1]) + 1 < 9 and v_checkenemy > 0:
            if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + 1) in team:
                a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) + 1))

        # Checks down left
        v_checkenemy = transfer("x", pos[0]) - 1
        if int(pos[1]) - 1 > 0 and v_checkenemy > 0:
            if not str(l_x_trans[v_checkenemy]) + str(int(pos[1]) - 1) in team:
                a_valid_positions.append(str(l_x_trans[v_checkenemy]) + str(int(pos[1]) - 1))

        if len(a_valid_positions) == 0:
            v_position = "None"

        # If the new position is in the valid positions the function returns true
        if new in a_valid_positions:
            return "valid"
        else:
            return "false"

def check_winner(team):
    global winner

    winner = ""

    if l_white_pos == team:
        for a, b in team.items():
            if b == "King":
                winner = "None"
        if not winner == "None":
            print (".B.L.A.C.K.V.I.C.T.O.R.Y.")
            sys.exit()

    winner = ""

    if l_black_pos == team:
        for a, b in team.items():
            if b == "King":
               winner = "None"
        if not winner == "None":
            print (".W.H.I.T.E.V.I.C.T.O.R.Y.")
            sys.exit()
# Arrays

def pawn(team):
    for a, b in team.items():
        if b == "Pawn":
            if a[1] == "8":
                team[a] = "Queen"

a_valid_positions = []

# Transfer lists
l_x_trans = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h"
}
l_y_trans = {
    1:"8",
    2:"7",
    3:"6",
    4:"5",
    5:"4",
    6:"3",
    7:"2",
    8:"1"
}
# Symbols
l_white_symbols = {
    "Pawn" : "♙",
    "Rook" : "♖",
    "Knight" : "♘",
    "Bishop" : "♗",
    "Queen" : "♕",
    "King" : "♔"
}
l_black_symbols = {
    "Pawn": "♟",
    "Rook": "♜",
    "Knight": "♞",
    "Bishop": "♝",
    "Queen": "♛",
    "King": "♚"
}
# Start positions
l_white_pos = {
    "a2" : "Pawn",
    "b2" : "Pawn",
    "c2" : "Pawn",
    "d2" : "Pawn",
    "e2" : "Pawn",
    "f2" : "Pawn",
    "g2" : "Pawn",
    "h2" : "Pawn",
    "a1" : "Rook",
    "b1" : "Knight",
    "c1" : "Bishop",
    "d1" : "Queen",
    "e1" : "King",
    "f1" : "Bishop",
    "g1" : "Knight",
    "h1" : "Rook"
}
l_black_pos = {
    "a7" : "Pawn",
    "b7" : "Pawn",
    "c7" : "Pawn",
    "d7" : "Pawn",
    "e7" : "Pawn",
    "f7" : "Pawn",
    "g7" : "Pawn",
    "h7" : "Pawn",
    "a8" : "Rook",
    "b8" : "Knight",
    "c8" : "Bishop",
    "d8" : "Queen",
    "e8" : "King",
    "f8" : "Bishop",
    "g8" : "Knight",
    "h8" : "Rook"
}

# Variables
v_display_new = ""
v_input = ""
v_get_pos = ""
v_new_pos = ""
v_piece = ""
v_checkenemy = ""
v_bool = ""
v_counter = 0
winner = ""
empty = ""
v_position = ""

print ("♝ ♞ ♟ C.H.E.S.S.G.A.M.E ♚ ♛ ♜ ")
while True:

    v_input = ""
    v_input = str(input())

    # Start of game
    if v_input == "start":

        while True:

            v_new_pos = ""
            v_get_pos = ""
            v_piece = ""
            display()

            # Start of white turn
            print ("WHITE TURN")
            # Gets valid position of chess piece
            while check_valid(v_get_pos, l_white_pos) == "false":
                v_get_pos = str(input("Enter position of chess piece to move :"))
                if v_get_pos == "check":
                    v_input = ""
                    v_input = str(input("Enter coord to check :"))
                    if v_input in l_white_pos:
                        print (l_white_pos[v_input])
                    elif v_input in l_black_pos:
                        print (l_black_pos[v_input])
                    else:
                        print ("Error")

                elif check_valid(v_get_pos, l_white_pos) == "false":
                    print("Error, position not valid")
                else:
                    v_piece = l_white_pos[v_get_pos]
                    empty = check_position(v_new_pos, v_piece, v_get_pos, l_white_pos, l_black_pos)
                    while v_position == "None":
                        empty = check_position(v_new_pos, v_piece, v_get_pos, l_white_pos, l_black_pos)
                        if v_position == "None":
                            print("Error, piece has no positions")
                            v_get_pos = str(input("Enter position of chess piece to move :"))
                            v_piece = l_white_pos[v_get_pos]


            # Gets type of chess piece
            v_piece = l_white_pos[v_get_pos]


            # Gets next position of chess piece
            while check_position(v_new_pos, v_piece, v_get_pos, l_white_pos, l_black_pos) == "false":
                v_new_pos = str(input("Enter position for chess piece to move to :"))
                if not v_new_pos == "check":
                    if check_position(v_new_pos, v_piece, v_get_pos, l_white_pos, l_black_pos) == "false":
                        print("Error, position not valid")
                else:
                    print(a_valid_positions)

            del l_white_pos[v_get_pos]
            if v_new_pos in l_black_pos:
                del l_black_pos[v_new_pos]
            l_white_pos[v_new_pos] = v_piece
            check_winner(l_black_pos)
            pawn(l_white_pos)

            v_position = ""
            v_new_pos = ""
            v_get_pos = ""
            v_piece = ""
            display()


            # Start of black turn
            print ("BLACK TURN")

            while check_valid(v_get_pos, l_black_pos) == "false":
                v_get_pos = str(input("Enter position of chess piece to move :"))
                if v_get_pos == "check":
                    v_input = ""
                    v_input = str(input("Enter coord to check :"))
                    if v_input in l_white_pos:
                        print (l_white_pos[v_input])
                    elif v_input in l_black_pos:
                        print (l_black_pos[v_input])
                    else:
                        print ("Error")

                elif check_valid(v_get_pos, l_black_pos) == "false":
                    print("Error, position not valid")
                else:
                    v_piece = l_black_pos[v_get_pos]
                    empty = check_position(v_new_pos, v_piece, v_get_pos, l_black_pos, l_white_pos)
                    while v_position == "None":
                        empty = check_position(v_new_pos, v_piece, v_get_pos, l_black_pos, l_white_pos)
                        if v_position == "None":
                            print("Error, piece has no positions")
                            v_get_pos = str(input("Enter position of chess piece to move :"))
                            v_piece = l_black_pos[v_get_pos]

            # Gets type of chess piece
            v_piece = l_black_pos[v_get_pos]


            # Gets next position of chess piece
            while check_position(v_new_pos, v_piece, v_get_pos, l_black_pos, l_white_pos) == "false":

                v_new_pos = str(input("Enter position for chess piece to move to :"))
                if not v_new_pos == "check":
                    if check_position(v_new_pos, v_piece, v_get_pos, l_black_pos, l_white_pos) == "false":
                        print("Error, position not valid")
                else:
                    print(a_valid_positions)

            del l_black_pos[v_get_pos]
            if v_new_pos in l_white_pos:
                del l_white_pos[v_new_pos]
            l_black_pos[v_new_pos] = v_piece
            check_winner(l_white_pos)
            pawn(l_black_pos)
