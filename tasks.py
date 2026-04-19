# Celery Tasks
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def send_alert(message):
    print(f'Sending alert: {message}')

if __name__ == '__main__':
    app.start()