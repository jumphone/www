# AI platform

[https://github.com/jumphone/ai](https://github.com/jumphone/ai)


# main_ai_magi.py

```python

from .common_imports import *
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

```


<br>
<br>

# main_ai_movie.py

## Open

```python

from .common_imports import *
from src.util import *

def buildOpen(start_content):
    start_content_update = '{' + start_content + '}' + '以上内容为一个电影的整体要求，现在设计一个开场画面，开场画面需要吸引人，生成用于绘制该开场画面的提示词，用于输入Stable Diffusion生成图像，用英文生成。'
    start_message=[{'role':'user','content': start_content_update }]
    start_img_prompts = getResult( start_message )

    start_content_update_2 = '{' + start_img_prompts +'}' +'以上为电影开头画面的提示词，现在设计一段5秒钟的电影，过程要吸引人，生成用于产生该电影片段的提示词，用于输入WAN生成电影片段，用中文生成'
    start_message_2 = [{'role':'user','content': start_content_update_2 }]
    start_video_prompts = getResult( start_message_2 )
    return( [start_img_prompts , start_video_prompts]  )

def run():
    start_content='生成一个科幻电影'
    result1=buildOpen(start_content)
   
```

## Question

```python

from .common_imports import *
from src.util import *

def buildOpen(start_content):
    start_content_update = '{' + start_content + '}' + '以上内容为一个电影的整体要求，现在设计一个开场画面，开场画面需要吸引人，生成用于绘制该开场画面的提示词，用于输入Stable Diffusion生成图像，用英文生成。'
    start_message=[{'role':'user','content': start_content_update }]
    start_img_prompts = getResult( start_message )

    start_content_update_2 = '{' + start_img_prompts +'}' +'以上为电影开头画面的提示词，现在设计一段5秒钟的电影，过程要吸引人，生成用于产生该电影片段的提示词，用于输入WAN生成电影片段，用中文生成'
    start_message_2 = [{'role':'user','content': start_content_update_2 }]
    start_video_prompts = getResult( start_message_2 )
    return( [start_img_prompts , start_video_prompts]  )

def buildQuestion(start_content):
    ###生成20s电影故事框架
    start_content_update = '{'+start_content+'}'+'以上内容为一个电影的整体要求，现在设计一个20秒的电影故事框架，该电影结尾要留有悬念，吸引观众期待结果，但是电影不给出结果。'
    start_message=[{'role':'user','content': start_content_update }]
    print('以下是20s电影整体框架:')
    start_all_prompts = getResult( start_message )
    ###生成第一帧画面
    start_content_update_2 = '{'+start_all_prompts+'}'+'以上内容为一个20秒电影的故事框架，现在设计一个开场画面，生成用于绘制该开场画面的提示词，用于输入Stable Diffusion生成图像，用英文生成。'
    start_message_2 =[{'role':'user','content': start_content_update_2 }]
    print('以下是电影第一帧提示词:')
    start_img_prompts = getResult( start_message_2 )
    ###使用循环生成20s电影
    start_video_prompts_list=[]
    print('以下是第一个5s的提示词:')
    start_content_update_3 = '{' + start_img_prompts +'}' +'以上为电影开头画面的提示词，现在根据以下20s电影框架设计第一个5秒钟的片段的提示词，{'+start_all_prompts +'}，用于输入WAN生成电影片段，用中文生成'
    start_message_3 = [{'role':'user','content': start_content_update_3 }]
    start_video_prompts_list.append(getResult(start_message_3))
    i=1
    while i < 4 :
        print('以下是第'+str(i+1)+'个片段的提示词:')
        start_content_update_i = '{' + start_all_prompts +'},以上为20s电影故事框架，以下是已经生成的电影片段的提示词：{'+';'.join(start_video_prompts_list)+'}'+', 生成下一个5秒的片段的提示词，用于输入WAN生成电影片段，用中文生成'
        start_message_i = [{'role':'user','content': start_content_update_i }]
        start_video_prompts_list.append(getResult(start_message_i))
        i=i+1
    return( [ start_all_prompts, start_img_prompts , start_video_prompts_list]  )

def run():
    start_content='生成一个科幻电影'
    result1=buildOpen(start_content)
    result2=buildQuestion(start_content)

```






