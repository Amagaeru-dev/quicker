#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  send_email.py

import mail1

ENCODING = 'utf-8'
SMTP_HOST = "smtp.mail.yahoo.co.jp"
SMTP_PORT = 587
USER_NAME = 'fryfishsee'
PASSWORD = 'pytonsaikou1040'

#~ recipients == 受け取る人
#~ sender == 送信者
mail1.send(subject='Test',
           text='This is a test!',
           recipients='konpebesu@gmail.com',
           sender='fryfishsee@yahoo.co.jp',
           smtp_host='smtp.orange.fr'
           encoding=ENCODING,
           smtp_host=SMTP_HOST,
           smtp_port=SMTP_PORT,
           username=USER_NAME,
           password=PASSWORD)

