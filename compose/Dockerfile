FROM python:3.9

WORKDIR /code

COPY ./compose/requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r ./requirements.txt

COPY . ./app

CMD ["uvicorn", "app.main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]
