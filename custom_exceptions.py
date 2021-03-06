
class GeneralException(Exception):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)


class UnimplementedMethodException(GeneralException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BadFieldValueException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BadFieldTypeException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ClientAndServerOutOfSyncException(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CollectionNotChosenYetException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DatabaseNotSelectedException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EmptyCollectionException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FieldNameAlreadyInUseException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
