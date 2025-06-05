FROM python:3.10

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        python3-tk \
        tk-dev \
        libx11-6 \
        libxext6 \
        libxext-dev \
        libxrender-dev \
        libxinerama-dev \
        libxi-dev \
        libxrandr-dev \
        libxcursor-dev \
        libxtst-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV DISPLAY=192.168.1.7:0.0

COPY . .

CMD ["python", "bubble_sort.py"]
