# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the bot
COPY . .

# Expose the port for Render (Flask)
EXPOSE 10000

# Start command
CMD ["python3", "bot_runner.py"]
