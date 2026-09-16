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
  |
  v
Recommended Action
