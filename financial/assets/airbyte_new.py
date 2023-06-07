# from dagster import AssetKey, with_resources
# from dagster_airbyte import airbyte_resource, load_assets_from_airbyte_instance, build_airbyte_assets
# from financial.resources import AIRBYTE_PASSWORD, AIRBYTE_USERNAME

# airbyte_instance = airbyte_resource.configured(
#     {
#         "host": "localhost",
#         "port": "8000",
#         "username": AIRBYTE_USERNAME,
#         "password": AIRBYTE_PASSWORD,
#     }
# )

# airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance)


# airbyte_assets = with_resources(
#     build_airbyte_assets(
#         connection_id="af05a274-4391-4233-8b0a-62388dbbb65d",
#         destination_tables=[
#             "organization", 
#             "organization_overview", 
#             "price_history", 
#             "_airbyte_raw_organization", 
#             "_airbyte_raw_organization_overview", 
#             "_airbyte_raw_price_history"
#         ],
#         asset_key_prefix=["financial_data", "financial_raw"]
#     ),
#     {"airbyte": airbyte_instance}
# )
