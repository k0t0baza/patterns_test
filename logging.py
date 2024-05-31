from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Log: {message}")

class FileLogger(Logger):
    def __init__(self, filename):
        self._filename = filename

    def log(self, message):
        with open(self._filename, 'a') as f:
            f.write(f"{message}\n")

class SuperConsoleLogger(Logger):
    def log(self, message):
        print(f"SUPER_Log: {message}")