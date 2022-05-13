Feature: Edit Route
In order to keep updated my previous routes I have done,
As a user
I want to edit a route register I created.

  Background: There is a registered user and a route created by him
    Given Exists a user "testing_user" with password "geiade2022"
    And Exists route registered by "testing_user"
      | id        | id_vehicle       | start_point:    | end_point:       | km:   |
      | route001  | BICYCLE01        | Calle Sendeja   | Calle Herreria   | 23    |


  Scenario: Edit owned route registry Km
    Given I login as user "testing_user" with password "geiade2022"
    When I edit the route with id "route001"
      | km:   |
      | 25    |
    Then I'm viewing the details page for route by "testing_user"
      | id        | id_vehicle       | start_point:    | end_point:       | km:   |
      | route001  | BICYCLE01        | Calle Sendeja   | Calle Herreria   | 25    |
    And There are "1" routes

  Scenario: Want to edit but not logged in
    Given I'm not logged in
    Then There are "0" routes
