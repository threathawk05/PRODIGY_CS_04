# 🖥️ Keylogger Project 🔑

This is a simple **keylogger** application built in Python. It records keystrokes and stores them in a log file. The log file contains timestamps and the keys pressed. This project is for educational purposes and demonstrates how keystrokes can be captured and saved in a file.

> ⚠️ **Important:** Keyloggers are powerful tools, and their misuse can lead to serious ethical and legal issues. Always ensure you have explicit permission from the device owner before running a keylogger.

## 📑 Table of Contents
- [✨ Features](#features)
- [💻 Installation](#installation)
- [🚀 Usage](#usage)
- [🖥️ Keylogger Operation](#keylogger-operation)
- [⏹️ Stopping the Keylogger](#stopping-the-keylogger)
- [⚖️ Ethical Considerations](#ethical-considerations)
- [📄 License](#license)


## ✨Features
- 📝 **Logs keystrokes with timestamps**: Records every keystroke with the time it was pressed.
- 💾 **Saves keystrokes in a text file** (`keylog.txt`): All logged keystrokes are stored in a simple text file.
- 🔄 **Appends new keystrokes on subsequent runs**: The log file keeps growing with new keystrokes without overwriting previous ones.
- 🛑 **Stopping functionality**
   - ⌨️ **Key combination**: Press `Ctrl + Shift + S` to stop logging.
- ⚙️ **Creates an executable** (`.exe`) for easy deployment on Windows: No need to install Python on the target system.

## 💻Installation

### 📦 Prerequisites
- Python 3.6 or higher.
- **`keyboard`** library for capturing keystrokes.

### Step-by-Step Installation

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/keylogger.git
   cd keylogger
     ```
2. Install required dependencies: If you don’t have the keyboard library installed, run the following command:
     ```bash
   pip install keyboard
     ```
3. Convert the Python script to an executable (optional): To run the keylogger as an executable, use PyInstaller. Follow these steps to create the .exe file:

   
    1. Install PyInstaller:

         ```bash
         pip install pyinstaller
         ```
     
    2. Navigate to the directory containing keylogger.py and run the following command:

         ```bash
         pyinstaller --onefile --noconsole keylogger.py
         ```
    3. After running the command, the .exe file will be generated inside the dist folder.
       
    
## 🚀Usage
  ### Running the Keylogger
  To start the keylogger

  1. Run the python script
     
       ```bash
        python keylogger.py
       ```



## 🖥️Keylogger Operation

Once the keylogger is running, it will start recording keystrokes and save them in `keylog.txt` with timestamps. Each time you run the program, it will append new keystrokes to the file.

## ⏹️Stopping the Keylogger

You can stop the keylogger using one of the following methods:

- **🖱️ Key Combination**: If you've set up a key combination (e.g., `Ctrl + Shift + S`), press it to stop logging.
- **📝 Stop Command File**: Create a `stop.txt` file containing the word `stop` in the same directory as the keylogger. Once the keylogger detects this file, it will stop logging.


## ⚖️Ethical Considerations

This tool is intended for **educational purposes only**. Always obtain explicit permission from the device owner before using any keylogger. Unauthorized use of a keylogger is illegal and unethical.

Before using this tool:
- ✅ Ensure you have written consent from the person whose device you are monitoring.
- 🚫 Do not use this for malicious purposes.

**Important**: Misuse of keyloggers may result in legal consequences, including criminal charges.

## Example Image(keylog.txt file)
<img width="596" alt="image" src="https://github.com/user-attachments/assets/50b25b0b-9c65-49b9-99d9-42be99776560">



## 📄License

This project is open source and available under the MIT License.

[MIT](https://choosealicense.com/licenses/mit/)

Created by Amaan Khojani 👨‍💻
   
