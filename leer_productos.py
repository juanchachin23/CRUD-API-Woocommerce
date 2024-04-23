import tkinter as tk
from tkinter import ttk
from woocommerce import API

# Initialize the WooCommerce API
wcapi = API(
        url="https://appcorezulia.lat/n1",
        consumer_key="ck_9bded2550e24bc4329bf2ababec8c904c767d181",
        consumer_secret="cs_ee901287d6b833bbff11aa0e0f60ab5dcb43c7c2",
        version="wc/v3"
    )

# Get the products using the WooCommerce API
products = wcapi.get("products").json()


# Create a Tkinter window
root = tk.Tk()

# Create a Treeview in the Tkinter window
treeview = ttk.Treeview(root)

# Create columns in the Treeview for each product data field
treeview["columns"]=("ID","Nombre", "Tipo", "Precio regular", "Descripcion", "Descripcion corta", "Categoria", "Url de la imagen","fecha de creacion", "fecha de actualizacion")
for column in treeview["columns"]:
    treeview.column(column, width=100)
    treeview.heading(column, text=column)

# Iterate over the products and add each one as a new row in the Treeview
# Iterate over the products and add each one as a new row in the Treeview
for product in products:
    if isinstance(product, dict):
        treeview.insert('', 'end', values=(product.get("id"), product.get("name"), product.get("type"), product.get("regular_price"), product.get("description"), product.get("short_description"), ", ".join([category.get("name") for category in product.get("categories", [])]), ", ".join([image.get("src") for image in product.get("images", [])]), product.get("date_created"), product.get("date_modified")))

# Pack the Treeview
treeview.pack()

# Start the Tkinter event loop
root.mainloop()