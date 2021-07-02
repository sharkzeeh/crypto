FROM python:3.8

WORKDIR /app/

COPY . .

RUN pip3 install aiofiles numpy websockets

CMD ["python3", "main.py"]