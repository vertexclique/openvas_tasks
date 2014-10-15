#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tasks import *

class Pool(object):
	"""docstring for Pool"""
	def __init__(self, dbpath="/var/lib/openvas/mgr/tasks.db"):
		super(Pool, self).__init__()
		self.dbpath = dbpath
		self.recv = OvasReceiver()

	def data(self):
		if self.dbpath:
			self.recv.set_db_path(self.dbpath)
		return self.recv.get_all_tasks_data()

	def count(self):
		return recv.get_all_tasks_count()
		

# def data(dbpath="/var/lib/openvas/mgr/tasks.db"):
# 	b = OvasReceiver()
# 	if self.dbpath:
# 		b.set_db_path(self.dbpath)
# 	return b.get_all_tasks_data()

# def count():
# 	b = OvasReceiver()
