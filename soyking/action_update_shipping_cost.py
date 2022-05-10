from soyking import input_schema


def update_shipping_cost(dat):
    shipping_costs = dat.shipping_costs.copy()
    params = input_schema.create_full_parameters_dict(dat)
    shipping_costs['Cost per ton'] = params['Shipping Cost Multiplier'] * shipping_costs['Cost per ton']
    shipping_costs = shipping_costs.round({'Cost per ton': 1})
    dat.shipping_costs = shipping_costs
    return dat
