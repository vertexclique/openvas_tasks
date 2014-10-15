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
		