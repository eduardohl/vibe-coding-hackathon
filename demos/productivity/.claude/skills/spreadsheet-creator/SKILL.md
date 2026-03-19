---
name: spreadsheet-creator
description: Create CSV spreadsheets with data from emails or conversation context. Use when the user mentions "create spreadsheet", "budget spreadsheet", "create csv", "make a spreadsheet", "export to csv", or "create a table".
---

# Spreadsheet Creator Skill

Automatically triggered when the user wants to create a spreadsheet or CSV file.

## When to Activate

This skill activates when the user mentions:
- "create spreadsheet", "make a spreadsheet"
- "budget spreadsheet", "expense spreadsheet"
- "create csv", "export to csv"
- "create a table with..."

## Actions

### 1. Identify the Data
- Extract numbers, categories, and labels from the source material
- Identify what calculations are needed (sums, averages, percentages, variances)

### 2. Design the Spreadsheet
- Clear column headers
- Organized rows (by category, date, or other logical grouping)
- Calculated columns (variance, percentage, totals)
- Summary row at the bottom

### 3. Generate the CSV
Create a well-formatted CSV file with:
- Header row
- Data rows with consistent formatting
- Calculated values (not formulas — actual computed numbers)
- Totals/summary row

### 4. Save the File
Write to `src/generated-budget.csv` (or appropriate name)

## Example Output

```csv
Department,Budget,Actual Spend,Variance,Variance %,Status
Warehouse Operations,"$980,000","$1,045,000","$65,000",6.6%,Over Budget
Transportation & Logistics,"$620,000","$571,000","-$49,000",-7.9%,Under Budget
Procurement,"$450,000","$438,000","-$12,000",-2.7%,Under Budget
Inventory Management,"$350,000","$256,000","-$94,000",-26.9%,Under Budget
TOTAL,"$2,400,000","$2,310,000","-$90,000",-3.8%,Under Budget
```

## Guidelines

- **Use clear headers** — anyone should understand the columns
- **Calculate everything** — don't leave math for the reader
- **Include a status column** — visual indicator (Over/Under Budget, On Track, etc.)
- **Add a totals row** — sum up numeric columns
- **Format numbers consistently** — use commas for thousands, consistent decimal places
- **Make it Excel-friendly** — CSV should open cleanly in Excel or Google Sheets

## Notes

- For complex spreadsheets with multiple sheets, create separate CSV files
- Always include the source data alongside calculated fields
- Round percentages to one decimal place
