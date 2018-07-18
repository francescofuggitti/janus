class InputHandler:

    def __init__(self, input_path):
        self.input_path = input_path
        self.event_log = None

    def load_txt(self):
        try:
            with open(self.input_path, 'r') as f:
                self.event_log = f.read().splitlines()
                f.close()
            return self.event_log
        except:
            raise IOError

    def load_csv(self):
        pass

    def load_xes(self):
        pass

    def load(self):
        if self.input_path.endswith('.txt'):
            return self.load_txt()
        elif self.input_path.endswith('.csv'):
            return self.load_csv()
        elif self.input_path.endswith('.xes'):
            return self.load_xes()
        else:
            raise ValueError

if __name__ == '__main__':
    input_handler = InputHandler('event_log.txt')
    result = input_handler.load()
    print(result)