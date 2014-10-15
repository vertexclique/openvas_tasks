import openvas_tasks
# openvas_tasks.get_all_tasks(dbpath="/home/mahmut/Downloads/tasks.db")
# openvas_tasks.get_all_tasks()
b = openvas_tasks.Pool("/home/vertexclique/tasks.db")
b.data()

a = openvas_tasks.Pool()
a.data()
