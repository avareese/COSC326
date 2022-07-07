import java.util.*; 
/**
 * Ava Reese - 2678742
 * Katherine Butt - 4347525
 */
class CountingUpMain{

    //* main method which gets user input and stores them as variables then creates an instance
    /* of CountingUp class and checks for correct input
    */
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    while(true){
        System.out.println("Please enter an integer for n or press ctrl+z to end: ");
        String n = sc.nextLine();
        System.out.println("Please inter an integer for k or press ctrl+z to end: ");
        String k  = sc.nextLine();
        CountingUp c = new CountingUp(); 
        c.checkInput(n,k);
        System.out.println("The result of c(n/k) = " + CountingUp.returnComb());
    }
}
}

        
    


