interface mi{
    public void method1();
    public void method2();
}
class interfrence implements mi{
        public void method1(){
            System.out.println("Implements method 1");
        }
        public void method2(){
            System.out.println("Implements method 2");
        }
        public static void main(String args[]){
            mi obj = new interfrence();
            obj.method1();
            obj.method2();
        }
}