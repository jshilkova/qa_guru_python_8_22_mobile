import dotenv
import pydantic
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    timeout: float = 10.0
    driver_remote_url: str = 'http://hub.browserstack.com/wd/hub'
    bs_user_name: str
    bs_password: str

    android_version: str = '9.0'
    android_device_name: str = 'Google Pixel 3'

    app: str = 'bs://16443d672ab979600b06068081a1a6bfeba2c054'

    project_name: str = 'Tests Wikipedia App'
    android_build_name: str = 'app-alpha-universal-release'
    android_session_name: str = 'BStack wiki test'


config = Config(_env_file=dotenv.find_dotenv('.env'))
