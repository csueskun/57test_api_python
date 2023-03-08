import json

# Define the content types to be used for the api resposes
CONTENT_TYPES = {
    'json': 'application/json',
    'plain': 'text/plain',
    'html': 'text/html',
}
# Define the correct content types values
VALID_CONTENT_TYPES = [
    'application/json', 'text/plain', 'text/html'
]
def send_response(handler, status_code, body=None, content_type='application/json'):
    # Send the HTTP response
    if content_type not in VALID_CONTENT_TYPES:
        content_type = CONTENT_TYPES.get(content_type, 'application/json')

    handler.send_response(status_code)
    handler.send_header('Content-type', content_type)
    handler.end_headers()

    if body is not None:
        # Encode the response body as JSON or text and send it
        if content_type == 'application/json':
            json_body = json.dumps(body).encode('utf-8')
            handler.wfile.write(json_body)
        elif content_type == 'text/plain':
            text_body = str(body).encode('utf-8')
            handler.wfile.write(text_body)
        elif content_type == 'text/html':
            html_body = str(body).encode('utf-8')
            handler.wfile.write(html_body)
