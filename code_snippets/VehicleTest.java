@Test
public void testIsAvailableForDates() {
    Vehicle vehicle = new Vehicle(1, "Toyota Camry", 50.0, true, VehicleType.ECONOMY);
    // Add existing booking
    Booking existingBooking = new Booking(1, 1, 1, parseDate("2023-10-01"), parseDate("2023-10-05"), 200.0, true);
    vehicle.addBooking(existingBooking);

    // Test availability for overlapping dates
    assertFalse(vehicle.isAvailableForDates(parseDate("2023-10-03"), parseDate("2023-10-07")));

    // Test availability for non-overlapping dates
    assertTrue(vehicle.isAvailableForDates(parseDate("2023-10-06"), parseDate("2023-10-10")));
}
