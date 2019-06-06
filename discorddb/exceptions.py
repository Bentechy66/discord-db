# Discord Exceptions
class Discord404Exception(Exception):
    pass  # No further functionality required


class Discord403Exception(Exception):
    pass  # No further functionality required


# Record / Table Exceptions
class DataTooLongException(Exception):
    pass  # No further functionality required


# Database Exceptions
class TableNotFoundException(Exception):
    pass  # No further functionality required


class TooManyTablesException(Exception):
    pass  # No further functionality required


class TooLongFieldNamesException(Exception):
    pass  # No further functionality required


class InvalidNameException(Exception):
    pass  # No further functionality required
