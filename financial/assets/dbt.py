import os

from dagster import file_relative_path, with_resources
from dagster_dbt import DbtCliClientResource, load_assets_from_dbt_project

DBT_PROJECT_PATH = "/home/jazzdung/projects/dbt_financial"
DBT_PROJECT_DIR = DBT_PROJECT_PATH if os.path.isabs(DBT_PROJECT_PATH) else file_relative_path(__file__, DBT_PROJECT_PATH)
DBT_PROFILE_PATH = "/home/jazzdung/.dbt"
DBT_TARGET = '/home/jazzdung/projects/dbt_financial/target/'

dbt_assets = with_resources(
    load_assets_from_dbt_project(
        project_dir=DBT_PROJECT_DIR, 
        profiles_dir=DBT_PROFILE_PATH, 
        target_dir=DBT_TARGET, 
        source_key_prefix="financial_data",
        key_prefix="raw",
    ),
    {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILE_PATH,
    ),
    }
)