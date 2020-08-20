FROM python:3.8.5

WORKDIR /var/apps/helloflask

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "./app.py"]
