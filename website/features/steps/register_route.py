from functools import reduce
from behave import *
import operator
from django.db.models import Q

@given(u'Exists a user "user" with password "geiade2022"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a user "user" with password "geiade2022"')


@given(u'I login as user "user" with password "geiade2022"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as user "user" with password "geiade2022"')


@when(u'I register route')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register route')


@then(u'I\'m viewing the details page for route by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for route by "user"')


@then(u'There are 1 route')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 route')