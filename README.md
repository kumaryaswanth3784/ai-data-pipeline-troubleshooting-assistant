# AI Data Pipeline Troubleshooting Assistant

A local Python prototype that demonstrates how AI-assisted systems can investigate Data Engineering pipeline failures using tools, RAG, vector search, and agent workflows.

## Project Overview

This project simulates an AI Data Pipeline Troubleshooting Assistant that analyzes pipeline failures and provides troubleshooting recommendations.

The prototype demonstrates concepts commonly used when designing AI-powered applications:

- Pipeline status and log analysis
- Schema comparison and validation
- Data quality checks
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector similarity search
- Tool calling
- Agent decision-making
- Multi-step agent workflows
- MCP concepts
- AI application security

## Architecture

```text
User
  |
  v
Data Pipeline Assistant
  |
  v
Agent
  |
  +----> Pipeline Status Tool
  |
  +----> Log Analysis
  |
  +----> Schema Comparison Tool
  |
  +----> Data Quality Tool
  |
  +----> Vector Search / RAG
  |
  v
Diagnosis



## Example

The simulated pipeline contains a Snowflake load failure caused by a schema mismatch.

```text
Source:
age = integer

Target:
age = string


Agent Decision:
compare_schema

Tool Result:
age → source = integer, target = string

Diagnosis:
Schema mismatch detected.

Recommendation:
Fix the schema mismatch before retrying the load.


Knowledge Documents
        |
        v
     Embeddings
        |
        v
   Vector Store
        |
        v
 Similarity Search
        |
        v
Relevant Knowledge
        |
        v
      Agent


### Then do these 3 things:

**1.** Click **Preview** at the top and check that it looks properly formatted.

**2.** Click **Commit changes...** at the top-right.

**3.** In the commit window:
- Keep **Commit directly to the `main` branch**
- Commit message:
  ```text
  Improve project documentation
  |
  v
Recommended Action
