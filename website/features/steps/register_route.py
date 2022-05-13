from functools import reduce


from behave import *
import operator
from django.db.models import Q
from django.contrib.auth.models import User
from main.models import Route

use_step_matcher("parse")


@given('Exists route registered by "{username}"')
def step_impl(context, username):
    user = User.objects.get(username=username)
    for row in context.table:
        route = Route(user=user)
        for heading in row.headings:
            setattr(route, heading, row[heading])
        route.save()


@when('I register a new route')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('http://127.0.0.1:8000/create/'))
        if context.browser.url == context.get_url('http://127.0.0.1:8000/create/'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for route by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    q_list.append(Q(('testing_user', User.objects.get(username=username))))
    route = Route.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(route)


@then('There are "{count:n}" routes')
def step_impl(context, count):
    assert count == Route.objects.count()


@when('I edit the route with id "{id}"')
def step_impl(context, id):
    route = Route.objects.get(id=id)
    context.browser.visit('/route/' + route.id + '/edit')
    form = context.browser.find_by_tag('form').fifth
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()
