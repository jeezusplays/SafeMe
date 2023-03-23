# Build: docker build -t user:latest
# Run: docker run -it --rm --name user user:latest
# Pull docker image
FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ../
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./user.py .
CMD [ "python", "./user.py" ]