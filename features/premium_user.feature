Feature: Premium user

Scenario: Check premium user response contains premium playlist
            Given this url "https://a8e38tulbj.execute-api.eu-west-2.amazonaws.com/api/playlists/premium"
            When the premium user request is sent
            Then we should receive a "200" response
            And "playlists" has field "name" and should contain "Premium"

Scenario: Check free user response DOES NOT contain premium playlist
            Given this url "https://a8e38tulbj.execute-api.eu-west-2.amazonaws.com/api/playlists/free"
            When the premium user request is sent
            Then we should receive a "200" response
            And "playlists" has field "name" and DOES NOT contain "Premium"

Scenario: Check other user response contains "Unknown user type"
            Given this url "https://a8e38tulbj.execute-api.eu-west-2.amazonaws.com/api/playlists/other"
            When the premium user request is sent
            Then we should receive a "400" response
            And response has field "messsage" and should contain "Unknown user type"