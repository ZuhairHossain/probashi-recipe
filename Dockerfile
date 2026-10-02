FROM python:3.10-slim

# Install curl and Ollama
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your app files
COPY . .

# Make the start script executable
RUN chmod +x start.sh

# Expose the port and start the app
EXPOSE 8501
CMD ["./start.sh"]