"""
test folders
"""
import uuid
import pytest
from ..checker import check


@pytest.mark.vcr()
def test_folders_folder_name_typeerror(api):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.folders.create(1)


@pytest.mark.vcr()
def test_folders_create(folder):
    """
    test to create the folders
    """
    assert isinstance(folder, int)


@pytest.mark.vcr()
def test_folders_delete(api, folder):
    """
    test to delete the folders
    """
    api.folders.delete(folder)
    assert folder not in [f['id'] for f in api.folders.list()]


@pytest.mark.vcr()
def test_folders_edit_name_typeerror(api, folder):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.folders.edit(folder, 1)


@pytest.mark.vcr()
def test_folders_edit(api, folder):
    """
    test to edit the folders
    """
    api.folders.edit(folder, str(uuid.uuid4())[:20])


@pytest.mark.vcr()
def test_folders_list_success(api):
    """
    test to list the folders and verifying their types
    """
    folders = api.folders.list()
    assert isinstance(folders, list)
    for fold in folders:
        check(fold, 'custom', int)
        check(fold, 'default_tag', int)
        check(fold, 'name', str)
        check(fold, 'type', str)
        check(fold, 'id', int)
        check(fold, 'unread_count', int)
