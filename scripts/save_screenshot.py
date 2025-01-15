import os
import shutil
from fpdf import FPDF

def save_screenshot_to_notes(screenshot_path, notes_directory, conversation_text, save_as_pdf=False, pdf_path=None):
    """
    Saves a screenshot and its related conversation to Notes, with optional PDF export.

    :param screenshot_path: File path of the screenshot (e.g., "screenshot.jpg")
    :param notes_directory: Path to the notes directory (e.g., "notes/")
    :param conversation_text: Conversation text to be saved with the screenshot
    :param save_as_pdf: Boolean, if True saves the notes as a PDF
    :param pdf_path: File path for the PDF file (e.g., "notes.pdf")
    """
    try:
        # Validate screenshot file
        if not os.path.exists(screenshot_path):
            raise FileNotFoundError(f"Screenshot not found at path: {screenshot_path}")

        # Ensure notes directory exists
        if not os.path.exists(notes_directory):
            os.makedirs(notes_directory)

        # Save screenshot to the notes directory
        screenshot_copy_path = os.path.join(notes_directory, os.path.basename(screenshot_path))
        shutil.copy2(screenshot_path, screenshot_copy_path)

        # Save notes to a text file
        note_file = os.path.join(notes_directory, "screenshot_notes.txt")
        with open(note_file, "a", encoding="utf-8") as note:
            note.write(f"Screenshot saved at: {screenshot_copy_path}\n")
            note.write("ChatGPT Conversation:\n")
            note.write(conversation_text + "\n")
            note.write("-" * 40 + "\n")

        print(f"Screenshot and conversation saved successfully to: {note_file}")

        # Optional: Save notes as a PDF
        if save_as_pdf:
            if not pdf_path:
                raise ValueError("PDF path must be provided if save_as_pdf is True.")
            
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Add screenshot and conversation text to the PDF
            pdf.cell(200, 10, txt="Screenshot and Notes", ln=True, align='C')
            pdf.ln(10)
            pdf.multi_cell(0, 10, txt=f"Screenshot saved at: {screenshot_copy_path}")
            pdf.ln(5)
            pdf.multi_cell(0, 10, txt="ChatGPT Conversation:")
            pdf.multi_cell(0, 10, txt=conversation_text)
            pdf.ln(10)
            pdf.cell(0, 10, txt="--- End of Notes ---", ln=True)

            # Save PDF file
            pdf.output(pdf_path)
            print(f"PDF successfully saved to: {pdf_path}")

    except Exception as e:
        print(f"Error: {str(e)}")
