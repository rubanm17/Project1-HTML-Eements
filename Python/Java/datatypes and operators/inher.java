class inher{
        int age,id;
        String name;
        void naming(String name){
            System.out.println("Name" + name);
        }
}

class heir extends inher{
    void ageN(int age){
        System.out.println("Age of the Student"+age);
    }
}

class Main {
    public static  void main(){
        heir s = new heir();
        s.naming("Gashwa");
        s.ageN(14);
    }
}