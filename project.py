from typing import Literal

import dotenv
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    context: Literal['android', 'ios'] = 'ios'
    timeout: float = 10.0
    driver_remote_url: str = 'http://hub.browserstack.com/wd/hub'
    bs_user_name: str
    bs_password: str

    android_version: str = '9.0'
    android_device_name: str = 'Google Pixel 3'

    ios_version: str = '16.0'
    ios_device_name: str = 'iPhone 14 Pro Max'

    android_app: str = 'bs://16443d672ab979600b06068081a1a6bfeba2c054'
    ios_app: str = 'bs://524c466aabbedecc62e9432ff651334599e5127e'

    project_name: str = 'Tests Wikipedia App'
    android_build_name: str = 'app-alpha-universal-release'
    android_session_name: str = 'BStack wiki test'

    ios_build_name: str = 'test-build'
    ios_session_name: str = 'BStack app test'


config = Config(_env_file=dotenv.find_dotenv('.env'))
