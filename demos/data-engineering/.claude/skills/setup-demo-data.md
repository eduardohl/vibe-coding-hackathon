# Setup Demo Data Skill

## Description
Creates mock grocery data in the specified catalog/schema for demo purposes.
Uses the Databricks MCP (uc-function-mcp) to execute SQL and populate tables.

## Triggers
- "setup demo data"
- "create mock data"
- "populate demo tables"
- "initialize demo tables"

## Instructions

When the user asks to set up demo data, follow these steps:

### Step 1: Determine Target Location
Parse the user's request for catalog.schema format (e.g., "my_catalog.my_schema").
If not provided, use `samples` catalog as default.

### Step 2: Verify Catalog Access
First, check if the catalog exists and is accessible:
```sql
SHOW CATALOGS
```

If the requested catalog doesn't exist in the list:
1. Try to create it: `CREATE CATALOG IF NOT EXISTS {catalog}`
2. If creation fails (no storage location), use `samples` catalog as fallback
3. Inform the user which catalog is being used

### Step 3: Create Schema
```sql
CREATE SCHEMA IF NOT EXISTS {catalog}.{schema};
```

### Step 4: Create and Populate Tables

Execute each SQL statement using the Databricks MCP tool `mcp__uc-function-mcp__execute_sql`:

#### 3a. Departments Table (21 rows)
```sql
CREATE OR REPLACE TABLE {catalog}.{schema}.departments AS
SELECT department_id, department FROM VALUES
  (1, 'frozen'), (2, 'other'), (3, 'bakery'), (4, 'produce'),
  (5, 'alcohol'), (6, 'international'), (7, 'beverages'), (8, 'pets'),
  (9, 'dry goods pasta'), (10, 'bulk'), (11, 'personal care'),
  (12, 'meat seafood'), (13, 'pantry'), (14, 'breakfast'),
  (15, 'canned goods'), (16, 'dairy eggs'), (17, 'household'),
  (18, 'babies'), (19, 'snacks'), (20, 'deli'), (21, 'missing')
AS t(department_id, department);
```

#### 3b. Aisles Table (50 rows)
```sql
CREATE OR REPLACE TABLE {catalog}.{schema}.aisles AS
SELECT aisle_id, aisle FROM VALUES
  (1, 'prepared soups salads'), (2, 'specialty cheeses'), (3, 'energy granola bars'),
  (4, 'instant foods'), (5, 'marinades meat preparation'), (6, 'other'),
  (7, 'packaged meat'), (8, 'bakery desserts'), (9, 'pasta sauce'),
  (10, 'kitchen supplies'), (11, 'cold flu allergy'), (12, 'fresh pasta'),
  (13, 'prepared meals'), (14, 'tofu meat alternatives'), (15, 'packaged seafood'),
  (16, 'fresh herbs'), (17, 'buns rolls'), (18, 'dog food care'),
  (19, 'tea'), (20, 'coffee'), (21, 'fresh fruits'), (22, 'fresh vegetables'),
  (23, 'packaged cheese'), (24, 'milk'), (25, 'cream'), (26, 'eggs'),
  (27, 'soy lactosefree'), (28, 'butter'), (29, 'yogurt'), (30, 'juice nectars'),
  (31, 'soft drinks'), (32, 'water seltzer sparkling water'), (33, 'energy sports drinks'),
  (34, 'ice cream ice'), (35, 'frozen meals'), (36, 'frozen pizza'),
  (37, 'frozen breakfast'), (38, 'frozen appetizers sides'), (39, 'frozen produce'),
  (40, 'chips pretzels'), (41, 'popcorn jerky'), (42, 'cookies cakes'),
  (43, 'candy chocolate'), (44, 'granola'), (45, 'cereal'), (46, 'breakfast bars'),
  (47, 'bread'), (48, 'tortillas flat bread'), (49, 'baby food formula'),
  (50, 'diapers wipes')
AS t(aisle_id, aisle);
```

#### 3c. Products Table (50 products)
```sql
CREATE OR REPLACE TABLE {catalog}.{schema}.products AS
WITH base_products AS (
  SELECT
    ROW_NUMBER() OVER (ORDER BY rand()) as product_id,
    product_name,
    aisle_id,
    department_id
  FROM (
    SELECT explode(array(
      struct('Banana' as product_name, 21 as aisle_id, 4 as department_id),
      struct('Bag of Organic Bananas', 21, 4),
      struct('Organic Strawberries', 21, 4),
      struct('Organic Baby Spinach', 22, 4),
      struct('Organic Hass Avocado', 21, 4),
      struct('Organic Avocado', 21, 4),
      struct('Large Lemon', 21, 4),
      struct('Limes', 21, 4),
      struct('Strawberries', 21, 4),
      struct('Organic Whole Milk', 24, 16),
      struct('2% Reduced Fat Milk', 24, 16),
      struct('Organic Large Brown Eggs', 26, 16),
      struct('Large White Eggs', 26, 16),
      struct('Plain Nonfat Greek Yogurt', 29, 16),
      struct('Vanilla Greek Yogurt', 29, 16),
      struct('Butter', 28, 16),
      struct('Cheddar Cheese', 23, 16),
      struct('Mozzarella Cheese', 23, 16),
      struct('Sourdough Bread', 47, 3),
      struct('Whole Wheat Bread', 47, 3),
      struct('Sparkling Water', 32, 7),
      struct('Spring Water', 32, 7),
      struct('Orange Juice', 30, 7),
      struct('Apple Juice', 30, 7),
      struct('Coffee Beans', 20, 7),
      struct('Ground Coffee', 20, 7),
      struct('Green Tea', 19, 7),
      struct('Chicken Breast', 7, 12),
      struct('Ground Beef', 7, 12),
      struct('Salmon Fillet', 15, 12),
      struct('Pasta', 9, 9),
      struct('Marinara Sauce', 9, 9),
      struct('Olive Oil', 13, 13),
      struct('Salt', 13, 13),
      struct('Black Pepper', 13, 13),
      struct('Garlic', 22, 4),
      struct('Onion', 22, 4),
      struct('Tomatoes', 22, 4),
      struct('Potato Chips', 40, 19),
      struct('Tortilla Chips', 40, 19),
      struct('Dark Chocolate Bar', 43, 19),
      struct('Granola Bars', 3, 19),
      struct('Ice Cream', 34, 1),
      struct('Frozen Pizza', 36, 1),
      struct('Frozen Vegetables', 39, 1),
      struct('Paper Towels', 17, 17),
      struct('Dish Soap', 10, 17),
      struct('Laundry Detergent', 17, 17),
      struct('Toothpaste', 11, 11),
      struct('Shampoo', 11, 11)
    )) as product
  )
  SELECT product.product_name, product.aisle_id, product.department_id
)
SELECT * FROM base_products;
```

#### 3d. Orders Table (~10,000 sample orders)
```sql
CREATE OR REPLACE TABLE {catalog}.{schema}.orders AS
SELECT
  ROW_NUMBER() OVER (ORDER BY rand()) as order_id,
  (rand() * 100000)::INT as user_id,
  CASE WHEN rand() < 0.6 THEN 'prior' WHEN rand() < 0.9 THEN 'train' ELSE 'test' END as eval_set,
  (rand() * 10)::INT as order_number,
  (rand() * 7)::INT as order_dow,
  (rand() * 24)::INT as order_hour_of_day,
  CASE WHEN rand() < 0.3 THEN NULL ELSE (rand() * 30)::INT END as days_since_prior_order
FROM range(10000);
```

#### 3e. Order Products Table (~50,000 sample records)
```sql
CREATE OR REPLACE TABLE {catalog}.{schema}.order_products AS
SELECT
  o.order_id,
  p.product_id,
  (rand() * 10 + 1)::INT as add_to_cart_order,
  CASE WHEN rand() < 0.4 THEN 1 ELSE 0 END as reordered
FROM {catalog}.{schema}.orders o
CROSS JOIN (SELECT product_id FROM {catalog}.{schema}.products ORDER BY rand() LIMIT 5) p;
```

### Step 5: Verify Data
Run counts on each table to verify:
```sql
SELECT 'departments' as table_name, COUNT(*) as row_count FROM {catalog}.{schema}.departments
UNION ALL
SELECT 'aisles', COUNT(*) FROM {catalog}.{schema}.aisles
UNION ALL
SELECT 'products', COUNT(*) FROM {catalog}.{schema}.products
UNION ALL
SELECT 'orders', COUNT(*) FROM {catalog}.{schema}.orders
UNION ALL
SELECT 'order_products', COUNT(*) FROM {catalog}.{schema}.order_products;
```

### Step 6: Update CLAUDE.md
After creating the data, remind the user to update their CLAUDE.md to point to the correct catalog/schema.

## Example Output
```
Demo data created successfully in {catalog}.{schema}:

| Table          | Rows    |
|----------------|---------|
| departments    | 21      |
| aisles         | 50      |
| products       | 50      |
| orders         | 10,000  |
| order_products | 50,000  |

Update your CLAUDE.md to use:
- Catalog: {catalog}
- Schema: {schema}
```
