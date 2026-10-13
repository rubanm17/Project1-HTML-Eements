
import java.util.Scanner;

interface Vehicle {
    void changeGear(int gear);
    void speedUp(int increment);
    void applyBrakes(int decrement);
    void printStates();
}

class Truck implements Vehicle {
    int speed = 0, gear = 0;

    public void changeGear(int gear) { this.gear = gear; }
    public void speedUp(int increment) { speed += increment; }
    public void applyBrakes(int decrement) { speed -= decrement; }

    public void printStates() {
        System.out.println("Truck - Speed: " + speed + ", Gear: " + gear);
    }
}

class Bike implements Vehicle {
    int speed = 0, gear = 0;

    public void changeGear(int gear) { this.gear = gear; }
    public void speedUp(int increment) { speed += increment; }
    public void applyBrakes(int decrement) { speed -= decrement; }

    public void printStates() {
        System.out.println("Bike - Speed: " + speed + ", Gear: " + gear);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Vehicle[] vehicles = {new Truck(), new Bike()};

        for (Vehicle v : vehicles) {
            System.out.print("Enter gear, speed increment and brake decrement: ");
            int gear = sc.nextInt();
            int increment = sc.nextInt();
            int decrement = sc.nextInt();

            v.changeGear(gear);
            v.speedUp(increment);
            v.applyBrakes(decrement);
            v.printStates();
        }

        sc.close();
    }
}
