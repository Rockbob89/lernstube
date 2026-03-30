# Task 6: Documentation & Lineage

## Objective
Document your dbt project and understand the lineage DAG. Use dbt docs to generate a browsable site.

## What to Learn
- Column-level descriptions in `schema.yml`:
  ```yaml
  models:
    - name: stg_orders
      description: "Cleaned orders from the raw ERP feed."
      columns:
        - name: order_id
          description: "Unique identifier for an order. Never null."
  ```
- Doc blocks: long-form descriptions in `.md` files, referenced in YAML via `{{ doc('block_name') }}`. Keeps YAML clean.
  ```markdown
  {% docs order_status %}
  Current state of the order. Values: `pending`, `completed`, `cancelled`, `refunded`.
  {% enddocs %}
  ```
  ```yaml
  - name: status
    description: "{{ doc('order_status') }}"
  ```
- `dbt docs generate` — builds `catalog.json` (warehouse metadata) and `manifest.json` (project graph) in `target/`.
- `dbt docs serve` — starts a local web server with a searchable docs site and interactive DAG visualization.
- Understanding the DAG: nodes are models/sources/seeds; edges are `ref()` and `source()` calls. Upstream failures block downstream models.
- Why documentation matters for data teams (discoverability, trust, onboarding)

## Exercises

1. **Schema descriptions**: Add descriptions to every model and every column in your `schema.yml` files. Be specific — not "the customer id" but "unique identifier for a customer, sourced from the ERP system".

2. **Doc blocks**: Create `models/docs.md` with doc blocks for:
   - A project overview
   - A description of the medallion architecture used (staging = silver, marts = gold)
   - A description of the `status` field with all valid values and their meanings

3. **Generate and review**: Run `dbt docs generate && dbt docs serve`. Take a screenshot or describe:
   - The DAG showing source -> staging -> mart flow
   - That your descriptions appear on the model pages

4. **Lineage analysis**: Looking at the DAG, answer:
   - How many models depend on `stg_orders`?
   - If `raw_orders` source had a schema change, which models would break?
   - What is the longest path from source to mart?

Write your YAML and markdown files as the solution. Write lineage answers in `solution.md`.
