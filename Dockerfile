FROM python:3.12.0-slim-bullseye

#workdir is where we want to store all the files
WORKDIR /docker

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

#copy source files to docker server
COPY . .

CMD ["python3", "-m", "flask", "--app", "loan", "run", "--host=0.0.0.0"]