# SupplyTrackSDK — Java API Reference

## Installation

```xml
<dependency>
    <groupId>com.supplytrack</groupId>
    <artifactId>supplytrack-sdk</artifactId>
    <version>2.4.1</version>
</dependency>
```

## Core Class: `SupplyTrackClient`

### Builder

```java
SupplyTrackClient client = SupplyTrackClient.builder()
    .warehouseId("WH-EAST-001")
    .apiKey("st_live_xxxx")
    .region("us-east-1")
    .build();
```

### Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getStockLevel(String sku)` | `StockInfo` | Current stock for a SKU |
| `reserveItems(String sku, int quantity)` | `Reservation` | Reserve items, returns reservation ID |
| `releaseReservation(String reservationId)` | `void` | Cancel a reservation |
| `getWarehouseCapacity()` | `WarehouseCapacity` | Current warehouse utilization |
| `checkExpiration(String sku)` | `ExpirationInfo` | Expiration dates and lot numbers |

## Model Classes

### `StockInfo`
- `String sku`
- `int available` — units available for reservation
- `int reserved` — units currently reserved
- `int total` — available + reserved
- `Instant lastUpdated`

### `Reservation`
- `String reservationId` — unique ID (format: `RSV-xxxxx`)
- `String sku`
- `int quantity`
- `Instant expiresAt` — reservation expires after 15 minutes

### `WarehouseCapacity`
- `String warehouseId`
- `int totalSlots`
- `int usedSlots`
- `double utilizationPercent`

### `ExpirationInfo`
- `String sku`
- `String lotNumber`
- `LocalDate expirationDate`
- `int unitsInLot`

## Exceptions

| Exception | When |
|-----------|------|
| `SupplyTrackException` | Base exception for all SDK errors |
| `InsufficientStockException` | `reserveItems()` when not enough stock |
| `SkuNotFoundException` | Any method when SKU doesn't exist |
| `WarehouseOfflineException` | Warehouse is unreachable |
