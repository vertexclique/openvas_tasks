from peewee import *
from playhouse.proxy import Proxy

database_proxy = Proxy()


class OvasBaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = database_proxy


class Tasks(OvasBaseModel):
    """docstring for Tasks"""
    id = PrimaryKeyField()
    uuid = TextField()
    owner = IntegerField()
    name = TextField()
    hidden = IntegerField()
    time = DateTimeField()
    comment = TextField()
    description = TextField()
    run_status = IntegerField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    config = IntegerField()
    target = IntegerField()
    schedule = IntegerField()
    schedule_next_time = DateTimeField()
    slave = IntegerField()
    config_location = IntegerField()
    target_location = IntegerField()
    schedule_location = IntegerField()
    slave_location = IntegerField()
    upload_result_count = IntegerField()
    creation_time = DateTimeField()
    modification_time = DateTimeField()

    def __init__(self):
        super(Tasks, self).__init__()


class Results(OvasBaseModel):
    """docstring for Results"""
    id = PrimaryKeyField()
    uuid = TextField()
    task = IntegerField()
    subnet = TextField()
    host = TextField()
    port = TextField()
    nvt = TextField()
    type = TextField()
    description = TextField()
    report = IntegerField()

    def __init__(self):
        super(Results, self).__init__()


class Reports(OvasBaseModel):
    """docstring for Reports"""
    id = PrimaryKeyField()
    uuid = TextField()
    owner = IntegerField()
    hidden = IntegerField()
    # task = ForeignKeyField(Tasks, related_name="id")
    task = IntegerField()
    date = DateTimeField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    nbefile = TextField()
    comment = TextField()
    scan_run_status = TextField()
    slave_progress = TextField()
    slave_task_uuid = TextField()
    highs = IntegerField()
    mediums = IntegerField()
    lows = IntegerField()
    logs = IntegerField()
    fps = IntegerField()
    override_highs = IntegerField()
    override_mediums = IntegerField()
    override_lows = IntegerField()
    override_logs = IntegerField()
    override_fps = IntegerField()

    def __init__(self):
        super(Reports, self).__init__()


class Targets(OvasBaseModel):
    """docstring for Targets"""
    id = PrimaryKeyField()
    uuid = TextField()
    owner = IntegerField()
    name = TextField()
    hosts = TextField()
    comment = TextField()
    lsc_credential = IntegerField()
    ssh_port = IntegerField()
    smb_lsc_credential = IntegerField()
    port_range = IntegerField()
    creation_time = DateTimeField()
    modification_time = DateTimeField()

    def __init__(self):
        super(Targets, self).__init__()


class Configs(OvasBaseModel):
    """docstring for Configs"""
    id = PrimaryKeyField()
    uuid = TextField()
    owner = IntegerField()
    name = TextField()
    nvt_selector = TextField()
    comment = TextField()
    family_count = IntegerField()
    nvt_count = IntegerField()
    families_growing = IntegerField()
    nvts_growing = IntegerField()
    creation_time = DateTimeField()
    modification_time = DateTimeField()


class Alerts(OvasBaseModel):
    """docstring for Alerts"""
    id = PrimaryKeyField()
    uuid = TextField()
    owner = IntegerField()
    name = TextField()
    comment = TextField()
    event = TextField()
    condition = IntegerField()
    method = IntegerField()
    filter_col = IntegerField()
    creation_time = DateTimeField()
    modification_time = DateTimeField()


class Slaves(OvasBaseModel):
    """docstring for Slaves"""
    id = PrimaryKeyField()
    uuid = TextField()
    owner = IntegerField()
    name = TextField()
    comment = TextField()
    host = TextField()
    port = IntegerField()
    login = TextField()
    password = TextField()
    creation_time = DateTimeField()
    modification_time = DateTimeField()

    def __init__(self):
        super(Targets, self).__init__()
