from dagster import define_asset_job, AssetSelection

refresh_tcbs_job = define_asset_job(
    name="refresh_tcbs",
    selection=AssetSelection.all(),
)