# Streamlit Playground

A collection of Streamlit applications for learning and experimenting with Streamlit features.

## Overview

This project contains several Streamlit demo applications showcasing different features and capabilities:

- **Basic Streamlit App** - Introduction to core Streamlit widgets
- **Dashboard Demo** - Sidebar and layout examples
- **ChatGPT Integration** - AI-powered chat interface using OpenAI

## Features

### Basic App (`app.py`)
- Interactive widgets (slider, text input, selectbox)
- User input handling
- Simple data display

### Dashboard (`streamlit_dashboard/app.py`)
- Sidebar configuration
- Number slider with dynamic display
- Dashboard layout patterns

### Chat Interface (`streamlit_dashboard/chat.py`)
- ChatGPT integration
- Chat message UI components
- Real-time AI responses

## Requirements

- Python >= 3.12.11
- Streamlit >= 1.51.0
- OpenAI (for chat functionality)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd 20251115_streamlit_play
```

2. Install dependencies using `uv`:
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Basic App
```bash
streamlit run app.py
```

### Run the Dashboard Demo
```bash
streamlit run streamlit_dashboard/app.py
```

### Run the Chat Interface
```bash
# Set your OpenAI API key first
export OPENAI_API_KEY='your-api-key-here'

streamlit run streamlit_dashboard/chat.py
```

## Project Structure

```
20251115_streamlit_play/
├── app.py                      # Basic Streamlit introduction app
├── streamlit_dashboard/
│   ├── app.py                 # Dashboard demo with sidebar
│   └── chat.py                # ChatGPT integration
├── pyproject.toml             # Project configuration
├── uv.lock                    # Dependency lock file
└── README.md                  # This file
```

## Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

## Notes

This is a learning project created for exploring Streamlit capabilities and building interactive web applications with Python.

