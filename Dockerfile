FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true

RUN poetry install --no-root --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "gunicorn", "techsolutions_blog_api.wsgi:application", "--bind", "0.0.0.0:8000"]