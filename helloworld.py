 # -*- coding:utf-8 -*-

import werobot

robot = werobot.WeRoBot(token='tokenhere')

@robot.handler
def hello(message):
    return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8000
robot.run()