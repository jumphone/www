```
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

def buildValue(value_content):
    ###生成15s广告故事框架
    start_content_update = '{'+value_content+'}'+'以上内容为一个广告的整体要求，现在设计一个15秒的广告故事框架，该广告要足够吸引人。'
    start_message=[{'role':'user','content': start_content_update }]
    print('以下是15s广告整体框架:')
    start_all_prompts = getResult( start_message )
    ###生成第一帧画面
    start_content_update_2 = '{'+start_all_prompts+'}'+'以上内容为一个15秒广告的故事框架，现在设计一个开场画面，生成用于绘制该开场画面的提示词，用于输入Stable Diffusion生成图像，用英文生成。'
    start_message_2 =[{'role':'user','content': start_content_update_2 }]
    print('以下是广告第一帧提示词:')
    start_img_prompts = getResult( start_message_2 )
    ###使用循环生成20s电影
    start_video_prompts_list=[]
    print('以下是第一个5s的提示词:')
    start_content_update_3 = '{' + start_img_prompts +'}' +'以上为广告开头画面的提示词，现在根据以下15s广告框架设计第一个5秒钟的片段的提示词，{'+start_all_prompts +'}，用于输入WAN生成广告片段，用中文生成提示词'
    start_message_3 = [{'role':'user','content': start_content_update_3 }]
    start_video_prompts_list.append(getResult(start_message_3))
    i=1
    while i < 3 :
        print('以下是第'+str(i+1)+'个片段的提示词:')
        start_content_update_i = '{' + start_all_prompts +'},以上为15s广告故事框架，以下是已经生成的广告片段的提示词：{'+';'.join(start_video_prompts_list)+'}'+', 生成下一个5秒的片段的提示词，用于输入WAN生成广告片段，用中文生成提示词'
        start_message_i = [{'role':'user','content': start_content_update_i }]
        start_video_prompts_list.append(getResult(start_message_i))
        i=i+1
    return( [ start_all_prompts, start_img_prompts , start_video_prompts_list]  )


def run():
    start_content='生成一个武打电影'
    #result1=buildOpen(start_content)
    #result2=buildQuestion(start_content)
    value_content='卖洗发水的广告'
    result3=buildValue(value_content)

```
