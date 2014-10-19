[![Stories in Ready](https://badge.waffle.io/vertexclique/openvas_tasks.png?label=ready&title=Ready)](https://waffle.io/vertexclique/openvas_tasks)
OpenVAS Tasks
============
[![Build Status](https://magnum.travis-ci.com/vertexclique/openvas_tasks.svg?token=bkEkktEjr45s2RgAZavn)](https://magnum.travis-ci.com/vertexclique/openvas_tasks)
[![PyPI version](https://badge.fury.io/py/openvas_tasks.svg)](http://badge.fury.io/py/openvas_tasks)

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
## Fields
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
