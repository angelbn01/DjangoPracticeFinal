Feature: View Route
In order to know the information of a route,
As a user
I want to view the route details including all the information about it.

  Background: There is a registered user and a route created by him
    Given Exists a user "testing_user" with password "geiade2022"
    And Exists route registered by "testing_user"
      | id        | id_vehicle                       | start_point:    | end_point:       | km:   |
      | route001  | BICYCLE01        | Calle Sendeja   | Calle Herreria   | 23    |


  Scenario: View details for owned route
    Given I login as user "testing_user" with password "geiade2022"
    When I view the details for the route "route001"
    Then I'm viewing route details of "route001"
      | id        | id_vehicle       | start_point:    | end_point:       | km:   |
      | route001  | BICYCLE01        | Calle Sendeja   | Calle Herreria   | 23    |
    
  Scenario: Want to view the details of a route but not logged in
    Given I'm not logged in
    Then There are "0" routes
    