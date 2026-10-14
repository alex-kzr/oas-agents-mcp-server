"""Official MCP Python SDK v2 entry point."""
import argparse
from mcp.server import MCPServer
from agents_mcp_server.tools import echo, lookup, controlled_error


def build_server():
    server=MCPServer('OAS synthetic fixture')
    for tool in (echo,lookup,controlled_error):
        server.tool()(tool)
    return server


def main():
    parser=argparse.ArgumentParser(description='OAS synthetic MCP fixture')
    parser.add_argument('--transport',choices=['stdio','streamable-http'],default='stdio')
    parser.add_argument('--port',type=int,default=8766)
    args=parser.parse_args()
    server=build_server()
    if args.transport=='stdio':
        server.run('stdio')
    else:
        server.run('streamable-http',host='127.0.0.1',port=args.port,max_request_body_size=64000,max_sessions=8,session_idle_timeout=60)


if __name__=='__main__':
    main()
