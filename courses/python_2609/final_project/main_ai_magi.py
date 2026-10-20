rom .common_imports import *
from src.util import *

################################
def run():
    new_messages=[{'role':'user', 'content':'最应该学什么'}]
    bkg_messages_1 = [{'role':'system', 'content':'所有回复都用中文，所有回复都用科学家视角口吻身份,回答在200字以内'}]
    bkg_messages_2 = [{'role':'system', 'content':'所有回复都用中文，所有回复都用女性视角口吻身份，回答在200字以内'}]
    bkg_messages_3 = [{'role':'system', 'content':'所有回复都用中文，所有回复都用母亲视角口吻身份，回答在200字以内'}]
    all_messages_1 = bkg_messages_1 + new_messages
    all_messages_2 = bkg_messages_2 + new_messages
    all_messages_3 = bkg_messages_3 + new_messages
    print('科学家:')
    result1 = getResult(all_messages_1)
    print('女性:')
    result2 = getResult(all_messages_2)
    print('母亲:')
    result3 = getResult(all_messages_3)
    #####################
    fo1=open('result1.txt','w')
    fo2=open('result2.txt','w')
    fo3=open('result3.txt','w')
    fo1.write(result1)
    fo2.write(result2)
    fo3.write(result3)
    fo1.close()
    fo2.close()
    fo3.close()
    ################
    result_messages_1=[{'role':'assistant','content':result1}]
    result_messages_2=[{'role':'assistant','content':result2}]
    result_messages_3=[{'role':'assistant','content':result3}]
    sum_messages = [{'role':'user', 'content':'用中文综合所有回答内容进行总结回复,回答在200字以内'}]
    all_messages_4 = new_messages + result_messages_1 + result_messages_2 + result_messages_3 + sum_messages
    print('综合:')
    sum_result = getResult(all_messages_4)
    #############################
    fo_sum=open('result_sum.txt','w')
    fo_sum.write(sum_result)
    fo_sum.close()
    #########################
