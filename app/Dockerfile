# ---- Build stage (wheels only) ----
    FROM python:3.11-slim AS build
    ENV PIP_NO_CACHE_DIR=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
    WORKDIR /app
    
    # Keep base OS patched; don't install extra tools
    RUN apt-get update \
     && apt-get upgrade -y --no-install-recommends \
     && rm -rf /var/lib/apt/lists/*
    
    # Upgrade packaging toolchain
    RUN python -m pip install --upgrade pip setuptools wheel
    
    # Copy & build wheels
    COPY requirements.txt .
    RUN pip wheel --no-deps -r requirements.txt -w /wheels
    
    # ---- Runtime stage (non-root) ----
    FROM python:3.11-slim
    ENV PIP_NO_CACHE_DIR=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
    WORKDIR /app
    
    # Patch OS packages at runtime layer as well
    RUN apt-get update \
     && apt-get upgrade -y --no-install-recommends \
     && rm -rf /var/lib/apt/lists/*
    
    # Create non-root user
    RUN groupadd -r app && useradd -r -g app app
    
    # Install from prebuilt wheels (no compilers)
    COPY --from=build /wheels /wheels
    RUN pip install --no-deps /wheels/*.whl
    
    # Copy app
    COPY . /app
    USER app
    
    EXPOSE 5000
    HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000', timeout=2)" || exit 1
    CMD ["python", "app.py"]
    