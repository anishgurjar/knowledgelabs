const { z } = require("zod");

const schema = z.coerce.date();

const inputs = [
  "2024-01-01",
  "not a date",
  "",
  null,
  undefined,
];

for (const input of inputs) {
  try {
    const result = schema.parse(input);
    console.log("INPUT:", input);
    console.log("RESULT:", result);
    console.log("isValid:", !isNaN(result.getTime()));
    console.log("----");
  } catch (err) {
    console.log("INPUT:", input);
    console.log("ERROR:", err.errors);
    console.log("----");
  }
}