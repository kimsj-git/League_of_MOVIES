FROM python:3.9.7

WORKDIR /lom-back

COPY requirements.txt /lom-back

RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /lom-back

EXPOSE 8100

CMD ["gunicorn", "pjt.asgi:application","-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8100"]