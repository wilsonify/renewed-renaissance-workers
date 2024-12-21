import React from 'react';
import { Auth0Provider } from '@auth0/auth0-react';
import { navigate } from 'gatsby';

// custom typefaces
import "@fontsource-variable/montserrat"
import "@fontsource/merriweather"
// normalize CSS across browsers
import "./src/normalize.css"
// custom CSS styles
import "./src/style.css"

// Highlighting for code blocks
import "prismjs/themes/prism.css"



const onRedirectCallback = (appState) => {
  // Use Gatsby's navigate method to replace the url
  navigate(appState?.returnTo || '/', { replace: true });
};

export const wrapRootElement = ({ element }) => {
/* wrapRootElement
hook from the Gatsby Browser API sets up the use of Provider components.
Wrap the root element in the <Auth0Provider>
Pass in the AUTH0_DOMAIN and  AUTH0_CLIENTID
into the domain and clientId props
Pass in window.location.origin
to the redirectUri prop,
which is the URL Auth0 will redirect your browser to with the authentication result.
onRedirectCallback
removes the code and state parameters from the URL when you are redirected from the authorize page.
*/
 return (
  <Auth0Provider
   domain={process.env.AUTH0_DOMAIN}
   clientId={process.env.AUTH0_CLIENTID}
   redirectUri={window.location.origin}
   onRedirectCallback={onRedirectCallback}
   >
    {element}
 </Auth0Provider>
 );
};