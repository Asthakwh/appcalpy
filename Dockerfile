# Use official Python image
FROM public.ecr.aws/docker/library/python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . /app

# Expose Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
