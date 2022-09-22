## Build
docker build -t minimal_server .
## Run 
docker run -d --restart unless-stopped -p 8080:80/tcp minimal_server