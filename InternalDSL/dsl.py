# Does not care which is max and min floor number, as any inputs would be buttons

# selectedFloor is the floor input selected by the user
# the initial "currentFloor" can be defined as 0 to begin with

state("IDLE").
    transition("START_PRESSED").to("DOOR_OPEN").setState("selected", selectedFloor)
state("DOOR_OPEN").
    transition("CLOSED_DOOR").to("GOING_UP").when("selected" > "currentFloor")
    transition("CLOSED_DOOR").to("GOING_DOWN").when("selected" < "currentFloor")
state("GOING_UP").
    transition("ARRIVED").to("STOPPED_AT_FLOOR").when("currentFloor" = "selected")
                        otherwise().changeState("currentFloor", +1)
state("GOING_DOWN").
    transition("ARRIVED").to("STOPPED_AT_FLOOR").when("currentFloor" = "selected")
                        otherwise().changeState("currentFloor", -1)
state("STOPPED_AT_FLOOR")
    transition("OPEN_EXIT_CLOSE").to("IDLE")