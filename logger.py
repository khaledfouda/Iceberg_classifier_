#! /usr/bin/env python
import logging

#---------------------------------------
class logger :
	'''
	A ready to use logging class.
	All you need to do is set an object with the parameters (log_filename, directory to save it)
	then whenever you want to add text, type obj.add("some text").
	The function obj.close() is not important, I just added it for coverage.
	You can edit any of the below configuration to whatever you like.
	'''
	def __init__(self, filename, log_dir='../data/log'):
		self.log = None
		self.handler = None
		LOG_PATH = log_dir
		assert type(filename) == str or filename != ''
		self.logger = logging.getLogger();
		self.logger.setLevel(logging.INFO)
		filename = LOG_PATH + str(filename)
		self.handler = logging.FileHandler(filename)
		self.handler.setLevel(logging.INFO)
		formatter = logging.Formatter(fmt='%(message)s')
		self.handler.setFormatter(formatter)
		self.logger.addHandler(self.handler)
		return
	#------------------------------------
	def add(self, message):
		assert type(message) == str
		self.logger.info(message);
		return
	#------------------------------------
	def close(self):
		self.logger.removeHandler(self.handler)
		return
	#----------------------------------------
