class SimulatedEntity:
    """
    A simulatedEntity keeps track of the simulation object, where you can access all the parameters
    of the simulation. No class of this type is directly instantiable.
    """
    def __init__(self, simulator):

        self.simulator = simulator


class Entity(SimulatedEntity):
    """
    The class Entity represents everything in the environment, for instance
    Drones, Events, Packets, etc... It extends SimulatedEntity.
    """

    def __init__(self,  simulator, identifier: int, coordinates: tuple):
        super().__init__(simulator=simulator)

        self.identifier = identifier     # the id of the entity
        self.coordinates = coordinates   # the coordinates of the entity on the map

    def __eq__(self, other):
        """
        Entity objects are uniquely identified by their identifier
        """
        if not isinstance(other, Entity):
            return False
        else:
            return other.identifier == self.identifier

    def __hash__(self):
        """
        The hash function is applied to the identifier and the current coordinates
        """
        return hash((self.identifier, self.coordinates))


# ------------------ Environment ----------------------
class Environment(SimulatedEntity):
    """ The enviromnet is an entity that represents the area of interest on which events are generated.
     WARNING this corresponds to an old view we had, according to which the events are generated on the map at
     random and then maybe felt from the drones. Now events are generated on the drones that they feel with
     a certain probability."""

    def __init__(self, simulator,  width, height):
        super().__init__(simulator)

        self.width = width
        self.height = height
        self.__drones = None
        self.__depot = None

        #self.event_generator = EventGenerator(height, width, simulator) %EventGenerator is not used
        self.active_events = []

    @property
    def drones(self):
        """

        @return:
        """

        return self.__drones

    @drones.setter
    def drones(self, drones: list):
        """

        @param drones:
        @return:
        """
        self.__drones = drones

    @property
    def depot(self):
        """

        @return:
        """

        return self.__depot

    @depot.setter
    def depot(self, depot):
        """

        @param depot:
        @return:
        """
        self.__depot = depot


# class EventGenerator(SimulatedEntity):
#     # Not used
#     def __init__(self, height, width, simulator):
#
#         super().__init__(simulator)
#         self.DISTRIBUTIONS = ["uniform", "poisson"]
#         self.height = height
#         self.width = width
#
#     def generate_event(self, distribution: str):
#         "This "
#         assert distribution in self.DISTRIBUTIONS
#         if distribution == "uniform": return self.uniform_event_generator()
#         elif distribution == "poisson": return self.poisson_event_generator()
#
#     def uniform_event_generator(self):
#         """ generates an event in the map """
#         x = self.simulator.rnd_env.randint(0, self.height)
#         y = self.simulator.rnd_env.randint(0, self.width)
#         return x, y
#
#     def poisson_event_generator(self):
#         """ generates an event in the map """
#         pass
