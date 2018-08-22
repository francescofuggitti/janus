import re

class Automa:
    """
        DFA Automa:
        - symbols          => list() ;
        - alphabet         => set() ;
        - states           => set() ;
        - initial_state    => str() ;
        - accepting_states => set() ;
        - transitions      => dict(), where
        **key**: *source* ∈ states
        **value**: {*action*: *destination*)
    """

    def __init__(self, symbols, alphabet, states, initial_state, accepting_states, transitions):
        self.symbols = symbols
        self.alphabet = alphabet
        self.states = states
        self._initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions
        self._current_state = self._initial_state
        self.validate()

    def valide_transition_start_states(self):
        for state in self.states:
            if state not in self.transitions:
                raise ValueError(
                    'transition start state {} is missing'.format(
                        state))

    def validate_initial_state(self):
        if self._initial_state not in self.states:
            raise ValueError('initial state is not defined as state')

    def validate_accepting_states(self):
        if any(not s in self.states for s in self.accepting_states):
            raise ValueError('accepting states not defined as state')

    def validate_input_symbols(self):
        alphabet_pattern = self.get_alphabet_pattern()
        for state in self.states:
            for action in self.transitions[state]:
                if not re.match(alphabet_pattern, action):
                    raise ValueError('invalid transition found')

    def get_alphabet_pattern(self):
        return re.compile("(^["+''.join(self.alphabet)+"]+$)")

    def validate(self):
        self.validate_initial_state()
        self.validate_accepting_states()
        self.valide_transition_start_states()
        self.validate_input_symbols()
        return True

    def __str__(self):
        automa = 'alphabet: {}\n'.format(str(self.alphabet))
        automa += 'states: {}\n'.format(str(self.states))
        automa += 'init_state: {}\n'.format(str(self._initial_state))
        automa += 'accepting_states: {}\n'.format(str(self.accepting_states))
        automa += 'transitions: {}'.format(str(self.transitions))
        return automa

    @property
    def current_state(self):
        return self._current_state

    @property
    def initial_state(self):
        return self._initial_state

    def make_transition(self, action):
        # print('make transition '+str(self.transitions))
        # print('transitions' + str(self.transitions))

        if action in self.symbols:
            #print('ACTION: '+str(action)+' in symbols')
            for act in self.transitions[self._current_state].keys():
                temp = dict(zip(self.symbols,[value for value in act]))
                #print('ACT: ' + str(act) + ' CURRENT_STATE: ' + str(self._current_state) + ' TEMP: '+str(temp))
                additional = temp.copy()
                del additional[action]
                #print(additional)
                if (temp[action] == '1' or temp[action] == 'X') and all(value in {'0', 'X'} for value in additional.values()):
                    # print('YES: ' + str(temp))
                    self._current_state = self.transitions[self._current_state][act]
                else:
                    continue
        else:
            #print('ACTION: '+str(action)+' NOT in symbols')
            number_of_symbols = len(self.symbols)
            if number_of_symbols == 0: # true when there is True automa
                self._current_state = self.transitions[self._current_state]['X']
            else:
                if 'X'*number_of_symbols in self.transitions[self._current_state]:
                    self._current_state = self.transitions[self._current_state]['X'*number_of_symbols]
                elif '0'*number_of_symbols in self.transitions[self._current_state]:
                    self._current_state = self.transitions[self._current_state]['0'*number_of_symbols]
                else:
                    raise ValueError('[ERROR]: could not make transition with action {}'.format(action))
        # print(self._current_state)

    def is_accepting(self):
        if self._current_state in self.accepting_states:
            return True
        else:
            return False

    def accepts(self, input_symbol):
        _current_state = self._current_state
        self._current_state = self._initial_state
        self.make_transition(input_symbol)
        if self.is_accepting():
            self._current_state = _current_state
            return True
        else:
            self._current_state = _current_state
            return False