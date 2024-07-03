# KeyloggerUI

KeyloggerUI is a simple keylogger application with a user interface that captures keystrokes and saves them into a JSON file. The JSON file is created automatically upon running the application.

## Features

- **Simple UI:** Start and stop the keylogger easily with a user-friendly interface.
- **Automatic Logging:** Keystrokes are captured and saved to a JSON file automatically.
- **JSON Output:** Logged keystrokes are stored in a structured JSON format for easy access and analysis.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries: `tkinter`, `pynput`, `json`

You can install the required libraries using pip:

```bash
pip install pynput
pip install tk
pip install pillow
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/eddyhacks/KeyloggerUI.git
cd KeyloggerUI
```

2. Run the keylogger:

```bash
python keylog.py
```

## Usage

1. Open the application by running the `keylog.py` script.
2. Use the interface to start and stop the keylogger.
3. The keystrokes will be logged into a JSON file named `log.txt` in the project directory.

## UI interface

*The Login interface*

![image](https://github.com/eddyhacks/KeyloggerUI/assets/88126377/c7e489ff-d304-4467-a8cd-ec70eb260014)

*The start screen*

![image](https://github.com/eddyhacks/KeyloggerUI/assets/88126377/b557ed34-9f6d-40b1-8d78-d7cfb33d1739)


## Example

Here's an example of what the JSON output file (`log.txt`) might look like:

![image](https://github.com/eddyhacks/KeyloggerUI/assets/88126377/a70cc206-6bc0-40f6-a48d-8b02a35afbf6)

## Close the application

`To close the application from running press ESC`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## License

This project code is open source. Feel free to clone it and modify the code.

## Acknowledgments

- Inspired by various keylogger projects and tutorials available online.

---
