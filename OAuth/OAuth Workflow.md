## Problem Statement: Implement an OAuth 2.0 Server with Custom Authentication

### Overview

Your task is to implement and OAuth2.0 workflow using an example OAuth provider server and OAuth client server that integrates with a custom authentication.

In this specific problem statement, the custom authentication provider will require the user to enter an admin token (assume hardcoded token "admin") before proceeding with the OAuth flow. 

Then you have to write documentation detailing the process for clients to use the provider, and the api documentation.

Brownie points, if you can randomize the admin token and send an email to the user with the token.

### Objectives

1. **Implement an OAuth 2.0 Server from the example in the repo**:
   - Set up an OAuth 2.0 server that can handle the various authorization flows, such as the Authorization Code Grant and Implicit Grant, by cloning the repo example.
   - Integrate a custom authentication provider that requires the user to enter an admin token before proceeding with the OAuth flow.

2. **Implement a Custom Authentication Provider**:
   - Develop a custom authentication provider that generates a random admin token and sends an email to the user with the token.
   - Integrate the custom authentication provider with the OAuth server, ensuring that the user is redirected to the custom authentication endpoint during the OAuth flow.

3. **Expose APIs**:
   - Expose the necessary OAuth server endpoints (e.g., authorization, token) as APIs that can be consumed by client applications.

4. **Provide a Client Application based on the exmample in the repo**:
   - Create a client backend server that can interact with the OAuth server and leverage the custom authentication provider to authenticate users, by cloning the example in the repo/
   
**Note**: You can use postman to test the client application out, so no need for frontend for the client application.

### Approach

You can use the examples from the following GitHub repositories as a starting point for your implementation:

1. **OAuth Server Implementations**:
   - [node-oauth2-server](https://github.com/oauthjs/node-oauth2-server): A complete, compliant, and well-tested OAuth 2.0 server for Node.js.
   - [Flask-OAuthlib](https://github.com/lepture/flask-oauthlib): A Flask extension that provides OAuth 1.0a and OAuth 2.0 support.

2. **OAuth Client Implementations**:
   - [Requests-OAuthlib](https://github.com/requests/requests-oauthlib): A Python library that allows you to interact with OAuth 1.0a and OAuth 2.0 protected resources.
   - [oauth2-client](https://github.com/seegno/oauth2-client): A simple JavaScript client for the OAuth 2.0 Authorization Code Grant flow.

You can use these repositories as a starting point and modify the code to fit your specific requirements. The key steps are:

1. **OAuth Server Implementation**:
   - Set up the OAuth server using one of the provided server implementations.
   - Configure the necessary settings, such as client credentials, authorized redirect URIs, and token expiration times.
   - Integrate the custom authentication provider with the OAuth server, ensuring that the user is redirected to the custom authentication endpoint during the OAuth flow.

2. **Custom Authentication Provider Implementation**:
   - Develop a custom authentication provider that either uses a hardcoded token, or generates a random admin token and sends an email to the user with the token.
   - Implement the logic to validate the entered admin token before proceeding with the OAuth flow.

3. **API Exposure**:
   - Expose the OAuth server endpoints as RESTful APIs that can be consumed by client applications.

4. **OAuth Client Implementation**:
   - Develop a client application (backend server) that can interact with the OAuth server and leverage the custom authentication provider to authenticate users.
   - Use one of the provided client libraries to handle the OAuth flows, such as the Authorization Code Grant or Implicit Grant.
   - Ensure that the client application properly manages the access tokens, including token expiration and refresh.
   - Implement the logic to access protected resources using the obtained access tokens.

### Documentation

Provide a comprehensive README file that includes the following:

1. **API Documentation**: Document the APIs exposed by the OAuth server, including the endpoints, request/response formats, and authentication/authorization requirements.
2. **Client Application Usage**: Include instructions for using the client application, including any necessary configuration.


### Resources

Here are some additional resources that may be helpful for this project:

- **OAuth 2.0 Specification**: [https://oauth.net/2/](https://oauth.net/2/)
- **OAuth 2.0 Playground**: [https://www.oauth.com/playground/](https://www.oauth.com/playground/)
- **Okta OAuth 2.0 and OpenID Connect Overview**: [https://developer.okta.com/docs/concepts/oauth-openid/](https://developer.okta.com/docs/concepts/oauth-openid/)
- **FusionAuth OAuth 2.0 Guide**: [https://fusionauth.io/articles/oauth/modern-guide-to-oauth](https://fusionauth.io/articles/oauth/modern-guide-to-oauth)

Good luck with your submission!
