from janus.io.InputHandler import InputHandler
from collections import Counter
import argparse, os

args_parser = argparse.ArgumentParser(description='Janus algorithm computes the interestingness degree of an RCon over'+
                                                  ' a trace taken by an event log L')
args_parser.add_argument('<event-log>', help='Path to the event log -- MANDATORY')
args_parser.add_argument('<activator>', type=str, help='Activator -- MANDATORY')
args_parser.add_argument('<formula>', type=str, help='Formula to be checked -- MANDATORY')

params = vars(args_parser.parse_args())

input_log = InputHandler(params['<event-log>'])
log = input_log.event_log
activator = params['<activator>']
formula = params['<formula>']

## JANUS ALGORITHM
O = Bag()
for event in trace:
    for past, now, future in sepautset:
        past.perform_transition(event)
    if event == activator:
        J = set()
        for past, now, future in sepautset:
            if past.is_accepting() and now.accepts(event):
                J.add( (future.current_state, future) )
        O.add(J)
    for j in O:
        for state, automa in J:
            state = automa.perform_transition(event)