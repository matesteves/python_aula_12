from abc import ABC, abstractmethod

class AbstractDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        raise NotImplementedError("Method not Implemented")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Method not Implemented")

    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Method not Implemented")
    
    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Method not Implemented")
    
    def hello_world(self):
        print('Hello World')