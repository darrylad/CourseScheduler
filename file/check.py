import os
from configs.text import Text

path: str = ''


class Check:


    

    def __init__(self):
        self.path = path

    # trim the path of any spaces and quotes
    def trimPath(path) -> str:
        return path.strip().strip('\'"')

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
        global path
        try:
            files: list[str] = os.listdir(self.path)
            for file in files:
                print('-- '+file)
            return True
        except Exception as e:
            print(Text.INVALID_PATH(e.args))
            path = ''
            return False

    # # check if all required files are present
    # def checkNames(self) -> bool:
    #     global path
    #     try:
    #         files = os.listdir(self.path)
    #         valid: bool = True

    #         for required_file in RequiredFilesConfig.requiredFilesFields.keys():
    #             if required_file not in files:
    #                 print(Text.FILE_NOT_FOUND_IN_DIRECTORY(required_file, self.path))
    #                 valid = False

    #         return valid
    #     except Exception as e:
    #         print(Text.INVALID_PATH(e.args))
    #         path=''
    #         return False
    
    # # check if all required fields are present in each file
    # def checkFiles(self) -> bool:
    #     global path

    #     try:
    #         files = os.listdir(self.path)
    #         valid = True

    #         for required_file, required_fields in RequiredFilesConfig.requiredFilesFields.items():

    #             if required_file not in files:
    #                 print(Text.FILE_NOT_FOUND_IN_DIRECTORY(required_file, self.path))
    #                 return False
                
    #             else:
    #                 with open(os.path.join(self.path, required_file), 'r') as f:
    #                     reader = csv.DictReader(f)

    #                     if not set(required_fields).issubset(set(reader.fieldnames)):
    #                         print(Text.INDORRECT_COLUMNS(required_file, required_fields))
    #                         valid = False

    #         if valid:
    #             print(Text.ALL_FILES_VALID)
    #         else:
    #             print()
            
    #         return valid
        
    #     except Exception as e:
    #         print(Text.INVALID_PATH(e.args))
    #         path = ''
    #         return False
    
    @classmethod
    def check_folder_structure(cls, base_path, required_structure):
        """
        Check if the folder structure follows the required structure.

        :param base_path: The base path of the folder to check.
        :param required_structure: The required folder structure.
        :return: True if the folder structure is valid, False otherwise.
        """

        for key, value in required_structure.items():
            if key == "files":
                for file in value:
                    file_path = os.path.join(base_path, file)
                    if not os.path.exists(file_path):
                        print(f"Missing file: {file_path}")
                        return False
            else:
                path = os.path.join(base_path, key)
                if not os.path.exists(path):
                    print(f"Missing folder: {path}")
                    return False

                if isinstance(value, dict):
                    if not cls.check_folder_structure(path, value):
                        return False

        return True

    @classmethod
    def check_csv_columns(cls, file_path, required_columns):
        """
        Check if the CSV file contains the required columns.

        :param file_path: The path of the CSV file to check.
        :param required_columns: The required columns.
        :return: True if the CSV file contains the required columns, False otherwise.
        """

        import csv
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            columns = set(reader.fieldnames)
            if not set(required_columns).issubset(columns):
                print(f"Incorrect columns in {file_path}. Required columns are: {required_columns}")
                return False
        return True
    
    @classmethod
    def validate_folder(cls, base_path, required_structure, required_columns):
        """
        Validate the folder structure and CSV columns.

        :param base_path: The base path of the folder to validate.
        :param required_structure: The required folder structure.
        :param required_columns: The required columns for the CSV files.
        :return: True if the folder structure and CSV columns are valid, False otherwise.
        """

        base_path = base_path.strip().strip('\'"')

        if not cls.check_folder_structure(base_path, required_structure):
            return False

        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.lower().endswith('.csv'):
                    file_path = os.path.join(root, file)
                    if not cls.check_csv_columns(file_path, required_columns):
                        return False

        print("All checks passed.")
        return True


def checkAll() -> bool:
    if not Check().readNames():
        return False
    validNames = Check().checkNames()
    print()
    if validNames:
        print(Text.ALL_FILES_PRESENT)
        print(Text.CHECKING_WITHIN)
        return Check().checkFiles()
    else:
        print(Text.SOME_CHECKS_FAILED)
        return False