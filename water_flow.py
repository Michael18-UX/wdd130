# water_flow.py

WATER_DENSITY = 998.2
GRAVITY = 9.80665
WATER_VISCOSITY = 0.0010016


def water_column_height(tower_height, tank_height):
    """
    Calculate the height of the water column.

    Formula:
    h = t + (3w / 4)
    """
    return tower_height + (3 * tank_height / 4)


def pressure_gain_from_water_height(height):
    """
    Calculate pressure gain from water height.

    Formula:
    P = (ρgh) / 1000
    """
    return (WATER_DENSITY * GRAVITY * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length,
                            friction_factor, fluid_velocity):
    """
    Calculate pressure loss from pipe friction.

    Formula:
    P = (-f * L * ρ * v²) / (2000 * d)
    """
    return (
        -friction_factor
        * pipe_length
        * WATER_DENSITY
        * fluid_velocity ** 2
    ) / (2000 * pipe_diameter)


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate pressure loss from fittings.

    Formula:
    P = (-0.04 * ρ * v² * n) / 2000
    """
    return (
        -0.04
        * WATER_DENSITY
        * fluid_velocity ** 2
        * quantity_fittings
    ) / 2000


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate Reynolds number.

    Formula:
    R = (ρdv) / μ
    """
    return (
        WATER_DENSITY
        * hydraulic_diameter
        * fluid_velocity
    ) / WATER_VISCOSITY


def pressure_loss_from_pipe_reduction(
        larger_diameter,
        fluid_velocity,
        reynolds_number_value,
        smaller_diameter):
    """
    Calculate pressure loss from pipe reduction.

    k = (0.1 + (50 / R)) * ((D / d)^4 - 1)

    P = (-k * ρ * v²) / 2000
    """

    k = (
        0.1
        + (50 / reynolds_number_value)
    ) * ((larger_diameter / smaller_diameter) ** 4 - 1)

    return (
        -k
        * WATER_DENSITY
        * fluid_velocity ** 2
    ) / 2000