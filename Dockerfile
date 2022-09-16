# Set Base Image
FROM python:3.9

# Set Working Dir
WORKDIR /code

# Copy Requirements txt
COPY ./requirements.txt /code/requirements.txt

# Install Dependencies
RUN pip install -r /code/requirements.txt

# Copy Code Files
COPY ./run.py /code/run.py

# CMD
CMD ["python", "run.py"]