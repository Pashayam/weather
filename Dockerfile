FROM python:3.8

RUN mkdir -p /usr/scr/app/

WORKDIR /usr/scr/app/

COPY . /usr/scr/app/

RUN pip install --no-cache-dir -r requirements

EXPOSE 5000

CMD ["python","app.py"]
