import readline
from constants.bcolors import bcolors
from cli.depricated_cmd import MyCLI


if __name__ == '__main__':
    
    try :
        if 'libedit' in readline.__doc__:
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")

        MyCLI().cmdloop()

    except KeyboardInterrupt:
        print(f"{bcolors.FAIL}\nProgram was killed.\nCourse Scheduler, by Darryl David and Vashisth Chaturvedi.\nThe Programming Club, IIT Indore.")