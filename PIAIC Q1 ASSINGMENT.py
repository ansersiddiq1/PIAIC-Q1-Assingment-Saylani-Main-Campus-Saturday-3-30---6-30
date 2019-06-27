{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ANSER SIDDIQ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Radius Of Circle: 0.5\n",
      "The Area Of Circle is : 0.7853981635\n"
     ]
    }
   ],
   "source": [
    "#calculate Area of circle..\n",
    "pi= 22/7\n",
    "radius=float(input(\"Enter Radius Of Circle: \"))\n",
    "area = pi*(radius**2)\n",
    "print(\"The Area Of Circle is :\",area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number: 25\n",
      "The Entered Number is Positive\n"
     ]
    }
   ],
   "source": [
    "#Find The Number is Negative or Positive or Zero..\n",
    "enter_number = int(input(\"Enter number: \"))\n",
    "if enter_number > 0:\n",
    "    print(\"The Entered Number is Positive\")\n",
    "elif enter_number < 0:\n",
    "    print(\"The Entered Number is Negative\")\n",
    "elif enter_number == 0:\n",
    "    print(\"The Entered Number is zero\")\n",
    "else:\n",
    "    print(\"Error\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter First Number: 4\n",
      "Enter Second Number: 2\n",
      "4.0 Number is completely divided by 2.0\n"
     ]
    }
   ],
   "source": [
    "#Check The Divisibility Of A Number..\n",
    "num1=float(input(\"Enter First Number: \"))\n",
    "num2=float(input(\"Enter Second Number: \"))\n",
    "\n",
    "if(num1 % num2 == 0):\n",
    "    print(num1 , \"Number is completely divided by\" , num2)\n",
    "else:\n",
    "    print(num1 , \"Number is not completely divided by\" , num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter radius of sphere: 1\n",
      "The volume of sphere:  4.189333333333333\n"
     ]
    }
   ],
   "source": [
    "#Calculate Volume Of Sphere..\n",
    "pi = 3.142\n",
    "radius = float(input(\"Enter radius of sphere: \"))\n",
    "volume = (4/3)*pi*(radius**3)\n",
    "print(\"The volume of sphere is: \", volume )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a date in (dd/mm/yy) format: 11/06/1999\n",
      "Enter a date in (dd/mm/yy) format: 27/06/2019\n",
      "There are 7321 days in between 11/06/1999 and 27/06/2019\n"
     ]
    }
   ],
   "source": [
    "#Calucalte Days..\n",
    "from datetime import datetime\n",
    "date_format = \"%d/%m/%Y\"\n",
    "date1 = input(\"Enter a date in (dd/mm/yy) format: \")\n",
    "date2 = input(\"Enter a date in (dd/mm/yy) format: \")\n",
    "a= datetime.strptime( date1 , date_format)\n",
    "b = datetime.strptime( date2 , date_format)\n",
    "change = b - a\n",
    "print (\"There are\", change.days, \"days in between\", date1 , \"and\" , date2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter String hi\n",
      "Enter How Many Times You Want To Copy.. 4\n",
      "hihihihi\n"
     ]
    }
   ],
   "source": [
    "#Copy Strings Nth Times..\n",
    "var = input(\"Enter String \")\n",
    "no_of_times = int(input(\"Enter How Many Times You Want To Copy.. \"))\n",
    "copy = var * no_of_times\n",
    "print(copy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Number:4\n",
      "4  is Even Number \n"
     ]
    }
   ],
   "source": [
    "#Check if number is Even or Odd..\n",
    "num = int(input(\"Enter Number:\"))\n",
    "if(num % 2 == 0):\n",
    "    print(num , \" is Even Number \")\n",
    "else:\n",
    "    print(num, \" is Odd Number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a Alphabet: A\n",
      "Given Alphabet is Consonant  A\n"
     ]
    }
   ],
   "source": [
    "#Check Whether give alphabet is vowel or not..\n",
    "var = input(\"Enter a Alphabet: \")\n",
    "if(var ==  (\"A\", \"E\", \"I\", \"O\", \"U\", \"a\", \"e\", \"i\", \"o\", \"u\")):\n",
    "    print(\"Given Alphabet is Vowel \", var)\n",
    "else:\n",
    "    print(\"Given Alphabet is Consonant \", var)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Base of Triangle: 4\n",
      "Enter Height of Triangle: 4\n",
      "Area of a Triangle is : 8.0\n"
     ]
    }
   ],
   "source": [
    "#Calculate Area of Triangle..\n",
    "base = float(input(\"Enter Base of Triangle: \"))\n",
    "height = float(input(\"Enter Height of Triangle: \"))\n",
    "Area = (1/2)* base* height\n",
    "print(\"Area of a Triangle is :\", Area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please Enter Principal Amount: 1\n",
      "Please Enter Rate of Interest in % :1\n",
      "Enter Number of years for Investment: 1\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'interst_rate' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-20-1cb317238189>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mvalue\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mamount\u001b[0m\u001b[1;33m*\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0.01\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0minterest_rate\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m**\u001b[0m \u001b[0myears\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"After{years} years your principal amount{amount} over an interest rate of{interst_rate} % will be: \"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'interst_rate' is not defined"
     ]
    }
   ],
   "source": [
    "#Calculate Interst Rate..\n",
    "amount = float(input(\"Please Enter Principal Amount: \"))\n",
    "interest_rate = float(input(\"Please Enter Rate of Interest in % :\"))\n",
    "years = float(input(\"Enter Number of years for Investment: \"))\n",
    "\n",
    "value = amount*((1+(0.01*interest_rate)) ** years)\n",
    "print(f\"After{years} years your principal amount{amount} over an interest rate of{interst_rate} % will be: \", value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Co-ordinate for x1: 2\n",
      "Enter Co-ordinate for x2: 4\n",
      "Enter Co-ordinate for y1: 4\n",
      "Enter Co-ordinate for y2: 4\n",
      "Distance between points 2.0\n"
     ]
    }
   ],
   "source": [
    "#calculate Euclidean Distance..\n",
    "import math\n",
    "\n",
    "x1 = int(input(\"Enter Co-ordinate for x1: \"))\n",
    "x2 = int(input(\"Enter Co-ordinate for x2: \"))\n",
    "y1 = int(input(\"Enter Co-ordinate for y1: \"))\n",
    "y2 = int(input(\"Enter Co-ordinate for y2: \"))\n",
    "euclidean_Distance = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))\n",
    "print(\"Distance between points\", euclidean_Distance)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input your height in Feet: 5\n",
      "5.0 Feet into Centimeter is  152.4\n"
     ]
    }
   ],
   "source": [
    "#Feet To Centimeter conversion..\n",
    "feet = float(input(\"Input your height in Feet: \"))\n",
    "centi = feet * 30.48\n",
    "\n",
    "print(f\"{feet} Feet into Centimeter is \",centi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your Height in Centimeter: 180\n",
      "Enter Your Weight in Kilogram: 75\n",
      "Your BMI is:  23.148148148148145\n"
     ]
    }
   ],
   "source": [
    "#BMI ...\n",
    "height = float(input(\"Enter Your Height in Centimeter: \"))\n",
    "weight = float(input(\"Enter Your Weight in Kilogram: \"))\n",
    "BMI= weight / ((height/100)**2)\n",
    "print(\"Your BMI is: \", BMI)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter value of n: 5\n",
      "Sum of n Integers is  15.0\n"
     ]
    }
   ],
   "source": [
    "#Sum of n Positive Integers..\n",
    "num = int(input(\"Enter value of n: \"))\n",
    "sum_num = (num * (num + 1)) / 2\n",
    "print(\"Sum of n Integers is \",sum_num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input a four digit numbers: 1234\n",
      "The sum of four numbers is  10\n"
     ]
    }
   ],
   "source": [
    "#Digits sum of numbers..\n",
    "num = int(input(\"Input a four digit numbers: \"))\n",
    "x = num //1000\n",
    "num1 = (num - x*1000)//100\n",
    "num2 = (num - x*1000 - num1*100)//10\n",
    "num3 = num - x*1000 - num1*100 - num2*10\n",
    "sum_of_num = x + num1 + num2 + num3\n",
    "print(\"The sum of four numbers is \", sum_of_num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter decimal number: 5\n",
      "The binary no. for 5 is 0101\n"
     ]
    }
   ],
   "source": [
    "#Decimal to Binary Converter..\n",
    "n=int(input('Enter decimal number: '))\n",
    "x=n\n",
    "k=[]\n",
    "while (n>0):\n",
    "    a=int(float(n%2))\n",
    "    k.append(a)\n",
    "    n=(n-a)/2\n",
    "k.append(0)\n",
    "string=\"\"\n",
    "for j in k[::-1]:\n",
    "    string=string+str(j)\n",
    "print('The binary no. for %d is %s'%(x, string))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a Binary number: 0101\n",
      "Decimal digit is 5\n"
     ]
    }
   ],
   "source": [
    "#Binary To Decimal Converter..\n",
    "bin_num = list(input(\"Enter a Binary number: \"))\n",
    "value = 0\n",
    "\n",
    "for i in range(len(bin_num)):\n",
    "    digit = bin_num.pop()\n",
    "    if digit == '1':\n",
    "        value = value + pow(2, i)\n",
    "print(f\"Decimal digit is\", value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter text: anser siddiq\n",
      "Total Number of Vowels in this String are  4\n",
      "Total Number of Consonants in this String are  8\n"
     ]
    }
   ],
   "source": [
    "#Vowel and Consonants Counter..\n",
    "text = input(\"Enter text: \")\n",
    "vowels = 0\n",
    "consonants = 0\n",
    "\n",
    "for i in text:\n",
    "    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'\n",
    "       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):\n",
    "        vowels = vowels + 1\n",
    "    else:\n",
    "        consonants = consonants + 1\n",
    "print(\"Total Number of Vowels in this String are \", vowels)\n",
    "print(\"Total Number of Consonants in this String are \", consonants)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter String to check Palindrome:Anser\n",
      "Not a Palindrome.\n"
     ]
    }
   ],
   "source": [
    "#Palindrome tester..\n",
    "Value = str(input(\"Enter String to check Palindrome:\"))\n",
    "Value = Value.casefold()\n",
    "\n",
    "Rev_Value = reversed(Value)\n",
    "\n",
    "if(list(Value) == list(Rev_Value)):\n",
    "    print(\"It is palindrome.\")\n",
    "else:\n",
    "    print(\"Not a Palindrome.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter String: ansersiddiq1@gmail.com\n",
      "\n",
      "Alphabets :   19\n",
      "Numbers :   1\n",
      "Spaces : 0\n",
      "Special Characters :  2\n"
     ]
    }
   ],
   "source": [
    "#Alphabet, Space, Digit and special character teseter...\n",
    "string = input(\"Enter String: \")\n",
    "dig=alpha=space=special=0\n",
    "for i in string:\n",
    "    if i.isdigit():\n",
    "        dig=dig+1\n",
    "    elif i.isalpha():\n",
    "        alpha=alpha+1\n",
    "    elif i.isspace():\n",
    "        space=space+1\n",
    "    else:\n",
    "        special=special+1\n",
    "print(\"\\nAlphabets :  \", alpha)\n",
    "print(\"Numbers :  \", dig)\n",
    "print(\"Spaces :\", space)\n",
    "print(\"Special Characters : \", special)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter value: 10\n",
      "\n",
      "* \n",
      "* * \n",
      "* * * \n",
      "* * * * \n",
      "* * * * * \n",
      "* * * * * * \n",
      "* * * * * * * \n",
      "* * * * * * * * \n",
      "* * * * * * * * * \n",
      "* * * * * * * * * * \n",
      "* * * * * * * * * \n",
      "* * * * * * * * \n",
      "* * * * * * * \n",
      "* * * * * * \n",
      "* * * * * \n",
      "* * * * \n",
      "* * * \n",
      "* * \n",
      "* \n"
     ]
    }
   ],
   "source": [
    "#pattern 1:\n",
    "n=int(input(\"Enter value: \"))\n",
    "for i in range(n):\n",
    "    for j in range(i):\n",
    "        print ('* ', end=\"\")\n",
    "    print('')\n",
    "\n",
    "for i in range(n,0,-1):\n",
    "    for j in range(i):\n",
    "        print('* ', end=\"\")\n",
    "    print('')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Value: 9\n",
      "1  \n",
      "1  2  \n",
      "1  2  3  \n",
      "1  2  3  4  \n",
      "1  2  3  4  5  \n",
      "1  2  3  4  5  6  \n",
      "1  2  3  4  5  6  7  \n",
      "1  2  3  4  5  6  7  8  \n",
      "1  2  3  4  5  6  7  8  9  \n",
      "1  2  3  4  5  6  7  8  \n",
      "1  2  3  4  5  6  7  \n",
      "1  2  3  4  5  6  \n",
      "1  2  3  4  5  \n",
      "1  2  3  4  \n",
      "1  2  3  \n",
      "1  2  \n",
      "1  \n"
     ]
    }
   ],
   "source": [
    "#pattern 2:\n",
    "n = int(input(\"Enter Value: \"))\n",
    "for i in range(1,n):\n",
    "    for j in range(1,i+1):\n",
    "        print(j,\" \",end=\"\")\n",
    "    print()\n",
    "for i in range(n,0,-1):\n",
    "    for j in range(1,i+1):\n",
    "        print(j,\" \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number of row: 9\n",
      "1  \n",
      "2  2  \n",
      "3  3  3  \n",
      "4  4  4  4  \n",
      "5  5  5  5  5  \n",
      "6  6  6  6  6  6  \n",
      "7  7  7  7  7  7  7  \n",
      "8  8  8  8  8  8  8  8  \n",
      "9  9  9  9  9  9  9  9  9  \n"
     ]
    }
   ],
   "source": [
    "#pattern 3:\n",
    "n=int(input(\"Enter Value: \"))\n",
    "count=1\n",
    "for row in range(1,n+1):\n",
    "    for col in range(1,row+count):\n",
    "        print(row ,\" \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
