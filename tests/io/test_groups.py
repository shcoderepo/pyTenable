"""
Groups
"""
import uuid
import pytest
from tenable.errors import NotFoundError
from ..checker import check


@pytest.fixture
def group(request, api):
    """
    fixture to create a group
    """
    group = api.groups.create(str(uuid.uuid4()))

    def teardown():
        try:
            api.groups.delete(group['id'])
        except NotFoundError:
            pass

    request.addfinalizer(teardown)
    return group


@pytest.mark.vcr()
def test_groups_create_name_typeerror(api):
    """
        test to raise the error when required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.groups.create(1)


@pytest.mark.vcr()
def test_groups_create(group):
    """
    test to create a group and verify their types
    """
    assert isinstance(group, dict)
    check(group, 'uuid', 'uuid')
    check(group, 'name', str)
    check(group, 'permissions', int)
    check(group, 'id', int)


@pytest.mark.vcr()
def test_groups_delete_id_typerror(api):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.groups.delete('nothing')


@pytest.mark.vcr()
def test_groups_delete_notfounderror(api):
    """
    test to raise exception when the group id is not found for deletion.
    """
    with pytest.raises(NotFoundError):
        api.groups.delete(1)


@pytest.mark.vcr()
def test_groups_delete_success(api, group):
    """
    test to delete the group
    """
    api.groups.delete(group['id'])


@pytest.mark.vcr()
def test_groups_edit_id_typeerror(api):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.groups.edit('nope', 'something')


@pytest.mark.vcr()
def test_groups_edit_name_typeerror(api):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.groups.edit(1, 1)


@pytest.mark.vcr()
def test_groups_edit_notfounderror(api):
    """

    test to raise exception when particular group is not found to do a edit.
    """
    with pytest.raises(NotFoundError):
        api.groups.edit(1, 'newname')


@pytest.mark.vcr()
def test_groups_edit_success(api, group):
    """
    test to edit the group and verify the types
    """
    edited = api.groups.edit(group['id'], 'New Example Name')
    assert isinstance(edited, dict)
    check(edited, 'uuid', 'uuid')
    check(edited, 'name', str)
    check(edited, 'permissions', int)
    check(edited, 'user_count', int)
    check(edited, 'id', int)


@pytest.mark.vcr()
def test_groups_list(api):
    """
    test to be raised to check the list and verify their types
    """
    groups = api.groups.list()
    assert isinstance(groups, list)
    for group in groups:
        assert isinstance(group, dict)
        check(group, 'id', int)
        check(group, 'name', str)
        check(group, 'permissions', int)
        check(group, 'user_count', int)
        check(group, 'uuid', 'uuid')


@pytest.mark.vcr()
def test_groups_list_users_id_typeerror(api):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.groups.list_users('nope')


@pytest.mark.vcr()
def test_groups_list_users_notfound(api):
    """
    test raised when list of users not found in the list
    """
    with pytest.raises(NotFoundError):
        api.groups.list_users(1)


@pytest.mark.vcr()
def test_groups_list_users_success(api, group, user):
    """
    test to list the users in the group

    """
    api.groups.add_user(group['id'], user['id'])
    users = api.groups.list_users(group['id'])
    assert isinstance(users, list)
    for use in users:
        assert isinstance(use, dict)
        check(use, 'id', int)
        check(use, 'username', str)
        check(use, 'name', str)
        check(use, 'email', str)
        check(use, 'permissions', int)
        check(use, 'type', str)
        check(use, 'login_fail_count', int)
        check(use, 'login_fail_total', int)
        check(use, 'last_login_attempt', int)
        check(use, 'enabled', bool)
        check(use, 'uuid_id', 'uuid')


@pytest.mark.vcr()
def test_group_add_user_to_group_group_id_typeerror(api):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.groups.add_user('nope', 1)


@pytest.mark.vcr()
def test_groups_add_user_to_group_user_id_typeerror(api):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.groups.add_user(1, 'nope')


@pytest.mark.vcr()
def test_groups_add_user_to_group_notfounderror(api):
    """
    test to raise error when the user needed to be added to the group is not found
    """
    with pytest.raises(NotFoundError):
        api.groups.add_user(1, 1)


@pytest.mark.vcr()
def test_groups_add_user_to_group_success(api, group, user):
    """
    test to add user to the group
    """
    api.groups.add_user(group['id'], user['id'])


@pytest.mark.vcr()
def test_groups_delete_user_from_group_group_id_tyupeerror(api):
    """
        test to raise the error when required type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.groups.delete_user('nope', 1)


@pytest.mark.vcr()
def test_groups_delete_user_from_group_user_id_typeerror(api):
    """
    test to raise the error when required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.groups.delete_user(1, 'nope')


@pytest.mark.vcr()
def test_groups_delete_user_from_group_notfounderror(api):
    """
    test to raise error when the user is not found in the group
    """
    with pytest.raises(NotFoundError):
        api.groups.delete_user(1, 1)


@pytest.mark.vcr()
def test_groups_delete_user_from_group_success(api, group, user):
    """
    test to delete user from group
    """
    api.groups.add_user(group['id'], user['id'])
    api.groups.delete_user(group['id'], user['id'])


@pytest.mark.vcr()
def test_groups_list_success(api):
    """
    test to list the group list and verifying the types
    """
    res = api.groups.list()
    assert isinstance(res, list)
    for i in enumerate(res):
        if not i[1].get('immutable') or not i[1].get('membership_fixed') or \
                not i[1].get('role'):
            check(i[1], 'name', str, allow_none=True)
            check(i[1], 'uuid', str, allow_none=True)
            check(i[1], 'user_count', int, allow_none=True)
            check(i[1], 'id', int, allow_none=True)
            check(i[1], 'container_uuid', str, allow_none=True)
        else:
            check(i[1], 'name', str, allow_none=True)
            check(i[1], 'uuid', str, allow_none=True)
            check(i[1], 'user_count', int, allow_none=True)
            check(i[1], 'id', int, allow_none=True)
            check(i[1], 'container_uuid', str, allow_none=True)
            check(i[1], 'role', str, allow_none=True)
            check(i[1], 'immutable', bool, allow_none=True)
            check(i[1], 'membership_fixed', bool, allow_none=True)
