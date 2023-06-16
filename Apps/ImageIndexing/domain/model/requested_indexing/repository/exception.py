class InvalidTaskIdException(Exception):
    pass


class TaskNotFoundException(Exception):
    pass


class TaskSubmittedException(Exception):
    pass


class InvalidTaskPayloadException(Exception):
    pass


class DuplicateKeyError(Exception):
    pass


class EntityOutdated(Exception):
    pass
