python -m venv venv
venv\Scripts\activate


### Token Utilization & API Usage (Markdown Table)

# Groq API: Streaming vs Non-Streaming Comparison

| Feature / Metric            | Non-Streaming (`stream=False`)                   | Streaming (`stream=True`)                                |
|-----------------------------|--------------------------------------------------|----------------------------------------------------------|
| Response Delivery           | Returned all at once                             | Returned chunk-by-chunk (real-time)                     |
| Perceived Latency          | Higher (wait for full response)                  | Lower (first tokens appear immediately)                 |
| Ease of Use                | Very easy (single object)                        | Requires loop to process chunks                         |
| Use Case                   | Batch processing, async tasks                    | Chat UI, terminals, live apps                           |
| Token Billing              | Same for both modes (prompt + completion tokens) | Same (streaming does NOT reduce or increase cost)       |
| API Usage                  | One request, one response                        | One request, multiple streamed chunks                   |
| Response Object            | `result.choices[0].message["content"]`           | `chunk.choices[0].delta.content`                        |
| Memory Usage               | Higher (stores full response)                    | Lower (processes tokens incrementally)                 |
| Completion Handling        | Simple                                           | Requires merging chunks                                 |
| Ideal For                  | Short/medium responses                           | Long responses, live output                             |


