### Generics 

- Generics help you infer a type when assigned when you don't know what type of input will be passed. If you didn't have generics, you would either have to use the `any` keyword or you would have to loose type safety. Both of which are not good. Example where generics come in clutch: 

    ```typescript

        //without generics
        const identity = (input:any):any => {
            return input;
        }

        const myinput = "anish"
        identity(myinput).toUpperCase() // works at both compile time and run time, because perfectly valid
        identity(myinput).toExponential() // say my junior adds this. it will still compile. Then in production if someone assigns a string to myinput, i'll get runtime error. 

    ```

    compared to generics where I could do:

    ```typescript

        const identity = <T>(input:T):T => {
            return input
        }

        identity("anish").toUpperCase() //works
        identity("anish").toExponential // will throw a compile time error. phew, saved a bug
    ```

