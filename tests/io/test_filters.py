from tenable.errors import *
from ..checker import check, single
import pytest

@pytest.mark.vcr()
def test_agent_filters(api):
    filters = api.filters.agents_filters()
    assert isinstance(filters, dict)
    for f in filters:
        check(filters[f], 'choices', list, allow_none=True)
        check(filters[f], 'operators', list)
        check(filters[f], 'pattern', str, allow_none=True)

@pytest.mark.vcr()
def test_workbench_vuln_filters(api):
    filters = api.filters.workbench_vuln_filters()
    assert isinstance(filters, dict)
    for f in filters:
        check(filters[f], 'choices', list, allow_none=True)
        check(filters[f], 'operators', list)
        check(filters[f], 'pattern', str, allow_none=True)

@pytest.mark.vcr()
def test_workbench_asset_filters(api):
    filters = api.filters.workbench_asset_filters()
    assert isinstance(filters, dict)
    for f in filters:
        check(filters[f], 'choices', list, allow_none=True)
        check(filters[f], 'operators', list)
        check(filters[f], 'pattern', str, allow_none=True)

@pytest.mark.vcr()
def test_scan_filters(api):
    filters = api.filters.scan_filters()
    assert isinstance(filters, dict)
    for f in filters:
        check(filters[f], 'choices', list, allow_none=True)
        check(filters[f], 'operators', list)
        check(filters[f], 'pattern', str, allow_none=True)

@pytest.mark.vcr()
def test_access_group_asset_rules_filters(api):
    filters = api.filters.access_group_asset_rules_filters()
    assert isinstance(filters, dict)
    for f in filters:
        check(filters[f], 'choices', list, allow_none=True)
        check(filters[f], 'operators', list)
        check(filters[f], 'pattern', str, allow_none=True)

@pytest.mark.vcr()
def test_access_group_filters(api):
    filters = api.filters.access_group_filters()
    assert isinstance(filters, dict)
    for f in filters:
        check(filters[f], 'choices', list, allow_none=True)
        check(filters[f], 'operators', list)
        check(filters[f], 'pattern', str, allow_none=True)

@pytest.mark.vcr()
def test_use_cache_true_filters(api):
    filters = api.filters._use_cache('rules', path='access-groups/rules/filters', field_name='rules', normalize=True)
    assert isinstance(filters, dict)
    for f in filters:
        check(filters[f], 'choices', list, allow_none=True)
        check(filters[f], 'operators', list)
        check(filters[f], 'pattern', str, allow_none=True)


@pytest.mark.vcr()
def test_use_cache_false_filters(api):
    filters = api.filters._use_cache('rules', path='access-groups/rules/filters', field_name='rules', normalize=False)
    assert isinstance(filters, list)
    for i in range(len(filters)):
        check(filters[i], 'operators', list, allow_none=True)
        check(filters[i], 'name', str, allow_none=True)
        check(filters[i], 'readable_name', str, allow_none=True)
        if type(filters[i].get('placeholder')) == str:
            check(filters[i], 'placeholder', str, allow_none=True)
        elif type(filters[i].get('placeholder')) is None:
            check(filters[i], 'placeholder', None, allow_none=True)
        check(filters[i], 'control', dict, allow_none=True)

@pytest.mark.vcr()
def test_use_cache_credentials_true_filters(api):
    filters = api.filters.credentials_filters(normalize=True)
    assert isinstance(filters, dict)
    check(filters, 'name', dict, allow_none=True)
    check(filters, 'type', dict, allow_none=True)
    check(filters, 'created_date', dict, allow_none=True)
    check(filters, 'operators', list, allow_none=True)
    for f in filters:
        if type(filters[f].get('choices')) is None:
            check(filters[f], 'choices', None, allow_none=True)
        else:
            check(filters[f], 'operators', list, allow_none=True)
        if type(filters[f].get('pattern')) is None:
            check(filters[f], 'pattern', None, allow_none=True)
        else:
            check(filters[f], 'pattern', str, allow_none=True)

@pytest.mark.vcr()
def test_use_cache_credentials_false_filters(api):
    filters = api.filters.credentials_filters(normalize=False)
    assert isinstance(filters, list)
    for i in range(len(filters)):
        check(filters[i], 'name', str, allow_none=True)
        check(filters[i], 'readable_name', str, allow_none=True)
        check(filters[i], 'operators', list, allow_none=True)
        check(filters[i], 'control', dict, allow_none=True)


