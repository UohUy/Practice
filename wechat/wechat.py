#!/usr/bin/python
# coding = utf-8

import itchat
from itchat.content import *

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
itchat.auto_login(True)
itchat.run()