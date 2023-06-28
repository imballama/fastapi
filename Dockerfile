FROM python:3.11.2

RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile.lock Pipfile /usr/src/app/

RUN pipenv install --system --deploy

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
