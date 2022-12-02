# clone or update
git clone https://github.com/apache/superset.git

rebuild(){
  docker compose build --force-rm
 
}
up(){
  docker compose -f docker-compose-non-dev.yml up

}
$@
