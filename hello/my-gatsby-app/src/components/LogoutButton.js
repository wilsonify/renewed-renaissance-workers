/*

Access the isAuthticated auth state
and the logoutmethod from the useAuth0 hook.
The logout() method redirects your users to your
Auth0 logout endpoint (https://YOUR_DOMAIN/v2/logout)
and then immediately redirects them to your application.
*/
import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

function LogoutButton() {
 const {
   isAuthenticated,
   logout,
   } = useAuth0();

   return isAuthenticated && (
     <button onClick={() => {
     logout({ returnTo: window.location.origin });
    }}>Log out</button>
 );
};

export default LogoutButton;