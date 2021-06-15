"""
test target_groups
"""
import uuid
import pytest
from tenable.errors import UnexpectedValueError, NotFoundError
from ..checker import check


@pytest.fixture
@pytest.mark.vcr()
def targetgroup(request, api):
    """
    fixture for target group returning the group
    """
    group = api.target_groups.create(str(uuid.uuid4()), ['192.168.0.1'])

    def teardown():
        try:
            api.target_groups.delete(group['id'])
        except NotFoundError:
            pass

    request.addfinalizer(teardown)
    return group


@pytest.mark.vcr()
def test_targetgroups_create_type_unexpectedvalue(api):
    """
        test to raise value error when value is not passed as is

    """
    with pytest.raises(UnexpectedValueError):
        api.target_groups.create('nope', [], type='nope')


@pytest.mark.vcr()
def test_targetgroups_create_acls_typeerror(api):
    """
    test to raise type exception when type is not given as is
    """
    with pytest.raises(TypeError):
        api.target_groups.create('nope', [], acls='nope')


@pytest.mark.vcr()
def test_targetgroups_create_members_unexpectedvalue(api):
    """
    test to raise value error when value is not passed as is
    """
    with pytest.raises(UnexpectedValueError):
        api.target_groups.create('nope', [])


@pytest.mark.vcr()
def test_targetgroups_create(targetgroup):
    """
    test to create target group and verify their types
    """
    assert isinstance(targetgroup, dict)
    check(targetgroup, 'acls', list)
    for i in targetgroup['acls']:
        check(i, 'display_name', str, allow_none=True)
        check(i, 'id', int, allow_none=True)
        check(i, 'name', str, allow_none=True)
        check(i, 'owner', int, allow_none=True)
        check(i, 'permissions', int)
        check(i, 'type', str)
    check(targetgroup, 'creation_date', int)
    check(targetgroup, 'default_group', int)
    check(targetgroup, 'id', int)
    check(targetgroup, 'last_modification_date', int)
    check(targetgroup, 'members', str)
    check(targetgroup, 'name', str)
    check(targetgroup, 'owner', str)
    check(targetgroup, 'owner_id', int)
    check(targetgroup, 'shared', int)
    check(targetgroup, 'user_permissions', int)


@pytest.mark.vcr()
def test_targetgroups_delete_id_typeerror(api):
    """
            test to raise the type error when required type of variable is not given

    """
    with pytest.raises(TypeError):
        api.target_groups.delete('nope')


@pytest.mark.vcr()
def test_targetgroups_delete():
    """
    test to delete the target group

    """



@pytest.mark.vcr()
def test_targetgroups_details_id_typeerror(api):
    """
            test to raise the type error when required type of variable is not given

    """
    with pytest.raises(TypeError):
        api.target_groups.details('nope')


@pytest.mark.vcr()
def test_targetgroups_details(api, targetgroup):
    """
    test to verify the details and their types
    """
    group = api.target_groups.details(targetgroup['id'])
    assert isinstance(group, dict)
    assert group['id'] == targetgroup['id']
    check(group, 'acls', list)
    for i in group['acls']:
        check(i, 'display_name', str, allow_none=True)
        check(i, 'id', int, allow_none=True)
        check(i, 'name', str, allow_none=True)
        check(i, 'owner', int, allow_none=True)
        check(i, 'permissions', int)
        check(i, 'type', str)
    check(group, 'creation_date', int)
    check(group, 'default_group', int)
    check(group, 'id', int)
    check(group, 'last_modification_date', int)
    check(group, 'members', str)
    check(group, 'name', str)
    check(group, 'owner', str)
    check(group, 'owner_id', int)
    check(group, 'shared', int)
    check(group, 'user_permissions', int)


@pytest.mark.vcr()
def test_targetgroups_edit_id_typeerror(api):
    """
        test to raise the type error when required type of variable is not given


    """
    with pytest.raises(TypeError):
        api.target_groups.delete('nope')


@pytest.mark.vcr()
def test_targetgroups_edit_name_typeerror(api):
    """
        test to raise the type error when required type of variable is not given


    """
    with pytest.raises(TypeError):
        api.target_groups.edit(1, 1)


@pytest.mark.vcr()
def test_targetgroups_edit_acls_typeerror(api):
    """
    test to raise the type error when required type of variable is not given
    """
    with pytest.raises(TypeError):
        api.target_groups.edit(1, acls=False)


@pytest.mark.vcr()
def test_targetgroups_edit(api, targetgroup):
    """
    test to edit the target groups
    """
    members = targetgroup['members'].split(',')
    members.append('192.168.0.2')
    resp = api.target_groups.edit(targetgroup['id'], members=members, name='targetgroup_name')
    assert isinstance(resp, dict)
    check(resp, 'acls', list)
    for i in resp['acls']:
        check(i, 'display_name', str, allow_none=True)
        check(i, 'id', int, allow_none=True)
        check(i, 'name', str, allow_none=True)
        check(i, 'owner', int, allow_none=True)
        check(i, 'permissions', int)
        check(i, 'type', str)
    check(resp, 'creation_date', int)
    check(resp, 'default_group', int)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'members', str)
    check(resp, 'name', str)
    check(resp, 'owner', str)
    check(resp, 'owner_id', int)
    check(resp, 'shared', int)
    check(resp, 'user_permissions', int)
    assert resp['members'] == ', '.join(members)


@pytest.mark.vcr()
def test_targetgroups_list(api):
    """
    test to list the target groups
    """
    assert isinstance(api.target_groups.list(), list)
