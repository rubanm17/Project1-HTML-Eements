package xolbor;

class geometry{
    public double getArea(){
        return 0;
    }
}

class triangle extends geometry{
    private double base;
    private double height;
    private double length;
    public triangle(double base,double height,double length){
        this.base = base;
        this.height =  height;
        this.length = length;
    }
    public double getArea(){
        return length*base*height;
    }
}
class square extends geometry{
    private double side;
    public square(double side){
        this.side = side;
    }
    public double getArea(){
        return side*side*side;
    }
}
class volume{
    public static void main(String args[]){
        geometry[] g =new geometry[2];
        g[1] = new square(10);
        g[0] = new triangle(5,5,5);
        System.out.println(g[0].getArea());
        System.out.println(g[1].getArea());
    }
}