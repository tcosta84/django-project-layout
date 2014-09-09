# -*- coding: utf-8 -*-

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(bind=True)
def example_task(self):
    pass
