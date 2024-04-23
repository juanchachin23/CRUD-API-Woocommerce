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
# Create a Tkinter window
root = tk.Tk()

# Create a variable to store the ID of the selected product
selected_id = tk.StringVar()

def create_product(tree):
    # Deselect any selected item in the Treeview
    tree.selection_remove(tree.selection())

    # Get the product data from the entry fields
    data = {
        "name": name_entry.get(),
        "type": type_entry.get(),
        "regular_price": price_entry.get(),
        "description": desc_entry.get(),
        "short_description": short_desc_entry.get(),
        "categories": [{"id": cat_entry.get()}],
        "images": [{"src": img_entry.get()}]
    }

 # Create the product using the WooCommerce API
    create_response = wcapi.post("products", data)

    # Print the response
    print(create_response.json())

def on_select(event):
    # Get the selected item
    selected_item = tree.selection()[0]
    item_values = tree.item(selected_item, "values")

    # Fill the entry fields with the item values and store the ID
    selected_id.set(item_values[0])
    name_entry.delete(0, tk.END)
    name_entry.insert(0, item_values[1])
    type_entry.delete(0, tk.END)
    type_entry.insert(0, item_values[2])
    price_entry.delete(0, tk.END)
    price_entry.insert(0, item_values[3])
    desc_entry.delete(0, tk.END)
    desc_entry.insert(0, item_values[4])
    short_desc_entry.delete(0, tk.END)
    short_desc_entry.insert(0, item_values[5])
    cat_entry.delete(0, tk.END)
    cat_entry.insert(0, item_values[6])
    img_entry.delete(0, tk.END)
    img_entry.insert(0, item_values[7])

def update_product():
    # Get the new product data from the entry fields
    data = {
        "name": name_entry.get(),
        "type": type_entry.get(),
        "regular_price": price_entry.get(),
        "description": desc_entry.get(),
        "short_description": short_desc_entry.get(),
        "categories": [{"id": cat_entry.get()}],
        "images": [{"src": img_entry.get()}]
    }

    # Update the product using the WooCommerce API
    update_response = wcapi.put(f"products/{selected_id.get()}", data)

    # Print the response
    print(update_response.json())

def delete_product():
    # Get the selected item
    selected_items = tree.selection()
    if selected_items:  # Check if there is any selected item
        selected_item = selected_items[0]
        item_values = tree.item(selected_item, "values")

        # Get the product ID from the selected item
        product_id = item_values[0]  # Assuming the ID is the first value

        # Delete the product using the WooCommerce API
        delete_response = wcapi.delete(f"products/{product_id}", params={"force": True}).json()

        # Print the response
        print(delete_response)

def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)

    def remove_placeholder(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)

    def insert_placeholder(event):
        if not entry.get():
            entry.insert(0, placeholder_text)

    entry.bind('<FocusIn>', remove_placeholder)
    entry.bind('<FocusOut>', insert_placeholder)

# Create a label and pack it at the beginning
label = tk.Label(root, text="CRUD para API de WooCommerce", font=("Helvetica", 16))
label.pack(pady=102)

# Create entry fields for the product data
name_entry = tk.Entry(root, width=50)
name_entry.pack(pady=10)  # Add vertical padding
add_placeholder(name_entry, "Coloque el nombre del producto")

type_entry = tk.Entry(root, width=50)
type_entry.pack(pady=10)  # Add vertical padding
add_placeholder(type_entry, "Coloque el tipo de producto (simple)")

price_entry = tk.Entry(root, width=50)
price_entry.pack(pady=10)  # Add vertical padding
add_placeholder(price_entry, "Coloque el Precio del producto")

desc_entry = tk.Entry(root, width=50)
desc_entry.pack(pady=10)  # Add vertical padding
add_placeholder(desc_entry, "Coloque la descripcion del producto")

short_desc_entry = tk.Entry(root, width=50)
short_desc_entry.pack(pady=10)  # Add vertical padding
add_placeholder(short_desc_entry, "Coloque la descripcion corta del producto")

cat_entry = tk.Entry(root, width=50)
cat_entry.pack(pady=10)  # Add vertical padding
add_placeholder(cat_entry, "coloque la categoria del producto")

img_entry = tk.Entry(root, width=50)
img_entry.pack(pady=10)  # Add vertical padding
add_placeholder(img_entry, "Coloque el url de la imagen del producto")

# Create a Treeview in the Tkinter window
tree = tk.ttk.Treeview(root)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)  # Add vertical padding

# Create buttons for the insert, update, and delete operations
insert_button = tk.Button(button_frame, text="Insertar", bg="green", fg="white", command=lambda: create_product(tree))
update_button = tk.Button(button_frame, text="Actualizar", bg="blue", fg="white", command=update_product)
delete_button = tk.Button(button_frame, text="Borrar", bg="red", fg="white", command=delete_product)

# Pack the buttons with horizontal padding
insert_button.pack(side=tk.LEFT, padx=10)
update_button.pack(side=tk.LEFT, padx=10)
delete_button.pack(side=tk.LEFT, padx=10)


# Create columns in the Treeview for each product data field
tree["columns"]=("ID", "Nombre", "Tipo", "Precio regular", "Descripcion", "Descripcion corta", "Categoria", "Url de la imagen", "Fecha de creacion", "Fecha de modificacion")
for column in tree["columns"]:
    tree.column(column, width=100)
    tree.heading(column, text=column)

# Bind the selection event to the on_select function
tree.bind('<<TreeviewSelect>>', on_select)

# Get the products using the WooCommerce API
products = wcapi.get("products").json()

# Iterate over the products and add each one as a new row in the Treeview
for product in products:
    if isinstance(product, dict):
        tree.insert('', 'end', values=(product.get("id"), product.get("name"), product.get("type"), product.get("regular_price"), product.get("description"), product.get("short_description"), ", ".join([category.get("name") for category in product.get("categories", [])]), ", ".join([image.get("src") for image in product.get("images", [])]), product.get("date_created"), product.get("date_modified")))

# Pack the Treeview
tree.pack()

# Start the Tkinter event loop
root.mainloop()