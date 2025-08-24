### Functions 

- This is nothing crazy. super simple. 

    ```

        const greet(name: string, age: number):void { 
            console.log(`My name is ${name}`)
        }

    ```

- Functional Overloading

    ```

        function reverse(str: string): string;
        function reverse(arr: string[]): string[];
        function reverse(value: string | string[]) {
          if (typeof value === "string") {
            return value.split("").reverse().join("");
          }
          return value.slice().reverse();
        }
        
        console.log(reverse("hello"));      // 'olleh'
        console.log(reverse(["a", "b"]));   // ['b', 'a']


    ```
