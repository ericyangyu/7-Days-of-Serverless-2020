# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
import numpy as np

def _calculate_turkey_brine_equation_and_roast_recommendation(weight: int) -> dict:
    # Generate recommendations for ingredients and brine/roast times with respect to turkey weight
    recommendations = {
        'hours of brine time': 2.4 * weight,
        'minutes of roast time': 15 * weight,
        'cups of salt': 0.05 * weight,
        'gallons of water': 0.66 * weight,
        'cups of brown sugar': 0.13 * weight,
        'shallots': 0.2 * weight,
        'cloves of garlic': 0.4 * weight,
        'tablespoons of whole peppercorns': 0.13 * weight,
        'tablespoons of dried juniper berries': 0.13 * weight,
        'tablespoons of fresh rosemary': 0.13 * weight,
        'tablespoons of thyme': 0.06 * weight
    }

    # Round all our decimal places to 2 decimal places
    recommendations = {key: np.around(value, 2) for key, value in recommendations.items()}

    # Convert dict to pretty string
    recommendations = ', '.join([str(value) + ' ' + key for key, value in recommendations.items()])
    recommendations = f'For a {weight} lb turkey, you want ' + recommendations + '.'

    return recommendations

def main(weight: int) -> str:
    return _calculate_turkey_brine_equation_and_roast_recommendation(weight)
