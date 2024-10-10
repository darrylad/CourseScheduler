import os
import csv

from configs.required_files import RequiredFilesConfig
from constants.bcolors import bcolors
from constants.text import Text

path: str = ''


class Check:
    def __init__(self):
        self.path = path

    # trim the path of any spaces and quotes
    def trimPath(path) -> str:
        path = path.strip().strip('\'"')

        return path

    # check if given path exists
    def checkPath(path) -> bool:
        if path == '':
            print(Text.EMPTY_PATH)
            return False
        elif not os.path.exists(path):
            print(Text.PATH_NOT_FOUND(path))
            return False
        else:
            return True

    # print all files in the directory
    def readNames(self) -> bool:
        try:
            files: list[str] = os.listdir(self.path)
            for file in files:
                print('-- '+file)
            return True
        except FileNotFoundError:
            return False

    # check if all required files are present
    def checkNames(self) -> bool:
        try:
            files = os.listdir(self.path)
            for required_file in RequiredFilesConfig.requiredFilesFields.keys():
                if required_file not in files:
                    print(Text.FILE_NOT_FOUND_IN_DIRECTORY(required_file, self.path))
                    return False
            # print(f"{bcolors.OKGREEN}All required files are present.{bcolors.ENDC}")
            return True
        except FileNotFoundError:
            print(Text.PATH_NOT_FOUND(self.path))
            return False
    
    # check if all required fields are present in each file
    def checkFiles(self) -> bool:
        try:
            files = os.listdir(self.path)
            valid = True

            for required_file, required_fields in RequiredFilesConfig.requiredFilesFields.items():

                if required_file not in files:
                    print(Text.FILE_NOT_FOUND_IN_DIRECTORY(required_file, self.path))
                    # print(f"{bcolors.FAIL}File {required_file} not found in directory {self.path}{bcolors.ENDC}")
                    return False
                
                else:
                    with open(os.path.join(self.path, required_file), 'r') as f:
                        reader = csv.DictReader(f)

                        if not set(required_fields).issubset(set(reader.fieldnames)):
                            print(Text.INDORRECT_COLUMNS(required_file, required_fields))
                            # print(f"{bcolors.FAIL}Incorrect columns in {required_file}. Required columns are {required_fields}{bcolors.ENDC}")
                            valid = False

            if valid:
                print(Text.ALL_FILES_VALID)
            else:
                print()
            
            return valid
        
        except FileNotFoundError:
            print(Text.PATH_NOT_FOUND(self.path))
            return False
        

def checkAll() -> bool:
    Check().readNames()
    validNames = Check().checkNames()
    print()
    if validNames:
        print(Text.ALL_FILES_PRESENT)
        print(Text.CHECKING_WITHIN)
        return Check().checkFiles()
    else:
        print(Text.SOME_CHECKS_FAILED)
        return False