import { Client } from "@langchain/langgraph-sdk";

export const createClient = () => {
  const apiUrl = 'http://localhost:2024'
  return new Client({
    apiUrl,
  });
};

const assistant_id = "fe096781-5601-53d2-b2f6-0d3403f7e9ca";

const client = createClient();

// Start a new thread
//const thread = await client.threads.create();

// Start a streaming run
const messages = [{ role: "human", content: "what's the weather in la" }];

const streamResponse = client.runs.stream(null,
  assistant_id,
  {
    input: { messages },
  }
);

for await (const chunk of streamResponse) {
  console.log("chunk event: ", chunk.event);
  console.log("chunk data: ", chunk.data);
}

