/**
 * Define the configurable parameters for the agent.
 */
import { Annotation } from "@langchain/langgraph";
import { RunnableConfig } from "@langchain/core/runnables";

export const ConfigurationSchema = Annotation.Root({
  systemPromptTemplate: Annotation<string>,
  model: Annotation<string>,
});

export function ensureConfiguration(
  config: RunnableConfig,
): typeof ConfigurationSchema.State {
  
  const configurable = config.configurable ?? {};
  return {
    systemPromptTemplate:
      configurable.systemPromptTemplate ?? "you are a helpful assistant for Lower.com.",
    model: configurable.model ?? "claude-3-5-haiku-latest",
  };
}
