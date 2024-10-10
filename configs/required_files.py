


class RequiredFilesConfig:
    """
    Stores configuration data for required CSV files.

    @class_attributes:
        COURSES_CSV: A set of required fields for the "courses.csv" file.
        ROOMS_CSV: A set of required fields for the "rooms.csv" file.

    @class_methods:
        get_required_fields(filename): Retrieves the required fields for a given file.
    """

    COURSES_CSV = {'Code', 'Students'}
    ROOMS_CSV = {'Room', 'Capacity'}


    requiredFilesFields: dict[str, list[str]] = {
        'courses.csv': ['Code', 'Students'],
        'rooms.csv': ['Room', 'Capacity'],
        # 'students.csv': ['roll']
    }
    


    @classmethod
    def get_required_fields(cls, filename):
        """
        Retrieves the required fields for a given file.

        @params:
            filename - Required : The name of the CSV file.

        @returns:
            A set of required fields for the given file, or None if the file is not recognized.
        """
        return getattr(cls, filename.upper(), None)


