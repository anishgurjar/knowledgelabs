import { createSupervisor } from "@langchain/langgraph-supervisor";
import { ChatOpenAI } from "@langchain/openai";
import { graph as hrAgent } from "../loai-hr/graph.js";
import { graph as underwritingAgent } from "../loai-underwriting/graph.js";
import { prompt } from "./prompt.js";

const supervisorGraph = createSupervisor({
  agents: [hrAgent, underwritingAgent],
  llm: new ChatOpenAI({ model: "gpt-4o" }),
  prompt: prompt,
  supervisorName: "LOAI_Supervisor",
  outputMode: "last_message",
  addHandoffBackMessages: true
});

export const graph = supervisorGraph.compile();