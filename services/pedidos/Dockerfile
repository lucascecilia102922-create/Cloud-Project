FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install flask requests

RUN useradd appuser

USER appuser

CMD ["python","app.py"]