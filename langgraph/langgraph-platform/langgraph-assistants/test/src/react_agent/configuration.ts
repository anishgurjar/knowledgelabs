/**
 * Define the configurable parameters for the agent.
 */
import { z } from "zod";
import { MessagesZodState } from "@langchain/langgraph";
import { SYSTEM_PROMPT_TEMPLATE } from "./prompts.js";
import type { BaseMessage } from "@langchain/core/messages";

/**
 * Extended state schema that includes both messages AND configuration.
 * This merges MessagesZodState with our runtime configuration fields.
 */
export const AgentStateSchema = MessagesZodState.merge(
  z.object({
    systemPromptTemplate: z
      .string()
      .optional()
      .describe("The system prompt template for the agent"),
    model: z
      .string()
      .optional()
      .describe("The LLM model to use (e.g., 'anthropic/claude-3-5-haiku-latest', 'openai/gpt-4')"),
  })
);

export type AgentStateType = {
  messages: BaseMessage[];
  systemPromptTemplate?: string;
  model?: string;
};

// Context-only schema for runtime configuration
export const ConfigurationSchema = z.object({
  systemPromptTemplate: z
    .string()
    .optional()
    .describe("The system prompt template for the agent"),
  model: z
    .string()
    .optional()
    .describe("The LLM model to use (e.g., 'anthropic/claude-3-5-haiku-latest', 'openai/gpt-4')"),
});

export type ConfigurationType = z.infer<typeof ConfigurationSchema>;

// Default values for runtime configuration
export const DEFAULT_SYSTEM_PROMPT_TEMPLATE = SYSTEM_PROMPT_TEMPLATE;
export const DEFAULT_MODEL = "claude-3-5-haiku-latest";
