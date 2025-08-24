### Classes and OOP

- Basically a class is a blueprint. Syntax is:

  ```

      class User{

          constructor(id: string | number, name: string){
              this.id = id
              this.name  = name
          }

          const greet = (name: string):void => {
              console.log(`Hello ${name}`)
          }
      }

      let anish:User = new User(123, "anish")
      anish.greet()

  ```

- Access Modifiers
  - public: accessible everywhere
  - private: only accessible in the same class
  - protected: inside class + subclasses
  - readonly: can't reassign after initialization

- Polymorphism is baiscally method overloading
