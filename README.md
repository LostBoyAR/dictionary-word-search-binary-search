# Dictionary Word Search System using Binary Search

A small **Design and Analysis of Algorithms (DAA)** mini project. It searches for a word in a sorted dictionary using **Binary Search** and shows every step of the algorithm in a simple **Python Tkinter** window.

## Features

- Searches a sorted dictionary of 16 computer-science words using iterative binary search
- Shows the **position** and the **meaning** of the word if it is found
- Shows a clear message if the word is not found
- Displays every step (`low`, `high`, `mid`) so the algorithm is easy to explain in a demo
- Not case-sensitive and ignores extra spaces (`" STACK "` works the same as `stack`)
- Press **Enter** or click **Search**
- Uses only standard Python. No extra library is needed.

## How to Run

1. Install [Python 3](https://www.python.org/downloads/). Tkinter comes with it.
2. Download or clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```
3. Run the program:
   ```bash
   python dictionary_search.py
   ```
4. Type a word such as `stack` or `recursion` and press **Search**.

> On some Linux systems Tkinter must be installed separately: `sudo apt install python3-tk`

## Example Output

Searching for `stack`:

```
Found at position 14
Meaning: A Last-In-First-Out (LIFO) data structure.

Step 1: low=0, high=15, mid=7 -> 'iteration'
Step 2: low=8, high=15, mid=11 -> 'recursion'
Step 3: low=12, high=15, mid=13 -> 'sort'
Step 4: low=14, high=15, mid=14 -> 'stack'
```

Searching for `apple` (not in the dictionary): `Word not found!` after 4 steps.

## How Binary Search Works

1. The words must be **sorted** (the program sorts them once with `sorted()`).
2. Set `low = 0` and `high = n - 1`.
3. Find `mid = (low + high) // 2` and compare the word at `mid` with the key.
4. If they are equal, the word is found.
5. If the word at `mid` is smaller than the key, search the right half (`low = mid + 1`).
6. Otherwise search the left half (`high = mid - 1`).
7. If `low > high`, the word is not present.

Each comparison removes half of the remaining words.

## Complexity

| Case | Time |
|------|------|
| Best case | O(1) |
| Average case | O(log n) |
| Worst case | O(log n) |
| Space (iterative) | O(1) |

For comparison, linear search takes O(n). For 1,000,000 words, binary search needs at most about 20 comparisons, while linear search may need 1,000,000.

## Project Files

| File | Description |
|------|-------------|
| `dictionary_search.py` | Complete source code (data, binary search function and Tkinter GUI) |
| `DAA_Project_Report.docx` | Full project report |
| `README.md` | This file |

## Tools Used

- Python 3
- Tkinter (GUI)

## Author

**Aditya Raj** – UID: 26MCI10217
MCA (AIML), Chandigarh University
Subject: Design and Analysis of Algorithms (DAA)
