import { SystemMessage } from "@langchain/core/messages";
import { createReactAgent } from "@langchain/langgraph/prebuilt";
import { Runtime } from "@langchain/langgraph";

import { 
  AgentStateSchema,
  AgentStateType,
  ConfigurationSchema, 
  ConfigurationType,
  DEFAULT_SYSTEM_PROMPT_TEMPLATE,
  DEFAULT_MODEL
} from "./configuration.js";
import { TOOLS } from "./tools.js";
import { loadChatModel } from "./utils.js";

/**
 * Dynamic prompt function that generates messages based on runtime context.
 * This is called each time the agent needs to format messages for the LLM.
 * It injects the system prompt with the current timestamp before the user messages.
 * 
 * Equivalent to Python:
 *   def prompt_func(state: State, runtime: Runtime[ContextSchema]):
 *       system_prompt = runtime.context["systemPromptTemplate"]
 */
function promptFunc(
  state: AgentStateType,
  runtime: Runtime<ConfigurationType>
) {
  const systemPromptTemplate = runtime.context?.systemPromptTemplate ?? DEFAULT_SYSTEM_PROMPT_TEMPLATE;
  
  // Ensure messages is an array
  const messages = Array.isArray(state.messages) ? state.messages : [];
  
  return [
    new SystemMessage(
      systemPromptTemplate.replace(
        "{system_time}",
        new Date().toISOString(),
      )
    ),
    ...messages,
  ];
}

/**
 * Dynamic model loader function that loads the appropriate model based on runtime context.
 * This follows the new LangGraph v0.4+ pattern where llm can be a function.
 * 
 * Equivalent to Python:
 *   def get_model(state: State, runtime: Runtime[ContextSchema]):
 *       model_name = runtime.context["model"]
 *       return init_chat_model(model_name)
 */
async function modelLoader(
  _state: AgentStateType,
  runtime: Runtime<ConfigurationType>
) {
  const modelName = runtime.context?.model ?? DEFAULT_MODEL;
  return await loadChatModel(modelName);
}

// Create the React agent using the prebuilt function.
// - stateSchema: Extended state with messages + config fields (enables chat UI)
// - contextSchema: Runtime configuration (shows config panel in UI)
export const graph = createReactAgent({
  llm: modelLoader,
  tools: TOOLS,
  prompt: promptFunc,
  stateSchema: AgentStateSchema as any,      // Messages + config state
  contextSchema: ConfigurationSchema as any, // Runtime configuration
});
