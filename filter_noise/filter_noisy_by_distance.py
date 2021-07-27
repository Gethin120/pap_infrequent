import copy
import itertools
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pm4py.objects.log.importer.xes import importer as xes_importer
from gethin_algorithm.printXES import *

# matplotlib.rcParams['font.family']='STSong'#修改了全局变量
# matplotlib.rcParams['font.size']=20
traces_frequent = ['abcdfhiklmyz*1', 'abcdehiklmopqstvz*1', 'abcdehjklmopruwxvz*1', 'abcdfhjklnpruwxvz*1',
                   'abcdehjklnprtvz*1', 'abcdghiklmyz*1', 'abcdfhjklnpqstvz*1', 'abcdehjklmopqsvz*1',
                   'abcdghjklmoprtvz*1', 'abcdghjklmopqsvz*1']
traces_infrequent = ['abcdehiklmoptvz*1', 'abcdehiopqsvz*1', 'abcdhejklmoprwxvz*1', 'abcdheiklmopwrxvz*1','abcdfhikglmynz*1','abdfhklyz*1']
#加了两条噪音，在频繁迹1的基础上增加和删除若干活动。
from pm4py.algo.clustering.trace_attribute_driven.variants.act_dist_calc import act_sim_percent_avg
from pm4py.algo.clustering.trace_attribute_driven.variants.suc_dist_calc import suc_sim_percent_avg
from pm4py.algo.clustering.trace_attribute_driven.util.evaluation import eval_avg_variant


def creat_xes(traces_frequent,traces_infrequent):
    len_fre=len(traces_frequent)
    len_infre=len(traces_infrequent)
    for i in range(len_fre):
        tem = []
        name = 'trace' + str(i)
        tem.append(traces_frequent[i])
        print_xes_from_list(tem, name)
    for i in range(len_infre):
        tem = []
        name = 'trace' + str(i + len_fre)
        tem.append(traces_infrequent[i])
        print_xes_from_list(tem, name)
creat_xes(traces_frequent,traces_infrequent)
def distance_beh(log1,log2,alpha=0.5):
    """
    behavioral inter_trace distance

    :param log1:
    :param log2:
    :param alpha: 0.5
    :return:
    """
    dist_act=act_sim_percent_avg(log1,log2,1,1)
    dist_suc=suc_sim_percent_avg(log1,log2,1,1)
    dist_beh=dist_act * alpha + dist_suc * (1 - alpha)
    return dist_beh


def creat_log_one_trace_list(traces_frequent,traces_infrequent):
    """
    生成单条迹的日志对象列表，分频繁和非频繁

    :param traces_frequent:
    :param traces_infrequent:
    :return:
    """
    log_fre_list = []
    log_infre_list = []
    for i in range(len(traces_frequent)):
        temp=xes_importer.apply('./trace'+str(i)+'.xes')
        log_fre_list.append(temp)
    # print(log_fre_list)
    # print(len(log_fre_list))

    for i in range(len(traces_infrequent)):
        temp=xes_importer.apply('./trace'+str(i+len(traces_frequent))+'.xes')
        log_infre_list.append(temp)
    # print(len(log_infre_list))
    return log_fre_list,log_infre_list

log_fre_list,log_infre_list=creat_log_one_trace_list(traces_frequent,traces_infrequent)
def filter_noisy_by_distance(log_fre_list,log_infre_list):
    log_fre_result=eval_avg_variant(log_fre_list,1,0.5)
    print(log_fre_result)
    print(len(log_fre_result))
    avg_val=sum(log_fre_result) / len(log_fre_result)
    max_val=max(log_fre_result)
    min_val=min(log_fre_result)
    print(avg_val)
    x = np.arange(len(log_fre_list))
    result_list=[]
    for item in log_infre_list:
        result = []
        for i in range(len(log_fre_list)):
            result.append(distance_beh(item,log_fre_list[i]))
        # print(result)
        result_list.append(result)
    print(result_list)

    fig, ax = plt.subplots(figsize=(8,4),dpi=600)
    ii=0
    format_str=["-,","-x","-^","-d","-o","-*"]
    for item in result_list:
        ax.plot(x, item, format_str[ii],label=str(ii))
        ii+=1

    from matplotlib import font_manager
    # 实例化 font_manager
    my_font = font_manager.FontProperties(family='SimHei', size=24)

    ax.legend(loc=4)
    plt.axhline(y=avg_val)
    plt.axhline(y=min_val)
    plt.axhline(y=max_val)
    # plt.xlabel('频繁项集',fontproperties=my_font,fontsize=10)
    # plt.ylabel('迹间距离',fontproperties=my_font,fontsize=10)
    plt.savefig('filetr_noisy_by_distance.png')
    plt.show()
filter_noisy_by_distance(log_fre_list,log_infre_list)

