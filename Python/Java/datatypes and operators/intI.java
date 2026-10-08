interface vehicle{
    void changegear(int g);
    void speedup(int g);
    void applyBrake(int g);
}
class wheel implements vehicle{
    int speed;
    int gear;

    @Override
    public void changegear(int a){
        gear = a;
    }
    @Override
    public void speedup(int b){
        speed = speed * b;
    }
    @Override
    public void applyBrake(int c){
        gear = speed * c;
    }
    public void printState(){
        System.out.println("speed" + speed + "gear" + gear);
    }
}
class car implements vehicle{
    int speed;
    int gear;

    @Override
    public void changegear(int d){
        gear = d;
    }
    @Override
    public void speedup(int e){
        speed = speed + e;
    }
    @Override
    public void applyBrake(int f){
        gear = speed - f;
    }
    public void printState(){
        System.out.println("speed" + speed + "gear" + gear);
    }
}
class intI {
    public static void main(String args[])
    {
        wheel wheel = new wheel();
        wheel.changegear(2);
        wheel.speedup(7);
        wheel.applyBrake(5);
        System.out.println("Bicycle presentstate:");
        wheel.printState();

        car cab = new car();
        cab.changegear(6);
        cab.speedup(8);
        cab.applyBrake(5);
        System.out.println("Car presentstate:");
        cab.printState();
    }
}