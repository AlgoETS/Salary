# Deployment

## Deploy to Vercel

1. Fork this repository
2. Create a Vercel project and link it to your forked repository
3. Add the following environment variables in your Vercel project settings
4. Deploy the project

https://vercel.com/<YourName>/<ProjectName>/settings/environment-variables

## Run locally with Docker

1. Install Docker
2. Add the following environment variables
3. Open a terminal in the root folder of the repository and execute:

```bash
docker-compose up -d
```


4. Navigate to `http://localhost:5000/` in your web browser to access the service
5. To stop the service, execute:


```bash
docker-compose down
```

