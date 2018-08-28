class Config:
    '''
    General config parent class.
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'


class ProdConfig(Config):
    '''
    Production config child class.

    Args:
    COnfig: The parent config class with general config settings
    '''
    pass

class DevConfig(Config):
     '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
