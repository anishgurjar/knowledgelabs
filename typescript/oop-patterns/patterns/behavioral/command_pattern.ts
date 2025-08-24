// Command Interface
interface Command {
    execute(): void;
    undo(): void;
}

// Receiver
class Light {
    on() { console.log("Light is ON"); }
    off() { console.log("Light is OFF"); }
}

// Concrete Commands
class LightOnCommand implements Command {
    private light: Light;
    constructor(light: Light) { this.light = light; }

    execute() { this.light.on(); }
    undo() { this.light.off(); }
}

class LightOffCommand implements Command {
    private light: Light;
    constructor(light: Light) { this.light = light; }

    execute() { this.light.off(); }
    undo() { this.light.on(); }
}

// Invoker
class RemoteControl {
    private command: Command | null = null;

    setCommand(command: Command) {
        this.command = command;
    }

    pressButton() {
        this.command?.execute();
    }

    pressUndo() {
        this.command?.undo();
    }
}

// Client
const livingRoomLight = new Light();
const lightOn = new LightOnCommand(livingRoomLight);
const lightOff = new LightOffCommand(livingRoomLight);

const remote = new RemoteControl();

remote.setCommand(lightOn);
remote.pressButton();  // Light is ON
remote.pressUndo();    // Light is OFF

remote.setCommand(lightOff);
remote.pressButton();  // Light is OFF
remote.pressUndo();    // Light is ON