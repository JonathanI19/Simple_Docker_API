# Use the official MongoDB image as the base image
FROM mongo:latest

# Set environment variable to define the name of the initial database
ENV MONGO_INITDB_DATABASE=movie_db
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=pass

COPY names.json /tmp/names.json
COPY titles.json /tmp/titles.json
COPY roles.json /tmp/roles.json

COPY importscript.sh /docker-entrypoint-initdb.d/

ADD init-mongo.js /docker-entrypoint-initdb.d/

# Expose port (optional)
EXPOSE 27017

# Default command to run when starting the container
CMD ["mongod"]