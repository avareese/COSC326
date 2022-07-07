import java.util.*;
/**
 * Ava Reese - 2678742
 * Katherine Butt - 4347525
 */
public class CountingUp {

    static Scanner sc = new Scanner(System.in);
    static long inputN;
    static long inputK;

    /** Makes a pascal triangle and the triangle is stored in a double array
     * of each row holding every column of the triangle
     */
    
    public static long pascalTriangle (long n, long k){

        if(k ==1){
            return n;
        }

        if(k == 2){
            if(n%2 ==0){
                return (n/2)*n - n/2;
            } else{
                return(n*(n+1))/2 -n;
            }
        }

        int sizeN = ((int) n) + 1; 
        int sizeK = ((int) k) + 1; 
   
        long [][] pascal = new long[sizeN][sizeK];
        
        /** Stores each pascal triangle */
        for (int i=0; i < sizeN; i++){
            pascal[i][0] = 1;

            if(i <= k)
                pascal[i][i] = 1;
            
            for (int j=1; j<sizeK && j< i; j++) {
                pascal[i][j] = pascal[i-1][j]+pascal[i-1][j-1];
            }
        }
        return pascal[sizeN-1][sizeK-1];
    }
/** Getter method which returns the binomial coefficent
 * 
 * @return binomal coefficent
 */
public static long returnComb(){
    return pascalTriangle(inputN, inputK); 
}

//* method which checks if input is integers and if so turns it into a long*/
    public void checkInput(String n, String k){
 
        try{
            inputN = Long.parseLong(n);
            inputK = Long.parseLong(k);
        } catch (NumberFormatException e){
            System.out.println("Please enter a intergers not letters.");
            System.exit(0);
        }
    }
}