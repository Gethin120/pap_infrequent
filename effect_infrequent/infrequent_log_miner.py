from pm4py.objects.log.importer.xes import importer as xes_importer
from effect_infrequent.model_evaluator import model_evaluator_fscore
from effect_infrequent.trace_combine import traces_infrequent_all_combine
from effect_infrequent.creat_trace_list import creat_trace_eva_list
import itertools
from matplotlib import pyplot as plt

import copy

traces_origin = ['abcdfhiklmyz*7964', 'abcdehiklmopqstvz*4358', 'abcdehjklmopruwxvz*3239', 'abcdfhjklnpruwxvz*3018',
                 'abcdehjklnprtvz*2865', 'abcdghiklmyz*2852', 'abcdfhjklnpqstvz*2574', 'abcdehjklmopqsvz*2457',
                 'abcdghjklmoprtvz*1782', 'abcdghjklmopqsvz*1371', 'abcdehiklmoptvz*75', 'abcdehiopqsvz*56',
                 'abcdhejklmoprwxvz*11', 'abcdheiklmopwrxvz*7']
traces_frequent = ['abcdfhiklmyz*1', 'abcdehiklmopqstvz*1', 'abcdehjklmopruwxvz*1', 'abcdfhjklnpruwxvz*1',
                   'abcdehjklnprtvz*1', 'abcdghiklmyz*1', 'abcdfhjklnpqstvz*1', 'abcdehjklmopqsvz*1',
                   'abcdghjklmoprtvz*1', 'abcdghjklmopqsvz*1']
traces_infrequent = ['abcdehiklmoptvz*1', 'abcdehiopqsvz*1', 'abcdhejklmoprwxvz*1', 'abcdheiklmopwrxvz*1']
len_trace_frequent=len(traces_frequent)#10
len_trace_infrequent=len(traces_infrequent)

log_check = xes_importer.apply('trace_origin.xes')
log_base = xes_importer.apply('trace_.xes')
trace__fscore=model_evaluator_fscore(log_base,log_check)#trace__fscore=0.9203156150090784

#产生低频组合的日志
# trace_all_combine,trace_all_combine_name=traces_infrequent_all_combine(traces_frequent,traces_infrequent)

trace_eva_list=creat_trace_eva_list(traces_frequent,traces_infrequent)
print(trace_eva_list)
def infrequent_log_miner_all_combine(trace_eva_list):
    result_list=[]
    result_list_dict={}
    log_check = xes_importer.apply('trace_origin.xes')
    # for items in trace_eva_list:
    #     for item in items:
    #         for i in item:
    #             print(i+'.xes')
    for item in trace_eva_list:
        for i in item:
            # print(i+'.xes')
            log_model = xes_importer.apply(i + ".xes")
            result = model_evaluator_fscore(log_model, log_check)
            result_list.append(result)
        result_list_dict[item[-1]]=result_list
        result_list=[]
    print(result_list_dict,len(result_list_dict))
for i in trace_eva_list:
    #i=0,1,2,3
    infrequent_log_miner_all_combine(i)