
touch ./docker/requirements-local.txt

up(){
  echo "mysqlclient" >> ./docker/requirements-local.txt

}

$@
