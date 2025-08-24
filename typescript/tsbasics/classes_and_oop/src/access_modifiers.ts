class BankBalance {
  readonly id: number;
  private balance: number;

  constructor(id: number, balance: number) {
    this.id = id;
    this.balance = balance;
  }

  deposit(amount: number): void {
    this.balance += amount;
  }

  getBalance(): number {
    return this.balance;
  }
}

const chase = new BankBalance(123, 1000);
chase.deposit(1000);
console.log(chase.getBalance());
