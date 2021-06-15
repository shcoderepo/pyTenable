"""
test agentexclusions
"""
import uuid
from datetime import timedelta, datetime
import pytest
from tenable.errors import UnexpectedValueError, NotFoundError
from ..checker import check


@pytest.fixture
@pytest.mark.vcr()
def agentexclusion(request, api):
    """
    fixture for agentexclusions
    """
    excl = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=datetime.utcnow(),
                                       end_time=datetime.utcnow() + \
                                                timedelta(hours=1))

    def teardown():
        try:
            api.agent_exclusions.delete(excl['id'])
        except NotFoundError:
            pass

    request.addfinalizer(teardown)
    return excl


@pytest.mark.vcr()
def test_agentexclusions_create_no_times(api):
    """
        test to raise the exception when no time is passed
    """
    with pytest.raises(AttributeError):
        api.agent_exclusions.create(str(uuid.uuid4()))


@pytest.mark.vcr()
def test_agentexclusions_create_scanner_id_typeerror(api):
    """
        test to raise the exception when false type is passed for scanner_id

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    scanner_id='nope',
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_name_typeerror(api):
    """
        test to raise the exception when false type is passed for name

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(1.02,
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_starttime_typerror(api):
    """
        test to raise the exception when false type is passed for start_time

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    start_time='fail',
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_endatetime_typerror(api):
    """
        test to raise the exception when false type is passed for end_time

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    start_time=datetime.utcnow(),
                                    end_time='nope')


@pytest.mark.vcr()
def test_agentexclusions_create_timezone_typerror(api):
    """
        test to raise the exception when false type is passed for timezone

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    timezone=1, start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_timezone_unexpectedvalue(api):
    """
        test to raise the exception when false value is passed for timezone

    """
    with pytest.raises(UnexpectedValueError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    timezone='not a real timezone',
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_description_typeerror(api):
    """
        test to raise the exception when false type is passed for description

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    description=True,
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_frequency_typeerror(api):
    """
        test to raise the exception when false type is passed for frequency

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    frequency=True,
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_frequency_unexpectedvalue(api):
    """
        test to raise the exception when false value is passed for frequency

    """
    with pytest.raises(UnexpectedValueError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    frequency='nope',
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_interval_typeerror(api):
    """
        test to raise the exception when false type is passed for interval

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    interval='nope',
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_weekdays_typerror(api):
    """
        test to raise the exception when false type is passed for weekdays

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    weekdays='nope',
                                    frequency='weekly',
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_weekdays_unexpectedvalue(api):
    """
        test to raise the exception when false value is passed for weekdays
    """
    with pytest.raises(UnexpectedValueError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    weekdays=['MO', 'TU', 'nope'],
                                    frequency='weekly',
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_dayofmonth_typeerror(api):
    """
        test to raise the exception when false type is passed for dayofmonth

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    day_of_month='nope',
                                    frequency='monthly',
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_dayofmonth_unexpectedvalue(api):
    """
    test to raise the exception when false value is passed for dayofmonth
    """
    with pytest.raises(UnexpectedValueError):
        api.agent_exclusions.create(str(uuid.uuid4()),
                                    day_of_month=0,
                                    frequency='monthly',
                                    start_time=datetime.utcnow(),
                                    end_time=datetime.utcnow() + \
                                             timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_create_onetime_exclusion(api):
    """
    test to raise the exception whlie creating one time exclusion
    """
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=datetime.utcnow(),
                                       end_time=datetime.utcnow() + \
                                                timedelta(hours=1))
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_daily_exclusion(api):
    """
    test to raise the exception while creating
    agentexclusions with daily frequency for enabling exclusion
    and checking for their types
    """
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=datetime.utcnow(),
                                       end_time=datetime.utcnow() + \
                                                timedelta(hours=1),
                                       frequency='daily')
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_weekly_exclusion(api):
    """
    test to raise the exception while creating
    agentexclusions with weekly frequency for enabling exclusion
    and checking for their types
    """
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=datetime.utcnow(),
                                       end_time=datetime.utcnow() + \
                                                timedelta(hours=1),
                                       frequency='weekly',
                                       weekdays=['mo', 'we', 'fr'])
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule']['rrules'], 'byweekday', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_monthly_exclusion(api):
    """
    test to raise the exception while creating
    agentexclusions with monthly frequency for enabling exclusion
    and checking for their types
    """
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=datetime.utcnow(),
                                       end_time=datetime.utcnow() + \
                                                timedelta(hours=1),
                                       frequency='monthly',
                                       day_of_month=15)
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule']['rrules'], 'bymonthday', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_yearly_exclusion(api):
    """
    test to raise the exception while creating
    agentexclusions with yearly frequency for enabling exclusion
    and checking for their types
    """
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=datetime.utcnow(),
                                       end_time=datetime.utcnow() + \
                                                timedelta(hours=1),
                                       frequency='yearly')
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_enabled_false_exclusion(api):
    """
    test to raise the exception while creating
    agentexclusions with false type for enabling exclusion
    and checking for their types
    """
    resp = api.agent_exclusions.create(str(uuid.uuid4()),
                                       enabled=False)
    assert isinstance(resp, dict)
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['enabled'] is False
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_create_standard_users_cant_create(stdapi):
    """
    test to raise the exception when tried to create the standard user
    """
    with pytest.raises(PermissionError):
        stdapi.agent_exclusions.create(str(uuid.uuid4()),
                                       start_time=datetime.utcnow(),
                                       end_time=datetime.utcnow() + \
                                                timedelta(hours=1))


@pytest.mark.vcr()
def test_agentexclusions_delete_notfounderror(api):
    """
    test to raise the exception when user is not found
    """
    with pytest.raises(NotFoundError):
        api.agent_exclusions.delete(123)


@pytest.mark.vcr()
def test_agentexclusions_delete_exclusion(api, agentexclusion):
    """
    test to delete the exclusion
    """
    api.agent_exclusions.delete(agentexclusion['id'])


@pytest.mark.vcr()
def test_agentexclusions_delete_standard_user_fail(stdapi, agentexclusion):
    """
    test to raise the exception when failed to delete standard user
    """
    with pytest.raises(PermissionError):
        stdapi.agent_exclusions.delete(agentexclusion['id'])


@pytest.mark.vcr()
def test_agentexclusions_edit_no_exclusion_id_typeerror(api):
    """
                test to raise the exception when the exclusion_id is not passed

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit()


@pytest.mark.vcr()
def test_agentexclusions_edit_exclusion_id_typeerror(api):
    """
                test to raise the exception when the exclusion_id type is not passed properly

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit('nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_scanner_id_typeerror(api, agentexclusion):
    """
                test to raise the exception when the scanner_id type is not passed properly

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  scanner_id='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_name_typeerror(api, agentexclusion):
    """
                test to raise the exception when the name type is not passed properly

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  name=1.02)


@pytest.mark.vcr()
def test_agentexclusions_edit_starttime_typerror(api, agentexclusion):
    """
                test to raise the exception when the starttime type is not passed properly

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  start_time='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_timezone_typerror(api, agentexclusion):
    """
                test to raise the exception when the timezone type is not passed properly

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  timezone=1)


@pytest.mark.vcr()
def test_agentexclusions_edit_timezone_unexpectedvalue(api, agentexclusion):
    """
                test to raise the exception when the timezone value is not passed properly

    """
    with pytest.raises(UnexpectedValueError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  timezone='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_description_typerror(api, agentexclusion):
    """
                test to raise the exception when the description type is not passed properly

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  description=1)


@pytest.mark.vcr()
def test_agentexclusions_edit_frequency_typerror(api, agentexclusion):
    """
            test to raise the exception when the frequency type is not passed properly

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  frequency=1)


@pytest.mark.vcr()
def test_agentexclusions_edit_frequency_unexpectedvalue(api, agentexclusion):
    """
        test to raise the exception when the frequency value is not passed properly

    """
    with pytest.raises(UnexpectedValueError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  frequency='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_interval_typerror(api, agentexclusion):
    """
    test to raise the exception when the interval is not passed of the desired type
    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  interval='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_weekdays_typerror(api, agentexclusion):
    """
        test to raise the exception when the type is
        not passed properly during edit of weekly agentexclusions

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  frequency='weekly',
                                  weekdays='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_weekdays_unexpectedvalue(api, agentexclusion):
    """
    test to raise the exception when the value
     is not passed properly during edit of weekly agentexclusions
    """
    with pytest.raises(UnexpectedValueError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  frequency='weekly',
                                  weekdays=['MO', 'WE', 'nope'])


@pytest.mark.vcr()
def test_agentexclusions_edit_dayofmonth_typerror(api, agentexclusion):
    """
    test to check value of agentexclusions for monthly
    frequency when correct type of variable is not passed

    """
    with pytest.raises(TypeError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  frequency='monthly',
                                  day_of_month='nope')


@pytest.mark.vcr()
def test_agentexclusions_edit_dayofmonth_unexpectedvalue(api, agentexclusion):
    """
    test to check value of agentexclusions for monthly frequency when correct value is not passed

    """
    with pytest.raises(UnexpectedValueError):
        api.agent_exclusions.edit(agentexclusion['id'],
                                  frequency='monthly',
                                  day_of_month=0)


@pytest.mark.vcr()
def test_agentexclusions_edit_standard_user_permission_error(stdapi, agentexclusion):
    """
    test to raise permission exception
    """
    with pytest.raises(PermissionError):
        stdapi.agent_exclusions.edit(agentexclusion['id'],
                                     name=str(uuid.uuid4()))


@pytest.mark.vcr()
def test_agentexclusions_edit_success(api, agentexclusion):
    """
    test to edit the agentexclusions
    """
    api.agent_exclusions.edit(agentexclusion['id'],
                              name=str(uuid.uuid4()))


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_daily(api, agentexclusion):
    """
    test to edit agentexclusions for daily frequency

    """
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     name=str(uuid.uuid4()),
                                     frequency='daily',
                                     interval=2)

    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'DAILY'
    assert resp['schedule']['rrules']['interval'] == '2'


@pytest.mark.vcr()
def test_agentexclusions_edit_enable_exclusion(api):
    """
    test to edit agentexclusions and to enable them

    """
    agentexclusion = api.agent_exclusions.create(str(uuid.uuid4()),
                                                 enabled=False)
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     enabled=True,
                                     start_time=datetime.utcnow(),
                                     end_time=datetime.utcnow() + timedelta(hours=1))
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['enabled'] is True
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_edit_onetime_to_weekly_valdefault(api, agentexclusion):
    """
    test to edit agentexclusions for weekly frequency

    """
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     frequency='Weekly')
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['rrules']['byweekday'] == 'SU,MO,TU,WE,TH,FR,SA'


@pytest.mark.vcr()
def test_agentexclusions_edit_onetime_to_weekly_valassigned(api, agentexclusion):
    """
    test to edit agentexclusions for weekly frequency

    """
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     frequency='Weekly',
                                     weekdays=['MO', 'TU'])
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['rrules']['byweekday'] == 'MO,TU'


@pytest.mark.vcr()
def test_agentexclusions_edit_onetime_to_weekly_valavailable(api):
    """
    test to edit agentexclusions for weekly frequency

    """
    agentexclusion = api.agent_exclusions.create(str(uuid.uuid4()),
                                                 frequency='Weekly',
                                                 weekdays=['TU', 'WE'],
                                                 start_time=datetime.utcnow(),
                                                 end_time=datetime.utcnow() + timedelta(hours=1))
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     name=str(uuid.uuid4()))
    check(resp, 'id', int)
    check(resp, 'name', str)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'last_modification_date', int)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    assert resp['schedule']['rrules']['byweekday'] == 'TU,WE'


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_monthly_valddefault(api, agentexclusion):
    """
    test to edit agentexclusions for monthly frequency with default value
    """
    resp = api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()),
                                     frequency='monthly',
                                     interval=2)
    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'MONTHLY'
    assert resp['schedule']['rrules']['interval'] == '2'


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_monthly_valassigned(api, agentexclusion):
    """
    test to edit agentexclusions for monthly frequency with value assigned

    """
    resp = api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()),
                                     frequency='monthly',
                                     interval=2,
                                     day_of_month=8)
    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'MONTHLY'
    assert resp['schedule']['rrules']['interval'] == '2'
    assert resp['schedule']['rrules']['bymonthday'] == '8'


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_monthly_valavailable(api):
    """
    test to edit agentexclusions for monthly frequency

    """
    agentexclusion = api.agent_exclusions.create(str(uuid.uuid4()),
                                                 start_time=datetime.utcnow(),
                                                 end_time=datetime.utcnow() + \
                                                          timedelta(hours=1),
                                                 frequency='monthly',
                                                 day_of_month=8)
    resp = api.agent_exclusions.edit(agentexclusion['id'],
                                     frequency='monthly',
                                     interval=2)
    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'MONTHLY'
    assert resp['schedule']['rrules']['interval'] == '2'
    assert resp['schedule']['rrules']['bymonthday'] == '8'
    api.agent_exclusions.delete(resp['id'])


@pytest.mark.vcr()
def test_agentexclusions_edit_freq_onetime_to_yearly(api, agentexclusion):
    """
test to edit agentexclusions for yearly frequency
    """
    resp = api.agent_exclusions.edit(agentexclusion['id'], name=str(uuid.uuid4()),
                                     frequency='yearly',
                                     interval=2)
    assert isinstance(resp, dict)
    check(resp, 'description', str, allow_none=True)
    check(resp, 'id', int)
    check(resp, 'last_modification_date', int)
    check(resp, 'name', str)
    check(resp, 'schedule', dict)
    check(resp['schedule'], 'enabled', bool)
    check(resp['schedule'], 'endtime', 'datetime')
    check(resp['schedule'], 'rrules', dict)
    check(resp['schedule']['rrules'], 'freq', str)
    check(resp['schedule']['rrules'], 'interval', str)
    check(resp['schedule'], 'starttime', 'datetime')
    check(resp['schedule'], 'timezone', str)
    assert resp['schedule']['rrules']['freq'] == 'YEARLY'
    assert resp['schedule']['rrules']['interval'] == '2'


@pytest.mark.vcr()
def test_agentexclusions_list_blackouts(api):
    """
    test to list the blackouts
    """
    items = api.agent_exclusions.list()
    assert isinstance(items, list)


@pytest.mark.vcr()
def test_agentexclusions_edit_all_success(api, agentexclusion):
    """
    test to edit all agentexclusions
    """
    freq = ['WEEKLY', 'MONTHLY', 'DAILY']

    for frequency in freq:
        resp = api.agent_exclusions.edit(exclusion_id=agentexclusion['id'],
                                         name='some_name',
                                         description='exclusion_description',
                                         start_time=datetime.now(),
                                         end_time=datetime.utcnow() + \
                                                  timedelta(hours=5),
                                         timezone='UTC',
                                         interval=20,
                                         enabled=True,
                                         frequency=frequency)

        assert isinstance(resp, dict)

        for _ in resp:
            check(resp, 'description', str, allow_none=True)
            check(resp, 'name', str, allow_none=True)
            check(resp, 'uuid', str, allow_none=True)
            check(resp, 'creation_date', int, allow_none=True)
            check(resp, 'last_modification_date', int, allow_none=True)
            check(resp, 'id', int, allow_none=True)
            check(resp, 'core_updates_blocked', bool, allow_none=True)
            check(resp, 'schedule', dict, allow_none=True)


@pytest.mark.vcr()
def test_agentexclusions_list_success(api):
    """
    test to list the agentexclusions and checking their types
    """
    resp = api.agent_exclusions.list(scanner_id=2)
    assert isinstance(resp, list)
    for i in enumerate(resp):
        check(i[1], 'description', str, allow_none=True)
        check(i[1], 'name', str, allow_none=True)
        check(i[1], 'uuid', str, allow_none=True)
        check(i[1], 'last_modification_date', int, allow_none=True)
        check(i[1], 'id', int, allow_none=True)
        check(i[1], 'core_updates_blocked', bool, allow_none=True)
        check(i[1], 'schedule', dict, allow_none=True)
