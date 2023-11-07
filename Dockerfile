FROM python:3.6

# The EXPOSE instruction indicates the ports on which a container
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
WORKDIR /app

COPY . /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]