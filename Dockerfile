# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency list & install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app.py .

# Expose container port for ALB
EXPOSE 80

# Start the Flask app using Gunicorn (production-ready)
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
