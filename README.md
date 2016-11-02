# taskserver

This is a basic taskserver to show case using Django along with Celery.  

`post_payload.py` gives an example of how the server is used and to an extent how it works.  

It accepts a JSON payload which describes a task to be run.  

There is also a GET method that should return the status of a requested task.
