FROM python:3.12.0

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

CMD uvicorn main:app --host 0.0.0.0 --port $PORT

# Deploy to Render:
#     a. Push your code (including the best_model.joblib file) to a GitHub repository.
#     b. Sign up for a free account on Render (https://render.com).
#     c. In Render, create a new Web Service and connect it to your GitHub repository.
#     d. Configure the deployment:
#     Choose "Docker" as the environment.
#     Set the start command to uvicorn main:app --host 0.0.0.0 --port $PORT.
#     e. Click "Create Web Service" to deploy your application.