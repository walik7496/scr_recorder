# Screen Recorder

A simple Python-based screen recording application with a graphical user interface (GUI) built using Tkinter. This tool captures your desktop screen and saves the recording as an MP4 file using FFmpeg.

## Features

- **Start/Stop Recording**: Easily begin and end screen recording with a single button.
- **Real-Time Timer**: Displays the elapsed recording time.
- **High Performance**: Utilizes FFmpeg with ultrafast preset for efficient screen capture.

## Prerequisites

- **Python 3.x**
- **FFmpeg** (Ensure `ffmpeg.exe` is downloaded and accessible in your system PATH)
- Python Libraries:
  - `tkinter` (comes pre-installed with Python)
  - `pyautogui`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/walik7496/scr_recorder.git
   cd screen-recorder
   ```

2. **Install required Python packages:**
   ```bash
   pip install pyautogui
   ```

3. **Download FFmpeg:**
   - Visit [FFmpeg official website](https://ffmpeg.org/download.html)
   - Download the suitable version for your OS
   - Add `ffmpeg.exe` to your system PATH or place it in the same directory as the script

## Usage

Run the application using Python:

```bash
python screen_recorder.py
```

### Instructions:
- Click the **Record** button to start recording your screen.
- The timer will display the duration of the recording.
- To stop the recording, simply close the application window.
- The recorded video will be saved as `output.mp4` in the same directory.

## File Structure

```
.
├── screen_recorder.py
├── output.mp4 (generated after recording)
└── README.md
```

## Troubleshooting

- **Recording Failed Error:** Ensure `ffmpeg.exe` is correctly installed and accessible via the system PATH.
- **Black Screen Issue:** Check your display settings and FFmpeg compatibility with your OS.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).


