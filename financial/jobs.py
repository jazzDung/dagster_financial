from dagster import define_asset_job, AssetSelection

refresh_tcbs_job = define_asset_job(
    name="refresh_tcbs",
    selection=AssetSelection.all()
)

send_email_job = define_asset_job(
    name="send_email_for_unchecked_query", 
    selection="check_record"
)

