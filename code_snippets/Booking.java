import java.util.Date;

public class Booking {
    private int bookingId;
    private int vehicleId;
    private int customerId;
    private Date startDate;
    private Date endDate;
    private double totalCost;
    private boolean confirmed;

    public Booking(int bookingId, int vehicleId, int customerId, Date startDate, Date endDate, double dailyRate) {
        this.bookingId = bookingId;
        this.vehicleId = vehicleId;
        this.customerId = customerId;
        this.startDate = startDate;
        this.endDate = endDate;
        this.totalCost = calculateCost(dailyRate, calculateNumberOfDays());
        this.confirmed = false;
    }

    private int calculateNumberOfDays() {
        long diff = endDate.getTime() - startDate.getTime();
        return (int) (diff / (1000 * 60 * 60 * 24));
    }

    public double calculateCost(double dailyRate, int numberOfDays) {
        return dailyRate * numberOfDays;
    }

    public double getTotalCost() {
        return totalCost;
    }

    @Override
    public String toString() {
        return "Booking ID: " + bookingId +
               "\nVehicle ID: " + vehicleId +
               "\nCustomer ID: " + customerId +
               "\nStart Date: " + startDate +
               "\nEnd Date: " + endDate +
               "\nTotal Cost: $" + totalCost +
               "\nConfirmed: " + confirmed;
    }
}
