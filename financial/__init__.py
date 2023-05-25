import os

from dagster import (
    Definitions, define_asset_job, ScheduleDefinition,
)
# from dagster_airbyte import airbyte_resource
from dagster_dbt import DbtCliClientResource
from financial.assets.dbt import dbt_assets, DBT_PROJECT_PATH, DBT_PROFILE_PATH 
from financial.assets.airbyte import airbyte_assets
from financial.jobs import refresh_tcbs_job
# from financial.schedules import schedules

resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILE_PATH,
    ),
}

defs = Definitions(
    assets= airbyte_assets + dbt_assets,
    resources=resources,
    jobs=[refresh_tcbs_job],

    schedules=[
        ScheduleDefinition(
            job=refresh_tcbs_job,
            cron_schedule="@daily",
        )
    ],
)