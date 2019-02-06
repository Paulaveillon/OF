from openfisca_france import FranceTaxBenefitSystem
tax_benefit_system = FranceTaxBenefitSystem()
scenario = tax_benefit_system.new_scenario()
scenario.init_single_entity(
    period = 2015,
    parent1 = dict(
        age = 30,
        salaire_de_base = 50000,
        ),
    enfants = [
        dict(age = 12),
        dict(age = 18),
        ],
    )
simulation = scenario.new_simulation()

#Some variable can only be computed on a monthly basis
#simulation.calculate('af', '2015')
print(simulation.calculate('af', '2015-01')) #calculate variable af for January 2015
simulation.calculate_add("af", "2015") #to sum on the whole year

#Some variable can only be computed on a anual basis
simulation.calculate('irpp', period = '2015')

scenario.init_single_entity(
    period = 2019,
    parent1 = dict(
        age = 30,
        salaire_de_base = 70000,
        ),
    )
simulation = scenario.new_simulation()

print("Louis")
print(simulation.calculate('irpp',period=2019))

#periods is a particular object and can be "instant" with a unit, a start date and a size
af_april_to_july = simulation.calculate_add(
    'af',
    period = periods.Period(('month', periods.Instant((2014, 3, 1)), 4))
    )
print(af_april_to_july)



#compute the irpp over several years:
# We have to initialise a new scenario
scenario_over_years = tax_benefit_system.new_scenario()
scenario_over_years.init_single_entity(
    period = 'year:2014:3', # three years starting in 2014
    parent1 = dict(
        date_naissance = 1975,
        salaire_de_base = 50000 * 3,
        # Multiplication by 3 is need so salaire de base is 50000 € for each of the three years
        ),
    enfants = [
        dict(date_naissance = 2001),
        dict(date_naissance = 1999),
        ],
    )
simulation_over_years = scenario_over_years.new_simulation()
print(simulation_over_years.calculate('irpp', '2015') + simulation_over_years.calculate('irpp', '2014'))
print(simulation_over_years.calculate_add('irpp', '2014') * 2)
simulation_over_years.calculate_add('af', 'month:2015-01:2')



scenario_over_years = tax_benefit_system.new_scenario()
scenario_over_years.init_single_entity(
    period = 'year:2014:3',
    parent1 = dict(
        date_naissance = 1975,
        salaire_de_base = {
            '2014': 50000,
            '2015': 50500,
            '2016': 51000
            },
        ),
    enfants = [
        dict(date_naissance = 2001),
        dict(date_naissance = 1999),
        ],
    )
simulation_over_years = scenario_over_years.new_simulation()

simulation_over_years.calculate_add('irpp', 'year:2014:3')