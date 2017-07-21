#coding=utf8
import itchat
import random
import numpy as np
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import get_response

@itchat.msg_register('Text')
def text_reply(msg):
    msg_clean = msg['Text'].replace(' ', '')
    if msg.user.remarkName == '南小倩' or msg.user.remarkName == '静静':
        if '很棒' in msg_clean:
            return random.choice(['哈哈哈','乖'])
        elif '停' == msg_clean:
            quit()
        elif '不说' in msg_clean:
            return '不跟你玩了'
        elif '讨厌' in msg_clean:
            return '讨厌就是喜欢'
        elif '不爱' in msg_clean:
            return '你可以走了'
        elif '爱你' in msg_clean:
            return '我也爱你'
        elif '喜欢你' in msg_clean:
            return '我你也喜欢你'
        elif '多爱' in msg_clean:
            return '比你爱我更爱你'
        elif '滚' in msg_clean:
            return '滚出去，再滚回来'
        elif '吃了' in msg_clean:
            return '你个吃货'
        elif '没吃' in msg_clean:
            return '快去吃吧'
        elif '没' in msg_clean:
            return '快去'
        elif '你才' in msg_clean:
            return '我选择投降'
        elif '不想' in msg_clean:
            return '你还想不想混了'
        elif '想' in msg_clean or '想你' in msg_clean:
            return '我也想你'
        elif '好烦' in msg_clean:
            return '女人每个月都有那么几天'
        elif '拜拜' in msg_clean or '再见' in msg_clean or '走了' in msg_clean:
            return random.choice(['走了就别回来','别走','爱我别走'])
        elif '开心' in msg_clean:
            return '开心'
        elif '谢谢' in msg_clean:
            return '不客气'
        elif '是不是' in msg_clean:
            return '是'
        elif '吗' in msg_clean:
            return '当然'
        elif '你' in msg_clean or '升' in msg_clean:
            return '真是瞎了眼'
        elif '不玩' in msg_clean:
            return '辛苦了'
        elif '笨蛋' in msg_clean:
            return '二货'
        elif '顶嘴' in msg_clean:
            return '不敢'
        elif '嫁给你' in msg_clean:
            return '好啊'
        elif '娶我' in msg_clean:
            return '娶你'
        elif '生气' in msg_clean:
            return '生气会长皱纹'
        else:
            flag = random.randint(0,10)
            if flag >= 7:
                return random.choice(['快说我很棒','说你爱我','你吃饭了吗','你喜欢谁','你想不想我'])
            else:
                return get_response(msg['Text'])


itchat.auto_login()
itchat.run()
