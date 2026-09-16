import math


# ============================================================
# AI DATA PIPELINE ASSISTANT
# ============================================================

print("AI Data Pipeline Assistant")
print("--------------------------")


# ============================================================
# 1. PIPELINE STATUS
# ============================================================

pipeline = {
    "source": "SUCCESS",
    "pyspark_etl": "FAILED",
    "transformation": "SUCCESS",
    "snowflake_load": "FAILED",
    "elasticsearch_load": "SUCCESS"
}

print("\nPIPELINE STATUS")

for stage, status in pipeline.items():
    print(stage, ":", status)


# ============================================================
# 2. PIPELINE LOGS
# ============================================================

logs = {
    "source": "Source data loaded successfully.",

    "pyspark_etl":
        "ERROR: PySpark job failed because of executor memory issue.",

    "transformation":
        "Transformation completed successfully.",

    "snowflake_load":
        "ERROR: Schema mismatch between source and target tables.",

    "elasticsearch_load":
        "Elasticsearch load completed successfully."
}


# ============================================================
# 3. SOURCE AND TARGET SCHEMA
# ============================================================

source_schema = {
    "customer_id": "integer",
    "customer_name": "string",
    "age": "integer",
    "email": "string"
}

target_schema = {
    "customer_id": "integer",
    "customer_name": "string",
    "age": "string",
    "email": "string"
}


# ============================================================
# 4. PIPELINE TOOLS
# ============================================================

def check_pipeline_status(stage):
    return pipeline.get(stage, "STAGE NOT FOUND")


def get_pipeline_log(stage):
    return logs.get(stage, "LOG NOT FOUND")


def check_data_quality():

    return {
        "row_count": 10000,
        "null_values": 25,
        "duplicate_records": 10
    }


# ============================================================
# 5. SCHEMA TOOL
# ============================================================

def compare_schemas():

    mismatches = {}

    for column in source_schema:

        if column in target_schema:

            if source_schema[column] != target_schema[column]:

                mismatches[column] = {
                    "source_type": source_schema[column],
                    "target_type": target_schema[column]
                }

        else:

            mismatches[column] = {
                "source_type": source_schema[column],
                "target_type": "COLUMN NOT FOUND"
            }

    return mismatches


# ============================================================
# 6. SNOWFLAKE TOOL
# ============================================================

def check_snowflake():

    return {
        "connection": "AVAILABLE",
        "authentication": "VALID",
        "warehouse": "RUNNING"
    }


# ============================================================
# 7. PYSPARK TOOL
# ============================================================

def check_pyspark():

    return {
        "application": "RUNNING",
        "executors": 4,
        "memory_status": "HIGH",
        "recommendation":
            "Increase executor memory or optimize transformations."
    }


# ============================================================
# 8. KNOWLEDGE BASE
# ============================================================

knowledge_base = [

    {
        "title": "Schema Troubleshooting",
        "content":
            "When a schema mismatch occurs, compare source and target "
            "column names and data types. Correct the target schema or "
            "transformation logic before retrying the pipeline."
    },

    {
        "title": "Snowflake Connectivity",
        "content":
            "When a Snowflake connection times out, check network "
            "connectivity, connection configuration, credentials, "
            "and retry the operation."
    },

    {
        "title": "PySpark Troubleshooting",
        "content":
            "For PySpark job failures, check application logs, "
            "executor errors, memory usage, input data, and "
            "transformation logic."
    },

    {
        "title": "Data Quality",
        "content":
            "Data quality checks should include row counts, "
            "null values, duplicate records, and schema validation."
    }
]


# ============================================================
# 9. VECTOR STORE
# ============================================================

vector_store = {

    "Schema Troubleshooting":
        [0.90, 0.20, 0.70],

    "Snowflake Connectivity":
        [0.20, 0.90, 0.30],

    "PySpark Troubleshooting":
        [0.80, 0.40, 0.20],

    "Data Quality":
        [0.40, 0.30, 0.90]
}


# ============================================================
# 10. VECTOR DISTANCE
# ============================================================

def vector_distance(vector1, vector2):

    total = 0

    for a, b in zip(vector1, vector2):

        total += (a - b) ** 2

    return math.sqrt(total)


# ============================================================
# 11. VECTOR SEARCH
# ============================================================

def vector_store_search(query_vector):

    results = []

    for document, vector in vector_store.items():

        distance = vector_distance(
            query_vector,
            vector
        )

        results.append(
            (document, distance)
        )

    results.sort(
        key=lambda x: x[1]
    )

    return results[:2]


# ============================================================
# 12. AGENT DECISION
# ============================================================

def decide_next_action(log, tool_history):

    log = log.lower()

    # First decision
    if len(tool_history) == 0:

        if "schema" in log:
            return "compare_schema"

        elif "pyspark" in log or "memory" in log:
            return "check_pyspark"

        elif "snowflake" in log or "timeout" in log:
            return "check_snowflake"

        else:
            return "check_data_quality"


    # Second decision
    if "compare_schema" in tool_history:

        if "check_data_quality" not in tool_history:
            return "check_data_quality"


    if "check_pyspark" in tool_history:

        if "check_data_quality" not in tool_history:
            return "check_data_quality"


    # No more tools required
    return "finish"


# ============================================================
# 13. DYNAMIC TOOL EXECUTOR
# ============================================================

def execute_tool(tool_name):

    if tool_name == "compare_schema":

        return compare_schemas()

    elif tool_name == "check_data_quality":

        return check_data_quality()

    elif tool_name == "check_snowflake":

        return check_snowflake()

    elif tool_name == "check_pyspark":

        return check_pyspark()

    else:

        return "Tool not available."


# ============================================================
# 14. AGENT LOOP
# ============================================================

def agent_loop(stage):

    status = check_pipeline_status(stage)

    if status != "FAILED":

        return {
            "stage": stage,
            "status": status,
            "message": "No investigation required."
        }


    log = get_pipeline_log(stage)

    tool_history = []

    tool_results = []


    # --------------------------------------------------------
    # Agent loop
    # --------------------------------------------------------

    for step in range(5):

        next_action = decide_next_action(
            log,
            tool_history
        )


        # Stop when agent decides investigation is complete

        if next_action == "finish":

            break


        print("\nAgent Step:", step + 1)

        print("Agent Decision:", next_action)


        # Execute selected tool

        result = execute_tool(next_action)

        print("Tool Result:", result)


        # Save tool history

        tool_history.append(next_action)

        tool_results.append(
            {
                "tool": next_action,
                "result": result
            }
        )


    # --------------------------------------------------------
    # Vector search
    # --------------------------------------------------------

    if "schema" in log.lower():

        query_vector = [0.85, 0.25, 0.65]

    elif "pyspark" in log.lower():

        query_vector = [0.80, 0.40, 0.20]

    elif "snowflake" in log.lower():

        query_vector = [0.20, 0.90, 0.30]

    else:

        query_vector = [0.50, 0.50, 0.50]


    vector_results = vector_store_search(
        query_vector
    )


    # --------------------------------------------------------
    # Diagnosis
    # --------------------------------------------------------

    if "schema" in log.lower():

        diagnosis = "Schema mismatch detected."

        recommendation = (
            "Fix the schema mismatch before retrying the load."
        )

    elif "pyspark" in log.lower():

        diagnosis = "PySpark resource issue detected."

        recommendation = (
            "Check executor memory and optimize the Spark job."
        )

    elif "snowflake" in log.lower():

        diagnosis = "Snowflake connectivity issue detected."

        recommendation = (
            "Check Snowflake connectivity and retry the load."
        )

    else:

        diagnosis = "Unknown pipeline failure."

        recommendation = "Review the pipeline logs."


    return {

        "stage": stage,

        "status": status,

        "log": log,

        "tool_history": tool_history,

        "tool_results": tool_results,

        "diagnosis": diagnosis,

        "recommendation": recommendation,

        "vector_results": vector_results
    }


# ============================================================
# 15. TEST AGENT LOOP
# ============================================================

print("\nAGENT LOOP TEST")
print("----------------")


failed_stage = "snowflake_load"

print("Investigating:", failed_stage)


result = agent_loop(failed_stage)


# ============================================================
# 16. FINAL REPORT
# ============================================================

print("\nFINAL AGENT REPORT")
print("------------------")

print("\nFailed Stage:")
print(result["stage"])

print("\nStatus:")
print(result["status"])

print("\nError Log:")
print(result["log"])


print("\nTools Used:")

for tool in result["tool_history"]:

    print("-", tool)


print("\nTool Results:")

for item in result["tool_results"]:

    print(
        item["tool"],
        ":",
        item["result"]
    )


print("\nDiagnosis:")
print(result["diagnosis"])


print("\nRelevant Knowledge:")

for document, distance in result["vector_results"]:

    print(
        document,
        "distance:",
        round(distance, 4)
    )


print("\nRecommendation:")
print(result["recommendation"])


print("\nAgent investigation completed.")