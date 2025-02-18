#!/bin/sh

wait_for_host() {
    local host=$1
    local port=$2

    until timeout 1 bash -c "</dev/tcp/$host/$port"; do
        echo "Waiting for $host:$port..."
        sleep 5
    done
    echo "$host:$port is ready!"
}

if [ -n "$DB_HOST" ] && [ -n "$DB_PORT" ]; then
    wait_for_host $DB_HOST $DB_PORT
    python manage.py mig && python manage.py gen
fi

if [ -n "$KAFKA_HOST" ] && [ -n "$KAFKA_PORT" ]; then
    wait_for_host $KAFKA_HOST $KAFKA_PORT
fi

exec "$@"