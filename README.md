OpenVAS Tasks
============
[![Build Status](https://travis-ci.org/vertexclique/openvas_tasks.svg)](https://travis-ci.org/vertexclique/openvas_tasks)
[![PyPI version](https://badge.fury.io/py/openvas_tasks.svg)](http://badge.fury.io/py/openvas_tasks)
[![Stories in Ready](https://badge.waffle.io/vertexclique/openvas_tasks.png?label=ready&title=Ready)](https://waffle.io/vertexclique/openvas_tasks)

This project is made for interacting with OpenVAS tasks in OpenVAS tasks database. It is used for acquiring all the tasks data,
history of them, report mappings and results. By default it will use the database on scanner machine and contains ORM mappings mostly (but not all of them). If you want to extend this project we happily accept your PRs.
Default installation of OpenVAS tasks database reside in `/var/lib/openvas/mgr/tasks.db`.

## Usage
If you are on scanner machine:

```
import openvas_tasks
b = openvas_tasks.Pool()
b.tasks_count()
```
or if you have your own database:
```
import openvas_tasks
b = openvas_tasks.Pool("/Users/vertexclique/projects/tasks.db")
b.shown_tasks()
```

# API

 - **openvas_tasks.Pool().tasks_data()**
	 - fetches all tasks data from db
 - **openvas_tasks.Pool().tasks_count()**
	 - fetches tasks count from db
 - **openvas_tasks.Pool().results_data()**
	 - fetches all result data from db
 - **openvas_tasks.Pool().results_count()**
	 - fetches results count from db
 - **openvas_tasks.Pool().shown_tasks()**
	 - fetches all shown tasks in any openvas gui (like greenbone)
 - **openvas_tasks.Pool().shown_tasks_count()**
	 - fetches shown tasks count
 - **openvas_tasks.Pool().past_tasks()**
	 - fetches all previous and deleted tasks data
 - **openvas_tasks.Pool().past_tasks_count()**
	 - fetches previous and deleted tasks count
 - **openvas_tasks.Pool().task_detail(taskid)**
	 - fetches all task detail with specified task id
 - **openvas_tasks.Pool().task_detail_count(taskid)**
	 - fetches task detail count from db

## Fields of Objects
Object fields of results. Currently:

* Tasks
* Results
* Reports
* Targets

are browsable.

### Tasks

 - id = `id of task`
 - uuid = `uuid of task`
 - owner = `owner id of the task`
 - name = `task name`
 - hidden = `is shown in scan task listing or not?`
 - time = `time for ongoing scan`
 - comment = `comment for the scan`
 - description = `description of the scan`
 - run_status = `run status of the scan`
 - start_time = `start time`
 - end_time = `end time`
 - config = `which configs enabled in this scan`
 - target = `target id`
 - schedule = `schedule if set`
 - schedule_next_time = `next time of the schedule if set`
 - slave = `slave scan runner id`
 - config_location = `config location`
 - target_location = `target location`
 - schedule_location = `schedule location`
 - slave_location = `slave location`
 - upload_result_count = `upload result count`
 - creation_time = `creation time of task`
 - modification_time = `modification time of task`

### Results


- id = `id of result`
- uuid = `uuid of result`
- task = `linked task of the result`
- subnet = `subnet of the target`
- host = `host of the result owner target`
- port = `port of the target that has vulnerability`
- nvt = `openvas nvt oid`
- type = `type of vulnerability`
- description = `description of vulnerability`
- report = `report id that is linked to specific result`

### Reports

 - id = `id of report`
 - uuid = `uuid of report`
 - owner = `owner id of report`
 - hidden = `hidden in UI or not`
 - task = `related task`
 - date = `date of it`
 - start_time = `start time of linked scan`
 - end_time = `end time of linked scan task`
 - nbefile = `nbe file path`
 - comment = `comment of report`
 - scan_run_status = `scan run status`
 - slave_progress = `slave progress`
 - slave_task_uuid = `slave task uuid`
 - highs = `high level vulnerability count`
 - mediums = `medium level vulnerability count`
 - lows = `low level vulnerability count`
 - logs = `log level vulnerability count`
 - fps = `FPs`
 - override_highs = `overridden highs`
 - override_mediums = `overridden mediums`
 - override_lows = `overridden lows`
 - override_logs = `overridden logs`
 - override_fps = `overridden FPs`

### Targets

- id = `id of the target`
- uuid = `uuid of the target`
- owner = `target owner id`
- name = `name of the target`
- hosts = `hosts of target`
- comment = `comment for target`
- lsc_credential = `local security check credentials`
- ssh_port = `ssh port`
- smb_lsc_credential = `smb lsc credentials`
- port_range = `port range for target whatever the task hits for`
- creation_time = `creation time for target`
- modification_time = `modification time of target`

### Configs

- id = `configs id`
- uuid = `configs uuid`
- owner = `config owner id`
- name = `config name`
- nvt_selector = `nvt feed selector`
- comment = `comment for configs`
- family_count = `family count of nvts`
- nvt_count = `nvt count`
- families_growing = `expanded family listings count`
- nvts_growing = `expanded nvt listings count`
- creation_time = `creation time for config`
- modification_time = `modification time for config`

### Alerts

- id = `id for alert`
- uuid = `uuid for alert`
- owner = `owner id for alert`
- name = `name of alert`
- comment = `comment of alert`
- event = `event of alert`
- condition = `condition of alert`
- method = `alert method`
- filter_col = `filter column for multiple alert types`
- creation_time = `creation time for alert`
- modification_time = `modification time for alert`

### Slaves
**This object is used in master-slave mode. It won't exist if you have single point installation.**

- id = `id for slave`
- uuid = `uuid for slave`
- owner = `owner id for slave`
- name = `name for slave`
- comment = `comment for slave`
- host = `host of the slave`
- port = `port of the slave`
- login = `login of the slave`
- password = `password of the slave`
- creation_time = `creation time for slave`
- modification_time = `modification time for slave`