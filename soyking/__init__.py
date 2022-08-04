__version__ = "0.1.2"

from soyking.schemas import input_schema, output_schema
from soyking.action_update_shipping_cost import update_shipping_cost
from soyking.main import solve

actions_config = {
    'Update Shipping Cost': {
        'schema': 'input',
        'engine': update_shipping_cost,
        'tooltip': "Update the shipping cost by the factor entered in the 'Shipping Cost Multiplier' parameter"}
    }
