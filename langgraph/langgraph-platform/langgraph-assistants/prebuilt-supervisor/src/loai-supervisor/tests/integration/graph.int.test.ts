import { it, expect } from "@jest/globals";
import { graph } from "../../graph.js";

it("Routes HR question to HR agent", async () => {
  const res = await graph.invoke({
    messages: [
      {
        role: "user",
        content: "How do I use Workday to request time off?",
      },
    ],
  });
  expect(res.messages.length).toBeGreaterThan(0);
  expect(res.messages[res.messages.length - 1]._getType()).toBe("ai");
});

it("Routes underwriting question to underwriting agent", async () => {
  const res = await graph.invoke({
    messages: [
      {
        role: "user",
        content: "What are the Fannie Mae underwriting guidelines?",
      },
    ],
  });
  expect(res.messages.length).toBeGreaterThan(0);
  expect(res.messages[res.messages.length - 1]._getType()).toBe("ai");
});
