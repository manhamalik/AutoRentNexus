import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Vehicle {
    private int id;
    private String model;
    private double rentalPrice;
    private List<Booking> bookings;

    public Vehicle(int id, String model, double rentalPrice) {
        this.id = id;
        this.model = model;
        this.rentalPrice = rentalPrice;
        this.bookings = new ArrayList<>();
    }

    public boolean isAvailableForDates(Date startDate, Date endDate) {
        for (Booking booking : bookings) {
            if (startDate.before(booking.getEndDate()) && endDate.after(booking.getStartDate())) {
                return false;
            }
        }
        return true;
    }

    public void addBooking(Booking booking) {
        bookings.add(booking);
    }

    @Override
    public String toString() {
        return "Vehicle ID: " + id +
               "\nModel: " + model +
               "\nPrice per day: $" + rentalPrice;
    }
}
