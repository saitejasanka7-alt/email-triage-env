FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (important for Hugging Face)
EXPOSE 7860

# Run app
CMD ["python", "app.py"]
