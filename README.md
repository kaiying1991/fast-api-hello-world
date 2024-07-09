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