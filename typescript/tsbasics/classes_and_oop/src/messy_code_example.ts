// This file is intentionally poorly formatted to demonstrate Prettier's power!

interface User {
  name: string;
  age: number;
  email?: string;
}

class UserManager {
  private users: User[];

  constructor() {
    this.users = [];
  }

  addUser(user: User): void {
    this.users.push(user);
    console.log(`Added user: ${user.name}`);
  }

  getUser(name: string): User | undefined {
    return this.users.find(u => u.name === name);
  }

  getAllUsers(): User[] {
    return this.users.filter((user, index) => {
      return user.age >= 18;
    });
  }

  removeUser(name: string): boolean {
    const index = this.users.findIndex(u => u.name === name);
    if (index !== -1) {
      this.users.splice(index, 1);
      return true;
    }
    return false;
  }
}

// Terrible object formatting
const manager = new UserManager();

// Horrible array formatting
const users = [
  { name: "Alice", age: 25, email: "alice@email.com" },
  { name: "Bob", age: 17 },
  { name: "Charlie", age: 30, email: "charlie@email.com" },
];

// Bad function calls
users.forEach(user => {
  manager.addUser(user);
});

// Inconsistent spacing in conditionals
if (users.length > 0) {
  console.log("Users found!");
} else {
  console.log("No users");
}

// Bad chaining
const adultUsers = manager.getAllUsers().map(user => ({
  ...user,
  isAdult: true,
}));

// Messy try-catch
try {
  const user = manager.getUser("Alice");
  if (user) {
    console.log(`Found user: ${user.name}, Age: ${user.age}`);
  }
} catch (error) {
  console.error("Error:", error);
}

// Export with bad spacing
export { UserManager, User };
