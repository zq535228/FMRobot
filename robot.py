# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# 创建一个ChatBot实例，名字为Ptorch，同时你可以任意叫什么
chatbot = ChatBot("Ptorch")

# 训练数据，非必须，但是建议训练
conversation = [
    "你好",
    "朋友你好!",
    "这是哪里?",
    "欢迎来到pytorch中文网",
    "ChatBot是什么？",
    "ChatBot是python开发的聊天机器人",
]
# 设置训练器
#chatbot.set_trainer(ListTrainer)
# 开始训练数据
#chatbot.train(conversation)

# 获取响应，这里只设置单词询问，后期对话看下一篇
response = chatbot.get_response("ChatBot是什么？")
print(response)