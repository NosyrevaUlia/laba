FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]


# FROM python:3.12
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD ["flask", "run", "--host=0.0.0.0"]
