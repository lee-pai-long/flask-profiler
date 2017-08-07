# NOTE: Docstring should be more explicit
class BaseStorage(object):
    """docstring for BaseStorage"""
    def __init__(self):
        super(BaseStorage, self).__init__()

    def filter(self, criteria):
        raise NotImplementedError("Not implemented Error")

    def getSummary(self, criteria):
        raise NotImplementedError("Not implemented Error")

    def insert(self, measurement):
        raise NotImplementedError("Not implemented Error")

    def delete(self, measurementId):
        raise NotImplementedError("Not implemented Error")

    def truncate(self):
        raise NotImplementedError("Not implemented Error")
