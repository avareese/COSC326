#include <iostream> 
#include "Integer.h"
#include "Integer.cpp"
#include "Rational.h"
#include "Rational.cpp"

/** Authors 
 * Ava Reese and Katherine Butt
 * main.cpp
 */

using namespace cosc326;

/** main method to test the program */
int main()
{


    Rational x = Rational("8.5/20");
    Rational y = Rational("5/4"); 
    
    

    std::cout << x * y <<"\n";


    return 0; 
}