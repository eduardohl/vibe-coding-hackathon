# SupplyTrackSDK — Node.js Examples

## Express.js Integration

```javascript
const { SupplyTrackClient } = require('@supplytrack/sdk');

const client = new SupplyTrackClient({
  warehouseId: process.env.SUPPLYTRACK_WAREHOUSE_ID,
  apiKey: process.env.SUPPLYTRACK_API_KEY,
  region: 'us-east-1'
});
```

## Reserve Items

```javascript
const { InsufficientStockError, SkuNotFoundError } = require('@supplytrack/sdk');

app.post('/api/supplies/:sku/reserve', async (req, res, next) => {
  try {
    const reservation = await client.reserveItems(req.params.sku, req.body.quantity);
    res.json(reservation);
  } catch (err) {
    if (err instanceof InsufficientStockError) {
      return res.status(409).json({ error: 'Insufficient stock', available: err.available });
    }
    if (err instanceof SkuNotFoundError) {
      return res.status(404).json({ error: `SKU not found: ${err.sku}` });
    }
    next(err);
  }
});
```

## Check Expiration

```javascript
const info = await client.checkExpiration('MED-GLV-001');
const daysUntilExpiry = Math.ceil((new Date(info.expirationDate) - Date.now()) / 86400000);
if (daysUntilExpiry < 30) {
  console.warn(`Lot ${info.lotNumber} expires in ${daysUntilExpiry} days`);
}
```

## Mocking in Tests

```javascript
jest.mock('@supplytrack/sdk', () => ({
  SupplyTrackClient: jest.fn().mockImplementation(() => ({
    getStockLevel: jest.fn(),
    reserveItems: jest.fn(),
    releaseReservation: jest.fn(),
    getWarehouseCapacity: jest.fn(),
    checkExpiration: jest.fn()
  }))
}));

// In test:
client.reserveItems.mockResolvedValue({
  reservationId: 'RSV-12345',
  sku: 'MED-GLV-001',
  quantity: 10,
  expiresAt: new Date(Date.now() + 900000).toISOString()
});
```
