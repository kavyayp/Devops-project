# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code
COPY calculator.py .

# Run the app
CMD ["python", "calculator.py"]
