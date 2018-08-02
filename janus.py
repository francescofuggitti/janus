from janus.io.InputHandler import InputHandler
from janus.formulas.separatedFormula import SeparatedFormula
from janus.formulas.formula import Formula
from janus.automata.sepautset import SeparatedAutomataSet
import argparse

args_parser = argparse.ArgumentParser(description='Janus algorithm computes the interestingness degree of an RCon over'+
                                                  ' a trace taken by an event log L')
args_parser.add_argument('<event-log>', help='Path to the event log -- MANDATORY')
args_parser.add_argument('<activator>', type=str, help='Activator -- MANDATORY')
# args_parser.add_argument('<formula>', type=str, help='Formula to be checked -- MANDATORY')

params = vars(args_parser.parse_args())

input_log = InputHandler(params['<event-log>'])
trace = input_log.event_log
print('[LOG]: ' + str(trace))
activator = params['<activator>']
print('[ACTIVATOR]: ' + activator)

# formula = params['<formula>']

sepFormula1 = SeparatedFormula(('Yb', 'T', 'T'))
sepFormula2 = SeparatedFormula(('T', 'T', 'Ec'))

constraint = Formula([sepFormula1, sepFormula2]) # set manually the constraint
print('[CONSTRAINT]: ' + str(constraint))

sepautset = SeparatedAutomataSet(constraint).automa_set

# JANUS ALGORITHM SKETCH
O = []
for event in trace:
    for past, now, future in sepautset:
        past.make_transition(event)
    if event == activator:
        J = set()
        # for past, now, future in sepautset:
        if past.is_accepting() and now.accepts(event):
            J.add((future.current_state, future))
        O.append(J)
    for j in O:
        for st, aut in J:
            aut.make_transition(event)
            st = aut.current_state

if O:
    count = 0
    for janus in O:
        for state, automa in janus:
            if state in automa.accepting_states:
                count += 1
            else:
                continue
    print('[ACTIVATED]: ' + str(len(O)))
    print('[FULFILLED]: ' + str(count))
    print(count/len(O))
else:
    print(0)