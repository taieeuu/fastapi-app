#!/usr/bin/env sh

redis-stack-server /usr/local/etc/redis/redis.conf &
REDIS_PID=$!

sleep 5

redis-cli -a "$REDIS_PWD" FT.CONFIG SET MINPREFIX 1

wait ${REDIS_PID}
