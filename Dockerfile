FROM python:latest
COPY practice.py .
RUN pip install psutil
CMD [ "python3" , "practice.py" ]
