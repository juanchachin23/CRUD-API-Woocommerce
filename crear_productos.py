import tkinter as tk
from woocommerce import API

# Initialize the WooCommerce API
wcapi = API(
    url="https://appcorezulia.lat/n1",
    consumer_key="ck_9bded2550e24bc4329bf2ababec8c904c767d181",
    consumer_secret="cs_ee901287d6b833bbff11aa0e0f60ab5dcb43c7c2",
    version="wc/v3"
)

def create_product():
    # Get the product data from the entry fields
    data = {
        "name": name_entry.get(),
        "type": type_entry.get(),
        "regular_price": price_entry.get(),
        "description": desc_entry.get(),
        "short_description": short_desc_entry.get(),
        "categories": [{"id": int(id)} for id in cat_entry.get().split(",")],
        "images": [{"src": src} for src in img_entry.get().split(",")]
    }

    # Create the product using the WooCommerce API
    response = wcapi.post("products", data)

    # Print the response
    print(response.json())

# Create a Tkinter window
root = tk.Tk()

# Create entry fields for the product data
name_entry = tk.Entry(root)
type_entry = tk.Entry(root)
price_entry = tk.Entry(root)
desc_entry = tk.Entry(root)
short_desc_entry = tk.Entry(root)
cat_entry = tk.Entry(root)
img_entry = tk.Entry(root)

# Create buttons for the insert, update, and delete operations
insert_button = tk.Button(root, text="Insert", command=create_product)

# Pack the widgets
name_entry.pack()
type_entry.pack()
price_entry.pack()
desc_entry.pack()
short_desc_entry.pack()
cat_entry.pack()
img_entry.pack()
insert_button.pack()

# Start the Tkinter event loop
root.mainloop()
