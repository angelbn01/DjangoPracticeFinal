Feature: Register Route
In order to keep track of the routes I do,
As a user
I want to register a route together with its location and vehicle details.

  Background: There is a registered user
    Given Exists a user "user" with password "geiade2022"

  Scenario: Register just route id
    Given I login as user "user" with password "geiade2022"
    When I register route
      | id          |
      | route001    |
    Then I'm viewing the details page for route by "user"
      | id        |
      | route001  |
    And There is 1 route