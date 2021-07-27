from gethin_algorithm.printXES import *
from gethin_API.process_discovery import *
from pm4py.evaluation import *
from pm4py.objects.log.importer.xes import importer as xes_importer
import itertools
import copy
from matplotlib import pyplot as plt

traces_origin = ['abcdfhiklmyz*7964', 'abcdehiklmopqstvz*4358', 'abcdehjklmopruwxvz*3239', 'abcdfhjklnpruwxvz*3018',
                 'abcdehjklnprtvz*2865', 'abcdghiklmyz*2852', 'abcdfhjklnpqstvz*2574', 'abcdehjklmopqsvz*2457',
                 'abcdghjklmoprtvz*1782', 'abcdghjklmopqsvz*1371', 'abcdehiklmoptvz*75', 'abcdehiopqsvz*56',
                 'abcdhejklmoprwxvz*11', 'abcdheiklmopwrxvz*7']
traces_frequent = ['abcdfhiklmyz*1', 'abcdehiklmopqstvz*1', 'abcdehjklmopruwxvz*1', 'abcdfhjklnpruwxvz*1',
                   'abcdehjklnprtvz*1', 'abcdghiklmyz*1', 'abcdfhjklnpqstvz*1', 'abcdehjklmopqsvz*1',
                   'abcdghjklmoprtvz*1', 'abcdghjklmopqsvz*1']
traces_infrequent = ['abcdehiklmoptvz*1', 'abcdehiopqsvz*1', 'abcdhejklmoprwxvz*1', 'abcdheiklmopwrxvz*1']
len_trace_frequent=len(traces_frequent)
len_trace_infrequent=len(traces_infrequent)

def model_evaluator_fscore(log_model,log_check):
    net, initial_marking, final_marking = alpha_miner(log_model)
    result = evaluator.apply(log_check, net, initial_marking, final_marking)
    result_fcore=result['fscore']
    return result_fcore
log_check = xes_importer.apply('trace_origin.xes')
log_base = xes_importer.apply('trace_.xes')
trace__fscore=model_evaluator_fscore(log_base,log_check)
print(trace__fscore)
def tuple_index(tup=(), traces=[]):
    # 由traces_infrequent_all_combine引用
    name = 'trace'
    for t in tup:
        if t in traces:
            # print(traces.index(t))
            name = name + '_' + str(traces.index(t))
    # print(name)
    return name
def traces_infrequent_all_combine(traces_frequent, traces_infrequent):
    """
    频繁迹+将非频繁迹的   全    组合，生成包含序列名的xes文件。包含trace_即没加infrequent元素
    :param trace_frequent:频繁迹列表
    :param traces_infrequent:非频繁迹列表
    :return traces_combine:返回频繁迹+非频繁迹的全组合
    :return traces_combine_name:返回每个组合的名字
    """
    import itertools
    from copy import deepcopy
    traces_frequent_copy = deepcopy(traces_frequent)
    trace_all_combine = []
    temp = deepcopy(traces_frequent)
    trace_all_combine.append(temp)
    trace_all_combine_name = ['trace_']
    for i in range(1, len(traces_infrequent) + 1):
        for j in itertools.permutations(traces_infrequent, i):
            traces_frequent.extend(list(j))
            # print(traces_frequent)
            name_add = tuple_index(j, traces_infrequent)
            trace_all_combine_name.append(name_add)
            # print(name_add)
            trace_all_combine.append(traces_frequent)
            traces_frequent = deepcopy(traces_frequent_copy)
    # print(trace_all_combine)
    # print(trace_all_combine_name)
    # print(len(trace_all_combine), len(trace_all_combine_name))
    for i in range(len(trace_all_combine)):
        print_xes_from_list(trace_all_combine[i], trace_all_combine_name[i])
    return trace_all_combine, trace_all_combine_name
trace_all_combine,trace_all_combine_name=traces_infrequent_all_combine(traces_frequent,traces_infrequent)

def creat_trace_eva_list(traces_frequent,traces_infrequent):
    trace_eva_list=[]
    list1=[i for i in range(len(traces_infrequent))]
    tem = copy.deepcopy(list1)
    for i in range(len(list1)):
        list1.pop(i)
        print(list1)
        aa = itertools.permutations(list1, 3)
        # print(list(aa))
        trace_name='trace_'+str(i)
        trace_name_ori=copy.deepcopy(trace_name)
        list_trace_name=[trace_name]
        # list_trace_name=[]
        for item in list(aa):
            print(item)
            temp=[]
            for i in range(len(item)):
                trace_name+='_'+str(item[i])
                temp.append(trace_name)
            list_trace_name.append(temp)
            trace_name=copy.deepcopy(trace_name_ori)

        print(list_trace_name)
        trace_eva_list.append(list_trace_name)
        # print(list(aa))
        list1 = copy.deepcopy(tem)
    for iterm in trace_eva_list:
        for i in iterm[1:]:
            i.insert(0, iterm[0])
            print(i)
        del iterm[0]
        print(iterm, len(iterm))
    return trace_eva_list
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
            print(i+'.xes')
            log_model = xes_importer.apply(i + ".xes")
            result = model_evaluator_fscore(log_model, log_check)
            result_list.append(result)
        result_list_dict[item[-1]]=result_list
        result_list=[]
    # print(result_list_dict_list,len(result_list_dict_list))
    x = list(range(0, len_trace_infrequent+1,1))
    print(x)
    fig, ax = plt.subplots()
    for i in result_list_dict.items():
        temp=[]
        temp.append(trace__fscore)
        temp.extend(i[1])
        ax.plot(x, temp, label=i[0])
        print(i[0])
    ax.legend()
    plt.show()
    print(result_list_dict)


trace_eva_list=creat_trace_eva_list(traces_frequent,traces_infrequent)
# print(trace_eva_list)

for i in trace_eva_list:

    infrequent_log_miner_all_combine(i)
# infrequent_log_miner_all_combine(trace_eva_list[3])
# trace_=xes_importer.apply('./traces-origin.xes')
# trace_3=xes_importer.apply('./trace_3.xes')
# trace_3_0=xes_importer.apply('./trace_3_0.xes')
# trace_3_1=xes_importer.apply('./trace_3_1.xes')
# trace_3_0_1=xes_importer.apply('./trace_3_0_1.xes')
# trace_3_0_1_2=xes_importer.apply('./trace_3_0_1_2.xes')
# a=model_evaluator_fscore(trace_3,trace_)
# b=model_evaluator_fscore(trace_3_0,trace_)
# print(model_evaluator_fscore(trace_3_1,trace_))
# c=model_evaluator_fscore(trace_3_0_1,trace_)
# d=model_evaluator_fscore(trace_3_0_1_2,trace_)
# print(b)
# fig,axx=plt.subplots()
# x=np.arange(0,4)
# y=[a,b,c,d]
# axx.plot(x,y)
# axx.legend()
# plt.show()



