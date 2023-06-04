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

# daily_assets = with_resources(
#     build_airbyte_assets(
#         connection_id="c0f34bc1-fc82-46f5-8cd5-788345bdff8f",
#         destination_tables=[
#             "price_history",
#             # "_airbyte_raw_price_history"
#         ],
#         asset_key_prefix=["price_history"],
#     ),
#     {"airbyte": airbyte_instance}
# )

# quarterly_assets = with_resources(
#     build_airbyte_assets(
#         connection_id="ac349419-681e-4d61-8fe2-80813fba2569",
#         destination_tables=[
#             "organization", 
#             "organization_overview", 
#             # "_airbyte_raw_organization", 
#             # "_airbyte_raw_organization_overview"
#         ],
#         asset_key_prefix=["organization"],
#     ),
#     {"airbyte": airbyte_instance}
# )