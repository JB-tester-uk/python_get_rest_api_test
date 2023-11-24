Feature: Premium user

Background: Set base URL
            Given a base URL "https://a8e38tulbj.execute-api.eu-west-2.amazonaws.com/api/playlists/"

Scenario: Check premium user response should contain premium in the playlist
            Given this url user option "premium"
            When the user GET request is sent
            Then we should receive a "200" response
            And "playlists" has field "name" and should contain "Premium"

Scenario: Check free user response SHOULD NOT contain premium in the playlist
            Given this url user option "free"
            When the user GET request is sent
            Then we should receive a "200" response
            And "playlists" has field "name" and SHOULD NOT contain "Premium"

Scenario: Check other user response should contain "Unknown user type"
            Given this url user option "other"
            When the user GET request is sent
            Then we should receive a "400" response
            And response has field "messsage" and should contain "Unknown user type"