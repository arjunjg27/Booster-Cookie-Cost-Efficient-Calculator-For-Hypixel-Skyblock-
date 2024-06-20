import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

bits = 0
items_affordable = []
cost_ranked = []

items = {
    "God Potion": 1400.00,
    "Kismet Feather": 1333.33,
    "Kat Flower": 1600.00,
    "Kat Bouquet": 1360.00,
    "Heat Core": 1533.33,
    "Hyper Catalyst Upgrade": 1666.67,
    "Ultimate Carrot Candy Upgrade": 1575.00,
    "Colossal Experience Bottle Upgrade": 1500.00,
    "Jumbo Backpack Upgrade": 1525.00,
    "Minion Storage X-pender": 1333.33,
    "Matriarch's Perfume": 1416.67,
    "Builder's Wand": 1166.67,
    "Block Zapper": 860.00,
    "Pocket Sack-in-a-Sack": 1250.00,
    "Abiphone Contacts Trio": 1581.40,
    "Expertise I Book": 1350.00,
    "Compact I Book": 1375.00,
    "Cultivating I Book": 1350.00,
    "Champion I Book": 1375.00,
    "Hecatomb I Book": 1283.33,
    "Toxophilite": 1325.00,
    "Autopet Rules 2-Pack": 1452.38
}

items1 = {
    "God Potion": 1500,
    "Kismet Feather": 1350,
    "Kat Flower": 500,
    "Kat Bouquet": 2500,
    "Heat Core": 3000,
    "Hyper Catalyst Upgrade": 300,
    "Ultimate Carrot Candy Upgrade": 8000,
    "Colossal Experience Bottle Upgrade": 1200,
    "Jumbo Backpack Upgrade": 4000,
    "Minion Storage X-pender": 1500,
    "Matriarch's Perfume": 1200,
    "Builder's Wand": 12000,
    "Block Zapper": 5000,
    "Pocket Sack-in-a-Sack": 8000,
    "Abiphone Contacts Trio": 6450,
    "Expertise I Book": 4000,
    "Compact I Book": 4000,
    "Cultivating I Book": 4000,
    "Champion I Book": 4000,
    "Hecatomb I Book": 6000,
    "Toxophilite": 4000,
    "Autopet Rules 2-Pack": 21000
}

root = tk.Tk()
root.title("Hypixel Skyblock Booster Cookie Data")

icon = Image.open("download.jpg")
icon = ImageTk.PhotoImage(icon)
root.iconphoto(False, icon)

def starting_page():
    def add_bits():
        global bits
        amount_of_bits = bits_entry.get().strip()
        if amount_of_bits == "":
            messagebox.showwarning("Warning", "Please Enter amount of bits")
            return
        bits = int(amount_of_bits)  # Update global bits variable
        bits_entry.delete(0, tk.END)
    
    def calculate(bits):
        global items_affordable, cost_ranked
        total_bits = bits
        for item, cost in items1.items():
            if cost <= total_bits:
                items_affordable.append(item)
        
        # Rank items by cost efficiency
        cost_ranked = sorted(items_affordable, key=lambda item: items[item])
        
        messagebox.showinfo("Affordable Items", f"Items you can afford with {total_bits} bits:\n" + "\n".join(items_affordable))
        messagebox.showinfo("Items ranked:", "\n".join(cost_ranked))
        
    def entry_calc():
        add_bits()
        calculate(bits)
    
    # Label for the entry "Amount of Bits:"
    bits_label = tk.Label(root, text="Amount of Bits:")
    bits_label.grid(row=0, column=0, padx=10, pady=10)
    
    # Entry for the amount of bits the player has
    bits_entry = tk.Entry(root, width=30)
    bits_entry.grid(row=0, column=1, padx=10, pady=10)
    
    # Add entry button
    add_entry = tk.Button(root, text="Add Entry", command=entry_calc)
    add_entry.grid(row=1, column=0, padx=10, pady=10)
    
    # Close button
    close_button = tk.Button(root, text="Close", command=root.destroy)
    close_button.grid(row=1, column=1, padx=10, pady=10)
    
    root.mainloop()

starting_page()
