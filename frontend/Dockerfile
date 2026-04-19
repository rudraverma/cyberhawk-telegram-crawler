# Dockerfile for Frontend

FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy application code
COPY . .

# Command to run the application
CMD ["npm", "start"]
