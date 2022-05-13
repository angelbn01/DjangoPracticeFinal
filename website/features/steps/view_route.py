from behave import *
from main.models import Route

use_step_matcher("parse")


@when('I view the details for the route "{id}"')
def step_impl(context, id):
    route = Route.objects.get(id=id)
    context.browser.visit(context.get_url('/routes/%20' + route.id))


@then('I\'m viewing route details of "{id}"')
def step_impl(context, id):
    route = Route.objects.get(id=id)
    review_par_links = context.browser.find_by_css('div#content ul li p')
    for i, row in enumerate(context.table):
        assert review_par_links.text.startwith(row['Id Route']) == route.id
        assert review_par_links.text.startwith(row['Start Point']) == route.start_point
        assert review_par_links.text.startwith(row['End Point']) == route.end_point
        assert review_par_links.text.startwith(row['Start Time']) == route.start_time
        assert review_par_links.text.startwith(row['Total Distance']) == route.km
