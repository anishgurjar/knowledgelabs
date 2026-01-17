import { createReactAgent } from "@langchain/langgraph/prebuilt";
import { MemorySaver } from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";
import { prompt } from "./prompt.js";

export const graph = createReactAgent({
  llm: new ChatOpenAI({ model: "gpt-4o-mini" }),
  tools: [],
  prompt: prompt,
  checkpointer: new MemorySaver(),
  name: "LOAI_Underwriting_Agent"
});