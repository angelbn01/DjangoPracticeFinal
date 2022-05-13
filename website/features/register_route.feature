Feature: Register Route
In order to keep track of the routes I do,
As a user
I want to register a route together with its location and vehicle details.

  Background: There is a registered user
    Given Exists a user "testing_user" with password "geiade2022"


  Scenario: Want to register route but not logged in
    Given I'm not logged in
    Then There are "0" routes


  Scenario: Register a new route
    Given I login as user "testing_user" with password "geiade2022"
    When I register a new route
      | id        | id_vehicle       | start_point:    | end_point:       | km:   |
      | route001  | BICYCLE01        | Calle Sendeja   | Calle Herreria   | 23    |
    Then I'm viewing the details page for route by "testing_user"
      | id        |
      | route001  |
    And There are "1" routes
