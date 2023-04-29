#!/bin/bash

export PGPASSWORD=postgres
psql -U postgres -c "CREATE DATABASE test_app"
psql -U postgres -c "CREATE DATABASE app"
PGPASSWORD=postgres pg_restore -U postgres -d app /app/dump.sql
