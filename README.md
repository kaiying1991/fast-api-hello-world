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
# `-t` - Refer to tag, used for versioning, if not provided after :, docker will default to "latest"
docker build -t fast-api-hello-world:v0.0.1 .
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
docker ps

# View container logs
docker logs <container_id>

# Stop container
docker stop <container_id>
```
