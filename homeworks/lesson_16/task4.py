# Task 4

# Custom exception

# Create your custom exception named `CustomException`, you can inherit from base Exception class, 
# but extend its functionality to log every error message to a file named `logs.txt`. 
# Tips: Use __init__ method to extend functionality for saving messages to file


class CustomException(Exception):

    def __init__(self, msg):
        self.message = msg
        with open('logs.txt', 'a') as log:
            log.write(self.message + '\n')
        super().__init__('Exception occured')


    def __str__(self) -> str:
        return 'Exception occured __str__'

raise CustomException('Test exception raised explicitly')