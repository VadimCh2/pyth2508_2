git pull origin main

uv init app
cd app
uv sync
uv add pytest
- uv init app
- cd app
- uv sync
- uv add pytest
- Ctrl-Alt-l
- uv run -m pytest .
- uv run -m pytest . -v
- uv run -m pytest . -s
- uv run -m pytest . -v -s