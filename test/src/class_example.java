class Box {
    double width, height, depth;

    void volume() {
        System.out.print("Volume is ");
        System.out.println(width * height * depth);
    }

    double volume_calc() {
        return width * height * depth;
    }

    int square(int i) {
        return i * i;
    }

}

class BoxDemo {
    public static void main(String args[]) {
        Box mybox = new Box();
        Box mybox2 = new Box();
        double vol;
        // assign values to mybox's instance variables
        mybox.width = 10;
        mybox.height = 20;
        mybox.depth = 15;

        mybox2.width = 21;
        mybox2.height = 30;
        mybox2.depth = 10;

        //compute volume of box
        vol = mybox.width * mybox.height * mybox.depth;
        System.out.println("Volume is " + vol);
        // If value is empty or not given, output will be zero
        System.out.println(mybox.width + " " + mybox.height + " " + mybox.depth);

        vol = mybox2.width * mybox2.height * mybox2.depth;
        System.out.println("Volume is " + vol);

        // reference to link
        Box mybox3 = mybox;
        System.out.println(mybox3);
        mybox = null;
        System.out.println(mybox);

        //display the vol by method
        mybox3.volume();
        mybox2.volume();

        //get volumn
        vol = mybox3.volume_calc();
        System.out.println(vol);

        // calc square
        int x;
        x = mybox3.square(5);
        System.out.println("Square: " + x);

    }
}
