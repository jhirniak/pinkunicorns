from celery import Celery


app = Celery('tasks', broker='amqp://guest@162.243.249.145//')


@app.task
def add(x, y):
    return x + y
