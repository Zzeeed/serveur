FROM python:3.12-slim

RUN pip install --no-cache-dir flask requests

# arborescence FlasK
RUN mkdir -p /app/templates /app/static

WORKDIR /app
EXPOSE 5000

CMD ["python", "app.py"]
