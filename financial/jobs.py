from dagster import define_asset_job, AssetSelection
from financial.assets.airbyte import *

ingest_all_job = define_asset_job(
    name="INGEST_EVERYTHING_EVERYWHERE_ALL_AT_ONCE",
    description="Ingest every available data",
    selection=AssetSelection.all()
)

send_email_job = define_asset_job(
    name="SEND_EMAIL_FOR_UNCHECKED_QUERY", 
    description="Check for record that have field value equal False every 30 seconds, then send email to the email in those records",
    selection=AssetSelection.keys("check_record")
        .upstream()
        .required_multi_asset_neighbors()
)

ingest_stock_history_job = define_asset_job(
    name="INGEST_STOCK_HISTORY", 
    description="Ingest stock price history, this job run daily",
    selection= AssetSelection.keys("financial_clean/dim_price_history")
        .upstream()
        .required_multi_asset_neighbors()
    )

ingest_org_overview_job = define_asset_job(
    name="INGEST_ORGANIZATION_OVERVIEW", 
    description="Ingest organization overview information, this job run at the start every quarter",
    selection= AssetSelection.keys("financial_clean/dim_organization_overview")
        .upstream()
        .required_multi_asset_neighbors()
    )