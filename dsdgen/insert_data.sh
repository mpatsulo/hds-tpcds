
for i in *.dat; do
    table="${i%.dat}"
    echo "Loading $table..."
    psql  << EOF
    TRUNCATE TABLE $table;
    \COPY $table FROM 'hds-tpcds/$i' WITH (FORMAT csv, DELIMITER '|');
EOF
done
