# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Выполнить запуск сервера разработки при старте контейнера.
<<<<<<< HEAD
CMD ["python3", "manage.py", "runserver", "0:8000"]
=======
CMD ["python3", "manage.py", "runserver", "0:8000"]
>>>>>>> 7a42cfe (ready for deploy1)
