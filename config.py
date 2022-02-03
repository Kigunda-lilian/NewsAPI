import os

class Config:

    API_KEY ='bee08ea86b574ea1a3f57291639fe77b'
    API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=bee08ea86b574ea1a3f57291639fe77b'
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}