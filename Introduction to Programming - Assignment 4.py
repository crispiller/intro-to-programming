##### 1. This is an exercise about reading and using _documentation_.
##### Here is a brief documentation on Python's built-in `print`
##### procedure (for Python 3). After reading this, you can try
##### and improve your board-printing function.

## The two oponents, represented by numbers.
RED = 0
BLACK = 1

## Initial setup of the board:
points_pieces = [2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2]
points_colour = [BLACK, 0, 0, 0, 0, RED, 0, RED, 0, 0, 0, BLACK, RED, 0, 0, 0, BLACK, 0, BLACK, 0, 0, 0, 0, RED]

## the bar, where checkers can bear off. First element is RED and second element
## is BLACK.
bar = [0, 0]

## Specify RED and BLACK home:
RED_home_pieces = points_pieces[0:6]
RED_home_colour = points_colour[0:6]

BLACK_home_pieces = points_pieces[18:24]
BLACK_home_colour = points_colour[18:24]

## First move of a player, collecting their colour, starting position and dice
## roll:
colour = int(input("Your colour (RED = 0, BLACK = 1): "))
start_pos = int(input("Your starting point (0,...,23): "))

## dice roll function, which can be 'called' or 'invoked' at any time:
def dice_roll():
    roll = int(input("Roll your dice and enter the number you got (1,...,6): "))
    while roll > 6:
        print("You must enter a valid number!")
        roll = int(input("Please write down your roll: "))
    print ("Great job! You rolled a ", roll)

dice_roll()

## Instructions as to what the program should do:
def move():
    if colour == RED and points_pieces[start_pos] > 0 and\
    points_colour[start_pos] == RED:
        end_pos = start_pos - roll
    
        points_pieces[start_pos] = points_pieces[start_pos] - 1
        points_colour[start_pos] = colour
    
        points_pieces[end_pos] = points_pieces[end_pos] + 1
        points_colour[end_pos] = colour

    elif colour == BLACK and points_pieces[start_pos] > 0 and\
    points_colour[start_pos] == BLACK:
        end_pos = start_pos + roll
    
        points_pieces[start_pos] = points_pieces[start_pos] - 1
        points_colour[start_pos] = colour
    
        points_pieces[end_pos] = points_pieces[end_pos] + 1
        points_colour[end_pos] = colour

move()

##### BEGINING: Teacher's solution for drawing the board implemented #####
## Strings for drawing the board:
colours = ["", ""]
colours[RED] = "R"
colours[BLACK] = "B"

## To print each point:
def print_point(checkers_number, checkers_colour):
    if checkers_number == 0:
        print( " 0 ", end="" )
    elif checkers_number < 10:         # one-digit number
        ## add extra space before:
        print( " ", checkers_number, checkers_colour, sep="", end="" )
    else:                       # two-digit number
        print( checkers_number, checkers_colour, sep="", end="" )

## Printing the board:
def print_board(points_pieces, points_colour):
    ## Add a space between the two columns
    space = "        "
    ## Printing a total of 12 rows, with two points each, making the total of 24:
    for i in range(12):
        ## Number of checkers at the two points
        column1 = points_pieces[11 - i] ## decreasing in number
        column2 = points_pieces[12 + i] ## increasing in number
        print_point(column1, colours[points_colour[11 - i]])
        print(space, end="" )
        print_point(column2, colours[points_colour[12 + i]])
        ## Always add a new line at the end:
        print()
print_board(points_pieces, points_colour)

##### END: Teacher's solution for drawing the board implemented #####

##### 2. Define some very simple functions (unrelated to backgammon).

## Write a function `largest( lst )`, which returns the largest
## integer in the list `lst`.

a = int(input("Please enter your favorite number: "))
print ("Your favourite number is: ", a)
b = int(input("Please enter the day you were born: "))
print ("You were born on the following day: ",  b)
c = int(input("Please enter your age: "))
print ("You are ", c, "years old")
lst = (a, b, c)
def largest(lst):
    largest = max(lst)
    print(largest)
largest(lst)

## Write a function `insert( lst, element, position, number_of_important )`,
## which inserts `element` into the list `lst` at `position` (so that
## the `position`th member of the list `lst` should be `element`
## afterwards). Both `position` and `number_of_important` are
## guaranteed to be smaller than the length of the list
## (which we can write as `len( lst )` in Python).
## The first `number_of_important` elements (the "important" ones)
##have to be preserved, i.e., shifted "to the right" in the list.
## For example, if the value of `l` is `[10, 20, 30, 40]`, then
## after executing `insert( l, 100, 2, 3 )`, `l` must have the
## value `[10, 20, 100, 30]`. Since the number of "important"
## elements is `3` here, we have to preserve the first three
## members of `l` (i.e., `10`, `20` and `30`). The member `40`
## is lost, but we don't care, because it is not among the
## "important" members.

def insert (lst, element, position, number_of_important):
## unsuccessful attempt at having a loop to check the validity of position and
## number_of_important:
    ## while position and number_of_important > len(lst):
        ## except ValueError:
            ## print("position and number_of_important must be smaller than length of lst")
            ## just for the sake of the exercise, we're asking for the user to input
            ## these numbers
            ## position = int(input("Position: ")
            ## number_of_important= int(input("Number of important ")
    ## defining which part of the list should be kept
    end = number_of_important
    ## new list, with only the important elements:
    lst = lst[0:end]
    ## Inserting the given element at the given index in the list:
    ## list.insert(index, obj)
    lst.insert(position, element)
    print("Final list: ", lst)
lst = [1, 2, 3, 4, 5]
insert(lst, 7, 2, 3)

## Write a function that sorts a list (with integer elements):
## `my_sort( list1, list2, size )`, where `list1` and `list2` are
## of the same size, `size`. The first argument is the list
## to be sorted, `list2` will contain its sorted version (what
## it contains at the outset is irrelevant). The algorithm is
## as follows: Go through the elements of `list1`, and insert
## them one by one in `list2` so that wherever you insert an
## element in `list2`, it must not be followed by any smaller
## number in the end. (Of course, you can use the previous
## function, `insert()` for this.)

def my_sort(list1, list2, size)
    ## make sure both lists are equal
    len(list1) = len(list2)
    ## sorting List2
    list2.sort()
    ## loop to insert objects from list2 into list1
    for elements in list1(range()):
        position = ?
        list2.insert(position, elements)

##### 3. Define various utility functions.

## A function `opponent( player )`. The argument is either RED or
## BLACK, the function returns the integer corresponding to the
## other player.

def opponent_player():
    player = int(input("Which player are you? (RED = 0, BLACK = 1): ")
    if player is 0:
        opponent = 1
    else:
        opponent = 0
    print("Your oponent is: ", opponent)

opponent_player()       

## A function `ask_point( prompt )`. The argument must be a
## string that is printed for asking the user to enter the index
## of a point. The function returns an integer that is at least
## 1 and at most 24. So the function must both catch the error
## if the string entered does not correspond to an integer and
## make sure the integer is in the right range.

def ask_point():
    point = int(input("Your starting point (0,...,23): "))
    while point > 24 or point < 0:
        print("You must enter a valid point!")
        point = int(input("Please write your point (0,...,23): "))
    print ("You chose point ", point)
ask_point()

## A function `can_bear_off( colours, pieces, bar, player )`.
## The first parameter refers to the memory area where we
## store a list that specifies the colour of each point
## (as we had for the symbol `point_colours` earlier);
## the second parameter refers to the similar list specifying
## the number of checkers at each point (as we had for the
## symbol `point_pieces` earlier).
## The third parameter is a two-element list specifying the
## number of red and black checkers that have been hit (and have
## not yet re-entered the board).
## The last argument is either RED or BLACK.
## The function returns True if the given player can bear off
## (which means that player has no checkers on the bar or anywhere
## on the board that is not their "home", i.e., the last 6 points
## that end their trajectory).

def can_bear_off(colours, pieces, bar, player):
    if player = RED:
        if bar[0] = 0 and (sum(pieces[7:24) = 0:
            print("You can bear off!")
        else:
            print("You cannot bear off just yet")
    else:
        if bar[1] = 0 and (sum(pieces[0:18) = 0:
            print("You can bear off!")
        else:
            print("You cannot bear off just yet")
