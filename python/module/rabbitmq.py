#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#===========================================
#   文件名称：rabbitmq.py
#   创 建 者：ZeQun
#   创建日期：2017年04月18日
#   描    述：
#   Copyright (C) 2017 All rights reserved.
#===========================================
import pika
credentials = pika.PlainCredentials('$USER','$PASS')
connection = pika.BlockingConnection(pika.ConnectionParameters(
	'$IP',5672,'$VHOST',credentials))

def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)
channel = connection.channel()

channel.queue_declare(queue='MY.celery_music')

channel.basic_publish(exchange='Test',
						routing_key='balance',
						body='Hello World!')
#channel.basic_consume(callback,
#		queue='balance',)
print(" [x] Sent 'Hello World!'")
connection.close()
