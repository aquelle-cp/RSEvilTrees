import datetime

# Get world and time until tree from user
# Store as world and time the tree will be active
# Show list of worlds with time until trees in each
# Sort those worlds by closest time til tree
# Delete any records with trees past 10 mins old
# Let the user remove worlds that have been checked

# Help - prints the help message
def print_help():
    print('commands:')
    print('\thelp\t\t\tprints this help message')
    print('\tshow\t\t\tshows list of trees and times')
    print('\t[world] [time(mins)]\tstores world number and time until tree')
    print('\tdel [world]\t\tremoves the record for the given world')
    print('\tquit\t\t\texits program')

# Entry - stores world number and time until tree (format [world] [time(mins)])
def entry(cmd, trees):
    # Make sure both world and time are numbers
    if (not cmd[0].isdigit()) or (not cmd[1].isdigit()):
        print('world and time must both be integers')
        return

    world = int(cmd[0])

    # Check if there's already a record for the world; if there is, delete it
    for t in trees:
        if t['world'] == world:
            trees.remove(t)
            break

    time = datetime.datetime.now() + datetime.timedelta(minutes=int(cmd[1]))
    data = {'world': world, 'time': time}
    trees.append(data)

    return trees

# Show - shows list of trees and times
def show(trees):
    if len(trees) == 0:
        print('no recent records')
        return

    # Clean the list of any trees older than 10 mins
    # for t in trees:
    #     if t['time'] < datetime.datetime.now() - datetime.timedelta(minutes=10):
    #         trees.remove(t)\
    if trees:
        trees = [t for t in trees if t['time'] >= datetime.datetime.now() - datetime.timedelta(minutes=10)]

    sorted_trees = sorted(trees, key=lambda d: d['time'])
    for t in sorted_trees:
        mins_til_tree = round((t['time'] - datetime.datetime.now()).total_seconds() / 60)
        print('w' + str(t['world']) + ' ' + str(mins_til_tree) + ' mins')

## Action loop - parses the input command and executes the appropriate function
trees = []
cont = True
while (cont):
    i = input('> ')
    cmd = i.split(' ')

    if cmd[0] == 'h' or cmd[0] == 'help':
        print_help()
    elif cmd[0] == 'q' or cmd[0] == 'quit':
        cont = False;
    elif cmd[0] == 's' or cmd[0] == 'show':
        show(trees)
    elif cmd[0] == 'del' and len(cmd) == 2:
        print('todo: del')
    elif len(cmd) == 2:
        trees = entry(cmd, trees)
    else:
        print('invalid command - see \'help\' for valid commands')
