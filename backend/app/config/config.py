from dotenv import dotenv_values

class Settings:

    def __init__(self, environment) -> None:
        self.environment = environment
        self.__config = None
    
    def set_config(self, config):
        self.__config = config
    
    def get_config(self):
        return self.__config

    def setup_config(self):
        self.__config = self.__get_envs(self.environment)

    def __get_envs(self, environment="dev"):
        if environment == "prod":
            return dotenv_values("./prod.env")  
        elif environment == "dev":
            return dotenv_values("./dev.env")  

        raise ValueError(f'Cannot get an invalid environment "{environment}" ')
    
    def get_env_variable(self, key: str):
        """Obtiene el valor de una variable de entorno dado su key"""
        if self.__config is None:
            raise ValueError("Configuration is not set up. Call setup_config() first.")
        return self.__config.get(key)
    
    def __getattr__(self, name: str):
        """Permite acceder a las variables de entorno como si fueran atributos de la clase"""
        if self.__config is None:
            raise ValueError("Configuration is not set up. Call setup_config() first.")
        if name == "environment":
            return self.environment
        if name in self.__config:
            if name.endswith("_PORT"):
                return int(self.__config[name])
            return self.__config[name]
        

        raise AttributeError(f"'Setting' object has no attribute '{name}'")