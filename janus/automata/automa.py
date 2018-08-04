import re

class Automa:
    """
        DFA Automa:
        - alphabet         => set() ;
        - states           => set() ;
        - initial_state    => str() ;
        - accepting_states => set() ;
        - transitions      => dict(), where
        **key**: *source* ∈ states
        **value**: {*action*: *destination*)
    """
    MAX_ALPHABET = 26
    en_alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z')
    used_alpha = None

    def __init__(self, symbol, alphabet, states, initial_state, accepting_states, transitions):
        self.symbol = symbol
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
        if 'X' in self.transitions[self._current_state]: # X means whatever action
            self._current_state = self.transitions[self._current_state]['X']
        elif action == self.symbol:
            self._current_state = self.transitions[self._current_state]['1']
        elif action != self.symbol:
            self._current_state = self.transitions[self._current_state]['0']
        else:
            raise ValueError('[ERROR]: could not make transition with action {}'.format(action))

    def is_accepting(self):
        if self._current_state in self.accepting_states:
            return True
        else:
            return False

    def accepts(self, input_symbol):
        if input_symbol == self.symbol:
            if ('X' or '1') in self.transitions[self._initial_state]:
                return True
            else:
                return False
        else:
            if ('X' or '0') in self.transitions[self._initial_state]:
                return True
            else:
                return False
        #
        # if input_symbol in self.transitions[self._initial_state]:
        #     return self.transitions[self._initial_state][input_symbol]
        # else:
        #     raise ValueError('[ERROR]: "{}" is not a valid input symbol'.format(input_symbol))