import json
import argparse
from classes.zone import *
from classes.agent import *
from classes.position import *
from classes.agreeablenessGraph import *
from classes.incomeGraph import *


def main():
    # Si on avait mis tout ça en bas, on aurait eu beaucoup de variables globales.
    parser = argparse.ArgumentParser("Display population stats")
    parser.add_argument("src", help="Path to source json agents file")
    args = parser.parse_args()

    # Load agents
    for agent_properties in json.load(open(args.src)):
        longitude = agent_properties.pop('longitude')
        latitude = agent_properties.pop('latitude')
        # store agent position in radians
        position = Position(longitude, latitude)

        zone = Zone.find_zone_that_contains(position)
        agent = Agent(position, **agent_properties)
        zone.add_inhabitant(agent)

    agreeableness_graph = AgreeablenessGraph()
    agreeableness_graph.show(Zone.ZONES)

    income_graph = IncomeGraph()
    income_graph.show(Zone.ZONES)


if __name__ == "__main__":
    main()
