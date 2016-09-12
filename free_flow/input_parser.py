

class AbstractInputParser(object):
    def __init__(self):
        self._pipes = []

    def parse(self):
        pass

    def get_pipes(self):
        return self._pipes

        
class FileInputParser(AbstractInputParser):
    def set_file(self, file):
        self._file = file

    def parse(self):
        if not hasattr(self, '_file'):
            return
        # TODO 


class StringInputParser(AbstractInputParser):
    def set_input(self, input_str):
        self._input_str = input_str

    def parse(self):
        if not hasattr(self, '_input_str'):
            return
