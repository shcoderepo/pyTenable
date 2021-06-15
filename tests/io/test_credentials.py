"""
test credentials
"""
import uuid
import pytest
from tenable.errors import UnexpectedValueError, APIError
from ..checker import check, single


def test_credentials_permissions_constructor_tuple_permission_type_typeerror(api):
    """
            test to raise the exception when the required type is not passed for the argument

    """
    with pytest.raises(TypeError):
        getattr(api.credentials,'_permissions_constructor')([
            (1, 32, str(uuid.uuid4()))])


def test_credentials_permissions_constructor_tuple_permission_type_unexpectedvalueerror(api):
    """
            test to raise the exception when the required value is not passed for the argument

    """
    with pytest.raises(UnexpectedValueError):
        getattr(api.credentials,'_permissions_constructor')([
            ('nope', 32, str(uuid.uuid4()))])


def test_credentials_permissions_constructor_tuple_permission_permission_unexpectedvalueerror(api):
    """
            test to raise the exception when the required value is not passed for the argument

    """
    with pytest.raises(UnexpectedValueError):
        getattr(api.credentials, '_permissions_constructor')([
            ('user', 256, str(uuid.uuid4()))])


def test_credentials_permissions_constructor_tuple_permission_uuid_typeerror(api):
    """
            test to raise the exception when the required type is not passed for the argument

    """
    with pytest.raises(TypeError):
        getattr(api.credentials, '_permissions_constructor')([
            ('user', 32, 1)])


def test_credentials_permissions_constructor_tuple_permission_uuid_unexpectedvalueerror(api):
    """
            test to raise the exception when the required value is not passed for the argument

    """
    with pytest.raises(UnexpectedValueError):
        getattr(api.credentials, '_permissions_constructor')([
            ('user', 32, 'someone')])


def test_credentials_permissions_constructor_dict_permission_type_typeerror(api):
    """
            test to raise the exception when the required type is not passed for the argument

    """
    with pytest.raises(TypeError):
        getattr(api.credentials, '_permissions_constructor')([{
            'type': 1,
            'permissions': 32,
            'grantee_uuid': str(uuid.uuid4())
        }])


def test_credentials_permissions_constructor_dict_permission_type_unexpectedvalueerror(api):
    """
            test to raise the exception when the required value is not passed for the argument

    """
    with pytest.raises(UnexpectedValueError):
        getattr(api.credentials, '_permissions_constructor')([{
            'type': 'nope',
            'permissions': 32,
            'grantee_uuid': str(uuid.uuid4())
        }])


def test_credentials_permissions_constructor_dict_permission_permission_unexpectedvalueerror(api):
    """
            test to raise the exception when the required value is not passed for the argument

    """
    with pytest.raises(UnexpectedValueError):
        getattr(api.credentials, '_permissions_constructor')([{
            'type': 'user',
            'permissions': 256,
            'grantee_uuid': str(uuid.uuid4())
        }])


def test_credentials_permissions_constructor_dict_permission_uuid_typeerror(api):
    """
            test to raise the exception when the required type is not passed for the argument

    """
    with pytest.raises(TypeError):
        getattr(api.credentials, '_permissions_constructor')([{
            'type': 'user',
            'permissions': 32,
            'grantee_uuid': 1
        }])


def test_credentials_permissions_constructor_dict_permission_uuid_unexpectedvalueerror(api):
    """
            test to raise the exception when the required value is not passed for the argument

    """
    with pytest.raises(UnexpectedValueError):
        getattr(api.credentials, '_permissions_constructor')([{
            'type': 'user',
            'permissions': 32,
            'grantee_uuid': 'someone'
        }])


def test_credentials_permissions_constructor_tuple_success(api):
    """
    test to validates and/or transforms thew permissions items into tuple
    """
    test_id = str(uuid.uuid4())
    resp = getattr(api.credentials, '_permissions_constructor')([('user', 32, test_id)])
    assert resp== [{
        'type': 'user',
        'permissions': 32,
        'grantee_uuid': test_id
    }]

    resp = getattr(api.credentials, '_permissions_constructor')([('user', 'use', test_id)])
    assert resp == [{
        'type': 'user',
        'permissions': 32,
        'grantee_uuid': test_id
    }]


def test_credentials_permissions_constructor_dict_success(api):
    """
     test to validates and/or transforms thew permissions items into the desired
        format
    """
    test_id = str(uuid.uuid4())
    resp = getattr(api.credentials, '_permissions_constructor')([{'type': 'user',
                                                                  'permissions': 32,
                                                                  'grantee_uuid': test_id}])
    assert resp == [{
        'type': 'user',
        'permissions': 32,
        'grantee_uuid': test_id
    }]


@pytest.fixture
def cred(request, api, vcr):
    """
    Returns: credential_uuid

    """
    with vcr.use_cassette('test_credentials_create_success'):
        cred = api.credentials.create('Example Cred', 'SSH',
                                      username='root',
                                      password='something',
                                      auth_method='password',
                                      elevate_privileges_with='Nothing',
                                      custom_password_prompt='')

    def teardown():
        try:
            with vcr.use_cassette('test_credentials_delete_success'):
                api.credentials.delete(cred)
        except APIError:
            pass

    request.addfinalizer(teardown)
    return cred


def test_credentials_create_cred_name_typeerror(api):
    """
        test to raise the exception when the required type is not passed for the argument

    """
    with pytest.raises(TypeError):
        api.credentials.create(1, 'something')


def test_credentials_create_cred_type_typeerror(api):
    """
        test to raise the exception when the required type is not passed for the argument

    """
    with pytest.raises(TypeError):
        api.credentials.create('something', 1)


def test_credentials_create_description_typeerror(api):
    """
        test to raise the exception when the required type is not passed for the argument

    """
    with pytest.raises(TypeError):
        api.credentials.create('something', 'something', 1)


@pytest.mark.vcr()
def test_credentials_create_success(cred):
    """
    test to create the credentials
    """
    single(cred, 'uuid')


def test_credentials_delete_id_typeerror(api):
    """
        test to raise the exception when the required type is not passed for the argument
    """
    with pytest.raises(TypeError):
        api.credentials.delete(1)


def test_credentials_delete_id_unexpectedvalueerror(api):
    """
        test to raise the exception when the required value is not passed for the argument

    """
    with pytest.raises(UnexpectedValueError):
        api.credentials.delete('something')


@pytest.mark.vcr()
def test_credentials_delete_success(api, cred):
    """
    test to delete the credentials
    """
    api.credentials.delete(cred)


def test_credentials_edit_id_typeerror(api):
    """
        test to raise the exception when the required type is not passed for the argument

    """
    with pytest.raises(TypeError):
        api.credentials.edit(1)


def test_credentials_edit_id_unexpectedvalueerror(api):
    """
        test to raise the exception when value is not passed as it should be

    """
    with pytest.raises(UnexpectedValueError):
        api.credentials.edit('something')


def test_credentials_details_id_typeerror(api):
    """
    test to raise the exception when the required type is not passed for the argument
    """
    with pytest.raises(TypeError):
        api.credentials.details(1)


def test_credentials_details_id_unexpectedvalueerror(api):
    """
    test to raise the exception when value is not passed as it should be
    """
    with pytest.raises(UnexpectedValueError):
        api.credentials.details('something')


@pytest.mark.vcr()
def test_credentials_details_success(api):
    """
    test to check the details of the credentials provided and to verify their types
    """
    credential_list = api.credentials.list()
    cred_list = []
    uuid_list = [cred_list.append(i.get('uuid')) for i in credential_list]
    creds = api.credentials.details(cred_list[0])
    assert isinstance(creds, dict)
    check(creds, 'name', str)
    check(creds, 'description', str)
    check(creds, 'category', dict)
    check(creds['category'], 'id', str)
    check(creds['category'], 'name', str)
    check(creds, 'type', dict)
    check(creds['type'], 'id', str)
    check(creds['type'], 'name', str)
    check(creds, 'ad_hoc', bool)
    check(creds, 'user_permissions', int)
    check(creds, 'settings', dict)
    for k in creds['settings']:
        check(creds['settings'], k, str)
    check(creds, 'permissions', list)
    for permission in creds['permissions']:
        check(permission, 'grantee_uuid', 'uuid')
        check(permission, 'type', str)
        check(permission, 'permissions', int)
        check(permission, 'name', str)


@pytest.mark.vcr()
def test_credentials_list_offset_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(offset='nope')


@pytest.mark.vcr()
def test_credentials_list_limit_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(limit='nope')


@pytest.mark.vcr()
def test_credentials_list_sort_field_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(sort=((1, 'asc'),))


@pytest.mark.vcr()
def test_credentials_list_sort_direction_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(sort=(('uuid', 1),))


@pytest.mark.vcr()
def test_credentials_list_sort_direction_unexpectedvalue(api):
    """
    test to raise the exceptionwhen the required value of variable is not passed
    """
    with pytest.raises(UnexpectedValueError):
        api.credentials.list(sort=(('uuid', 'nope'),))


@pytest.mark.vcr()
def test_credentials_list_filter_name_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list((1, 'match', 'win'))


@pytest.mark.vcr()
def test_credentials_list_filter_operator_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(('name', 1, 'win'))


@pytest.mark.vcr()
def test_credentials_list_filter_value_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(('name', 'match', 1))


@pytest.mark.vcr()
def test_credentials_list_filter_type_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(filter_type=1)


@pytest.mark.vcr()
def test_credentials_list_wildcard_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(wildcard=1)


@pytest.mark.vcr()
def test_credentials_list_wildcard_fields_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        api.credentials.list(wildcard_fields='nope')


@pytest.mark.vcr()
def test_credentials_upload(api):
    """
    test to upload the credentials
    """
    api.credentials.upload('ExampleDataGoesHere')


@pytest.mark.vcr()
def test_credentials_types_success(api):
    """
    test to check the types of credentials
    """
    resp = api.credentials.types()
    assert isinstance(resp, list)
    for i in resp:
        check(i, 'id', str)
        check(i, 'category', str, allow_none=True)
        check(i, 'default_expand', bool, allow_none=True)
        check(i, 'types', list, allow_none=True)
        for j in i.get('types'):
            check(j, 'id', str, allow_none=True)
            check(j, 'name', str, allow_none=True)
            check(j, 'max', int, allow_none=True)
            check(j, 'configuration', list, allow_none=True)
            for k in j.get('configuration'):
                check(k, 'type', str)
                check(k, 'name', str)
                if 'hint' in k.keys():
                    check(k, 'hint', str, allow_none=True)
                check(k, 'id', str)


@pytest.mark.vcr()
def test_credentials_edit_success(api, cred):
    """
    test to check the credentials that are to be edited
    """
    creds = api.credentials.edit(cred_uuid=cred,
                                 cred_name='updated cred',
                                 description='description',
                                 permissions=[('user', 32, cred)],
                                 ad_hoc=False,
                                 settings={'Can Use': 32, 'Can Edit': 64}
                                 )
    assert isinstance(creds, bool)


@pytest.mark.vcr()
def test_credentials_list(api, scan):
    """
    test to check the list of credentials and their types
    """
    count = 0
    credentials = api.credentials.list(filter_type='or',
                                       limit=45,
                                       offset=2,
                                       wildcard='match',
                                       wildcard_fields=['name'],
                                       owner_uuid=scan['owner_uuid']
                                       )
    for creds in credentials:
        count += 1
        assert isinstance(creds, dict)
        check(creds, 'uuid', str)
        check(creds, 'name', str)
        check(creds, 'description', str)
        check(creds, 'category', dict)
        check(creds['category'], 'id', str)
        check(creds['category'], 'name', str)
        check(creds, 'type', dict)
        check(creds['type'], 'id', str)
        check(creds['type'], 'name', str)
        check(creds, 'created_date', int)
        check(creds, 'created_by', dict)
        check(creds['created_by'], 'id', int)
        check(creds['created_by'], 'display_name', str)
        check(creds, 'last_used_by', dict)
        check(creds['last_used_by'], 'id', int, allow_none=True)
        check(creds['last_used_by'], 'display_name', str, allow_none=True)
        check(creds, 'permission', int)
        check(creds, 'user_permissions', int)
    assert count == credentials.total


@pytest.mark.vcrx()
def test_credentials_permissions_constructor_typeerror(api):
    """
    test to raise the exception when the required type of variable is not passed
    """
    with pytest.raises(TypeError):
        getattr(api.credentials, '_permissions_constructor')('string')
