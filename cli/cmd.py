import cmd
import rlcompleter
from cli.bcolors import bcolors
from file.check import Check, checkAll
import file.check


class MyCLI(cmd.Cmd, rlcompleter.Completer):
    
    intro = f''' {bcolors.HEADER}
Welcome to Course Scheduler! 
Type help or ? to list commands. Type q or quit to exit.

Created inside Indian Institute of Technology, Indore, by The Programming Club.{bcolors.ENDC}
'''
    
    def __init__(self):
        super().__init__()
        self.prompt = f'{bcolors.HEADER}CourseScheduler>>{bcolors.ENDC} '


    def do_hello(self, arg):
        'Say hello'
        print(f"hello", arg)

    def do_target(self, arg):
        'See the target folder path'
        if file.check.path == '':
            print(f"{bcolors.WARNING}Target is not set.{bcolors.ENDC}")
        else:
            print(f"Target is {file.check.path}")

    def do_setTarget(self, arg):
        'Set the target folder'
        if Check.checkPath(arg):
            file.check.path = arg
            print(f"{bcolors.OKBLUE}Target set as {file.check.path}{bcolors.ENDC}")

    def complete_setTarget(self, text, line, begidx, endidx):
        completions = [command for command in self.commands if command.startswith(text)]
        return completions
        

    def do_check(self, arg):
        'Check the target folder'
        print(f"Checking file in target {file.check.path}...")
        checkAll()

    # ------------------  rudimentary commands: ------------------

    def do_quit(self, arg):
        'Quit the application'
        print(f'{bcolors.YELLOW}Quitting.\nThank you for using Course Scheduler.\nBy Darryl David and Vashistha Chaturvedi.\nThe Programming Club, IIT Indore.')
        return True
    
    do_q = do_quit
    
    def do_EOF(self, arg):
        'Exit the application'
        return True
    
    def do_about(self, arg):
        'Information about Course Scheduler'
        print(f"{bcolors.HEADER}Course Scheduler, by Darryl David and Vashisth Chaturvedi.\nThe Programming Club, IIT Indore.{bcolors.ENDC}")
    
    def default(self, line):
        print(f"{bcolors.WARNING}Unrecognized command \"{bcolors.RED}{line}{bcolors.WARNING}\". Type help or ? to view commands.{bcolors.ENDC}\n")

    def do_help(self, arg):
        'Show this help'
        commands = [name[3:] for name in dir(self) if name.startswith('do_') and name != 'do_EOF']
        max_length = max(len(command) for command in commands)
        print(f"{bcolors.BOLD}Documented commands:{bcolors.ENDC}")
        for command in commands:
            print(f"{bcolors.BOLD}{command.ljust(max_length+2)}:{bcolors.ENDC}  {getattr(self, 'do_' + command).__doc__}")
        print()

    # def complete(self, text, line, begidx, endidx):
    #     # commands = [name[3:] for name in dir(self) if name.startswith('do_') and name != 'do_EOF']
    #     completions = [command for command in self.commands if command.startswith(text)]
    #     return completions


    