import java.util.Scanner;

class MeterToFeet {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input distance in meters
        System.out.print("Enter distance in meters: ");
        double meters = sc.nextDouble();

        // Convert meters to feet
        double feet = meters * 3.28084;

        // Display result with two decimal places
        System.out.printf("Distance in feet: %.2f", feet);

        sc.close();
    }
}
