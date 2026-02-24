# Databricks notebook source
# MAGIC %md
# MAGIC # Setup Demo Data
# MAGIC
# MAGIC This notebook creates mock grocery data for the hackathon demos.
# MAGIC Run this once to populate your catalog with sample data.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

# Set your target catalog and schema
# Change these to match your environment
dbutils.widgets.text("catalog", "my_catalog", "Target Catalog")
dbutils.widgets.text("schema", "my_schema", "Target Schema")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

print(f"Creating demo data in: {catalog}.{schema}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Schema

# COMMAND ----------

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")
print(f"Schema {catalog}.{schema} ready")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Departments Table

# COMMAND ----------

departments_data = [
    (1, "frozen"),
    (2, "other"),
    (3, "bakery"),
    (4, "produce"),
    (5, "alcohol"),
    (6, "international"),
    (7, "beverages"),
    (8, "pets"),
    (9, "dry goods pasta"),
    (10, "bulk"),
    (11, "personal care"),
    (12, "meat seafood"),
    (13, "pantry"),
    (14, "breakfast"),
    (15, "canned goods"),
    (16, "dairy eggs"),
    (17, "household"),
    (18, "babies"),
    (19, "snacks"),
    (20, "deli"),
    (21, "missing"),
]

departments_df = spark.createDataFrame(
    departments_data, ["department_id", "department"]
)
departments_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.departments")
print(f"Created departments table: {departments_df.count()} rows")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Aisles Table

# COMMAND ----------

aisles_data = [
    (1, "prepared soups salads"),
    (2, "specialty cheeses"),
    (3, "energy granola bars"),
    (4, "instant foods"),
    (5, "marinades meat preparation"),
    (6, "other"),
    (7, "packaged meat"),
    (8, "bakery desserts"),
    (9, "pasta sauce"),
    (10, "kitchen supplies"),
    (11, "cold flu allergy"),
    (12, "fresh pasta"),
    (13, "prepared meals"),
    (14, "tofu meat alternatives"),
    (15, "packaged seafood"),
    (16, "fresh herbs"),
    (17, "buns rolls"),
    (18, "dog food care"),
    (19, "tea"),
    (20, "coffee"),
    (21, "fresh fruits"),
    (22, "fresh vegetables"),
    (23, "packaged cheese"),
    (24, "milk"),
    (25, "cream"),
    (26, "eggs"),
    (27, "soy lactosefree"),
    (28, "butter"),
    (29, "yogurt"),
    (30, "juice nectars"),
    (31, "soft drinks"),
    (32, "water seltzer sparkling water"),
    (33, "energy sports drinks"),
    (34, "ice cream ice"),
    (35, "frozen meals"),
    (36, "frozen pizza"),
    (37, "frozen breakfast"),
    (38, "frozen appetizers sides"),
    (39, "frozen produce"),
    (40, "chips pretzels"),
    (41, "popcorn jerky"),
    (42, "cookies cakes"),
    (43, "candy chocolate"),
    (44, "granola"),
    (45, "cereal"),
    (46, "breakfast bars"),
    (47, "bread"),
    (48, "tortillas flat bread"),
    (49, "baby food formula"),
    (50, "diapers wipes"),
    (51, "facial care"),
    (52, "oral hygiene"),
    (53, "shave needs"),
    (54, "skin care"),
    (55, "hair care"),
    (56, "eye ear care"),
    (57, "first aid"),
    (58, "feminine care"),
    (59, "deodorants"),
    (60, "body lotions soap"),
    (61, "vitamins supplements"),
    (62, "digestion"),
    (63, "protein bars"),
    (64, "food storage"),
    (65, "cleaning products"),
    (66, "air fresheners candles"),
    (67, "trash bags liners"),
    (68, "laundry"),
    (69, "dish detergents"),
    (70, "cat food care"),
    (71, "cat litter"),
    (72, "dog treats"),
    (73, "bird food"),
    (74, "fish food"),
    (75, "more household"),
    (76, "plates bowls cups flatware"),
    (77, "baking ingredients"),
    (78, "spices seasonings"),
    (79, "oils vinegars"),
    (80, "condiments"),
    (81, "pickled goods olives"),
    (82, "spreads"),
    (83, "honeys syrups nectars"),
    (84, "sugar sweeteners"),
    (85, "flour"),
    (86, "nuts seeds dried fruit"),
    (87, "dried fruits"),
    (88, "latino foods"),
    (89, "asian foods"),
    (90, "kosher foods"),
    (91, "indian foods"),
    (92, "british foods"),
    (93, "grains rice dried goods"),
    (94, "canned meat seafood"),
    (95, "canned fruit applesauce"),
    (96, "canned vegetables"),
    (97, "soup broth bouillon"),
    (98, "canned jarred vegetables"),
    (99, "poultry counter"),
    (100, "beef counter"),
]

aisles_df = spark.createDataFrame(aisles_data, ["aisle_id", "aisle"])
aisles_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.aisles")
print(f"Created aisles table: {aisles_df.count()} rows")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Products Table

# COMMAND ----------

products_data = [
    (1, "Banana", 21, 4),
    (2, "Bag of Organic Bananas", 21, 4),
    (3, "Organic Strawberries", 21, 4),
    (4, "Organic Baby Spinach", 22, 4),
    (5, "Organic Hass Avocado", 21, 4),
    (6, "Organic Avocado", 21, 4),
    (7, "Large Lemon", 21, 4),
    (8, "Limes", 21, 4),
    (9, "Strawberries", 21, 4),
    (10, "Organic Raspberries", 21, 4),
    (11, "Organic Whole Milk", 24, 16),
    (12, "2% Reduced Fat Milk", 24, 16),
    (13, "Organic Large Brown Eggs", 26, 16),
    (14, "Large White Eggs", 26, 16),
    (15, "Plain Nonfat Greek Yogurt", 29, 16),
    (16, "Vanilla Greek Yogurt", 29, 16),
    (17, "Butter", 28, 16),
    (18, "Salted Butter", 28, 16),
    (19, "Cheddar Cheese", 23, 16),
    (20, "Mozzarella Cheese", 23, 16),
    (21, "Sourdough Bread", 47, 3),
    (22, "Whole Wheat Bread", 47, 3),
    (23, "Sparkling Water", 32, 7),
    (24, "Spring Water", 32, 7),
    (25, "Orange Juice", 30, 7),
    (26, "Apple Juice", 30, 7),
    (27, "Coffee Beans", 20, 7),
    (28, "Ground Coffee", 20, 7),
    (29, "Green Tea", 19, 7),
    (30, "Black Tea", 19, 7),
    (31, "Chicken Breast", 7, 12),
    (32, "Ground Beef", 7, 12),
    (33, "Salmon Fillet", 15, 12),
    (34, "Shrimp", 15, 12),
    (35, "Pasta", 9, 9),
    (36, "Spaghetti", 9, 9),
    (37, "Marinara Sauce", 9, 9),
    (38, "Alfredo Sauce", 9, 9),
    (39, "Olive Oil", 79, 13),
    (40, "Vegetable Oil", 79, 13),
    (41, "Salt", 78, 13),
    (42, "Black Pepper", 78, 13),
    (43, "Garlic", 22, 4),
    (44, "Onion", 22, 4),
    (45, "Tomatoes", 22, 4),
    (46, "Cucumber", 22, 4),
    (47, "Potato Chips", 40, 19),
    (48, "Tortilla Chips", 40, 19),
    (49, "Dark Chocolate Bar", 43, 19),
    (50, "Milk Chocolate", 43, 19),
]

products_df = spark.createDataFrame(
    products_data, ["product_id", "product_name", "aisle_id", "department_id"]
)
products_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.products")
print(f"Created products table: {products_df.count()} rows")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Orders Table

# COMMAND ----------

from pyspark.sql import functions as F

# Generate 10,000 sample orders
orders_df = (
    spark.range(1, 10001)
    .withColumnRenamed("id", "order_id")
    .withColumn("user_id", (F.rand() * 5000).cast("int") + 1)
    .withColumn(
        "eval_set",
        F.when(F.rand() < 0.6, "prior").when(F.rand() < 0.8, "train").otherwise("test"),
    )
    .withColumn("order_number", (F.rand() * 20).cast("int") + 1)
    .withColumn("order_dow", (F.rand() * 7).cast("int"))
    .withColumn("order_hour_of_day", (F.rand() * 24).cast("int"))
    .withColumn(
        "days_since_prior_order",
        F.when(F.rand() < 0.15, None).otherwise((F.rand() * 30).cast("int")),
    )
)

orders_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.orders")
print(f"Created orders table: {orders_df.count()} rows")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Order Products Table

# COMMAND ----------

# Generate order-product relationships (variable basket sizes, 2-8 products per order)
order_products_df = spark.sql(f"""
        SELECT
            order_id,
            product_id,
            ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY add_to_cart_order) as add_to_cart_order,
            CASE WHEN rand() < 0.4 THEN 1 ELSE 0 END as reordered
        FROM (
            SELECT
                o.order_id,
                p.product_id,
                rand() as add_to_cart_order
            FROM {catalog}.{schema}.orders o
            CROSS JOIN {catalog}.{schema}.products p
            WHERE rand() < 0.12
        )
    """)

order_products_df.write.mode("overwrite").saveAsTable(
    f"{catalog}.{schema}.order_products"
)
print(f"Created order_products table: {order_products_df.count()} rows")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verify Data

# COMMAND ----------

print("\n" + "=" * 50)
print("DEMO DATA SETUP COMPLETE")
print("=" * 50 + "\n")

tables = ["departments", "aisles", "products", "orders", "order_products"]
for table in tables:
    count = spark.table(f"{catalog}.{schema}.{table}").count()
    print(f"  {table:20} : {count:>10,} rows")

print("\n" + "=" * 50)
print(f"Data location: {catalog}.{schema}")
print("=" * 50)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Next Steps
# MAGIC
# MAGIC Update your `CLAUDE.md` file to point to your catalog:
# MAGIC
# MAGIC ```markdown
# MAGIC ### Data Sources
# MAGIC - **Catalog:** `{your_catalog}`
# MAGIC - **Schema:** `{your_schema}`
# MAGIC ```
