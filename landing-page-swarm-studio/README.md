# Landing page swarm studio

Python **3.10+** required. From this directory:

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env — set OPENAI_API_KEY
python -m app.main --message "Draft a hero for a meal-kit launch"
```

Interactive mode: `python -m app.main`

## Author 👤

**Shivay Bajaj**

- GitHub: https://github.com/IDropCoins
