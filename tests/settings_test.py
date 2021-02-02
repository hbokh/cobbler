import os
import time

import pytest
from schema import SchemaError

from cobbler import settings
from cobbler.settings import Settings


class TestSettings:
    def test_set(self):
        # Arrange
        test_settings = Settings()

        # Act
        test_settings.set()

        # Assert
        assert False

    def test_to_string(self):
        # Arrange
        test_settings = Settings()

        # Act
        test_settings.to_string()

        # Assert
        assert False

    def test_to_dict(self):
        # Arrange
        test_settings = Settings()

        # Act
        test_settings.to_dict()

        # Assert
        assert False

    def test_from_dict(self):
        # Arrange
        test_settings = Settings()

        # Act
        test_settings.from_dict()

        # Assert
        assert False


@pytest.mark.parametrize("parameter,expected_exception,expected_result", [
    ({}, pytest.raises(SchemaError), None)
])
def test_validate_settings(parameter, expected_exception, expected_result):
    # Arrange

    # Act
    with expected_exception:
        result = settings.validate_settings(parameter)

    # Assert
    assert result == expected_result


def test_parse_bind_config():
    # Arrange

    # Act
    settings.parse_bind_config()

    # Assert
    assert True


def test_autodect_bind_chroot():
    # Arrange

    # Act
    settings.autodetect_bind_chroot()

    # Assert
    assert True


def test_read_settings_file():
    # Arrange
    # Default path should be fine for the tests.

    # Act
    result = settings.read_settings_file()

    # Assert
    assert isinstance(result, dict)
    assert result.get("include")


@pytest.mark.skip("This breaks a lot of tests if we don't insert the full settings here.")
def test_update_settings_file():
    # Arrange
    settings_data = None
    time_before_write = time.time()

    # Act
    result = settings.update_settings_file(settings_data)

    # Assert
    assert result
    # This should work the following: The time of modifying the settings file should be greater then the time taken
    # before modifying it. Thus the value of the subtraction of both should be greater than zero. If writing to the
    # files does not work, this is smaller then 0. The content is a yaml file thus we don't want to test if writing a
    # YAML file is logically correct. This is the matter of the library we are using.
    assert os.path.getmtime("/etc/cobbler/settings.yaml") - time_before_write > 0


@pytest.mark.skip("This breaks a lot of tests if we don't insert the full settings here.")
def test_update_settings_file_safe():
    # Arrange

    # Act
    settings.update_settings_file_safe()

    # Assert
    assert False
