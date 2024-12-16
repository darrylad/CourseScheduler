import cmd
import rlcompleter
import time

from cli.automator import startCurses
from configs.bcolors import bcolors
import file

from configs.text import Text
from cli.output import Output
from algorithms import generate
import file.parse 

class MyCLI(cmd.Cmd, rlcompleter.Completer):
    
    intro = Text.WELCOME_TEXT()
    
    def __init__(self):
        super().__init__()
        self.prompt = Text.PROMPT

        

    def do_read(self, arg) -> None:
        'Read the target folder'

        print('\n'+"Reading "+arg)

        file.parse.Parse.populate_timetable_data(arg)
        file.parse.Parse.printdata()


    def do_start(self, arg) -> None:
        'Run automator'

        # set patha

        # if Check.checkPath(arg):
        #     file.check.path = arg
        #     print(Text.TARGET_SET(file.check.path))
        # else:
        #     return

        # # check path
        # if (file.check.path == ''): 
        #     print(Text.TARGET_NOT_SET)
        #     return
        
        # print('\n'+Text.CHECKING(file.check.path))
        # if checkAll():
        #     time.sleep(1)
        #     print()
        #     print(Text.STARTING)
        #     print('\n')
        #     time.sleep(4)
        #     startCurses()

    def do_viewdata(self, arg) -> None:
        'View input data'
        print(generate.timetable_data)

    # ------------------  rudimentary commands: ------------------

    def do_quit(self, arg) -> bool:
        'Quit the application'
        print(Text.QUIT)
        return True
    
    do_q = do_quit

    do_exit = do_quit
    
    def do_EOF(self, arg) -> bool:
        'Exit the application'
        return True
    
    def do_about(self, arg) -> None:
        'Information about Course Scheduler'
        print(Text.ABOUT)
    
    def default(self, line):
        print(Text.UNRECOGNIZED_COMMAND(line))
        # print(f"{bcolors.WARNING}Unrecognized command \"{bcolors.ENDC}{line}{bcolors.WARNING}\". Type help or ? to view commands.{bcolors.ENDC}")

    def do_help(self, arg):
        'Show this help'

        commands = [name[3:] for name in dir(self) if name.startswith('do_') and name != 'do_EOF']
        max_length = max(len(command) for command in commands)

        print(f"\n{bcolors.OKCYAN}Documented commands:{bcolors.ENDC}")
        print()
        for command in commands:
            print(f"    {bcolors.BOLD}{command.ljust(max_length+2)}:{bcolors.ENDC}  {getattr(self, 'do_' + command).__doc__}")
        print()

    def do_loading(self, arg):
        # A List of Items
        items = list(range(0, 57))
        l = len(items)

        # Initial call to print 0% progress
        Output.printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i, item in enumerate(items):
            # Do stuff...
            time.sleep(0.1)
            # Update Progress Bar
            Output.printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


    # def complete(self, text, line, begidx, endidx):
    #     # commands = [name[3:] for name in dir(self) if name.startswith('do_') and name != 'do_EOF']
    #     completions = [command for command in self.commands if command.startswith(text)]
    #     return completions


    