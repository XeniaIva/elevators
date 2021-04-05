class Operator:
    def __init__(self, elevator: Elevator):
        pass

    def open_doors() -> bool:
        return elevator.open_doors()

    def close_doors() -> bool:
        return elevator.close_doors()

    def turn_light_on() -> None:
        elevator.turn_light_on()

    def turn_light_off() -> None:
        elevator.turn_light_off()

    # Todo: Recheck the requirements' spec. Might be better to return bool, not void
    # Or throw an exception, but this seems like an overkill
    def call() -> None:
        pass

    # Same consideration as with the call method
    def move_to_floor(floor: int) -> None:
        pass

    def get_lift_state() -> LiftState:
        pass

    # And again, may be bool will be better
    def restart() -> None:
        pass