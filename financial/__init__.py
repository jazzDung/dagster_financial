import os

from dagster import (
    Definitions, ScheduleDefinition, AssetSelection
)
from financial.assets.dbt import *
from financial.assets.airbyte import *
from financial.assets.email import *
from financial.sensors import *
from financial.jobs import *
from financial.schedules import *

defs = Definitions(
    assets= [airbyte_assets] + dbt_assets + [fetch_unchecked, send_email, check_record],
    jobs=[ingest_all_job, send_email_job, ingest_stock_history_job, ingest_org_overview_job],
    sensors=[unchecked_records_exist],
    schedules=schedules,
)