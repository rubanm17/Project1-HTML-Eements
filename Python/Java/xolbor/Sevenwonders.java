class SevenWonders {
    void location() {
        System.out.println("Location is:");
    }

    void famousFor() {
        System.out.println("Famous for:");
    }
}

class TajMahal extends SevenWonders {
    void location() {
        System.out.println("Taj Mahal is in Agra, India");
    }

    void famousFor() {
        System.out.println("It is famous for its white marble architecture");
    }
}

class GreatWall extends SevenWonders {
    void location() {
        System.out.println("Great Wall is in China");
    }

    void famousFor() {
        System.out.println("It is famous for its long defensive walls");
    }
}

class Petra extends SevenWonders {
    void location() {
        System.out.println("Petra is in Jordan");
    }

    void famousFor() {
        System.out.println("It is famous for its rock-cut architecture");
    }
}

class Colosseum extends SevenWonders {
    void location() {
        System.out.println("Colosseum is in Rome, Italy");
    }

    void famousFor() {
        System.out.println("It is famous for its ancient Roman arena");
    }
}

class ChichenItza extends SevenWonders {
    void location() {
        System.out.println("Chichen Itza is in Mexico");
    }

    void famousFor() {
        System.out.println("It is famous for its Mayan pyramid");
    }
}

class MachuPicchu extends SevenWonders {
    void location() {
        System.out.println("Machu Picchu is in Peru");
    }

    void famousFor() {
        System.out.println("It is famous for its Inca ruins");
    }
}

class ChristRedeemer extends SevenWonders {
    void location() {
        System.out.println("Christ the Redeemer is in Brazil");
    }

    void famousFor() {
        System.out.println("It is famous for its giant statue");
    }
}

class Main {
    public static void main(String args[]) {
        SevenWonders A = new TajMahal();
        SevenWonders B = new GreatWall();
        SevenWonders C = new Petra();
        SevenWonders D = new Colosseum();
        SevenWonders E = new ChichenItza();
        SevenWonders F = new MachuPicchu();
        SevenWonders G = new ChristRedeemer();

        A.location();
        A.famousFor();

        B.location();
        B.famousFor();

        C.location();
        C.famousFor();

        D.location();
        D.famousFor();

        E.location();
        E.famousFor();

        F.location();
        F.famousFor();

        G.location();
        G.famousFor();
    }
}