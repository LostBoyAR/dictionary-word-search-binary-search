"""
DAA Mini Project: Dictionary Word Search System using Binary Search
Time Complexity : O(log n)   (Linear search would be O(n))
Space Complexity: O(1)
"""
import tkinter as tk

# ---------- Data (kept sorted, because Binary Search needs sorted data) ----------
dictionary = {
    "algorithm": "A step-by-step procedure to solve a problem.",
    "array": "A collection of items stored at contiguous memory locations.",
    "binary": "A number system with only two digits: 0 and 1.",
    "complexity": "Measure of time or space an algorithm needs.",
    "data": "Raw facts and figures.",
    "graph": "A set of nodes connected by edges.",
    "heap": "A tree-based data structure used for priority queues.",
    "iteration": "Repeating a set of instructions.",
    "list": "An ordered collection of items.",
    "loop": "A statement that repeats a block of code.",
    "queue": "A First-In-First-Out (FIFO) data structure.",
    "recursion": "A function that calls itself.",
    "search": "Finding an item in a collection.",
    "sort": "Arranging items in a particular order.",
    "stack": "A Last-In-First-Out (LIFO) data structure.",
    "tree": "A hierarchical data structure with a root and children.",
}
words = sorted(dictionary.keys())


# ---------- Binary Search ----------
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    steps = []
    while low <= high:
        mid = (low + high) // 2
        steps.append(f"Step {len(steps)+1}: low={low}, high={high}, "
                     f"mid={mid} -> '{arr[mid]}'")
        if arr[mid] == key:
            return mid, steps
        elif arr[mid] < key:
            low = mid + 1      # search right half
        else:
            high = mid - 1     # search left half
    return -1, steps


# ---------- GUI ----------
def search():
    key = entry.get().strip().lower()
    steps_box.delete("1.0", tk.END)
    if not key:
        result.config(text="Please enter a word.", fg="orange")
        return

    index, steps = binary_search(words, key)
    steps_box.insert(tk.END, "\n".join(steps))

    if index != -1:
        result.config(text=f"Found at position {index}\nMeaning: {dictionary[key]}",
                      fg="dark green")
    else:
        result.config(text="Word not found!", fg="red")


root = tk.Tk()
root.title("Dictionary Word Search (Binary Search)")
root.geometry("520x470")

tk.Label(root, text="Dictionary Word Search", font=("Arial", 16, "bold")).pack(pady=8)

entry = tk.Entry(root, font=("Arial", 13), width=25)
entry.pack(pady=5)
entry.bind("<Return>", lambda e: search())
entry.focus()

tk.Button(root, text="Search", font=("Arial", 11), command=search).pack(pady=5)

result = tk.Label(root, text="", font=("Arial", 11), wraplength=480)
result.pack(pady=5)

tk.Label(root, text="Binary Search Steps:", font=("Arial", 10, "bold")).pack()
steps_box = tk.Text(root, height=7, width=60)
steps_box.pack(pady=3)

tk.Label(root, text="Available words (sorted):", font=("Arial", 10, "bold")).pack()
tk.Label(root, text=", ".join(words), wraplength=490, fg="gray").pack()

root.mainloop()
