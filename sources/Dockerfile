# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]
