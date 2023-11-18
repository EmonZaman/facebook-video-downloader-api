# Facebook Video Downloader API

The Facebook Video Downloader API is a Flask-based web service that provides an efficient way to fetch download links for videos from Facebook. It allows users to retrieve both standard and high-definition video links.

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Flask
- Requests

### Installation

1. **Clone the Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/ornob011/Facebook-Video-Downloader-API
   ```

2. **Install Dependencies**:
    Navigate to the project directory and install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Run the application with the following command:

```bash
python app.py
```

The Flask server will start at http://127.0.0.1:5000/.


### Using the API
#### Endpoint: Get Video Links

- URL: /get_video_links
- Method: GET
- URL Params:
    - Required: url=[string] (The Facebook video URL)

### Testing the Endpoint
#### Via Web Browser

To test the endpoint via a web browser, simply navigate to the following URL (replace <Facebook_Video_URL> with the actual Facebook video URL):

```bash
http://127.0.0.1:5000/get_video_links?url=<Facebook_Video_URL>
```

For example:

```bash
http://127.0.0.1:5000/get_video_links?url=https://www.facebook.com/watch/?v=409178427022717
```

#### Via cURL

You can also use cURL in your command line:

```bash
curl "http://127.0.0.1:5000/get_video_links?url=https://www.facebook.com/watch/?v=409178427022717"
```

#### Via Postman

1. Open Postman: Launch the Postman application on your computer.

2. Create a New Request:
    - Click on the 'New' button or '+' tab to start a new request. Set the request method to GET by selecting it from the dropdown menu next to the URL input field.

3. Enter the URL:
    - In the URL input field, enter: http://127.0.0.1:5000/get_video_links

4. Add Query Parameters:
    - Below the URL input field, locate the section for entering query parameters.
    - In the `Key` field, enter `url`.
    - In the `Value` field, enter the Facebook video URL. For example: https://www.facebook.com/watch/?v=409178427022717

5. Send the Request:
    - Click the 'Send' button to execute the request.

6. View the Response:
    - The response will be displayed in the lower section of the Postman interface.
    - If successful, you should see a JSON response with the video title and download links.

Here's an illustration of what your Postman setup might look like:

- Method: GET
- URL: http://127.0.0.1:5000/get_video_links
- Query Params:
    - Key: `url`
    - Value: https://www.facebook.com/watch/?v=409178427022717

#### Sample Response:

The API responds with a JSON object containing the title of the video and download links:

```bash
{
    "links": {
        "Download Low Quality": "https://example.com/sd_link&dl=1",
        "Download High Quality": "https://example.com/hd_link&dl=1"
    },
    "success": true,
    "title": "Example Video Title"
}
```

If an error occurs (e.g., invalid URL), the API responds with:

```bash
{
    "links": {
    },
    "success": false,
    "message": "Error message"
}
```

### Important Notice

#### Warning: This API cannot retrieve download links for private videos on Facebook. It only works with videos that are publicly accessible. If you attempt to fetch links for a private video, the API will not be able to retrieve the necessary data and will return an error message.

Always ensure that the URL provided is for a public Facebook video. This limitation is due to privacy restrictions on Facebook's platform.

### Troubleshooting

- Ensure that the provided URL is a valid Facebook video URL (e.g., https://www.facebook.com/watch/?v=409178427022717).
- Check if the Flask server is running and accessible.