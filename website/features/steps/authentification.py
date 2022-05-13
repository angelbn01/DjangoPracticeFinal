from behave import *
from django.contrib.auth.models import User

use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    User.objects.create_user(username=username, password=password)


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/accounts/login/?next=/create/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('testing_user', username)
    context.browser.fill('geiade2022', password)
    form.find_by_value('login').first.click()
    assert context.browser.is_text_present('User: ' + username)


@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('/home/'))
    assert context.browser.is_text_present('Log In')


