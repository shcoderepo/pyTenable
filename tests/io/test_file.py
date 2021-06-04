from tenable.errors import *
from ..checker import check, single
import uuid, pytest

@pytest.mark.vcr()
def test_files_upload(api):
    api.files.upload('ExampleDataGoesHere')

@pytest.mark.vcr()
def test_files_encryption_success(api):
    with open('tests/io/testfile.txt', 'rb') as fobj:
        api.files.upload(fobj, encrypted=True)