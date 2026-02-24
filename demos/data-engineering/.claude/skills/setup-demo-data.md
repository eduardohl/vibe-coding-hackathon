---
name: setup-demo-data
description: Creates mock grocery data for demo purposes via Databricks MCP
triggers:
  - setup demo data
  - create mock data
  - populate demo tables
  - initialize demo tables
---

# Setup Demo Data Skill

## Instructions

When the user asks to set up demo data, follow these steps:

### Step 1: Determine Target Location
Parse the user's request for catalog.schema format (e.g., "my_catalog.my_schema").
If not provided, ask the user for a target catalog and schema.

### Step 2: Verify Catalog Access
First, check if the catalog exists and is accessible:
```sql
SHOW CATALOGS
```

If the requested catalog doesn't exist in the list:
1. Try to create it: `CREATE CATALOG IF NOT EXISTS {catalog}`
2. If creation fails (no storage location), suggest a catalog from the list
3. Inform the user which catalog is being used

### Step 3: Create Schema
```sql
CREATE SCHEMA IF NOT EXISTS {catalog}.{schema};
```

### Step 4: Create and Populate Tables

Execute each SQL statement using the Databricks MCP tool `mcp__uc-function-mcp__execute_sql`:

#### 4a. Departments Table (21 rows)
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

#### 4b. Aisles Table (100 rows)
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
  (50, 'diapers wipes'), (51, 'facial care'), (52, 'oral hygiene'),
  (53, 'shave needs'), (54, 'skin care'), (55, 'hair care'),
  (56, 'eye ear care'), (57, 'first aid'), (58, 'feminine care'),
  (59, 'deodorants'), (60, 'body lotions soap'), (61, 'vitamins supplements'),
  (62, 'digestion'), (63, 'protein bars'), (64, 'food storage'),
  (65, 'cleaning products'), (66, 'air fresheners candles'), (67, 'trash bags liners'),
  (68, 'laundry'), (69, 'dish detergents'), (70, 'cat food care'),
  (71, 'cat litter'), (72, 'dog treats'), (73, 'bird food'),
  (74, 'fish food'), (75, 'more household'), (76, 'plates bowls cups flatware'),
  (77, 'baking ingredients'), (78, 'spices seasonings'), (79, 'oils vinegars'),
  (80, 'condiments'), (81, 'pickled goods olives'), (82, 'spreads'),
  (83, 'honeys syrups nectars'), (84, 'sugar sweeteners'), (85, 'flour'),
  (86, 'nuts seeds dried fruit'), (87, 'dried fruits'), (88, 'latino foods'),
  (89, 'asian foods'), (90, 'kosher foods'), (91, 'indian foods'),
  (92, 'british foods'), (93, 'grains rice dried goods'), (94, 'canned meat seafood'),
  (95, 'canned fruit applesauce'), (96, 'canned vegetables'), (97, 'soup broth bouillon'),
  (98, 'canned jarred vegetables'), (99, 'poultry counter'), (100, 'beef counter')
AS t(aisle_id, aisle);
```

#### 4c. Products Table (50 products)
```sql
CREATE OR REPLACE TABLE {catalog}.{schema}.products AS
SELECT product_id, product_name, aisle_id, department_id FROM VALUES
  (1, 'Banana', 21, 4), (2, 'Bag of Organic Bananas', 21, 4),
  (3, 'Organic Strawberries', 21, 4), (4, 'Organic Baby Spinach', 22, 4),
  (5, 'Organic Hass Avocado', 21, 4), (6, 'Organic Avocado', 21, 4),
  (7, 'Large Lemon', 21, 4), (8, 'Limes', 21, 4),
  (9, 'Strawberries', 21, 4), (10, 'Organic Raspberries', 21, 4),
  (11, 'Organic Whole Milk', 24, 16), (12, '2% Reduced Fat Milk', 24, 16),
  (13, 'Organic Large Brown Eggs', 26, 16), (14, 'Large White Eggs', 26, 16),
  (15, 'Plain Nonfat Greek Yogurt', 29, 16), (16, 'Vanilla Greek Yogurt', 29, 16),
  (17, 'Butter', 28, 16), (18, 'Salted Butter', 28, 16),
  (19, 'Cheddar Cheese', 23, 16), (20, 'Mozzarella Cheese', 23, 16),
  (21, 'Sourdough Bread', 47, 3), (22, 'Whole Wheat Bread', 47, 3),
  (23, 'Sparkling Water', 32, 7), (24, 'Spring Water', 32, 7),
  (25, 'Orange Juice', 30, 7), (26, 'Apple Juice', 30, 7),
  (27, 'Coffee Beans', 20, 7), (28, 'Ground Coffee', 20, 7),
  (29, 'Green Tea', 19, 7), (30, 'Black Tea', 19, 7),
  (31, 'Chicken Breast', 7, 12), (32, 'Ground Beef', 7, 12),
  (33, 'Salmon Fillet', 15, 12), (34, 'Shrimp', 15, 12),
  (35, 'Pasta', 9, 9), (36, 'Spaghetti', 9, 9),
  (37, 'Marinara Sauce', 9, 9), (38, 'Alfredo Sauce', 9, 9),
  (39, 'Olive Oil', 79, 13), (40, 'Vegetable Oil', 79, 13),
  (41, 'Salt', 78, 13), (42, 'Black Pepper', 78, 13),
  (43, 'Garlic', 22, 4), (44, 'Onion', 22, 4),
  (45, 'Tomatoes', 22, 4), (46, 'Cucumber', 22, 4),
  (47, 'Potato Chips', 40, 19), (48, 'Tortilla Chips', 40, 19),
  (49, 'Dark Chocolate Bar', 43, 19), (50, 'Milk Chocolate', 43, 19)
AS t(product_id, product_name, aisle_id, department_id);
```

#### 4d. Orders Table (10,000 rows)
```sql
CREATE OR REPLACE TABLE {catalog}.{schema}.orders AS
SELECT
  id + 1 as order_id,
  CAST(rand() * 5000 AS INT) + 1 as user_id,
  CASE WHEN rand() < 0.6 THEN 'prior' WHEN rand() < 0.8 THEN 'train' ELSE 'test' END as eval_set,
  CAST(rand() * 20 AS INT) + 1 as order_number,
  CAST(rand() * 7 AS INT) as order_dow,
  CAST(rand() * 24 AS INT) as order_hour_of_day,
  CASE WHEN rand() < 0.15 THEN NULL ELSE CAST(rand() * 30 AS INT) END as days_since_prior_order
FROM range(10000);
```

#### 4e. Order Products Table (~35,000 rows, variable basket sizes)
```sql
CREATE OR REPLACE TABLE {catalog}.{schema}.order_products AS
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
);
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
| aisles         | 100     |
| products       | 50      |
| orders         | 10,000  |
| order_products | ~35,000 |

Update your CLAUDE.md to use:
- Catalog: {catalog}
- Schema: {schema}
```
