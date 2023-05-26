import os

from dagster import (
    Definitions, ScheduleDefinition, AssetSelection
)
from dagster_dbt import DbtCliClientResource
from financial.assets.dbt import dbt_assets
from financial.assets.airbyte import airbyte_assets
from financial.assets.email import fetch_unchecked, send_email, check_record
from financial.sensors import new_table_modification_sensor
from financial.jobs import refresh_tcbs_job, send_email_job

defs = Definitions(
    assets= airbyte_assets + dbt_assets + [fetch_unchecked, send_email, check_record],
    jobs=[refresh_tcbs_job, send_email_job],
    sensors=[new_table_modification_sensor],
    schedules=[
        ScheduleDefinition(
            job=refresh_tcbs_job,
            cron_schedule="@daily",
        )
    ],
)