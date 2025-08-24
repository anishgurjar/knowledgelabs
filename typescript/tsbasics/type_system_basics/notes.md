### Types in TS

- Primitive Types: This involves:
    - string
    - number
    - boolean
    - symbol
    - bigint
    - null
    - undefined

    and is executed using `:`. for example:
    ```
        const greet = (name: string): null => { console.log(`Hello ${name}`)}
    ```

- Typescript can infer types. For instance `let x = 5` means ts understands x is a number, but always better to explictly annotate the types.

- Types can be Unioned. For instance: 

    ```
        let id: string | number
        x = 1 //allowed
        x = "Abc" //allowed
        x = true //allowed
    ```

- Types can be intersected. For instance:

    ```
        type hasName = { name: string }
        type hasAge = { age: number }
        type Person: hasName & hasAge

        const anish:Person = { name: "anish", age: 23}
    ```

- `any`, `unknown`, and `never`

    - `any` → Disables type checking

    ```
        let data: any = 123;
        data = "hello"; // No error
    ```


    - `unknown` → Safer any (forces type check before use)

    ```
        let value: unknown = "TS";
        if (typeof value === "string") {
            console.log(value.toUpperCase());
        }
    ```

    - `never` → Function never returns

    ```
        function fail(msg: string): never {
            throw new Error(msg);
        }
    ```

- Literal Types: useful for enums without enums. for instance: 
    ```
        let direction: "up" | "down"
        const x:direction = "up" //allowed
        const y:direction = "left" //not allowed
    ```

- Interface vs Type. Interface is a rough blueprint of how an object looks like. a class implements an interface. Type on the other hand is a literal type assigned to an enity that can be unioned or intersected.

