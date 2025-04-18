FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY scripts/wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

WORKDIR /app

COPY pyproject.toml requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "/usr/local/bin/wait-for-it.sh", "db:5432", "--"]
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
