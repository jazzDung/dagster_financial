from dagster import define_asset_job, AssetSelection,job, op

refresh_tcbs_job = define_asset_job(
    name="refresh_tcbs",
    selection=AssetSelection.all(),
)



def send_email():
    return True

@job
def send_email_job():
    send_email()



