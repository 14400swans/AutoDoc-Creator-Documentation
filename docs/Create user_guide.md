# User Guide

## Generating Documentation
1. Navigate to the project directory.
2. Run the following command to generate documentation:
    ```bash
    python main.py --generate-docs /path/to/your/project
    ```

## Uploading Files to OneDrive
1. Ensure you have authenticated with your Microsoft account.
2. Use the following command to upload a file:
    ```bash
    curl -X POST https://api.example.com/upload-to-onedrive \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"file_name": "example.txt"}'
    ```

## Managing Files in GitHub
1. Authenticate using your GitHub personal access token.
2. Upload a file to your repository using this command:
    ```bash
    curl -X POST https://api.example.com/upload-to-github \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"repository": "username/repo", "file_path": "docs/example.txt"}'
    ```
