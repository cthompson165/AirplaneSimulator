from physics.vector_2d import Vector2D
from flight.flying_object import FlyingObject


class Airplane(FlyingObject):

    def __init__(self, initial_state, mass,
                 mass_moment_of_inertia, atmosphere):

        FlyingObject.__init__(
            self, mass, mass_moment_of_inertia,
            initial_state, atmosphere)

    def apply_pitch_control(self, percent):
        raise NotImplementedError

    def set_throttle(self, percent):
        if self.engines() is not None:
            for engine in self.engines():
                engine.set_throttle(percent)

    def calculate_thrust_forces(self):
        thrust_forces = []
        if self.engines() is not None:
            for engine in self.engines():
                thrust_forces.append(engine.get_thrust())
        self.add_local_forces(thrust_forces)

    def engines(self):
        raise NotImplementedError

    def surfaces(self):
        raise NotImplementedError

    def cg(self):
        return Vector2D(0, 0)
