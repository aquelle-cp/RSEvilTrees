# eviltrees.py
A simple command line tool to track the Evil Tree activity in Runescape 3

## Usage
Clone the repository, navigate to the folder in a terminal application, then use python to run eviltrees.py

## Commands
```
help                    prints this help message
show                    shows list of trees and times
[world] [time(mins)]    stores world number and time until tree
del [world]             removes the record for the given world
quit                    exits program
```

## Example run
```bash
eviltrees % python3 eviltrees.py
> 5 60
> 2 3
> 42 35
> 65 78
> show
w2 3 mins
w42 35 mins
w5 60 mins
w65 78 mins
> q
eviltrees % 
```

## Notes
- The in-game timer for the activity shows the time as [hr:mins], but the tracker just takes minutes right now, so be sure to convert to minutes

## Future updates
- Support for [hr:min] format, possibly [hr.min] and/or [hr min] format for easier typing
- Approximate calculations for future times after a tree dies (right now the program just deletes the record once the tree is over 10 mins old)
- Store records in a file so they don't get wiped out when the program is reset