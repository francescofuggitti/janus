from janus.io.InputHandler import InputHandler
from janus.formulas.separatedFormula import SeparatedFormula
from janus.formulas.formula import Formula
from janus.automata.sepautset import SeparatedAutomataSet
import argparse, copy

args_parser = argparse.ArgumentParser(description='Janus algorithm computes the interestingness degree of an RCon over'+
                                                  ' a trace taken by an event log L')
args_parser.add_argument('<event-log>', help='Path to the event log -- MANDATORY')
#args_parser.add_argument('<activator>', type=str, help='Activator -- MANDATORY')
# args_parser.add_argument('<formula>', type=str, help='Formula to be checked -- MANDATORY')

params = vars(args_parser.parse_args())

input_log = InputHandler(params['<event-log>'])
log_set = input_log.event_log

#activator = params['<activator>']
#print('[ACTIVATOR]: ' + activator)

# formula = params['<formula>']

# trace = (['erregistration'], ['ertriage','ersepsistriage'], ['lacticacid','ivliquid'], ['leucocytes','lacticacid'], ['crp'], ['lacticacid'],
#          ['leucocytes', 'lacticacid'], ['leucocytes','ivantibiotics'], ['ivliquid'], ['releasea'])

#sepFormula0 = SeparatedFormula(('false', 'leucocytes', 'false'))
sepFormula1 = SeparatedFormula(('Yerregistration', 'true & leucocytes', 'true'))
sepFormula2 = SeparatedFormula(('true', 'true & leucocytes', 'Fcrp'))

#constraint = Formula([sepFormula0, sepFormula1, sepFormula2]) # set manually the constraint
constraint = Formula([sepFormula1, sepFormula2])
print('[SEPARATED FORMULAS]: ' + str(constraint))

sepautset = SeparatedAutomataSet(constraint).automa_set

for trace in list(log_set)[:5]:
    print('[TRACE]: ' + str(trace))
    # JANUS ALGORITHM
    O = []
    for event in trace:
        #print('[EVENT]: ' + event)
#########################################
        # for pastAut in sepautset:
        #     pastAut[0].make_transition([event.replace(' ','').lower()])
        #     # print(pastAut[0].transitions)
        #
        # #if event == activator:
        # if sepautset[0][1].accepts([event.replace(' ','').lower()]):
            # J = {}
            # for past, now, future in sepautset:
            #     if past.is_accepting() and now.accepts([event.replace(' ','').lower()]):
            #         #print('[PAST ' + str(past.symbols) + ' IN ACCEPTING]: state == ' + str(past.current_state))
            #         #J.add((future.initial_state, future))
            #         temp = copy.deepcopy(future)
            #         J[temp] = future.initial_state
            # # print('Janus is: ' + str(J))
            # O.append(J)
#########################################
        for past, now, future in sepautset:
            past.make_transition([event.replace(' ','').lower()])
            if now.accepts([event.replace(' ','').lower()]) and past.is_accepting():
                J = {}
                temp = copy.deepcopy(future)
                J[temp] = future.initial_state
                O.append(J)
            #print('O bag is: ' + str(O))
        # print('[OBAG EVENT ' + event + '] ' + str(O))
        for j in O:
            for aut, st in j.items():
                aut.make_transition([event.replace(' ','').lower()])
                #print('aut {0}, state after transition {1}: {2}'.format(aut.symbols, event, aut.current_state))
                j[aut] = aut.current_state

    if O:
        count = 0
        for janus in O:
            for automa, state in janus.items():
                if state in automa.accepting_states:
                    count += 1
                    break
                else:
                    continue
        print('[ACTIVATED]: ' + str(len(O)))
        print('[FULFILLED]: ' + str(count))
        print('[INTERESTINGNESS DEGREE]: ' + str(count/len(O)))
    else:
        print('[ACTIVATED]: 0')
        print('[FULFILLED]: 0')
        print('[INTERESTINGNESS DEGREE]: 0')

# [event.replace(' ','').lower()]
