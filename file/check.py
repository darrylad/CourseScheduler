import os
import csv
from constants.bcolors import bcolors

path: str = ''


requiredFilesFields: dict[str, list[str]] = {
    'courses.csv': ['Code', 'Students'],
    'rooms.csv': ['Room', 'Capacity'],
    # 'students.csv': ['roll']
}

class Check:
    def __init__(self):
        self.path = path

    # check if given path exists
    def checkPath(self) -> bool:
        if self == '':
            print(f"{bcolors.FAIL}Empty path. Please provide a valid path.{bcolors.ENDC}")
            return False
        elif not os.path.exists(self):
            print(f"{bcolors.FAIL}Directory \"{self}\" not found.{bcolors.ENDC}")
            return False
        else:
            return True

    # print all files in the directory
    def readNames(self) -> bool:
        try:
            files: list[str] = os.listdir(self.path)
            for file in files:
                print('--'+file)
            return True
        except FileNotFoundError:
            return False

    # check if all required files are present
    def checkNames(self) -> bool:
        try:
            files = os.listdir(self.path)
            for required_file in requiredFilesFields.keys():
                if required_file not in files:
                    print(f"{bcolors.FAIL}File {required_file} not found in directory {self.path}{bcolors.ENDC}")
                    return False
            # print(f"{bcolors.OKGREEN}All required files are present.{bcolors.ENDC}")
            return True
        except FileNotFoundError:
            print(f"{bcolors.FAIL}Directory {self.path} not found.{bcolors.ENDC}")
            return False
    
    # check if all required fields are present in each file
    def checkFiles(self) -> bool:
        try:
            files = os.listdir(self.path)
            valid = True

            for required_file, required_fields in requiredFilesFields.items():

                if required_file not in files:
                    print(f"{bcolors.FAIL}File {required_file} not found in directory {self.path}{bcolors.ENDC}")
                    return False
                
                else:
                    with open(os.path.join(self.path, required_file), 'r') as f:
                        reader = csv.DictReader(f)

                        if not set(required_fields).issubset(set(reader.fieldnames)):
                            print(f"{bcolors.FAIL}Incorrect columns in {required_file}. Required columns are {required_fields}{bcolors.ENDC}")
                            valid = False

            if valid:
                print(f"{bcolors.OKGREEN}All required files are valid.{bcolors.ENDC}")
            else:
                print()
            
            return valid
        
        except FileNotFoundError:
            print(f"{bcolors.FAIL}Directory {self.path} not found.{bcolors.ENDC}")
            return False
        

def checkAll() -> bool:
    Check().readNames()
    validNames = Check().checkNames()
    if validNames:
        print(f"{bcolors.OKGREEN}All required files are present.{bcolors.ENDC}")
        return Check().checkFiles()
    else:
        print(f"{bcolors.FAIL}Some checks failed.{bcolors.ENDC}")
        return False