import openvas_tasks
# openvas_tasks.get_all_tasks(dbpath="/home/mahmut/Downloads/tasks.db")
# openvas_tasks.get_all_tasks()
# b = openvas_tasks.Pool("/Users/vertexclique/projects/tasks.db")
b = openvas_tasks.Pool("/home/travis/build/vertexclique/openvas_tasks/tasks.db")
b.tasks_data()
b.tasks_count()
b.results_data()
b.results_count()
b.shown_tasks()
b.shown_tasks_count()
b.past_tasks()
b.past_tasks_count()
b.task_detail(4)
assert b.task_detail_count(4) == 8

# a = openvas_tasks.Pool()
# a.tasks_data()
