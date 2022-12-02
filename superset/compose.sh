rebuild(){
  docker compose build --force-rm
 
}
up(){
  docker-compose -f docker-compose-non-dev.yml up

}
$@
