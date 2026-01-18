FROM python:3.11-slim

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy the converter script to a fixed location
COPY main.py /usr/local/bin/converter.py

# Set working directory where files will be mounted
WORKDIR /data

# Set the entrypoint to run the converter
ENTRYPOINT ["python", "/usr/local/bin/converter.py"]
