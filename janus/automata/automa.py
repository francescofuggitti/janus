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

    def __init__(self, alphabet, states, initial_state, accepting_states, transitions):
        self.alphabet = alphabet
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions
        self.current_state = self.initial_state
        self.validate()

    def valide_transition_start_states(self):
        for state in self.states:
            if state not in self.transitions:
                raise ValueError(
                    'transition start state {} is missing'.format(
                        state))

    def validate_initial_state(self):
        if self.initial_state not in self.states:
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
        automa += 'init_state: {}\n'.format(str(self.initial_state))
        automa += 'accepting_states: {}\n'.format(str(self.accepting_states))
        automa += 'transitions: {}'.format(str(self.transitions))
        return automa

    def make_transition(self, action):
        pass

    def is_accepting(self):
        if self.current_state in self.accepting_states:
            return True
        else:
            return False

    def accepts(self, input_symbol):
        if input_symbol in self.transitions[self.initial_state]:
            return self.transitions[self.initial_state][input_symbol]
        else:
            raise ValueError('{} is not a valid input symbol'.format(input_symbol))
