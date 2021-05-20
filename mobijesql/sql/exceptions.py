from mobijesql.exceptions import MobijeSQLError


class DataDuplicatedError(MobijeSQLError):
    pass


class DataNotFoundError(MobijeSQLError):
    pass
