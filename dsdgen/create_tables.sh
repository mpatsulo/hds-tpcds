for i in ../schema/*.sql; do
    table="${i%.sql}"
    echo "Loading $table..."
done
