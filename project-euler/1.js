/* 
Multiples of 3 or 5 | Problem 1 - https://www.freecodecamp.org/learn/project-euler/project-euler-problems-1-to-100/problem-1-multiples-of-3-and-5
     - If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
     - Find the sum of all the multiples of 3 or 5 below 1000. 
     Answer: 233168
 */

function multiplesOf3and5(number) {

     let multiples = [];
     let sum = 0;

     for (let x=0; x<= number-1; x++) {
          if (x % 3 === 0 || x % 5 === 0) {
               multiples.push(x)    
          }
     }
     for (let i = 0; i < multiples.length; i++){
          sum += multiples[i];
     }

     return sum;
}

multiplesOf3and5(1000);