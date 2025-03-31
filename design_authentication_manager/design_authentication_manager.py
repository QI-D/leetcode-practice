'''
1797. Design Authentication Manager
Medium
Topics
Companies
Hint
There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire timeToLive seconds after the currentTime. If the token is renewed, the expiry time will be extended to expire timeToLive seconds after the (potentially different) currentTime.

Implement the AuthenticationManager class:

AuthenticationManager(int timeToLive) constructs the AuthenticationManager and sets the timeToLive.
generate(string tokenId, int currentTime) generates a new token with the given tokenId at the given currentTime in seconds.
renew(string tokenId, int currentTime) renews the unexpired token with the given tokenId at the given currentTime in seconds. If there are no unexpired tokens with the given tokenId, the request is ignored, and nothing happens.
countUnexpiredTokens(int currentTime) returns the number of unexpired tokens at the given currentTime.
Note that if a token expires at time t, and another action happens on time t (renew or countUnexpiredTokens), the expiration takes place before the other actions.

'''

class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        count = 0
        for tokenId, expirationTime in self.tokens.items():
            if expirationTime > currentTime:
                count += 1

        return count


# Create an AuthenticationManager with 5 seconds timeToLive
auth = AuthenticationManager(5)

# Generate token "abc" at time 1
auth.generate("abc", 1)

# Count valid tokens at time 2 (should be 1)
print(auth.countUnexpiredTokens(2))  # Output: 1

# Renew token "abc" at time 3
auth.renew("abc", 3)

# Count valid tokens at time 6 (still valid because renewed)
print(auth.countUnexpiredTokens(6))  # Output: 1

# Count valid tokens at time 7 (expired now)
print(auth.countUnexpiredTokens(7))  # Output: 0

