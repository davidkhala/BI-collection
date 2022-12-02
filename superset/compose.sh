# clone or update
curl https://raw.githubusercontent.com/davidkhala/davidkhala/main/git.sh | bash -s update-clone https://github.com/apache/superset.git

cd superset
rebuild(){
  docker compose build --force-rm
 
}
up(){
  docker compose -f docker-compose-non-dev.yml up

}
$@
