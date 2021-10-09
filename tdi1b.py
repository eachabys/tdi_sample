{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "contained-queens",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from collections import Counter\n",
    "import matplotlib.pylab as plt\n",
    "import numpy as np\n",
    "\n",
    "df= pd.read_csv('RAW_recipes.csv')\n",
    "timer=df.minutes\n",
    "ingred=df.n_ingredients\n",
    "#analyze whats the distribution of time to cook \n",
    "ingr_count=Counter(ingred)\n",
    "d1=ingr_count.items()\n",
    "\n",
    "total_quantity=np.array([x[1] for x in d1])\n",
    "i_quantity=np.array([x[0] for x in d1])\n",
    "fig = plt.figure()\n",
    "ax = fig.add_subplot(111)\n",
    "#show distribution of how many recipes depending on how many ingredients\n",
    "ax.plot(i_quantity,total_quantity,'o')\n",
    "plt.show()"
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
