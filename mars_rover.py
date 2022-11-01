def robot():   
    dirs = "NESW"                   # Directions Notation
    shifts=[(0,1),(1,0),(0,-1),(-1,0)] # delta vector for each direction
    # One letter function names corresponding to each robot direction
    r = lambda x, y, a: (x, y, (a + 1) % 4)
    l = lambda x, y, a: (x, y, (a - 1 + 4) % 4)
    f = lambda x, y, a: (x + shifts[a][0], y + shifts[a][1], a)

    print ("What is the Grid Size?")
    input()    # Ignore the grid size
    while 1:

        print ("What is the Robot initial position?")
        # parse initial position triplet
        x, y, dir = input().split() 
        pos = (int(x),int(y),dirs.find(dir))

        print ("How do you want your Robot to move?")
        # parse instructions
        robot_instruction = input().lower() 
        # Invoke the corresponding functions passing prev position
        for i in robot_instruction: pos = eval('%s%s' % (i, str(pos)))
        result = "OUTPUT:", pos[0], pos[1], dirs[pos[2]]
        print (result)
        return result

if __name__ == '__main__':
    robot()