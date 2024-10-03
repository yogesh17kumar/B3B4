{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5888d3fb-878c-4028-bec1-19b5c2a68652",
   "metadata": {},
   "outputs": [],
   "source": [
    "def showDetails(*args):\n",
    "    for i in range(len(args)):\n",
    "        variable = args[i]\n",
    "        print(f\"The Value of { i+1 } variable is \\t{variable }\\t its id is \\t {id(variable)}\")\n",
    "    \n",
    "    print(\"\\n\\n\")"
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
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
