from dagster import ScheduleDefinition
from financial.jobs import *

schedules=[
    ScheduleDefinition(
        job=ingest_stock_history_job,
        cron_schedule="@daily",
    ),
    ScheduleDefinition(
        job=ingest_org_overview_job,
        cron_schedule="* * * 1-12/3 *",
    )
]