# __init__.py

import random
import logging

# Configure logging for the package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        logger.info("Preprocessing data...")
        # Implement preprocessing logic
        return self.data

    def postprocess(self, processed_data):
        logger.info("Postprocessing data...")
        # Implement postprocessing logic
        return processed_data

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

def random_greeting():
    greetings = ['Hello', 'Hi', 'Hey', 'Greetings', 'Welcome']
    return random.choice(greetings)

def complex_computation(x):
    logger.info("Performing a complex computation...")
    result = (MathUtils.multiply(x, x) + MathUtils.add(x, 2)) / 2
    return result

class CustomException(Exception):
    pass

def risky_operation():
    if random.random() < 0.5:
        raise CustomException("Risky operation failed")
    return "Success"

if __name__ == "__main__":
    # Example usage of the package's functionality
    processor = DataProcessor([1, 2, 3, 4])
    processed_data = processor.preprocess()
    postprocessed_data = processor.postprocess(processed_data)

    print(random_greeting())
    print(f"Complex computation result: {complex_computation(10)}")

    try:
        result = risky_operation()
        print(f"Risky operation result: {result}")
    except CustomException as e:
        logger.error(f"An error occurred: {e}")
