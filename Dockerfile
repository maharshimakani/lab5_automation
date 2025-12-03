FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /opt/hello_world

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# The Flask app in hello_world.py runs on port 4049
EXPOSE 4049

# Start the Flask app
CMD ["python", "hello_world.py"]
