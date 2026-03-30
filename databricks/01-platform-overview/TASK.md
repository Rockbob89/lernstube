# Task 1: Platform Overview

## Objective
Understand the Databricks platform architecture, workspace components, and how it compares to raw Spark on Kubernetes.

## What to Learn
- Databricks workspace: notebooks, repos, clusters, jobs, SQL warehouses
- Cluster types: all-purpose vs job clusters, single-node vs multi-node
  - All-purpose: long-lived, shared, used for interactive development; billed while running.
  - Job cluster: ephemeral, spun up per job run, terminated on completion — cheaper for production workloads.
- Autoscaling and spot instances — cost optimization
  - Autoscaling adds/removes workers between a min and max; spot instances (AWS) or preemptible VMs (GCP) cut compute cost ~60-80% at the risk of eviction.
- Unity Catalog: unified governance for data and AI assets (catalogs, schemas, tables, volumes)
  - Three-level namespace: `catalog.schema.table` e.g. `prod.sales.orders`. Permissions, lineage, and audit logs are managed at catalog level across all workspaces.
- Databricks vs raw Spark on K8s: what Databricks adds (managed infra, Delta Lake, collaborative notebooks, governance)
- Pricing model: DBU-based pricing, cluster costs
  - DBU (Databricks Unit) = normalized compute unit. Cost = DBUs/hour × instance cost. All-purpose clusters cost more DBUs per hour than job clusters.
- When Databricks is overkill (small data, simple ETL, cost-constrained teams)

## Exercises

1. **Component mapping**: Map each Databricks component to its open-source or cloud-native equivalent:
   - Databricks workspace notebooks -> ?
   - Unity Catalog -> ?
   - Job clusters -> ?
   - DBFS -> ?
   - Delta Live Tables -> ?
   - SQL Warehouse -> ?

2. **Cluster configuration**: You need to run a nightly ETL job processing 500GB of Parquet files. Design the cluster configuration:
   - Cluster type (all-purpose vs job)
   - Node type and count
   - Autoscaling settings
   - Spot vs on-demand ratio
   - Justify each choice

3. **Cost analysis**: Your team currently runs Spark on EKS with 10 `r5.2xlarge` instances. Estimate the monthly Databricks cost for equivalent workloads. Identify what Databricks features would justify the premium.
