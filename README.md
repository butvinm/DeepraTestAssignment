# A test assignment for employment in Deepra company.

## Task

> We need to create a simple web application, that should response with "Hello {name}! {message}!" on GET request to the "/?name={name}&message={message}"

## Preview

You can find project preview [there](https://deepratestass-1-c6825783.deta.app/?name=Rekruto&message=Давай%20дружить!)

## Run

### If you have [Poetry](https://python-poetry.org):

Just run:

```bash
make dev
```

### Otherwise:

Run following commands:

```bash
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app
```
