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
    result2=buildQuestion(start_content)

```


## Value

```python


from .common_imports import *
from src.util import *

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
    ###使用循环生成15s广告
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
    start_content='生成一个科幻电影'
    value_content='卖洗发水的广告'
    result3=buildValue(value_content)


```

## Answer


```python

# Complete Code for AI Platform: https://github.com/jumphone/ai


from .common_imports import *
from src.util import *

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

def buildAnwser(question_content):
    ###生成20s电影故事框架
    start_content_update = '{'+question_content+'}'+'以上内容为一个悬疑电影的框架，现在设计一个20秒的接下来的框架，该电影结尾要消除悬念，帮助观众给出结果。'
    start_message=[{'role':'user','content': start_content_update }]
    print('以下是20s电影整体框架:')
    start_all_prompts = getResult( start_message )
    ###生成第一帧画面
    start_content_update_2 = '{'+start_all_prompts+'}'+'以上内容为一个20秒电影的故事框架，现在设计一个开场画面，生成用于绘制该开场画面的提示>词，用于输入Stable Diffusion生成图像，用英文生成。'
    start_message_2 =[{'role':'user','content': start_content_update_2 }]
    print('以下是电影第一帧提示词:')
    start_img_prompts = getResult( start_message_2 )
    ###使用循环生成20s电影
    start_video_prompts_list=[]
    print('以下是第一个5s的提示词:')
    start_content_update_3 = '{' + start_img_prompts +'}' +'以上为电影开头画面的提示词，现在根据以下20s电影框架设计第一个5秒钟的片段的提示词>，{'+start_all_prompts +'}，用于输入WAN生成电影片段，用中文生成'
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
    result2=buildQuestion(start_content)
    result4=buildAnwser(result2[0])

```
<br>


## Making Movie

Doubao + wan2_2_start2end (start2end, start and end frames)

### 1. Generate film script

Use the revised "main_ai" to generate the full film script.

### 2. Adjust storyboards and transition shots

Tool: Doubao (work task)

Input: The complete film script produced by main_ai

Prompt: Ignore the original segmentation. Extract key frames with scenes, characters and camera changes based on the story framework, and create detailed prompts for these key frame images. Prepare detailed prompts for transition clips linking these frames (wan2_2). Save them into two separate TXT files with sequential numbering.

### 3. Generate character and scene assets

Tool: Doubao (work task)

Input: The two TXT files from Step 2

Prompt: Create front-view portraits of core characters on plain white backgrounds. Create background scene plates with no characters. Also generate images for supporting     characters and secondary environments.

### 4. Generate key frame images

Tool: Doubao (work task)

Input: The two TXT files from Step 2, plus character and scene assets from Step 3

Prompt: Generate all key frame images using the provided reference images and prompts. Name the files sequentially starting from 01 and save them to the desktop.

### 5. Generate transition footage

Tool: ComfyUI, wan2_2_start2end

Input: Key frame images from Step 4, transition prompts from Step 2.

### 6. Video editing and voiceover

Tool: Jianying

Input: Stitch together the video clips produced in Step 5


<br>
<br>
<br>

## 制作电影

豆包 + wan2_2_start2end (start2end, 首尾帧)

### 1. 生成电影脚本

使用修改后的 “main_ai” 生成所有电影脚本

### 2. 调整分镜和过度镜头   

工具：豆包（工作任务）

输入：main_ai 产生的完整电影脚本

提示词：不要在乎原有的分段，基于故事框架，提取出带有场景、人物、镜头变化的，适合作为关键帧，形成用于生成这些关键帧画面的详细提示词。在画面之间形成中文的适合作为提示词详细的连接视频的提示词(适用于wan2_2)。分别放到两个txt文件里。标好顺序

### 3. 生成人物和场景素材

工具：豆包（工作任务）

输入：第2步产生的两个txt文件

提示词：形成关键人物角色的正面图、背景白色。形成关键场景的背景图，背景图不要有人物。还有配角的图像，和附属场景的图像.

### 4. 生成关键帧图像

工具：豆包（工作任务）

输入：第2步产生的两个txt文件，第3步产生的人物和场景素材

提示词：基于给的图片和提示词，生成所有关键帧的图片，并且按顺序从01开始往后命名放到桌面。

### 5. 生成过度镜头影像

工具：ComfyUI, wan2_2_start2end

输入：第4步生成的关键帧图像，第2步生成的过渡镜头（连接关键帧影像）的提示词.

### 6. 视频剪辑和配音

工具：剪映

输入：第5步产生的视频拼接起来





















