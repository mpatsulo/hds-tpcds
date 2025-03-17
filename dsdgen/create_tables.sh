for i in *.sql; do
    table="${i%.sql}"
    echo "Loading $table..."
done
