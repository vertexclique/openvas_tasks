#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tasks import *


class Pool(object):
    """docstring for Pool"""

    def __init__(self, dbpath="/var/lib/openvas/mgr/tasks.db"):
        super(Pool, self).__init__()
        self.dbpath = dbpath
        self.recv = OvasReceiver()
        if self.dbpath:
            self.recv.set_db_path(self.dbpath)

    def tasks_data(self):
        return self.recv.get_all_tasks_data()

    def tasks_count(self):
        return self.recv.get_all_tasks_count()

    def results_data(self):
        return self.recv.get_all_results()

    def results_count(self):
        return self.recv.get_all_results_count()

    def shown_tasks(self):
        return self.recv.get_shown_tasks()

    def shown_tasks_count(self):
        return self.recv.get_shown_tasks_count()

    def past_tasks(self):
        return self.recv.get_past_tasks()

    def past_tasks_count(self):
        return self.recv.get_past_tasks_count()

    def task_detail(self, taskid):
        return self.recv.get_task_detail(taskid=taskid)

    def task_detail_count(self, taskid):
        return self.recv.get_task_detail_count(taskid=taskid)

# def data(dbpath="/var/lib/openvas/mgr/tasks.db"):
# b = OvasReceiver()
# if self.dbpath:
# b.set_db_path(self.dbpath)
# return b.get_all_tasks_data()

# def count():
# b = OvasReceiver()
