FROM python:3.10

WORKDIR /app

COPY . .

RUN python -m pip install poetry
RUN python -m poetry config virtualenvs.in-project true
RUN python -m poetry install

CMD ["python", "-m", "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]