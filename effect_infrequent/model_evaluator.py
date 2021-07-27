from pm4py.evaluation import evaluator
from gethin_API.process_discovery import alpha_miner

def model_evaluator_fscore(log_model,log_check):
    net, initial_marking, final_marking = alpha_miner(log_model)
    result = evaluator.apply(log_check, net, initial_marking, final_marking)
    result_fcore=result['fscore']
    return result_fcore