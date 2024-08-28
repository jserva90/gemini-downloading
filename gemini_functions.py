import requests

def download_file(url: str, save_path: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {save_path}")
        return {"status": "File downloaded successfully"}
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        return {"status": "Downloading file failed"}


definitions = [
    {
        "name": "download_file",
        "description": "Downloads a file from the given URL and saves it to the specified path.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL to download the file from"
                },
                "save_path": {
                    "type": "string",
                    "description": "The local file path to save the downloaded file"
                }
            }
        }
    }
]