from woocommerce import API

wcapi = API(
    url="https://appcorezulia.lat/n1",
    consumer_key="ck_9bded2550e24bc4329bf2ababec8c904c767d181",
    consumer_secret="cs_ee901287d6b833bbff11aa0e0f60ab5dcb43c7c2",
    version="wc/v3"
)

data = {
   
}

print(wcapi.put("products/23", data).json())