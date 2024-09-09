FROM python:3.12.0

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip list
RUN which uvicorn
RUN python -c "import uvicorn; print(uvicorn.__file__)"

COPY . /code

COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]
