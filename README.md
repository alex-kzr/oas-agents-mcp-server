# OpenAI Agents MCP Server

Independent synthetic fixture using official MCP Python SDK 2.3.0 (MCPServer public API), locked for Python 3.12. Tools: bounded echo, allowlisted sample.discount lookup and controlled diagnostic failure. No real accounts, filesystem, shell or network tool access.

WSL2: `uv sync --locked`; `uv run --offline --locked python -m unittest discover -s tests -v`.

Serve stdio with `uv run --offline --locked python -m agents_mcp_server`. Local Streamable HTTP entry point: `uv run --offline --locked python -m agents_mcp_server --transport streamable-http --port 8766`, binding only 127.0.0.1 with body/session limits. Stdio discovery and native Agent tool calls have actual SDK integration tests in the runtime repository; Streamable HTTP entry point remains unverified until its separate integration test.

Registry extension is build_server() plus independent tool contracts. This official protocol server is permitted integration glue, not another agent orchestration framework. No remote URL is invented or pushed.
