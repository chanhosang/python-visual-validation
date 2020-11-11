import pytest
import json
from selenium import webdriver

from core.eyes_manager import EyesManager


@pytest.fixture(scope='module')
def manager(driver):
    eyes_manager = EyesManager(driver)
    yield eyes_manager


@pytest.fixture(scope='module')
def config():

  # Read the file
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  # Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config so it can be used
  return config

@pytest.fixture(scope='module')
def driver(config):
    # driver = webdriver.Chrome()

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        driver = webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    yield driver
    driver.quit()
