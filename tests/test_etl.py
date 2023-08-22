import pytest
import tempfile
import os

from src.jobs.etl import extract_data

# Define a fixture to create a temporary directory for testing
@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp:
        yield temp

# Define the test function
def test_extract_data(temp_dir):
    extract_data(destination_dir=temp_dir)

    # Check if the destination directory is not empty
    assert os.listdir(temp_dir)
