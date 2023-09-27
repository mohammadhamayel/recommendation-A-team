import logging

log_level = logging.INFO

logger = logging.getLogger(__name__)
logger.setLevel(log_level)

log_file = './recommendation_app.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(log_level)

console_handler = logging.StreamHandler()
console_handler.setLevel(log_level)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Function to log request and response details
def log_request_response_details(request=None, response=None):
    try:
        # Log the request method, path, and headers
        if request is not None:
            logger.info(f'Request Method: {request.method}')
            logger.info(f'Request Path: {request.path}')
            logger.info(f'Request Headers: {dict(request.headers)}')

        if response is not None:
            # Log the response status code, body, and headers
            logger.info(f'Response : {response}')


    except Exception as e:
        logger.error(f'Error logging request/response details: {str(e)}')
