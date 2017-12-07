from celery import task

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task()
def add(x, y):
    return x + y


@task(bind=True)
def div(self,x, y):
    logger.info(('Execting task_id {0.id}, args:{0.args!r} '
                 'kwargs: {0.kwargs!r}').format(self.request))
    try:
        result =  x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=5, max_retries=3)
    return result