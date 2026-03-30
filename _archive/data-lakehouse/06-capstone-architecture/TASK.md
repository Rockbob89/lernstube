# Task 6: Capstone — Architecture Design

## Objective
Design a complete lakehouse architecture for a realistic business scenario. Produce an Architecture Decision Record (ADR) justifying every major choice.

## Scenario
A mid-size logistics company operates 200 warehouses across Europe. They need to:
- Ingest IoT sensor data from warehouse equipment (temperature, vibration, uptime) — ~10k events/second across all warehouses
- Ingest daily batch feeds: inventory snapshots, shipment records, employee schedules (CSV/JSON from legacy ERP)
- Enable data science team to train predictive maintenance models on historical sensor data
- Provide near-real-time dashboards for warehouse managers (equipment health, inventory levels)
- Meet GDPR requirements for employee data

## Deliverables

1. **Architecture diagram**: Create an ASCII or text-based architecture diagram showing all components and data flows. Include: ingestion, storage layers, compute, serving, orchestration, governance.

2. **ADR document**: Write an ADR (`adr.md`) covering:
   - **Context**: Restate the problem in your own words
   - **Decisions** (for each, state what you chose and 1-2 alternatives you rejected with reasons):
     - Cloud provider and primary services
     - Table format (Delta/Iceberg/Hudi)
     - Streaming ingestion approach
     - Batch ingestion approach
     - Medallion layer design (what lives in each layer)
     - Compute engine(s)
     - Orchestration tool
     - Catalog and governance
     - GDPR compliance approach for employee data
   - **Consequences**: What are the operational tradeoffs of your design?

3. **Cost estimate**: Provide a rough monthly cost estimate (order of magnitude) for the streaming ingestion + storage components. State your assumptions.

No code for this task. Write everything in markdown files in this folder.
