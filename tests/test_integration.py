import pytest
from kaggle import api 

def test_kaggle_api():
    # Call the competitions_list function
    competitions = api.competitions_list()

    # Check if the returned value is not None
    assert competitions is not None, "competitions_list returned None"

    # Check if the list is not empty
    assert len(competitions) > 0, "competitions_list returned an empty list"


