import os
from dagster import sensor, RunRequest, RunConfig
from financial.jobs import refresh_tcbs_job

# @sensor(job=refresh_tcbs_job, minimum_interval_seconds=30)
# def new_table_v_sensor():
#     yield RunRequest(run_key=None, run_config={})