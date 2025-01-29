import tkinter as tk


def authenticate():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        login_frame.pack_forget()
        main_frame.pack()
    else:
        auth_label.config(text="Invalid credentials", fg="red")


def add_inventory():
    item_name = item_name_entry.get()
    item_qty = int(item_qty_entry.get())
    item_price = float(item_price_entry.get())
    with open('inventory.txt', 'a') as file:
        file.write(f'{item_name},{item_qty},{item_price}\n')
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)


def update_inventory():
    item_name = item_name_entry.get()
    item_qty = int(item_qty_entry.get())
    item_price = float(item_price_entry.get())
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    with open('inventory.txt', 'w') as file:
        for line in inventory_data:
            name, qty, price = line.strip().split(',')
            if name == item_name:
                file.write(f'{name},{item_qty},{item_price}\n')
            else:
                file.write(line)
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)


def search_inventory():
    search_name = item_name_entry.get()
    with open('inventory.txt', 'r') as file:
        for line in file:
            name, qty, price = line.strip().split(',')
            if name == search_name:
                result_label.config(text=f'{name} - {qty} in stock, ${price} each')
                return
    result_label.config(text=f'{search_name} not found in inventory.')
    item_name_entry.delete(0, tk.END)


def remove_inventory():
    remove_name = item_name_entry.get()
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    with open('inventory.txt', 'w') as file:
        for line in inventory_data:
            name, qty, price = line.strip().split(',')
            if name != remove_name:
                file.write(line)
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)


def generate_inventory():
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    inventory_text = '\n'.join(inventory_data)
    result_label.config(text=inventory_text)

root = tk.Tk()
root.title("Inventory Management")


login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

auth_label = tk.Label(login_frame, text="")
auth_label.grid(row=2, column=0, columnspan=2)

tk.Button(login_frame, text="Login", command=authenticate).grid(row=3, column=0, columnspan=2)


main_frame = tk.Frame(root)


tk.Label(main_frame, text="Item Name:").grid(row=0, column=0)
item_name_entry = tk.Entry(main_frame)
item_name_entry.grid(row=0, column=1)

tk.Label(main_frame, text="Item Quantity:").grid(row=1, column=0)
item_qty_entry = tk.Entry(main_frame)
item_qty_entry.grid(row=1, column=1)

tk.Label(main_frame, text="Item Price:").grid(row=2, column=0)
item_price_entry = tk.Entry(main_frame)
item_price_entry.grid(row=2, column=1)


tk.Button(main_frame, text="Add Inventory", command=add_inventory).grid(row=3, column=0)
tk.Button(main_frame, text="Update Inventory", command=update_inventory).grid(row=4, column=0)
tk.Button(main_frame, text="Search Inventory", command=search_inventory).grid(row=5, column=0)
tk.Button(main_frame, text="Remove Inventory", command=remove_inventory).grid(row=6, column=0)
tk.Button(main_frame, text="Generate Inventory", command=generate_inventory).grid(row=7, column=0)

result_label = tk.Label(main_frame, text="List")
result_label.grid(row=3, column=1, columnspan=2)

root.mainloop()