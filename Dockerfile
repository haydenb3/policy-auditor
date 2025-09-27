# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY backend/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application code to the working directory
COPY backend/ .

# Copy the policy documents so they are available at runtime
COPY ["Public Policies", "/app/Public Policies/"]

# Expose the port the app runs on
EXPOSE 8000

# Run the application
# We use 0.0.0.0 to ensure it's accessible from outside the container.
# The port is set by Railway via the $PORT environment variable.
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
