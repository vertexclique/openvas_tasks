#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tasks import *

def get_all_tasks(dbpath="/var/lib/openvas/mgr/tasks.db"):
	b = OvasReceiver()
	if dbpath:
		b.set_db_path(dbpath)
	return b.get_all_tasks_data()