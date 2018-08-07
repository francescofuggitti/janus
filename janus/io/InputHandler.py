import csv
from opyenxes.data_in.XUniversalParser import XUniversalParser
from opyenxes.classification.XEventAttributeClassifier import XEventAttributeClassifier

class InputHandler:

    def __init__(self, input_path):
        self.input_path = input_path
        self._event_log = None
        self.load()

    @property
    def event_log(self):
        return self._event_log

    def load_txt(self):
        try:
            with open(self.input_path, 'r') as f:
                self._event_log = set(tuple(i) for i in [f.read().splitlines()])
                f.close()
        except:
            raise IOError('[ERROR]: Unable to import text file')

    def load_csv(self):
        self._event_log = []
        try:
            with open(self.input_path, newline='', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                for row in reader:
                    self._event_log.append(row[0])
        except:
            raise IOError('[ERROR]: Unable to import csv file')

    def load_xes(self):
        try:
            with open(self.input_path) as log_file:
                log = XUniversalParser().parse(log_file)[0]

            # get classifiers
            classifiers = []
            for cl in log.get_classifiers():
                classifiers.append(str(cl))

            classifier = XEventAttributeClassifier("activity", [classifiers[0]])
            log_list = list(map(lambda trace: list(map(classifier.get_class_identity, trace)), log))

            self._event_log = set(tuple(trace) for trace in log_list)

        except:
            raise IOError('[ERROR]: Unable to import xes file')

    def load(self):
        if self.input_path.endswith('.txt'):
            self.load_txt()
        elif self.input_path.endswith('.csv'):
            self.load_csv()
        elif self.input_path.endswith('.xes'):
            self.load_xes()
        else:
            raise ValueError('[ERROR]: File extension not recognized')

if __name__ == '__main__':
    input_handler = InputHandler('files/sepsis.xes')
    result = input_handler.load()
    print(result)