# Remote Control Tool

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Commands](#commands)
4. [Setup](#setup)
5. [Usage](#usage)

## Introduction

This Discord bot provides a variety of functionalities, including system control, file management, and media handling, making it a versatile tool for managing your computer via Discord commands.

## Features

- **System Control**: Shutdown, reboot, lock, and sleep your computer.
- **File Management**: Open files, copy files, list directories, and manage attachments.
- **Media Handling**: Take screenshots, capture images from your webcam, and record your screen.
- **Keyboard and Mouse Control**: Simulate keyboard and mouse actions.
- **System Information**: Retrieve system, memory, and CPU information.
- **Utility Commands**: Show message boxes, run shell commands, and manage system startup.

## Commands

### General Commands

- `!explorer` - Open File Explorer.
- `!ss` - Take a screenshot and send it.
- `!cam` - Capture an image from the webcam and send it.
- `!ask [question]` - Display a dialog box asking the given question and return the user's response.
- `!msgbox [message]` - Display a message box with the given message.

### Keyboard and Mouse Commands

- `!key [key]` - Simulate pressing and releasing the specified key.
- `!altf4` - Simulate pressing Alt+F4.
- `!mouse1` - Simulate right mouse click.
- `!mouse2` - Simulate left mouse click.
- `!type [text]` - Type the given text.
- `!volume_up` - Increase the volume.
- `!volume_down` - Decrease the volume.
- `!mute` - Mute the volume.

### File and Directory Commands

- `!copy [path]` - Copy the specified file to the current directory and send it.
- `!pull` - Save attached files and move them to the desktop.
- `!open [path]` - Open the specified file or directory.
- `!listdir [directory]` - List files in the specified directory.

### System Control Commands

- `!reboot` - Reboot the computer.
- `!shutdown` - Shutdown the computer.
- `!lock` - Lock the computer.
- `!sleep` - Put the computer to sleep.

### Information Commands

- `!sysinfo` - Get system information.
- `!uptime` - Get system uptime.
- `!meminfo` - Get memory information.
- `!cpuinfo` - Get CPU information.

### Utility Commands

- `!wallpaper` - Change the desktop wallpaper to the attached image.
- `!logkeys` - Start logging keystrokes for 60 seconds.
- `!shell [command]` - Run a shell command and return the output.
- `!killproc [pid]` - Kill the process with the specified PID.

### Media Commands

- `!screenrec [duration]` - Record the screen for the specified duration and send the recording.

## Setup

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Install the required Python packages by running the following command:

    ```bash
    pip install discord pynput pyautogui opencv-python-headless pyaudio ffmpeg-python psutil tk
    ```

### Obtaining the Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application and navigate to the "Bot" section.
3. Add a bot to your application and copy the bot token.

### Configuration

1. Replace the placeholder token in the code with your actual bot token:

    ```python
    TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
    ```

2. Save the file.

## Usage

1. Run the bot by executing the following command in the terminal:

    ```bash
    python bot.py
    ```

    

2. Invite the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal.

3. Use the commands listed above to interact with your system via Discord messages.

Enjoy using your new Discord bot! If you have any issues or questions, feel free to create an issue on the project's repository.

## Made by
Made by [@c4gwn](https://instagram.com/c4gwn)

Get help: [www.pyrollc.com.tr](https://pyrollc.com.tr)
