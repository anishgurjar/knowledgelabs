### Behavioral Patterns

These are basically patterns on how objects interact with each other, more so than what's happening within a class itself.

### Common Patterns:

    - Strategy → Encapsulate interchangeable algorithms (Payment methods, Sorting strategy). 

    - Observer (Pub/Sub) → Notify multiple dependents (Notification service, Event bus).

    - Command → Encapsulate actions as objects (Undo/Redo, Remote control).

    - Chain of Responsibility → Request passes through handlers (Approval workflow, Logging pipeline).

    - State → Object changes behavior with internal state (Vending machine, Order lifecycle).

    - Template Method → Base algorithm with customizable steps (Framework hooks).

### Strategy Pattern:

This is used when I have multiple ways of implementing a common type that some other class needs. for instance in google map, the ETA calculator method might have multiple implementation based on commuteType. so one way to do this is: 

    ```typescript

            class Map{
                ETA = (start, end, commuteType:string):number => {
                    if (commuteType == 'walk') { 
                        // some implementation 
                    }
                    else if (commuteType = 'car') {
                        // some implementation
                    }
                }
            }

    ```

    above is a wrong way of doing this because of a lot of nested if else. Violates OCP because class needs to be modified. 

    a better way would be to define commuteStrategy interface, which walking implements, dirving implements and each does it's thing and returns ETA. then ETA function accepts start, end and commuteStrategy and return based on commuteStrategy. 

### Observer Pattern

As the name suggests, basically when you have a parent class that's source of truth for some data, or for one change in a parent object, you a few other objects to also act differently, you can use this pattern. it's like pub sub without a broker. wrong way to execute this would be for the parent subject object you create methods on how to update child objects, but then parent object does and know too much. 

Instead use observer pattern where parent holds a list of all observers, and observer has an upate method. now the parent can do a state change, and just on statechagne have the observer also call and all of em get notified. 

