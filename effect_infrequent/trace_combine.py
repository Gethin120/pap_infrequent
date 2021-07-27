from gethin_algorithm.printXES import *

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


if __name__ == '__main__':
    traces_frequent = ['abcdfhiklmyz*1', 'abcdehiklmopqstvz*1', 'abcdehjklmopruwxvz*1', 'abcdfhjklnpruwxvz*1',
                       'abcdehjklnprtvz*1', 'abcdghiklmyz*1', 'abcdfhjklnpqstvz*1', 'abcdehjklmopqsvz*1',
                       'abcdghjklmoprtvz*1', 'abcdghjklmopqsvz*1']
    traces_infrequent = ['abcdehiklmoptvz*1', 'abcdehiopqsvz*1', 'abcdhejklmoprwxvz*1', 'abcdheiklmopwrxvz*1']

    trace_all_combine, trace_all_combine_name = traces_infrequent_all_combine(traces_frequent, traces_infrequent)
