import java.util.ArrayList ;

class lambdae{
    public static void main(String args[]){
        ArrayList<String> animals = new ArrayList<>();

        animals.add("Lion");
        animals.add("tiger");
        animals.add("Cheeta");
        System.out.println("-------------Printing current----------");

        System.out.println(animals);
        animals.clear();
        System.out.println("--------Array Cleared-------");
        if(animals.isEmpty()){
            System.out.println("array empty");
        }else{
            System.out.println("Array is not empty");
        }
        animals.add("Lion");
        animals.add("tiger");
        animals.add("Cheeta");
        System.out.println("The size of the array:" +  animals.size());
        System.out.println("Adding more elements:" + animals.add("Realm"));
        System.out.println(animals);
        animals.remove(2);
        System.out.println(animals);
    }
}