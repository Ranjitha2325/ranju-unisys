# building docker image
docker build -t ranjuweb:testv1  . 
# checking image
docker images | grep -i ranjuweb