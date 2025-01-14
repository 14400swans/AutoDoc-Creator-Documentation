# API Reference

## Generate Content
- **Endpoint**: `/generate-content`
- **Method**: POST
- **Parameters:**
  - `prompt` (string): User input for generating content.
- **Response**:
    ```json
    {
      "content": "Generated content based on the input."
    }
    ```

## Upload File to OneDrive
- **Endpoint**: `/upload-to-onedrive`
- **Method**: POST
- **Parameters:**
  - `file_name` (string): Name of the file to upload.
- **Response**:
    ```json
    {
      "status": "success",
      "file_url": "https://onedrive.com/your-file-url"
    }
    ```

## Upload File to GitHub
- **Endpoint**: `/upload-to-github`
- **Method**: POST
- **Parameters:**
  - `repository` (string): Target GitHub repository.
  - `file_path` (string): Path where the file should be uploaded.
- **Response**:
    ```json
    {
      "status": "success",
      "file_url": "https://github.com/username/repo/path/to/file"
    }
    ```
