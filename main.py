import os
import readline

from cli.cmd import MyCLI
from configs.text import Text


# clear the console
os.system('cls||clear')

if __name__ == '__main__':
    
    try :
        if 'libedit' in readline.__doc__:
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")

        # begin prompt loop
        MyCLI().cmdloop()

    except KeyboardInterrupt:
        print(Text.INTERRUPT)