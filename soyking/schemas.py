"""
Defines the input and output schemas of the SoyKing problem
"""

from ticdat import PanDatFactory

# region INPUT SCHEMA
input_schema = PanDatFactory(
    # syntax: table_name=[['Primary Key One', 'Primary Key Two'], ['Data Field One', 'Data Field Two']]
    parameters=[['Name'], ['Value']],
    suppliers=[['Farm ID'], ['Availability']],
    demands=[['DC ID'], ['Demand']],
    shipping_costs=[['Farm ID', 'DC ID'], ['Cost Per Ton']])
# endregion

# region USER PARAMETERS
input_schema.add_parameter('Shipping Cost Multiplier', default_value=1.5, number_allowed=True, strings_allowed=(),
                           must_be_int=False, min=0.0, inclusive_min=True, max=10, inclusive_max=True)
input_schema.add_parameter('Time Limit', default_value=120, number_allowed=True, strings_allowed=(),
                           must_be_int=False, min=0.0, inclusive_min=True, max=1*60**2, inclusive_max=True)
input_schema.add_parameter('MIP Gap', default_value=0.01, number_allowed=True, strings_allowed=(),
                           min=0, inclusive_min=False, max=1, inclusive_max=False)
# endregion

# region OUTPUT SCHEMA
output_schema = PanDatFactory(
    ship_flow=[['Farm ID', 'DC ID'], ['Shipped Tons']])
# endregion

# region DATA TYPES AND PREDICATES - INPUT SCHEMA
# region suppliers
table = 'suppliers'
input_schema.set_data_type(table=table, field='Farm ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Availability', number_allowed=True, strings_allowed=(),
                           min=0, inclusive_min=True, max=float('inf'), inclusive_max=False)
# endregion
# region demands
table = 'demands'
input_schema.set_data_type(table=table, field='DC ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Demand', number_allowed=True, strings_allowed=(),
                           min=0, inclusive_min=True, max=float('inf'), inclusive_max=False, nullable=False)
# endregion
# region shipping_costs
table = 'shipping_costs'
for field in ['Farm ID', 'DC ID']:
    input_schema.set_data_type(table=table, field=field, number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Cost Per Ton', number_allowed=True, strings_allowed=(),
                           min=0, inclusive_min=True, max=float('inf'), inclusive_max=False)
input_schema.add_foreign_key(native_table='shipping_costs', foreign_table='suppliers',
                             mappings=('Farm ID', 'Farm ID'))
input_schema.add_foreign_key(native_table='shipping_costs', foreign_table='demands',
                             mappings=('DC ID', 'DC ID'))
# endregion
# endregion

# region DATA TYPES AND PREDICATES - OUTPUT SCHEMA
# region ship
table = 'ship_flow'
output_schema.set_data_type(table=table, field='Farm ID', number_allowed=False, strings_allowed='*')
output_schema.set_data_type(table=table, field='DC ID', number_allowed=False, strings_allowed='*')
output_schema.set_data_type(table=table, field='Shipped Tons', number_allowed=True, strings_allowed=(),
                            min=0, inclusive_min=True, max=float('inf'), inclusive_max=False)
# endregion

# endregion
