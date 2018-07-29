import csv
from opyenxes.data_in.XUniversalParser import XUniversalParser

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
            raise IOError('[ERROR] - Unable to import text file')

    def load_csv(self):
        self.event_log = []
        try:
            with open(self.input_path, newline='', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.event_log.append(row[0])
            return self.event_log
        except:
            raise IOError('[ERROR] - Unable to import csv file')

    def load_xes(self):
        try:
            with open(self.input_path) as log_file:
                self.event_log = XUniversalParser().parse(log_file)[0]
            return self.event_log
        except:
            raise IOError('[ERROR] - Unable to import xes file')

    def load(self):
        if self.input_path.endswith('.txt'):
            return self.load_txt()
        elif self.input_path.endswith('.csv'):
            return self.load_csv()
        elif self.input_path.endswith('.xes'):
            return self.load_xes()
        else:
            raise ValueError('[ERROR] - File extension not recognized')

if __name__ == '__main__':
    input_handler = InputHandler('files/event_log.csv')
    result = input_handler.load()
    print(result)