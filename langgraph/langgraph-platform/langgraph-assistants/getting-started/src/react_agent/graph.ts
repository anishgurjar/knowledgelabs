import { createReactAgent } from "@langchain/langgraph/prebuilt";
import { MemorySaver } from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";

export const graph = createReactAgent({
  llm: new ChatOpenAI({ model: "gpt-4o-mini" }),
  tools: [],
  prompt: "you are a helpful assistant for Lower.com.",
  checkpointer: new MemorySaver(),
  name: "LOAI Single Agent System"
});