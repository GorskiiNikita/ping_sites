from ping_sites.celery import app


@app.task
def ping_site():
    return 'ping'






