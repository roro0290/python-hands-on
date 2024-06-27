{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "72ce7686-eadf-47c2-903b-6123682bc4a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import math"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fdd3aba5-3fb8-455e-be34-c9e96f55607f",
   "metadata": {},
   "source": [
    "# High School Reunion Problem\n",
    "With your high school reunion fast approaching, you decide to get in shape and lose some weight . You record your weight every day for five weeks starting on a Monday.\n",
    "Given these daily weights, build an array with your average weight per weekend (Saturday and Sunday)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1ec108f4-5797-447c-9b4b-11ff86ac6aea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[185.  184.8 184.6 184.4 184.2 184.  183.8 183.6 183.4 183.2 183.  182.8\n",
      " 182.6 182.4 182.2 182.  181.8 181.6 181.4 181.2 181.  180.8 180.6 180.4\n",
      " 180.2 180.  179.8 179.6 179.4 179.2 179.  178.8 178.6 178.4 178.2]\n"
     ]
    }
   ],
   "source": [
    "dailywts = 185 - np.arange(5*7)/5\n",
    "print(dailywts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "20fba433-6ef0-4605-9825-09d14b7d0f2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[183.9 182.5 181.1 179.7 178.3]\n"
     ]
    }
   ],
   "source": [
    "# Use slicing to get the weight for Saturday - 1st sat occurs at index 5, remaining in the array are 7 days later\n",
    "sat = dailywts[5::7]\n",
    "sun = dailywts[6::7]\n",
    "average = (sat+sun)/2\n",
    "print(average)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "febcff62-e03a-4f51-8792-a4ed9754776c",
   "metadata": {},
   "source": [
    "# Nola Problem\n",
    "Make the following 4x7 array called nola that starts with 1 and steps by 2. However, note that the first element in each row is always 4 more than the last element in the previous row."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfefb8e9-3aec-4f90-9d66-c926a62f5a40",
   "metadata": {},
   "source": [
    "## Approach 1 (Mine)\n",
    "Initialise the results array, create the individual arrays and insert it into the results using a for loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "64db79d8-a93e-43fa-bea6-d756f52f2efd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  3  5  7  9 11 13]\n",
      " [17 19 21 23 25 27 29]\n",
      " [33 35 37 39 41 43 45]\n",
      " [49 51 53 55 57 59 61]]\n"
     ]
    }
   ],
   "source": [
    "# by default, it will create with floating point numbers which means there will be a trailing .0\n",
    "# result = np.zeros(shape=(4,7))\n",
    "result = np.zeros(shape=(4,7),dtype=int)\n",
    "index = 0\n",
    "start = 1\n",
    "step = 2\n",
    "for index in range(0,4):\n",
    "    stop = start + 7 * step\n",
    "    array = np.arange(start,stop,step)\n",
    "    result[index] = array\n",
    "    start = stop + 2\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "865398c4-44d2-4be4-b4f6-cfda071c0ecd",
   "metadata": {},
   "source": [
    "## Approach 2\n",
    "The trick here is to think of nola as the first 7 columns in this 4x8 array where we can chop the last to get the (4x7) array\n",
    "```\n",
    "[[ 1  3  5  7  9 11 13 15]\r\n",
    " [17 19 21 23 25 27 2 319]\r\n",
    " [33 35 37 39 41 43  4745]\r\n",
    " [49 51 53 55 57 59 63 6\n",
    "```\n",
    " `nola[:, :-1]` can be interpreted as \"Select every row, and select all columns from the start, up to but excluding the last column\". -1 means \"last\" index. See negative indexing1]]6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2d8ba759-bc87-4f12-b792-1dab50322bd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  3  5  7  9 11 13]\n",
      " [17 19 21 23 25 27 29]\n",
      " [33 35 37 39 41 43 45]\n",
      " [49 51 53 55 57 59 61]]\n"
     ]
    }
   ],
   "source": [
    "# build the sequence array\n",
    "arr = np.arange(start=1,stop=65,step=2)\n",
    "# reshape the 1D array into a 2D array\n",
    "nola = np.reshape(arr,(4,8))\n",
    "# delete the last element == select all the elements but the last\n",
    "nola = nola[:, :-1]\n",
    "print(nola)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20b11330-cf98-48fd-81d9-1f3ae024e2aa",
   "metadata": {},
   "source": [
    "# Gold Miner Problem\n",
    "After binge watching the discovery channel, you ditch your job as a trial lawyer to become a gold miner  . You decide to prospect five locations underneath a 7x7 grid of land. How much gold do you uncover at each location?\n",
    "1. gold states how much gold is under each location in the 7x7 grid of land\n",
    "2. \n",
    "locs states the coordinates of the five locations where you dig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ed57e344-dc2e-42bd-b69a-98bf8c1498d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 3 0 5 2 0 3]\n",
      " [8 8 0 7 1 5 3]\n",
      " [0 1 6 2 1 4 5]\n",
      " [4 0 8 9 9 8 7]\n",
      " [4 2 7 0 7 2 1]\n",
      " [9 8 9 2 5 0 8]\n",
      " [1 9 8 2 6 4 3]]\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "np.random.seed(5555)\n",
    "gold = np.random.randint(low=0, high=10, size=(7,7))\n",
    "\n",
    "print(gold)\n",
    "# [[2 3 0 5 2 0 3]\n",
    "#  [8 8 0 7 1 5 3]\n",
    "#  [0 1 6 2 1 4 5]\n",
    "#  [4 0 8 9 9 8 7]\n",
    "#  [4 2 7 0 7 2 1]\n",
    "#  [9 8 9 2 5 0 8]\n",
    "#  [1 9 8 2 6 4 3]]\n",
    "\n",
    "locs = np.array([\n",
    "    [0,4],\n",
    "    [2,2],\n",
    "    [2,3],\n",
    "    [5,1],\n",
    "    [6,3]\n",
    "])\n",
    "\n",
    "# loop over every array in locs and get the value of gold and add it to the total\n",
    "mined = 0\n",
    "for location in locs:\n",
    "    row = location[0]\n",
    "    col = location[1]\n",
    "    mined += gold[row][col]\n",
    "\n",
    "print(mined)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ebccd43-37cc-4b08-8e23-5cd6663ada56",
   "metadata": {},
   "source": [
    "# Roux Problem\n",
    "Define a  roux array as a 1-D array such that, when it's reversed, it represents the sequence of square numbers 1, 4, 9, 16, ... with 0s interwoven between them. odd-length arrays begin with a square number while even-length arrays begin with a 0. Implement a function called make_roux(n) that inputs n, the desired size of the array, and outputs the corresponding roux array. Then test it on the examples above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "35cd326b-85b7-4bca-916c-f714e413fb7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[9, 0, 4, 0, 1]\n",
      "[0, 16, 0, 9, 0, 4, 0, 1]\n",
      "[0, 36, 0, 25, 0, 16, 0, 9, 0, 4, 0, 1]\n"
     ]
    }
   ],
   "source": [
    "# roux array of length 5 = [9 0 4 0 1]\n",
    "# roux array of length 8 = [0 16  0  9  0  4  0  1]\n",
    "# roux array of length 12 = [0 36  0 25  0 16  0  9  0  4  0  1]\n",
    "def make_roux(n):\n",
    "    roux = [] #initialise an array\n",
    "    i = math.ceil(n/2)\n",
    "    square_num = i * i\n",
    "    while len(roux) < n:\n",
    "        roux.append(square_num)\n",
    "        if(len(roux)<n):\n",
    "            roux.append(0) #append a 0 after appending the squared number all the time\n",
    "        i-=1\n",
    "        square_num = i*i\n",
    "    if(n%2==0): # additional 0 to append for even numbers\n",
    "        roux.insert(0,0)\n",
    "        roux = roux[:n] # to check that roux has exactly n elements\n",
    "    return roux\n",
    "\n",
    "print(make_roux(5))\n",
    "print(make_roux(8))\n",
    "print(make_roux(12))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63814fb6-a7cf-4f7b-af10-f83ecf572219",
   "metadata": {},
   "source": [
    "Source: https://www.practiceprobs.com/problemsets/python-numpy/beginner"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
