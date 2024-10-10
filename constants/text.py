from typing import Final

from constants.bcolors import bcolors


class Text:
    """
    
    """

    @staticmethod
    def WELCOME_TEXT():

        text = f''' {bcolors.HEADER}
Welcome to CourseScheduler! 
Press tab to autocomplete. Type help or ? to list commands. Type q or quit to exit.

Created inside Indian Institute of Technology, Indore, by The Programming Club.{bcolors.ENDC}
        '''

        return text

        lines = text.split('\n')
        return '\n'.join([line.center(width) for line in lines])


    
    PROMPT = f'\n{bcolors.HEADER}CourseScheduler>>{bcolors.ENDC} '

    TARGET_NOT_SET = f"{bcolors.FAIL}Target is not set. Please set a target by: setTarget <your folder path>{bcolors.ENDC}"

    EMPTY_PATH = f"{bcolors.FAIL}Empty path. Please provide a valid path.{bcolors.ENDC}"

    @staticmethod
    def PATH_NOT_FOUND(path):
        return f"{bcolors.FAIL}Directory \"{path}\" not found.{bcolors.ENDC}"

    @staticmethod
    def TARGET_SET(path):
        return f"{bcolors.OKBLUE}Target set as {path}{bcolors.ENDC}"
    
    @staticmethod
    def CHECKING(path):
        return f"Checking files in target {path}..."
    
    @staticmethod
    def FILE_NOT_FOUND_IN_DIRECTORY(required_file, path):
        return f"{bcolors.FAIL}File {required_file} not found in directory {path}{bcolors.ENDC}"
    
    @staticmethod
    def INDORRECT_COLUMNS(required_file, required_fields):
        return f"{bcolors.FAIL}File {bcolors.ENDC}{required_file}{bcolors.FAIL} does not contain the required columns: {bcolors.ENDC}{required_fields}"
    
    ALL_FILES_PRESENT = f"{bcolors.OKGREEN}All required files are present.{bcolors.ENDC}"

    ALL_FILES_VALID = f"{bcolors.OKGREEN}All files are valid.{bcolors.ENDC}"

    CHECKING_WITHIN = f"Now checking withing these files..."

    SOME_CHECKS_FAILED = f"{bcolors.FAIL}Some checks failed.{bcolors.ENDC}"
    

    # ------------------ rudimentary ------------------

    BLOCK = '█'

    HASH = '#'
    
    def UNRECOGNIZED_COMMAND(cmd):
        return f"{bcolors.WARNING}Unrecognized command \"{bcolors.ENDC}{cmd}{bcolors.WARNING}\". Type help or ? to view commands.{bcolors.ENDC}"

    QUIT = f'{bcolors.YELLOW}Quitting.\n\nThank you for using Course Scheduler.\n\nBy Darryl David and Vashistha Chaturvedi.\nThe Programming Club, IIT Indore.{bcolors.ENDC}\n'

    ABOUT = f"{bcolors.BLUE}Course Scheduler, by Darryl David and Vashistha Chaturvedi.\nThe Programming Club, IIT Indore.{bcolors.ENDC}"

    INTERRUPT = f"{bcolors.FAIL}\nProgram was killed.\nCourse Scheduler, by Darryl David and Vashistha Chaturvedi.\nThe Programming Club, IIT Indore.{bcolors.ENDC}"


    

