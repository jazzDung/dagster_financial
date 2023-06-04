from dagster import AssetKey, with_resources, asset
from dagster_airbyte import airbyte_resource, load_assets_from_airbyte_instance, build_airbyte_assets
from financial.resources import AIRBYTE_PASSWORD, AIRBYTE_USERNAME

airbyte_instance = airbyte_resource.configured(
    {
        "host": "localhost",
        "port": "8000",
        "username": AIRBYTE_USERNAME,
        "password": AIRBYTE_PASSWORD,
    }
)

airbyte_assets = load_assets_from_airbyte_instance(
    airbyte_instance, 
    workspace_id='dd650ead-2a00-4489-bb29-73550f4bf242',
    connection_to_asset_key_fn=lambda c, n: AssetKey([c.name, n]),
)