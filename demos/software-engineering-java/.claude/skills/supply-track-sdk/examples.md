# SupplyTrackSDK — Java Examples

## Spring Boot Bean

```java
@Bean
public SupplyTrackClient supplyTrackClient(
        @Value("${supplytrack.warehouse-id}") String warehouseId,
        @Value("${supplytrack.api-key}") String apiKey) {
    return SupplyTrackClient.builder()
        .warehouseId(warehouseId)
        .apiKey(apiKey)
        .region("us-east-1")
        .build();
}
```

## Reserve Items

```java
try {
    Reservation reservation = client.reserveItems("MED-GLV-001", 50);
    log.info("Reserved: {}", reservation.getReservationId());
} catch (InsufficientStockException e) {
    log.warn("Only {} available", e.getAvailable());
} catch (SkuNotFoundException e) {
    log.error("Unknown SKU: {}", e.getSku());
}
```

## Check Expiration

```java
ExpirationInfo info = client.checkExpiration("MED-GLV-001");
if (info.getExpirationDate().isBefore(LocalDate.now().plusDays(30))) {
    log.warn("Lot {} expires soon: {}", info.getLotNumber(), info.getExpirationDate());
}
```

## Mocking in Tests

```java
@MockitoBean
private SupplyTrackClient supplyTrackClient;

@Test
void shouldReserveItems() throws Exception {
    when(supplyTrackClient.reserveItems("MED-GLV-001", 10))
        .thenReturn(new Reservation("RSV-12345", "MED-GLV-001", 10, Instant.now().plusSeconds(900)));

    mockMvc.perform(post("/api/supplies/MED-GLV-001/reserve")
            .contentType(MediaType.APPLICATION_JSON)
            .content("{\"quantity\": 10}"))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$.reservationId").value("RSV-12345"));
}
```
