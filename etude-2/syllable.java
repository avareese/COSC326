import java.util.*;

/*
This program estimates the number of syllables in a given word
This is achieved by applying a set of rules which help to determine
when a new syllable occurs
Authors: Ava Reese, Francesca Totty, Matt Dixon, Katherine Butt
*/


public class syllable{

    /*
    Setting the data fields for the program
    */
    static ArrayList<Character> vowels = new ArrayList<Character>();
    //static char[] vowels = {'a', 'e', 'i', 'o', 'u', 'y'};
    static String word;
    static int count = 0; 
    static Scanner sc = new Scanner(System.in);


    static{
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('y');

    }

    /*
    This function contains all the required checks to determine
    the occurance and number of syllables in a word
    */
    public static int checkSyllables (String word){
        count = 0;
        word = word.toLowerCase();
        char [] wordArray = word.toCharArray();

        //* When there is no input
        if(wordArray.length == 0){
            return 0;
        }

        //* When the length of the input is only 1 or 2 characters there can't be more than on syllable
        if(wordArray.length == 1 || wordArray.length==2){
            return 1;
        }
      

    /*
    These for loops go through the input and check for any vowels
    If a vowel is found then the counter is increased by 1
    */
        for(char w : wordArray){
            for( char c : vowels){
                if(w == c){
                    count++;
                }

            }
        }

        /*
        If a e is found at the end of word it means it is a silent vowel.
        Silent vowels don't indicate the begining of a new syllable
        Therefore the counter is reduced by 1
        */
        if(word.charAt(word.length()-1) == 'e'){
            count--;
        }

        /*
        If a 'ue', 'ea' or 'oo' or 'ee' is found in the word it is not counted as a syllable.
        Therefore the counter is decreased by 1.
        */
        if (word.contains("ue") || word.contains ("ea") || word.contains("oo") || word.contains("ee")){
            count--;
        }

        /*
        If a 'lly' is found in the word it is counted as a syllable.
        Therefore the counter is increased by 1.
        */
        if (word.contains("lly")){
            count++; 
        }

        /*
        if the word ends with ed decrease the count
        */
        if(word.endsWith("ed")){
            count--;
        }

        if(word.endsWith("le")){
            count++;
        }
    
        /*
        Iterates through each char in a word to check if it contains more than one consecutive vowel
        */
        for(int i = 1; i < wordArray.length; i++){
            char firstletter = word.charAt(i-1);
            char nextletter = word.charAt(i);
            
            if(vowels.contains(firstletter)){
                if(firstletter == nextletter){
                    return 1;
                }
            else if (wordArray.length == 3){
                count++;

            }
        }
    }
    

        /*
        If a word contains 'mes', 'ves', 'kes', 'bes', 'des', 'les', 'nes', 'ees' and 'ries' is found in the word it is not counted as a syllable.
        Therefore the counter is decreased by 1.
        */

        String[] checkDecrease = new String[]{"mes", "ves", "kes", "bes", "des", "les", "nes", "ries", "ees"};

            for(String x : checkDecrease ){
                if(word.contains(x)){
                    count--;
                    break;
                }
            }

        /*
        If a word contains 'zes', 'xes' or 'ges' it is counted as a syllable.
        Therefore the counter is increased by 1.
        */
        String[] checkIncrease = new String[]{"zes", "xes", "ges"}; 

            for(String y : checkIncrease){
                if(word.contains(y)){
                    count++;
                    break;
                }
            }

        /*
        When there is more than one vowel in a row, each vowel doesn't indicate a new syllable
        Therefore the counter is reduce by 1 when this occurs
        Because there is only some vowels that can occur consecutively we only check for those vowels
        This helps to improve the efficency of the program
        */
        for(int x = 2; x < wordArray.length; x++){
            char first = wordArray[x];
            char second = wordArray[x-1];
            char third = wordArray[x-2];


            if(first == 'i' && second == 'o' && third =='u'){
                count--;
            }
            if(second == 'o' && first == 'u'){
                count--;
            }
            if(second == 'a' && first == 'u'){
                count--;
            }
            if(second == 'a' && first == 'i'){
                count--; 
            }
            if(second == 'a' && first == 'y'){
                count--; 
            }
            if(third == 'q' && vowels.contains(second) && vowels.contains(first) ){
                count--;
            }


        }

        /* divide between two middle consonants 
        When there is a odd number of consonants bewteen two vowels it indicates
        the begining of a new syllable.
        Therefore the counter is increased by 1
        */
        int firstVowelPos = 1000;
        int secondVowelPos = 0;
        for(int y = 0; y < wordArray.length;y+=3){
            for(char c : vowels){
                if(wordArray[y] == c){
                    if(firstVowelPos == 1000){
                        firstVowelPos = y;
                    }else{
                        secondVowelPos = y;
                    }
                }
            }
            if(firstVowelPos+1 != secondVowelPos){
                count++;
            } 
        }

        /* 
        When an -le or a -ys occurs it doesn't start a new syllable
        The counter is reduced by 1 to reflect this
        */
        for(int p = 0; p < wordArray.length-1; p++){
            if(!word.startsWith("le")){
                if(wordArray[p] == 'l' && wordArray[p+1] == 'e' && vowels.contains(wordArray[p-1])){
                    count--;
                if(wordArray[p] == 'l' && wordArray[p+1] == 'e' && !vowels.contains(wordArray[p-1])){
                    count++;
                 }
                }
            }

            if(wordArray[p] == 'y' && wordArray[p+1] == 's' ){
                count--;
            }
        }
        
        count = count/2;

        /* This gives the syllable estimate to the user */
        return count;
    }


    public static void main(String[] args){
        System.out.println("Please enter a word or press control+D to finish: ");
        while(sc.hasNextLine()){
            System.out.println(checkSyllables(sc.nextLine()));
            }
        }
    }

