 # -*- coding:utf-8 -*-

import werobot

robot = werobot.WeRoBot(token='football1898tokenhere')

@robot.handler
def hello(message):
	 print message
	 return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
