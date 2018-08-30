class AllMailInfo(object):
    def __init__(self, file, name):
        self._file = file
        self._name = name

    def get_file(self):
        return self._file

    def get_name(self):
        return self._name