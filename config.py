import os
from typing import Literal
from appium.options.android import UiAutomator2Options

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from qa_guru_python_8_22_mobile import utils


class Config(BaseSettings):
    context: Literal["bstack", "local_real", "local_emulator"] = 'bstack'

    timeout: float = os.getenv('TIMEOUT')
    remote_url: str = os.getenv('REMOTE_URL')
    platform_name: str = os.getenv('PLATFORM_NAME', 'Android')
    platform_version: str = os.getenv('ANDROID_VERSION', '10')
    device_name: str = os.getenv('DEVICE_NAME', 'Pixel 4a')

    udid: str = os.getenv('UDID', '')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY', '')
    app_local: str = utils.file.abs_path_from_project(os.getenv('APP'))

    app_bs: str = os.getenv('APP')

    project_name: str = os.getenv('PROJECT_NAME', '')
    build_name: str = os.getenv('BUILD_NAME', '')
    session_name: str = os.getenv('SESSION_NAME', '')

    load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env.credentials'))
    bs_user_name: str = os.getenv('BS_USERNAME')
    bs_password: str = os.getenv('BS_PASSWORD')

    def to_driver_options(self, context) -> UiAutomator2Options:
        options = UiAutomator2Options()

        if context == 'local_real':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_local)

        if context == 'local_emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_local)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('platformVarsion', self.platform_version)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_bs)
            options.set_capability(
                'bstack:options', {
                    'projectName': config.project_name,
                    'buildName': config.build_name,
                    'sessionName': config.session_name,
                    'userName': self.bs_user_name,
                    'accessKey': self.bs_password,
                },
            )

        return options


config = Config()
