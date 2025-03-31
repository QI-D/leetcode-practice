/*
 * 1797. Design Authentication Manager
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
 * 
 */

package design_authentication_manager;

import java.util.HashMap;
import java.util.Map;

public class DesignAuthenticationManager {
    private int timeToLive;
    private Map<String, Integer> tokens;

    public DesignAuthenticationManager(int timeToLive) {
        this.timeToLive = timeToLive;
        this.tokens = new HashMap<>();
    }

    public void generate(String tokenId, int currentTime) {
        tokens.put(tokenId, currentTime + timeToLive);
    }

    public void renew(String tokenId, int currentTime) {
        if (tokens.containsKey(tokenId) && tokens.get(tokenId) > currentTime) {
            tokens.put(tokenId, currentTime + timeToLive);
        }
    }

    public int countUnexpiredTokens(int currentTime) {
        int count = 0;

        for (Map.Entry<String, Integer> entry : tokens.entrySet()) {
            if (entry.getValue() > currentTime) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        DesignAuthenticationManager auth = new DesignAuthenticationManager(5);

        auth.generate("abc", 1);
        System.out.println(auth.countUnexpiredTokens(2)); // Output: 1

        auth.renew("abc", 3);
        System.out.println(auth.countUnexpiredTokens(6)); // Output: 1

        System.out.println(auth.countUnexpiredTokens(7)); // Output: 0
    }
}
