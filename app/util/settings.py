import os 

class Settings():
    PROJECT_TITLE: str = "TSEU Sandbox Application"
    PROJECT_VERSION: str = "0.0.1" 

    # DATABASE_DRIVER = os.environ["DATABASE_DRIVER"]
    # DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
    # DATABASE_HOST = os.environ["DATABASE_HOST"]
    # DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
    # DATABASE_NAME = os.environ["DATABASE_NAME"]
    
    def __init__(self) -> None:
        self.project_title: str = "TSEU Sandbox Application"
        self.project_version: str = "0.0.1"
        self.database_driver: str = os.environ["DATABASE_DRIVER"]
        self.database_username: str = os.environ["DATABASE_USERNAME"]
        self.database_host: str = os.environ["DATABASE_HOST"]
        self.database_password: str = os.environ["DATABASE_PASSWORD"]
        self.database_name: str = os.environ["DATABASE_NAME"]

    def get_alchemy_dict(self) -> dict:
        alchemy_dict = {
            "drivername": self.database_driver, 
            "username": self.database_username,
            "host": self.database_host, 
            "password":self.database_password, 
            "database":self.database_name
        }

        return alchemy_dict

    # def get_alchemy_dict(self) -> dict:
    #     alchemy_dict = {
    #         "drivername": self.DATABASE_DRIVER, 
    #         "username": self.DATABASE_USERNAME,
    #         "host": self.DATABASE_HOST, 
    #         "password":self.DATABASE_PASSWORD, 
    #         "database":self.DATABASE_NAME
    #     }

    #     return alchemy_dict