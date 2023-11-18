from flask import Flask, request, jsonify
import requests
import re
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

class VideoLinkExtractor:
    """Class for extracting video links from HTML content."""
    
    def __init__(self, html_content):
        self.html_content = html_content

    def clean_str(self, s):
        """Cleans and returns a JSON-encoded string."""
        try:
            return json.loads(f'{{"text": "{s}"}}')['text']
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return None

    def get_link(self, regex):
        """Extracts and returns link based on the provided regex."""
        match = re.search(regex, self.html_content)
        return self.clean_str(match.group(1)) if match else None

    def get_title(self):
        """Extracts and returns the title from HTML content."""
        return self.get_link(r'<title>(.*?)<\/title>')

@app.route('/get_video_links', methods=['GET'])
def get_video_links():
    """Endpoint to get video links."""
    url = request.args.get('url')
    if not url:
        return jsonify({'success': False, 'message': 'Please provide the URL'}), 400

    headers = {
        'sec-fetch-user': '?1',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-site': 'none',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'cache-control': 'max-age=0',
        'authority': 'www.facebook.com',
        'upgrade-insecure-requests': '1',
        'accept-language': 'en-GB,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,en-US;q=0.6',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        extractor = VideoLinkExtractor(response.text)

        video_info = {
            'success': True,
            'title': extractor.get_title(),
            'links': {}
        }

        sd_link = extractor.get_link(r'browser_native_sd_url":"([^"]+)"')
        if sd_link:
            video_info['links']['Download Low Quality'] = sd_link + '&dl=1'

        hd_link = extractor.get_link(r'browser_native_hd_url":"([^"]+)"')
        if hd_link:
            video_info['links']['Download High Quality'] = hd_link + '&dl=1'

        return jsonify(video_info)
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Specified port

