# vulnerable Dockerfile (single-stage, root, old packages, no pinning)
FROM python:3.8-slim
WORKDIR /app

# install tools and system packages in one layer (no --no-install-recommends)
RUN apt-get update && apt-get install -y curl net-tools

# copy code and install deps without hashes
COPY . /app
RUN pip install -r requirements.txt

# expose and run as root
EXPOSE 5000
CMD ["python", "app.py"]

