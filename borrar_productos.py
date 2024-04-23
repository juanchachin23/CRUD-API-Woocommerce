from woocommerce import API

def delete_product():
    """
    Deletes a product from the WooCommerce store using the WooCommerce API.

    Returns:
        dict: The JSON response from the API call.
    """
    wcapi = API(
        url="https://appcorezulia.lat/n1",
        consumer_key="ck_9bded2550e24bc4329bf2ababec8c904c767d181",
        consumer_secret="cs_ee901287d6b833bbff11aa0e0f60ab5dcb43c7c2",
        version="wc/v3"
    )

    return wcapi.delete("products/34", params={"force": True}).json()

print(delete_product())
