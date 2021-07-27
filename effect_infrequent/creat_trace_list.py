"""

[
[
['trace_0', 'trace_0_1', 'trace_0_1_2', 'trace_0_1_2_3'],
['trace_0', 'trace_0_1', 'trace_0_1_3', 'trace_0_1_3_2'],
['trace_0', 'trace_0_2', 'trace_0_2_1', 'trace_0_2_1_3'],
['trace_0', 'trace_0_2', 'trace_0_2_3', 'trace_0_2_3_1'],
['trace_0', 'trace_0_3', 'trace_0_3_1', 'trace_0_3_1_2'],
['trace_0', 'trace_0_3', 'trace_0_3_2', 'trace_0_3_2_1']],
[['trace_1', 'trace_1_0', 'trace_1_0_2', 'trace_1_0_2_3'], ['trace_1', 'trace_1_0', 'trace_1_0_3', 'trace_1_0_3_2'], ['trace_1', 'trace_1_2', 'trace_1_2_0', 'trace_1_2_0_3'], ['trace_1', 'trace_1_2', 'trace_1_2_3', 'trace_1_2_3_0'], ['trace_1', 'trace_1_3', 'trace_1_3_0', 'trace_1_3_0_2'], ['trace_1', 'trace_1_3', 'trace_1_3_2', 'trace_1_3_2_0']],
[['trace_2', 'trace_2_0', 'trace_2_0_1', 'trace_2_0_1_3'], ['trace_2', 'trace_2_0', 'trace_2_0_3', 'trace_2_0_3_1'], ['trace_2', 'trace_2_1', 'trace_2_1_0', 'trace_2_1_0_3'], ['trace_2', 'trace_2_1', 'trace_2_1_3', 'trace_2_1_3_0'], ['trace_2', 'trace_2_3', 'trace_2_3_0', 'trace_2_3_0_1'], ['trace_2', 'trace_2_3', 'trace_2_3_1', 'trace_2_3_1_0']],
[['trace_3', 'trace_3_0', 'trace_3_0_1', 'trace_3_0_1_2'], ['trace_3', 'trace_3_0', 'trace_3_0_2', 'trace_3_0_2_1'], ['trace_3', 'trace_3_1', 'trace_3_1_0', 'trace_3_1_0_2'], ['trace_3', 'trace_3_1', 'trace_3_1_2', 'trace_3_1_2_0'], ['trace_3', 'trace_3_2', 'trace_3_2_0', 'trace_3_2_0_1'], ['trace_3', 'trace_3_2', 'trace_3_2_1', 'trace_3_2_1_0']]]

"""

import copy
import itertools


def creat_trace_eva_list(traces_frequent, traces_infrequent):
    trace_eva_list = []
    list1 = [i for i in range(len(traces_infrequent))]
    tem = copy.deepcopy(list1)
    for i in range(len(list1)):
        list1.pop(i)
        # print(list1)
        aa = itertools.permutations(list1, 3)
        # print(list(aa))
        trace_name = 'trace_' + str(i)
        trace_name_ori = copy.deepcopy(trace_name)
        list_trace_name = [trace_name]
        # list_trace_name=[]
        for item in list(aa):
            # print(item)
            temp = []
            for i in range(len(item)):
                trace_name += '_' + str(item[i])
                temp.append(trace_name)
            list_trace_name.append(temp)
            trace_name = copy.deepcopy(trace_name_ori)

        print(list_trace_name)
        trace_eva_list.append(list_trace_name)
        # print(list(aa))
        list1 = copy.deepcopy(tem)
    for iterm in trace_eva_list:
        for i in iterm[1:]:
            i.insert(0, iterm[0])
            # print(i)
        del iterm[0]
        print(iterm, len(iterm))
    return trace_eva_list
