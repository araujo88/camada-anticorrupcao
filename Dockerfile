FROM python:3.9
ENV PYTHONBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8888

CMD cd src && uvicorn main:app --reload --host 0.0.0.0 --port 8888
