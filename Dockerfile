FROM python

WORKDIR /costcounter

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./costs ./costs

CMD ["python", "costs/__main__.py"]