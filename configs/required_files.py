


class RequiredFilesConfig:
    """
    Stores configuration data for required CSV files.

    Attributes:
        COURSES_CSV: A set of required fields for the "courses.csv" file.
        ROOMS_CSV: A set of required fields for the "rooms.csv" file.

    Methods:
        get_required_fields(filename): Retrieves the required fields for a given file.
    """

    COURSES_CSV = {'Code', 'Students'}
    ROOMS_CSV = {'Room', 'Capacity'}

    @classmethod
    def get_required_fields(cls, filename):
        """
        Retrieves the required fields for a given file.

        Args:
            filename: The name of the CSV file.

        Returns:
            A set of required fields for the given file, or None if the file is not recognized.
        """
        return getattr(cls, filename.upper(), None)
    



RequiredFilesConfig.get_required_fields()