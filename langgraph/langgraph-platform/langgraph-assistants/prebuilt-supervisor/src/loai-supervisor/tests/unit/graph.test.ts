import { it, expect } from "@jest/globals";
import { graph } from "../../graph.js";

it("Supervisor graph is defined", async () => {
  expect(graph).toBeDefined();
  expect(typeof graph.invoke).toBe("function");
});
