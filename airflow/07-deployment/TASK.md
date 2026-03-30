# Task 07: Deployment

## Objective
Deploy Airflow locally with Docker Compose and understand executor choices for production.

## What to Learn
- Official Airflow Docker Compose: the official `docker-compose.yaml` from `apache/airflow` runs scheduler, webserver, triggerer, and flower. Key env vars: `AIRFLOW__CORE__EXECUTOR`, `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`, `AIRFLOW__CELERY__BROKER_URL`.
- LocalExecutor vs CeleryExecutor vs KubernetesExecutor: LocalExecutor runs tasks as subprocesses on the scheduler host (simple, single-node); CeleryExecutor distributes tasks to worker pods via Redis/RabbitMQ; KubernetesExecutor spawns one pod per task instance (strong isolation, no persistent workers).
- KubernetesExecutor: pod templates, resource requests, sidecar patterns. The `pod_template_file` config points to a YAML spec. Airflow patches it with the task's image and command. You know K8s — focus on the `KubernetesExecutor`-specific keys in `airflow.cfg`: `pod_template_file`, `namespace`, `worker_container_repository`.
- DAG distribution: git-sync sidecar clones your DAG repo into a volume shared with the scheduler/worker containers. Alternatively, bake DAGs into a custom image (immutable, slower iteration).
- Health checks, monitoring, and `airflow db check`: `airflow db check` verifies DB connectivity. Expose `/health` endpoint for liveness probes. Key metrics: `scheduler_heartbeat`, `dag_processing_total_parse_time`.
- Scaling considerations: run multiple schedulers for HA (Airflow 2.x supports it natively). Tune `min_file_process_interval` to reduce parse load. Use pools to cap concurrency for resource-intensive tasks.

## Exercises

1. **Docker Compose**: Write a minimal `docker-compose.yml` that runs Airflow with:
   - PostgreSQL as metadata DB
   - LocalExecutor (no Celery/Redis needed)
   - A volume mount for DAGs from `./dags`
   - Webserver on port 8080
   - Use the official `apache/airflow:2.9-python3.11` image

2. **Executor comparison**: Create a table (in a comment or docstring) comparing LocalExecutor, CeleryExecutor, and KubernetesExecutor across: concurrency model, infrastructure needs, isolation level, scaling, and when to use each.

3. **KubernetesExecutor pod template**: Write a `pod_template.yaml` for KubernetesExecutor that:
   - Sets resource requests (256Mi memory, 250m CPU)
   - Sets resource limits (512Mi memory, 500m CPU)
   - Mounts DAGs from a git-sync sidecar init container
   - Uses `airflow-worker` service account

Write all files (`docker-compose.yml`, `pod_template.yaml`, executor comparison) in this folder.
