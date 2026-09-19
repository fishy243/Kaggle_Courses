"""
Question 1¶
You work at a college admissions office. When inspecting a dataset of
 college applicants, you notice that some students have represented
   their grades with letters ("A", "B", "C", "D", "F"), whereas 
   others have represented their grades with a number between 0 
   and 100.

You realize that for consistency, all of the grades should be 
formatted in the same way, and you decide to format them all as 
letters. For the conversion, you decide to assign:

"A" - any grade 90-100, inclusive
"B" - any grade 80-89, inclusive
"C" - any grade 70-79, inclusive
"D" - any grade 60-69, inclusive
"F" - any grade <60
Write a function get_grade() that takes as input:

score - an integer 0-100 corresponding to a numerical grade
It should return a Python string with the letter grade that it 
corresponds to. For instance,

A score of 85 corresponds to a B grade. In other words, 
get_grade(85) should return "B".
A score of 49 corresponds to an F grade. In other words, 
get_grade(49) should return "F".
Make sure that when supplying the grade that is returned by 
the function, it is enclosed in quotes. (For instance, if you 
want to return "A", you should write return "A" and not return A.)

"""

# TODO: Edit the function to return the correct grade for different 
# scores
def get_grade(score):
    # Grade Student Received
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C" 
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

print(get_grade(85)) # "B"

"""
Question 2¶
In the exercise for the previous lesson, you wrote a function 
cost_of_project() that estimated the price of rings for an online 
shop that sells rings with custom engravings. This function did not 
use conditional statements. In this exercise, you will rewrite the 
function to use conditional statements. Recall that the online shop 
has the following price structure:

Gold plated rings have a base cost of $50, and you charge $7 per 
engraved unit.
Solid gold rings have a base cost of $100, and you charge $10 per 
engraved unit.
Spaces and punctuation are counted as engraved units.
Your function cost_of_project() takes two arguments:

engraving - a Python string with the text of the engraving
solid_gold - a Boolean that indicates whether the ring is solid 
gold
It should return the cost of the project.

The function has been partially completed for you, and you need to 
fill in the blanks to complete the function.

"""

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = len(engraving) * 10 + 100
    else:
        cost = len(engraving) * 7 + 50
    return cost

def get_expected_cost(beds, baths, has_basement):
    value = 80000 + 30000 * beds + 10000 * baths + 40000 * has_basement
    value
    return value

# Corrected:
def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (len(engraving) * 10 + 100) + (not solid_gold) * (len(engraving) * 7 + 50)
    return cost

"""
Question 3¶
You are a programmer at a water agency. Recently, you have been tasked to 
write a function get_water_bill() that takes as input:

num_gallons = the number of gallons of water that a customer used that month.
(This will always be an integer with no decimal part.)
It should output the water bill.

The water agency uses this pricing structure:

Tier	Amount in gallons	Price per 1000 gallons
Tier 1	0 - 8,000	$5
Tier 2	8,001 - 22,000	$6
Tier 3	22,001 - 30,000	$7
Tier 4	30,001+	$10
For example:

Someone who uses 10,000 gallons of water in a month is placed in Tier 2, and 
needs to pay a water bill of $6 * 10 = $60. 

In other words, 
get_water_bill(10000) should return 60.0.
Someone who uses 25,000 gallons of water in a month is placed in Tier 3, and 
needs to pay a water bill of $7 * 25 = $175. 

In other words, 
get_water_bill(25000) should return 175.0.
Do not round your answer. So, your answer might return fractions of a penny.
"""

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = num_gallons * 5 / 1000
    elif num_gallons <= 22000:
        bill = num_gallons * 6 / 1000
    elif num_gallons <= 30000:
        bill = num_gallons * 7 / 1000
    else:
        bill = num_gallons * 10 / 1000
    return bill

"""
Question 4
You work for a company that provides data services. 
For $100/month, your company provides 15 gigabytes (GB) of data. 
Then, any additional data is billed at $0.10/MB (or $100/GB, 
since 1,000 MB are in 1 GB).

Use the next code cell to write a function get_phone_bill() that takes as 
input:

gb = number of GB that the customer used in a month
It should return the customer's total phone bill.

For instance:

A customer who uses 10 GB of data in one month is billed only $100, 
since the usage stayed under 15 GB. In other words, get_phone_bill(10) 
should return 100.
A customer who uses 15.1 GB (or 15 GB + 100 MB) of data in one month has 
gone over by .1 GB, so they must pay $100 (cost of plan), 
plus $0.10 * 100 = $10, for a total bill of $110. In other words,
get_phone_bill(15.1) should return 110.
Do not round your answer.
"""

def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = 100 + (gb - 15) * 100
    return bill

"""
🌶️ Question 5
In Mexico, foods and beverages that are high in saturated fat, trans fat, 
sugar, sodium, and/or calories appear with warning labels that are designed 
to help consumers make healthy food choices.

For instance, the box of cookies in the image below appears with two labels 
(in the upper right corner):

EXCESO CALORÍAS (in English, EXCESS CALORIES)
EXCESO AZÚCARES (in English, EXCESS SUGAR)
drawing

In this question, you'll work with a function get_labels() that takes the 
nutritional details about a food item and prints the needed warning labels. 
This function takes several inputs:

food_type = one of "solid" or "liquid"
serving_size = size of one serving (if solid, in grams; if liquid, 
in milliliters)
calories_per_serving = calories in one serving
saturated_fat_g = grams of saturated fat in one serving
trans_fat_g = grams of trans fat in one serving
sodium_mg = mg of sodium in one serving
sugars_g = grams of sugar in one serving
Note that some of the code here should feel unfamiliar to you, since we have not shared the details of how some of the functions like excess_sugar() or excess_saturated_fat() work. But at a high level, these are functions that return a value of True if the food is deemed to have an excess of sugar or saturated fat, respectively. These functions are used within the get_labels() function, and whenever there is an excess (of sugar or saturated fat, but also of trans fat, sodium, or calories), it prints the corresponding label.
"""

# Define the helper functions locally so this file does not depend on Kaggle's
# optional learntools package.
def excess_sugar(sugars_g, calories_per_serving):
    return sugars_g * 4 >= calories_per_serving * 0.10


def excess_saturated_fat(saturated_fat_g, calories_per_serving):
    return saturated_fat_g * 9 >= calories_per_serving * 0.10


def excess_trans_fat(trans_fat_g, calories_per_serving):
    return trans_fat_g * 9 >= calories_per_serving * 0.01


def excess_sodium(calories_per_serving, sodium_mg):
    return sodium_mg >= calories_per_serving


def excess_calories(food_type, calories_per_serving, serving_size):
    limit = 275 if food_type == "solid" else 70
    return calories_per_serving / serving_size * 100 >= limit

def get_labels(food_type, serving_size, calories_per_serving, saturated_fat_g, trans_fat_g, sodium_mg, sugars_g):
    # Print messages based on findings
    if excess_sugar(sugars_g, calories_per_serving) == True:
        print("EXCESO AZÚCARES / EXCESS SUGAR")
    if excess_saturated_fat(saturated_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT")
    if excess_trans_fat(trans_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS TRANS / EXCESS TRANS FAT")
    if excess_sodium(calories_per_serving, sodium_mg) == True:
        print("EXCESO SODIO / EXCESS SODIUM")
    if excess_calories(food_type, calories_per_serving, serving_size) == True:
        print("EXCESO CALORÍAS / EXCESS CALORIES")

"""
The next code cell demonstrates how to use `get_labels()` to get the warning 
labels that the food item should contain.  We begin with
 [bologna](https://world.openfoodfacts.org/product/4099100179378/bologna).  
 Here is [an image](https://storage.googleapis.com/kaggle-media/learn/images/Cfcx72e.png)
 with all of the nutritional information.  
 
 Note that for this food,
- `food_type = "solid"` (because bologna is a solid and not a liquid)
- `serving_size = 32` (the serving size is 32 grams)
- `calories_per_serving = 110` (there are 110 calories per serving)
- `saturated_fat_g = 2.5` (there are 2.5 grams of saturated fat per serving)
- `trans_fat_g = 0` (there are 0 grams of trans fat per serving)
- `sodium_mg = 400` (there are 400 mg of sodium per serving)
- `sugars_g = 1` (the nutrition facts say <1g, but we will round it up to 1 gram per serving to be safe)

By supplying all of these values to the function, we can print the warning labels.
"""

get_labels("solid",
           32, # serving size in grams
           110, # calories per serving
           2.5, # saturated fat in grams
           0, # trans fat in grams
           sodium_mg = 400, # sodium per serving in mg
           sugars_g = 1 # sugar in grams
)

"""
This bologna has three labels, printed in the output above.

For the rest of this question, you will use the same get_labels() function to 
determine the labels for more foods. This question is designed to help you 
get practice with feeling comfortable with code that other people have written, 
and where you don't have time to review every single line of code before 
interacting with it. For instance, when you take the Intro to Machine Learning 
course, you'll work with a Python package called "scikit-learn", which is a 
large collection of code that you'll learn how to run without reviewing all of the code in detail 
(as it would take too long, and you can trust that it was implemented correctly).

In general, as you continue coding in Python, you will often be running code that other people have written. 
This is common practice for advanced programmers.

In the next code cell, fill in the values for this cereal. Here is an image with all of the nutritional 
information.

Note: running the line of code below as-is will return an error. You have to fill in the nutritional values first.
"""

# Cereal: [Kellogg's Corn Flakes](https://world.openfoodfacts.org/product/0038000015035/kellogg-s-corn-flakes)
get_labels("solid",
           40, # grams per cup
           150, # calories per serving
           0, # saturated fat in grams
           0, # trans fat in grams
           sodium_mg = 150, # sodium per serving in mg
           sugars_g = 12 # sugar in grams
)

# mozzarella sticks https://world-es.openfoodfacts.org/producto/0062325540104/mozzarella-cheese-sticks

get_labels("solid",
           21, # grams per stick
           68, # calories per serving
           3.0, # saturated fat in grams
           0.2, # trans fat in grams
           sodium_mg = 208, # sodium per serving in mg
           sugars_g = 0 # sugar in grams
)
