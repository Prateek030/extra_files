import logging

# Configure logging
logging.basicConfig(filename='record.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
logging.info('This is an informational message')
logging.warning('This is a warning message')
logging.error('This is an error message')
