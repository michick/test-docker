# Base image for python apps
FROM python:3-onbuild

# Create directory where shared volume will be mapped
RUN mkdir -p /var/impraise

# Run the app
CMD ["python", "-u", "./app.py"]

