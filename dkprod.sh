docker build -t dgbia /home/busercamp/bia
docker stop dgbia
docker rm dgbia
docker run -d -p 8005:8000 --name=dgbia \
	-v /home/busercamp/bia/dbdata:/dbdata \
	--env-file=/home/busercamp/bia/dg.properties \
	dgbia \
	./start_prod.sh