# Setup
- Create environment
```bash
python3 -m venv .venv
```
- Activate environment
```bash
source .venv/bin/activate
```
- Install dependencies
```bash
pip install -r requirements.txt
```
- Run application
```bash
python3 main.py
```

# Accessing API
## GET request
```bash
curl http://localhost:8000
```

## POST request
```bash
curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d "{\"4\": \"pear\"}"
```

# Build docker image
- Build image
```bash
# `--no-cache` - Do not use previous build cache
# `--process=plain` - Will show container output (for debugging)
docker build . -t <app_name>:<tag> --no-cache --process=plain

# `-t` - Refer to tag, used for versioning, if not provided after :, docker will default to "latest"
docker build . -t fast-api-hello-world:v0.0.1 --no-cache --process=plain
```

# Running docker image
```bash
# Create a container with the given image
# `-d` - Run in detached mode (in the background)
# If :v0.0.1 is not provided, docker will default to "latest"
docker run -d -p 8000:8000 fast-api-hello-world:v0.0.1
```

# Common commands
```bash
# Inspect images
docker images

# Run docker container
# `-d` - Run in detached mode (in the background)
# If :v0.0.1 is not provided, docker will default to "latest"
docker run -d -p 8000:8000 fast-api-hello-world:v0.0.1

# Check running containers
# `-a` - Show all containers, including stopped
docker ps -a

# View container logs
docker logs <container_id>

# Stop container
docker stop <container_id>

# Removing a container
# `-f` - Force remove running container
docker rm -f <container_id_or_name>

# Remove all stopped containers
docker container prune

# Removing image
# tag is optional, can remove with only <image_id_or_name>
# `-f` - Force removing an image that is tagged to a container
docker rmi -f <image_id_or_name>:<tag>

# Remove all unused images
docker image prune -a

# Clean docker build cache
docker builder prune

# Remove all stopped containers, not used networks, all images that has got no container and build cache
docker system prune -a
```

# Moving from development to production
```bash
# Exporting docker image
docker save fast-api-hello-world:v0.0.1 > fast-api-hello-world.tar

# Loading from saved image
docker load < fast-api-hello-world.tar
```
