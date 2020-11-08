# Day 1 of Serverless: Turkey Brine

Authors: Eric Yang Yu

## Description

This program simply recommends an amount of ingredients to use and time to brine/roast turkey given the weight of the turkey in pounds. It follows these ratios:

Brine time (in hours) = 2.4 * lbs of turkey
 
Salt (in cups) = 0.05 * lbs of turkey
 
Water (gallons) = 0.66 * lbs of turkey
 
Brown sugar (cups) = 0.13 * lbs of turkey
 
Shallots = 0.2 * lbs of turkey
 
Cloves of garlic = 0.4 * lbs of turkey
 
Whole peppercorns (tablespoons) = 0.13 * lbs of turkey
 
Dried juniper berries (tablespoons) = 0.13 * lbs of turkey
 
Fresh rosemary (tablespoons) = 0.13 * lbs of turkey
 
Thyme (tablespoons) = 0.06 * lbs of turkey
 
Roast time (in minutes) = 15 * lbs of turkey

## Usage
1. To run the program (only tested on Mac):
```
click F5 or run program in debug
```

2. Then, paste the HttpStart URL from terminal to browser, replacing `{functionName}` with `TurkeyOrchestrator`. Here's a sample URL:
```
http://localhost:7071/api/orchestrators/TurkeyOrchestrator
```

3. Open up the URL associated with `statusQueryGetUri` in a new window.

4. Look at the value under `output`