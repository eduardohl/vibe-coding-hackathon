# SupplyTrackSDK — Node.js API Reference

## Installation

```bash
npm install @supplytrack/sdk
```

## Core Class: `SupplyTrackClient`

### Constructor

```javascript
const { SupplyTrackClient } = require('@supplytrack/sdk');

const client = new SupplyTrackClient({
  warehouseId: 'WH-EAST-001',
  apiKey: 'st_live_xxxx',
  region: 'us-east-1'
});
```

### Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getStockLevel(sku)` | `Promise<StockInfo>` | Current stock for a SKU |
| `reserveItems(sku, quantity)` | `Promise<Reservation>` | Reserve items, returns reservation ID |
| `releaseReservation(reservationId)` | `Promise<void>` | Cancel a reservation |
| `getWarehouseCapacity()` | `Promise<WarehouseCapacity>` | Current warehouse utilization |
| `checkExpiration(sku)` | `Promise<ExpirationInfo>` | Expiration dates and lot numbers |

## Response Shapes

### `StockInfo`
- `sku` (string)
- `available` (number) — units available for reservation
- `reserved` (number) — units currently reserved
- `total` (number) — available + reserved
- `lastUpdated` (ISO 8601 string)

### `Reservation`
- `reservationId` (string) — unique ID (format: `RSV-xxxxx`)
- `sku` (string)
- `quantity` (number)
- `expiresAt` (ISO 8601 string) — reservation expires after 15 minutes

### `WarehouseCapacity`
- `warehouseId` (string)
- `totalSlots` (number)
- `usedSlots` (number)
- `utilizationPercent` (number)

### `ExpirationInfo`
- `sku` (string)
- `lotNumber` (string)
- `expirationDate` (ISO 8601 date string)
- `unitsInLot` (number)

## Errors

| Error Class | When |
|-------------|------|
| `SupplyTrackError` | Base error for all SDK errors |
| `InsufficientStockError` | `reserveItems()` when not enough stock (has `.available` property) |
| `SkuNotFoundError` | Any method when SKU doesn't exist (has `.sku` property) |
| `WarehouseOfflineError` | Warehouse is unreachable |
