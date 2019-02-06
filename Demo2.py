from openfisca_france import FranceTaxBenefitSystem
import matplotlib.pylab as plt
import numpy as np
tax_benefit_system = FranceTaxBenefitSystem()

scenario = tax_benefit_system.new_scenario()

scenario.init_single_entity(

    # Axe declaration
    axes=[
        dict(  # in a dictionary
            count=100,  # 'count' : indicates the number of step
            min=0,
            max=100000,
            name='salaire_de_base',  # the variable you want to make evolve
        ),
    ],

    period=2014,
    parent1=dict(
        date_naissance='1980-01-01',
    )
)

simulation = scenario.new_simulation()
simulation.calculate_add('salaire_de_base', 2014)



#income tax
income_tax = - simulation.calculate('irpp', 2014)
gross_wage = simulation.calculate_add('salaire_de_base', 2014)
taxable_income = simulation.calculate_add('salaire_imposable', 2014)

plt.plot(gross_wage,income_tax)
plt.ylabel(u"Tax Income")
plt.xlabel(u"Gross Wage")
plt.show()


#average rate
average_rate = income_tax/gross_wage
average_rate=np.nan_to_num(average_rate)
print(average_rate)

plt.plot(gross_wage, average_rate)
plt.ylabel("Averate Tax Rate")
plt.xlabel("Gross Wage")
plt.show()


#marginal tax rate
marginal_rate =  (income_tax[:-1] - income_tax[1:]) / (taxable_income[:-1] - taxable_income[1:] )
plt.plot(gross_wage[:-1], marginal_rate)
plt.ylabel("Marginal Tax Rate")
plt.xlabel("Gross Wage")
plt.show()

from openfisca_core.rates import average_rate, marginal_rate

#CSG
csg = simulation.calculate_add('csg', period = 2014)
1 - average_rate(-csg[1:], gross_wage[1:])

plt.ylim(0,0.1)
plt.plot(gross_wage[1:], 1-average_rate(-csg[1:], gross_wage[1:]))
plt.show()
