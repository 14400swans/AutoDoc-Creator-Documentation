# AutoDoc Creator Documentation

AutoDoc Creator automates document creation, management, and storage with integrations to GitHub, Microsoft OneDrive, and OpenAI.

## Features
1. **Content Generation**: Generate content using OpenAI's API.
2. **File Uploads to OneDrive**: Manage file uploads using Microsoft Graph API.
3. **File Management in GitHub**: Upload files programmatically to GitHub repositories.

## Documentation
- [Features](docs/features.md)
- [API Reference](docs/api.md)
![Screenshot of AutoDoc Creator](path/to/screenshot.png)
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/14400swans/AutoDoc-Creator-Documentation.git
   cd AutoDoc-Creator-Documentation
## Screenshot and Notes Saving Feature

This feature allows saving screenshots and related conversations to:
1. **Notes Directory:** Files are saved as text and image.
2. **Optional PDF Export:** Notes can be exported to a PDF file.

### Usage Example
```python
from scripts.save_screenshot import save_screenshot_to_notes

save_screenshot_to_notes(
    screenshot_path="example_screenshot.jpg",
    notes_directory="C:/Users/YourUsername/Documents/my_notes/",
    conversation_text="This is the conversation text from ChatGPT.",
    save_as_pdf=True,
    pdf_path="C:/Users/YourUsername/Documents/my_notes/notes.pdf"
)
