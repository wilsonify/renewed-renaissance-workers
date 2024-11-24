renewed-renaissance-workers
============

This is the source code for an e-commerce bundle platform built on Cloudflare Workers,

providing Woot-style deals on content.

## important directories:

- `api`: [Cloudflare Workers](https://workers.dev) 
 
    application that serves static HTML, CSS, and JS, as well as acts as a serverless API and webhook handler for Stripe.

- `app`: [Nuxt.js](https://nuxtjs.org) 
 
    static application that renders data from Sanity.io as HTML/JS components.

- `lambda`: 
   
    A Lambda function managed by Serverless framework that writes information to a Google Sheet via an API request.

- `sanity`:

    The dataset and configuration for the Sanity.io headless CMS deploy that powers this application.


## Configuration

A number of example configuration files have been set up across the codebase. These can be copied (and `.example` removed) to prepare the project for deployment:

- `cp config.example.js config.js`
- `cp api/wrangler.example.toml api/wrangler.toml`
- `cp sanity/sanity.example.json api/sanity.json`
- `cp api/sanity.json app/sanity.json`

note, `sanity/sanity.json` should be duplicated to `app/sanity.json` so the Nuxt.js frontend can properly talk to your Sanity CMS deployment:


### config.js

As much as possible, the configuration has been contained to `config.js` - this allows the same information to be shared between the frontend, API, and other ancilliary tooling. Make sure to look inside that file for detailed comments on what each key/value pair does, and how to correctly configure it.

## Secrets

A number of [wrangler secrets](https://developers.cloudflare.com/workers/cli-wrangler/commands#secret) should be set for your application to work properly. Note that the `wrangler.toml` provided with this project contains two environments, a default (development) environment, and a `production` environment. These secrets should be set on both environments, which can be configured using the environment (`-e`) flag: e.g. `wrangler secret put` for development, and `wrangler secret put -e production` for production:

_This section is in progress - the list of secrets can be found below, and explanations on how/where to get these values is coming soon._

| Name                          | What is it |
| ----------------------------- | ---------- |
| AUTH_TOKEN                    |            |
| AWS_ACCESS_KEY                |            |
| AWS_SECRET_KEY                |            |
| LAMBDA_FN                     |            |
| MAILGUN_API_KEY               |
| MAILGUN_DOMAIN                |            |
| SALT                          |            |
| SANITY_DATASET                |            |
| SANITY_PROJECT_ID             |            |
| STRIPE_SECRET_KEY             |            |
| STRIPE_WEBHOOK_SIGNING_SECRET |            |

## Example

You can see an example deployment at [ecommerce-example.signalnerve.workers.dev](https://ecommerce-example.signalnerve.workers.dev/).
