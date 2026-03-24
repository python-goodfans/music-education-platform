# Docker Deployment Guide for Music Education Platform

This quick reference guide provides instructions for deploying the Music Education Platform using Docker.

## Prerequisites
- Install Docker on your local machine.
- Basic knowledge of Python and Docker concepts.

## Getting Started
1. **Clone the repository**
   ```bash
   git clone https://github.com/python-goodfans/music-education-platform.git
   cd music-education-platform
   ```

2. **Build the Docker image**
   ```bash
   docker build -t music-education-platform .
   ```

3. **Run the Docker container**
   ```bash
   docker run -d -p 8000:8000 music-education-platform
   ```
   This command runs the container in detached mode and maps port 8000 on your host to port 8000 in the container.

4. **Access the application**
   Open your web browser and go to `http://localhost:8000` to access the Music Education Platform.

## Additional Commands
- **Stop the running container**:
   ```bash
   docker ps  # Note the container ID
   docker stop <container_id>
   ```
- **Remove the container**:
   ```bash
   docker rm <container_id>
   ```
- **View logs**:
   ```bash
   docker logs <container_id>
   ```

## Troubleshooting
- Ensure that Docker is running and you have sufficient permissions to run Docker commands.
- Check the application logs for error messages if the container fails to start.

## Conclusion
Following these steps, you can quickly set up and run the Music Education Platform using Docker. For additional configuration or deployment options, refer to the project's documentation.