---
name: spark-optimization
description: Analyze and optimize PySpark code for better performance
triggers:
  - optimize spark
  - slow job
  - performance issue
  - shuffle
  - skew
  - spark tuning
---

# Spark Optimization Skill

Automatically triggered when the user mentions Spark performance concerns.

## When to Activate

This skill activates when the user mentions:
- "optimize", "slow", "performance"
- "shuffle", "skew", "partition"
- "takes too long", "speed up"
- "Spark tuning", "job optimization"

## Actions

### 1. Analyze the Code

Review PySpark code for common performance issues:

**Anti-patterns to look for:**
- `collect()` on large datasets
- UDFs instead of built-in functions
- Unnecessary shuffles from `groupBy` or `join`
- Missing partition pruning
- Cross joins or cartesian products
- String operations without optimization

### 2. Check for Specific Issues

**Shuffle Issues:**
```python
# Bad: Multiple shuffles
df.groupBy("col1").agg(...).groupBy("col2").agg(...)

# Better: Single shuffle with window functions
from pyspark.sql.window import Window
window = Window.partitionBy("col1")
df.withColumn("metric", F.sum("value").over(window))
```

**Skew Issues:**
```python
# Add salting for skewed joins
df = df.withColumn("salt", F.expr("floor(rand() * 10)"))
```

**Broadcast Joins:**
```python
# Small table should be broadcast
from pyspark.sql.functions import broadcast
result = large_df.join(broadcast(small_df), "key")
```

### 3. Review Spark Configuration

Recommend settings based on workload:

```python
# For shuffle-heavy workloads
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")

# For skewed data
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

# For Delta optimization
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")
spark.conf.set("spark.databricks.delta.autoCompact.enabled", "true")
```

### 4. Generate Recommendations

Present findings in actionable format:

```
## Spark Optimization Analysis

### Issues Found
1. **Unnecessary Shuffle** (Line 45)
   - `groupBy` followed by another `groupBy`
   - Impact: High (multiple shuffle operations)
   - Fix: Combine into single aggregation

2. **Missing Broadcast** (Line 67)
   - Small lookup table joined without broadcast
   - Impact: Medium (shuffle on both sides)
   - Fix: Add `broadcast()` hint

### Recommended Configuration
Add to cluster spark_conf:
- spark.sql.adaptive.enabled: true
- spark.sql.adaptive.skewJoin.enabled: true

### Estimated Impact
- Current: ~15 minutes
- After optimization: ~5 minutes (estimated 67% improvement)
```

## Example Interaction

```
User: My job is taking too long, can you optimize it?

Claude: [Skill activates]
I'll analyze your Spark code for optimization opportunities.

[Reviews code]

Found 3 optimization opportunities:

1. **Line 78: Use broadcast join**
   The products table is small (50 rows). Broadcasting it will eliminate a shuffle.

   Current:
   df.join(products, "product_id")

   Optimized:
   df.join(broadcast(products), "product_id")

2. **Enable Adaptive Query Execution**
   Add these Spark configs to your cluster...
```
