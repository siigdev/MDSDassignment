


state("IDLE").
    transition("START_PRESSED").to("DOOR_OPEN").setState("floor", 0)
state("DOOR_OPEN").
    transition("CLOSED").to("GOING_UP").whenStateEquals("UP_CLICK")
    transition("CLOSED").to("IDLE").whenStateEquals("NULL")
state("GOING_UP").
    transition("ARRIVED").to("STOPPED_AT_FLOOR").whenStateEquals("floor", selected)
                        else.changeState("floor", +1)
state("GOING_DOWN").
    transition("ARRIVED").to("STOPPED_AT_FLOOR").whenStateEquals("floor", 0).
                        else.changeState("floor", -1)
state("STOPPED_AT_FLOOR")
    transition("OPEN").to("DOOR_OPEN")
    transition("GO_DOWN").to("GOING_DOWN")