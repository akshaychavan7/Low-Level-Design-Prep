class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance



s1 = Singleton()
s2 = Singleton()
print(s1 is s2) # True

"""
It prevents multiple instances of a class.

Ensures shared access to a single, consistent object.

It’s commonly used in scenarios like:

Configuration managers

Logging systems

Database connection pools
"""