FROM python

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY ./requirments.txt /src/requirments.txt
RUN pip install -r /src/requirments.txt

COPY . /src

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
