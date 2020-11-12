import os

from applitools.common import BatchInfo
from applitools.selenium import Eyes

from core.helper import get_resources_dir_path
from core.helper import get_libs_dir_path
from core.io import execute_cmd

# from config.base import APPLITOOLS_API_KEY
import configparser
config = configparser.ConfigParser()
config.read('config/.env')
APPLITOOLS_API_KEY = config['APPLITOOLS']['APPLITOOLS_API_KEY']


IMAGE_TESTER_PATH = "{}/ImageTester_1.4.5.2.jar".format(get_libs_dir_path())

class EyesManager:
    def __init__(self, driver):
        self.app_name = None
        self.driver = driver
        self.eyes = self.initialize_eyes()

    @staticmethod
    def initialize_eyes():
        if os.path.exists(IMAGE_TESTER_PATH):
            eyes = Eyes()
            eyes.api_key = APPLITOOLS_API_KEY
            return eyes
        else:
            raise Exception(f'Unable to access jarfile:"{IMAGE_TESTER_PATH}". Please download from https://bintray.com/applitoolseyes/generic/ImageTester.')

    def set_app_name(self, app_name):
        self.app_name = app_name

    def set_batch(self, batch_name):
        if batch_name:
            batch_info = BatchInfo(batch_name)
            self.eyes.batch = batch_info

    def validate_window(self, tag=None, full_page=False):
        if full_page:
            self.eyes.force_full_page_screenshot = True

        self.eyes.check_window(tag=tag)

    def validate_element(self, element, tag=None):
        self.eyes.check_region(element, tag=tag)

    def validate_frame(self, frame_reference, region, tag=None):
        self.eyes.check_region_in_frame(frame_reference, region, tag=tag)

    @staticmethod
    def validate_pdf():
        print("validate_pdf.IMAGE_TESTER_PATH="+IMAGE_TESTER_PATH)
        print("validate_pdf.APPLITOOLS_API_KEY="+APPLITOOLS_API_KEY)
        print("validate_pdf.get_resources_dir_path()="+get_resources_dir_path())
        cmd = """java -jar {} -k {} -f {}""".format(IMAGE_TESTER_PATH,
                                                    APPLITOOLS_API_KEY,
                                                    get_resources_dir_path())

        output, _ = execute_cmd(cmd)
        str_output = output.decode('utf-8')

        print('Command execution completed... \n' + str_output)
        return str_output

    def open_eyes(self, test_name):
        self.eyes.open(self.driver, self.app_name,
                       test_name=test_name)

    def close_eyes(self):
        self.eyes.close()
