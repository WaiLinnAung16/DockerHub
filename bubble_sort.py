import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter Table with Bubble Sort")

# Create the Treeview table
columns = ("ID", "Name", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Define column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

data = [
    (1, "Alice", 29), (2, "Bob", 41), (3, "Charlie", 35), (4, "David", 26),
    (5, "Eve", 47), (6, "Frank", 33), (7, "Grace", 22), (8, "Hank", 39),
    (9, "Ivy", 31), (10, "Jack", 45), (11, "Kara", 28), (12, "Leo", 37),
    (13, "Mia", 43), (14, "Nina", 30), (15, "Oscar", 48), (16, "Paul", 36),
    (17, "Quinn", 24), (18, "Rose", 32), (19, "Steve", 44), (20, "Tina", 27)
]

# Bubble Sort Class
class BubbleSort:
    """
    Using Bubble Sort Algorithm, Sort the data by Age in ascending order
    """
    @staticmethod
    def sort(items, type = "age"):
        if type == "age":
            type_index = 2
        else:
            type_index = 0

        for i in range(len(items)):
            for j in range(len(items) - 1):
                if items[j][type_index] > items[j + 1][type_index]:
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items
    
def update_table(type):
    sorted_data = BubbleSort.sort(data, type) 
    tree.delete(*tree.get_children()) # Clear the table
    for item in sorted_data: # Insert sorted data into the table
        tree.insert("", "end", values=item)

# Sort by Id
sort_button = tk.Button(root, text="Sort by ID", command=lambda: update_table("id"))
sort_button.grid(row=0, column=0, columnspan=1, pady=10)

# Sort by Age
sort_button = tk.Button(root, text="Sort by Age", command=lambda: update_table("age"))
sort_button.grid(row=0, column=2, columnspan=1, pady=10)


# Insert data into the table
for item in data:
    tree.insert("", "end", values=item)

# Place the table below everything
tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Make columns expand properly
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)



# Run the Tkinter event loop
root.mainloop()
