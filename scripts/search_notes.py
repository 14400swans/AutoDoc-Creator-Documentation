import os

def search_notes(notes_directory, keyword):
    """
    Searches for a keyword in all notes in the specified directory.

    :param notes_directory: Path to the directory containing notes (e.g., "notes/")
    :param keyword: Keyword to search for in the notes
    :return: List of files containing the keyword
    """
    try:
        # Ensure the directory exists
        if not os.path.exists(notes_directory):
            raise FileNotFoundError(f"Notes directory not found: {notes_directory}")

        # Search for the keyword in all files
        matching_files = []
        for file_name in os.listdir(notes_directory):
            file_path = os.path.join(notes_directory, file_name)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    if keyword.lower() in content.lower():
                        matching_files.append(file_name)

        return matching_files

    except Exception as e:
        print(f"Error during search: {str(e)}")
        return []
