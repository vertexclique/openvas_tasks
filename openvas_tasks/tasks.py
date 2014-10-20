#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ovastypes import *


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
        # print(Tasks._meta.database.__dict__)
        for scan in Tasks.select():
            allscans.append(scan)
            return allscans

    def get_all_tasks_count(self):
        return Tasks.select().count()

    def get_all_results(self):
        allresults = []
        # print(Results._meta.database.__dict__)
        for result in Results.select():
            allresults.append(result)
        return allresults

    def get_all_results_count(self):
        return Results.select().count()

    def get_shown_tasks(self):
        shownscans = []
        for scan in \
                Tasks.select(Tasks.target, Tasks.name, fn.Count(Reports.task).alias('total'), Targets.hosts,
                             Tasks.run_status, Tasks.start_time, Tasks.end_time) \
                        .join(Reports, on=(Reports.task == Tasks.id)) \
                        .join(Targets, on=(Targets.id == Tasks.target)) \
                        .where((Tasks.hidden == 0)) \
                        .naive() \
                        .group_by(Reports.task):
            shownscans.append(scan)
        return shownscans

    def get_shown_tasks_count(self):
        return Tasks.select() \
            .join(Reports, on=(Reports.task == Tasks.id)) \
            .where((Tasks.hidden == 0)) \
            .naive() \
            .group_by(Reports.task) \
            .count()

    def get_past_tasks(self):
        pasttasks = []
        for scan in \
                Tasks.select(Tasks.name, fn.Count(Reports.task).alias('total'), Targets.hosts, Tasks.run_status,
                             Tasks.start_time, Tasks.end_time) \
                        .join(Reports, on=(Reports.task == Tasks.id)) \
                        .join(Targets, on=(Targets.id == Tasks.target)) \
                        .where((Tasks.hidden != 0)) \
                        .naive() \
                        .group_by(Reports.task):
            pasttasks.append(scan)
        return pasttasks

    def get_past_tasks_count(self):
        return Tasks.select() \
            .join(Reports, on=(Reports.task == Tasks.id)) \
            .where((Tasks.hidden != 0)) \
            .naive() \
            .group_by(Reports.task) \
            .count()

    def get_task_detail(self, taskid):
        shownscans = []
        for scan in \
                Reports.select(Tasks.name, Tasks.comment, Configs.name, Tasks.schedule, Targets.name, Slaves.name, \
                               Reports.scan_run_status, Reports.date, Reports.task, Reports.highs, Reports.mediums,
                               Reports.lows, Reports.logs, \
                               Reports.fps, ) \
                        .join(Tasks, on=(Reports.task == Tasks.id)) \
                        .join(Configs, on=(Configs.id == Tasks.config)) \
                        .join(Targets, on=(Targets.id == Tasks.target)) \
                        .join(Slaves, on=(Slaves.id == Tasks.slave)) \
                        .where((Reports.task == taskid)) \
                        .naive():
            shownscans.append(scan)
        return shownscans

    def get_task_detail_count(self, taskid):
        return Reports.select(Reports.date, Reports.task, Reports.highs, Reports.mediums, Reports.lows, Reports.logs,
                              Reports.fps) \
            .where((Reports.task == taskid)) \
            .naive() \
            .count()