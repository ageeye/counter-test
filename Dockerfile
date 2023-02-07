FROM python:3
EXPOSE 5000
WORKDIR /src
RUN pip install --no-cache-dir Flask
COPY server.py /src/
USER www-data
CMD [ "python", "/src/server.py" ]
