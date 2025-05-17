FROM python:3.10.12-slim-buster

WORKDIR /app

RUN apt-get update --yes --quiet \
 && apt-get install --yes --quiet --no-install-recommends \
      build-essential \
      unixodbc \
      unixodbc-dev \
      logrotate \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir uvicorn

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

COPY app/db/odbc_driver/ibm-iaccess-1.1.0.28-1.0.amd64.deb /app/
RUN dpkg -i /app/ibm-iaccess-1.1.0.28-1.0.amd64.deb || true

COPY app/db/odbc_driver/odbcinst.ini /etc/
RUN rm -f /app/ibm-iaccess-1.1.0.28-1.0.amd64.deb

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
