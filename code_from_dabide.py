{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#get data\n",
    "data = requests.get(\"https://raw.githubusercontent.com/00Dabide/Advent_of_Code_2024/refs/heads/main/Day1/Day1Text.txt\").text.split(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#put pairs to a list\n",
    "for row in range(0,len(data)):\n",
    "    data[row] = data[row].split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "#make two lists for the two rows\n",
    "left_values = []\n",
    "right_values = []\n",
    "\n",
    "for pair in data:\n",
    "    #get the two ID\n",
    "    id1 = int(pair[0])\n",
    "    id2 = int(pair[1])\n",
    "\n",
    "    #put them in the lists\n",
    "    left_values.append(id1)\n",
    "    right_values.append(id2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the counter\n",
    "from collections import Counter\n",
    "\n",
    "#make object\n",
    "right_counter = Counter(right_values)\n",
    "\n",
    "#create empty similarity value list\n",
    "sim_values = []\n",
    "\n",
    "\n",
    "#get the similarity score\n",
    "for value in left_values:\n",
    "    #get the multiplier for the value\n",
    "    mult = right_counter[value]\n",
    "\n",
    "    #calculate the score\n",
    "    sim_score = value * mult\n",
    "\n",
    "    #add to the list\n",
    "    sim_values.append(sim_score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24349736"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#add together\n",
    "sum(sim_values)"
   ]
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
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
