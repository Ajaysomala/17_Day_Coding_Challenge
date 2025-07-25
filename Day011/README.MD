 # 🐍 Python Utilities: Notes Manager & File Organizer

This repository contains two simple but powerful Python scripts that demonstrate practical applications of file handling and OS operations. These tools are designed to be simple, effective, and easy to use.

---

## 📝 Notes Manager (`notes_manager.py`)

A command-line application to quickly jot down and view your notes. All notes are saved to a `notes.txt` file, ensuring your thoughts are persistent and easily accessible.

### Features
*   **✍️ Add Notes:** Easily add new entries through a simple prompt.
*   **👀 View Notes:** Display all previously saved notes from the file.
*   **💾 Persistent Storage:** Notes are saved locally in `notes.txt`.
*   **✅ User-Friendly Menu:** A clean, interactive menu for easy navigation.

### How to Use
1.  Run the script from your terminal:
    ```bash
    python notes_manager.py
    ```
2.  Follow the on-screen menu to either add a new note or view existing ones.
3.  A `notes.txt` file will be automatically created in the same directory to store your notes.

---

## 📂 Simple File Organizer (`file_organizer.py`)

Tired of a messy "Downloads" or project folder? This script automatically organizes all files in its directory into categorized subfolders based on their file extension.

### Features
*   **🤖 Automatic Sorting:** Sorts files into default categories like `Images`, `Documents`, `Videos`, and `Others`.
*   **📁 Smart Folder Creation:** Automatically creates category folders if they don't already exist.
*   **🔧 Extensible:** The script can be easily modified to handle new file types and custom folder categories.

### How to Use
1.  **Important:** It's highly recommended to **back up your files** before running the script for the first time on an important directory.
2.  Place the `file_organizer.py` script inside the folder you want to organize.
3.  Run the script from your terminal:
    ```bash
    python file_organizer.py
    ```
4.  Watch as your files are neatly moved into their respective category folders!

### Customization
You can easily add new categories or file extensions by editing the script. For example, you could add a category for audio files.

---

## 🛠️ Technologies Used

*   **Python 3**
*   Core Modules:
    *   `os`: For interacting with the operating system (creating directories, checking paths).
    *   `shutil`: For high-level file operations (moving files).

## 🚀 Getting Started

1.  Clone this repository or simply download the `.py` files.
2.  Navigate to the directory in your terminal.
3.  Run the scripts as described above. Enjoy your new, organized workflow!
