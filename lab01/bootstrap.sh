BASE_FOLDER=${PWD}

echo "Building all images for lab01..."

echo "🧪 BUILDING AUTH MICROSERVICES..."
cd ${BASE_FOLDER}/auth/; make docker-build;
if [ $? -eq 1 ];
then
    echo "Something went wrong while building auth microservice"
    exit 1
fi
echo "Done."

echo "🧪 BUILDING TODO MICROSERVICES..."
cd ${BASE_FOLDER}/todo/; make docker-build;
if [ $? -eq 1 ];
then
    echo "Something went wrong while building todo microservice"
    exit 1
fi
echo "Done."

echo "🧪 BUILDING FRONTEND MICROSERVICES..."
cd ${BASE_FOLDER}/frontend/; make docker-build;
if [ $? -eq 1 ];
then
    echo "Something went wrong while building frontend microservice"
    exit 1
fi
echo "Done."
echo "------------------- "
echo "🚀🚀 All images are built. Nice! 🚀🚀"
echo "Type 'make start' or 'docker-compose up -d' to start the services."