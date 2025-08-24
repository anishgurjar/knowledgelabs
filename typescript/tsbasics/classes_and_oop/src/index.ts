class User {
  id: string | number;
  name: string;

  constructor(id: string | number, name: string) {
    this.id = id;
    this.name = name;
  }

  greet(): void {
    console.log(`Hello ${this.name}`);
  }
}

let anish: User = new User(123, "anish");
anish.greet();
