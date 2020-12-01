FROM python:3.8

ENV URL ""
ENV NUMBER_OF_SENTENCES 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install lxml

COPY main.py .

CMD ["sh", "-c", "python main.py $URL $NUMBER_OF_SENTENCES"]
