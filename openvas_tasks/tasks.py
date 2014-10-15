#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ovastypes import *
from datetime import *

# -- Describe TASKS
# CREATE TABLE tasks   (id INTEGER PRIMARY KEY, uuid, owner INTEGER, name, hidden INTEGER, time, comment, description, run_status INTEGER
# , start_time, end_time, config INTEGER, target INTEGER, schedule INTEGER, schedule_next_time, slave INTEGER, config_location INTEGER, 
# target_location INTEGER, schedule_location INTEGER, slave_location INTEGER, upload_result_count INTEGER, creation_time, modification_time)

class OvasReceiver(object):
    """docstring for OvasReceiver"""
    def __init__(self):
        super(OvasReceiver, self).__init__()

    def set_db_path(self, dbpath):
    	database = SqliteDatabase(dbpath)
    	database_proxy.initialize(database)
    	pass

    def get_all_tasks_data(self):
        allscans = []
        print(Tasks._meta.database.__dict__)
        for scan in Tasks.select():
            allscans.append(scan)
        return allscans

    def get_all_tasks_count(self):
        return Tasks.select().count()

    def get_all_results(self):
        allresults = []
        print(Results._meta.database.__dict__)
        for result in Results.select():
            allresults.append(result)
        return allresults

    def get_all_results_count(self):
        return Results.select().count()

