# FastAPI + GraphQL Starter 
A python starter project using FastAPI and GraphQL. This project leverages docker for containerization and provides the scripts to deploy to Heroku. The starter is created for and used in the <a href="/">Building Python Apps with FastAPI</a> book by <a href="https://eidanrosado.com">Eidan J. Rosado</a>.

### Running Services with Docker
To avoid setting up MongoDB and other such services locally, the team uses Docker. You'll need to install Docker to proceed pulling the image from the team's hub. Contact one of the team admins for access to the hub. To start peripheral services simply execute the following:

```bash
docker-compose up
```

To refresh the image on your local (for server devs), run the following: 

```bash
docker build -t fastapistarter -f Dockerfile.web .
```

You can run the one off image and container with the following:

```bash
docker run -d --name fastapistarter -p 8000:8000 -p 8001:8001 fastapistarter
```

## Using Heroku
If you are pushing to your personal stack on Heroku, you'll need to run the dockerization steps above to build the base image and then follow up with the Heroku containerization steps below.

```bash
heroku container:push --recursive
heroku container:release web
```

<em>Note: You must do a heroku login or use API tokens to push to the container registry</em>

### Running API Locally
You'll need the following environment variables configured or in a .env file to run the server successfully:

```bash
# FastAPI Setup
export HOST="127.0.0.1"
export PORT=8000
export WEBHOOKS_PORT=8001

# fastapistarter DB Setup
export DB_URL='mongodb://localhost:27017'
export DB_NAME='fastapistarter'
```

The main entry point is main.py, so you can start that file from command line or use whatever execution method is available from your IDE. To install the IDE to interact with GraphQL, look in the SETUP.md for GraphQL Playground installation instructions then simply open the GraphQL Playground to interact with the local server and insert the base url <em>http://127.0.0.1:8000/graph</em>. For more detailed instructions, check the wiki.

## Dev Notes
### Viewing Changes
Changes under /app may be picked up by the auto-refresh (no need to restart server). To understand how to use the playground to run queries, please reference the following: <a href="https://graphql.org/learn/queries/">GraphQL Queries Reference</a>

### Running Tests
All tests are located under the <em>tests</em> folder. To run them from terminal, execute the following:

```bash
pytest tests
```
