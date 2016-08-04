#!/usr/bin/env python
#-*- coding: UTF-8 -*
#coding:utf-8 
# -*- coding: utf-8 -*-
import os.path
import re
import redis
import time
import tornado.auth
import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import sys
import random
import hashlib
import requests
import urllib2
import urllib
from random import sample
import copy
import tornado.autoreload 
import operator
import socket
from tornado.options import define, options
import json
import config
from Models.usersmodel import UsersModel
from Models.notemodel import NoteModel
from Models.notecommodel import NoteComModel
from Models.postmodel import PostModel
from Models.postcommodel import PostComModel
from Func.publicfunc import PublicFunc
# from Func.publicfunc import PublicFunc
from bson.objectid import ObjectId

class ShareController:
	def __init__(self):
		self.share_title = options.share_title

	def share_post(self,post_id):
		post_info = PostModel().get_post_info(post_id)
		share_url = 'http://101.200.214.68/RunCircle/index.html?uid=35&token=83adde48c7654c46ae1bbe73fdac93bd&cat=ios#/app/hudongxiangqing/57a2a21eea766f2a3fa43b33'
		token_pos = share_url.find('token')
		share_url = share_url[:token_pos] + share_url[token_pos + 39:]
		share_dict = {'title':self.share_title,'content':post_info['content'],'image':options.ipnet + post_info['pic_list'][0],'url':share_url}
		return share_dict

	def share_note(self,note_id):
		note_info = NoteModel().get_note_info(note_id)
		share_url = 'http://101.200.214.68/RunCircle/index.html?uid=35&token=83adde48c7654c46ae1bbe73fdac93bd&cat=ios#/app/tiezixiangqing/577d0baeea766f096a0a611b'
		token_pos = share_url.find('token')
		share_url = share_url[:token_pos] + share_url[token_pos + 39:]
		share_dict = {'title':self.share_title,'content':note_info['title'],'image':'not have','url':share_url}
		return share_dict
