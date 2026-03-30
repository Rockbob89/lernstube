# Task 04: Connections & Hooks

## Objective
Manage external system connections in Airflow and use hooks to interact with them.

## What to Learn
- Airflow connections: store credentials centrally (host, port, login, password, schema, extras JSON). Referenced in code by `conn_id` string — credentials never hardcoded.
- Creating connections via UI, CLI, and environment variables:
  ```bash
  # CLI
  airflow connections add my_pg --conn-type postgres --host db.example.com --port 5432 --login etl --password s3cret --schema analytics
  ```
- The `AIRFLOW_CONN_*` environment variable format: URI-encoded connection, no UI/CLI needed. Format: `<type>://<login>:<password>@<host>:<port>/<schema>`.
  ```bash
  export AIRFLOW_CONN_MY_PG="postgresql://etl:s3cret@db.example.com:5432/analytics"
  ```
- Hooks: thin wrappers around client libraries that accept a `conn_id` and handle credential lookup. Operators use hooks internally.
  ```python
  from airflow.providers.postgres.hooks.postgres import PostgresHook
  hook = PostgresHook(postgres_conn_id="my_pg")
  df = hook.get_pandas_df("SELECT * FROM orders LIMIT 10")
  ```
- Providers: installable packages (`apache-airflow-providers-*`) that ship operators, hooks, and sensors for external systems (AWS, GCP, Postgres, HTTP, etc.).
- Secrets backends (Vault, AWS SSM, K8s secrets): Airflow looks up connections/variables from an external secret store instead of the metadata DB. Config in `airflow.cfg`.

## Exercises

1. **Connection via env var**: Write the `AIRFLOW_CONN_` environment variable for a Postgres connection to `db.example.com:5432/analytics` with user `etl_user` and password `s3cret`.

2. **Hook usage**: Write a DAG `hook_demo` with a task that:
   - Uses `HttpHook` with connection id `api_default` to GET `/health`
   - Prints the response status code
   - Falls back gracefully if the connection doesn't exist

3. **Custom connection test**: Write a function `test_postgres_connection(conn_id: str) -> bool` that uses `PostgresHook` to run `SELECT 1` and returns True/False.

```python
# Example:
# test_postgres_connection("my_postgres") -> True
```
