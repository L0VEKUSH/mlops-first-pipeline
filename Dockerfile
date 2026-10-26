#pull the python image from Docker hub
#using light weight python image
FROM python:3.14-slim
#set the working directory in the container
WORKDIR /app
#copy the dependencies list before copying installation code
COPY requirements.txt .
#install dependencies
RUN pip install --no-cache-dir -r requirements.txt
#copy the source code into the container
COPY . .
#document the port use by FastAPI application
EXPOSE 8000
#start the API server when container is ready
#0.0.0.0 all connectionn through the container interface

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
