class employee {
    int empo;
    String name;
    float sal;

    employee(){
        System.out.println("****");
        empo = 101;
        name = "Abhishek";
        sal = 500;
    }

    void displayDetails(){
        System.out.println(empo + "|" + name + "|" + sal);;
    }
}

class Main{
    public static void main(String[] args) {
        employee emp1 = new employee();
        employee emp2 = new employee();
        employee emp3 = new employee();
        emp1.displayDetails();
        emp2.displayDetails();
        emp3.displayDetails();
    }
}