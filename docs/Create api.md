# API Reference

## 1. Generate Content
- **Endpoint**: `/generate-content`
- **Method**: POST
- **Parameters:**
  - `prompt` (string): User input for generating content.
- **Response:**
    ```json
    {
      "content": "Generated content based on the input."
    }
    ```

## 2. Upload File to OneDrive
- **Endpoint**: `/upload-to-onedrive`
- **Method**: POST
- **Parameters:**
  - `file_name` (string): Name of the file to upload.
- **Response:**
    ```json
    {
      "status": "success",
      "file_url": "https://onedrive.com/your-file-url"
    }
    ```

## 3. Upload File to GitHub
- **Endpoint**: `/upload-to-github`
- **Method**: POST
- **Parameters:**
  - `repository` (string): Target GitHub repository.
  - `file_path` (string): Path where the file should be uploaded.
- **Response:**
    ```json
    {
      "status": "success",
      "file_url": "https://github.com/username/repo/path/to/file"
    }
    ```
