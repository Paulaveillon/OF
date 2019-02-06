
import openfisca_france
from openfisca_france.reforms import landais_piketty_saez
from reforme_parametrique import MaReforme



# Consultez la situation actuelle
legislation_france = openfisca_france.FranceTaxBenefitSystem()

resultat_actuel = legislation_france.parameters.impot_revenu.bareme[1].rate

print("Résultat actuel")
print(resultat_actuel)

# Consultez la situation avec la reforme
legislation_reforme = MaReforme(legislation_france)

resultat_apres_reforme = legislation_reforme.parameters.impot_revenu.bareme[1].rate

print("Resultat après reforme")
print(resultat_apres_reforme)


#Create a new scenario

scenario = legislation_france.new_scenario()
scenario.init_single_entity(
    period = 2015,
    parent1 = dict(
        age = 30,
        salaire_de_base = 20000,
        ),
    enfants = [
        dict(age = 12),
        dict(age = 18),
        ],
    )

simulation = scenario.new_simulation()
print(simulation.calculate('af', '2015-01'))


#New reform from pour une révolution fiscale
reform = landais_piketty_saez.landais_piketty_saez(legislation_france)

def init_profile(scenario):
    scenario.init_single_entity(
        period = '2013',
        parent1 = dict(
            age = 40,
            salaire_de_base = 50000,
            ),
        )
    return scenario

# Indicate that you want to perfom the reform on this scenario
reform_scenario = init_profile(reform.new_scenario())

#Simulate the reform
reform_simulation = reform_scenario.new_simulation()

# Choose the variable you want to calcul : here the disposable income, "revenu_disponible"
print(reform_simulation.calculate('revenu_disponible', '2013'))

# Indicate that you want to perfom the standard system on this scenario
baseline_scenario = init_profile(legislation_france.new_scenario())

# Simulate the standard scenario
baseline_simulation = baseline_scenario.new_simulation()



# Choose the variable you want to calcul
print(baseline_simulation.calculate('revenu_disponible', '2013'))