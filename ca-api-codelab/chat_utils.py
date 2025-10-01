# Utility functions for streaming and formatting responses
import altair as alt
import http.server
import pandas as pd
import proto
import socketserver
import threading

_server_thread = None
_httpd = None


# Prints a formatted section title
def display_section_title(text):
    print(f"\n--- {text.upper()} ---")


# Handles and displays data responses
def handle_data_response(resp):
    if "query" in resp:
        query = resp.query
        display_section_title("Retrieval query")
        print(f"Query name: {query.name}")
        print(f"Question: {query.question}")
        print("Data sources:")
        for datasource in query.datasources:
            display_datasource(datasource)
    elif "generated_sql" in resp:
        display_section_title("SQL generated")
        print(resp.generated_sql)
    elif "result" in resp:
        display_section_title("Data retrieved")
        fields = [field.name for field in resp.result.schema.fields]
        d = {field: [] for field in fields}
        for el in resp.result.data:
            for field in fields:
                d[field].append(el[field])
        print(pd.DataFrame(d))


# Starts a local web server to preview charts
def preview_in_browser(port: int = 8080):
    """Starts a web server in a background thread and waits for user to stop it."""
    global _server_thread, _httpd
    if _server_thread and _server_thread.is_alive():
        print(
            f"\n--> A new chart was generated. Refresh your browser at http://localhost:{port}")
        return
    Handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    try:
        _httpd = socketserver.TCPServer(("", port), Handler)
    except OSError as e:
        print(f"❌ Could not start server on port {port}: {e}")
        return
    _server_thread = threading.Thread(target=_httpd.serve_forever)
    _server_thread.daemon = False
    _server_thread.start()
    print("\n" + "=" * 60)
    print(" 📈CHART READY - PREVIEW IN BROWSER ".center(60))
    print("=" * 60)
    print(
        f"1. In the Cloud Shell toolbar, click 'Web Preview' and select port {port}.")
    print(f"2. Or, open your local browser to http://localhost:{port}")
    print("=" * 60)
    try:
        input(
            "\n--> Press Enter here after viewing all charts to shut down the server...\n\n")
    finally:
        print("Shutting down server...")
        _httpd.shutdown()
        _server_thread.join()
        _httpd, _server_thread = None, None
        print("Server stopped.")


# Handles chart responses
def handle_chart_response(resp, chart_generated_flag: list):
    def _value_to_dict(v):
        if isinstance(v, proto.marshal.collections.maps.MapComposite):
            return {k: _value_to_dict(v[k]) for k in v}
        elif isinstance(v, proto.marshal.collections.RepeatedComposite):
            return [_value_to_dict(el) for el in v]
        return v
    if "query" in resp:
        print(resp.query.instructions)
    elif "result" in resp:
        vega_config_dict = _value_to_dict(resp.result.vega_config)
        chart = alt.Chart.from_dict(vega_config_dict)
        chart_filename = "index.html"
        chart.save(chart_filename)
        if chart_generated_flag:
            chart_generated_flag[0] = True


# Displays the schema of a data source
def display_schema(data):
    fields = getattr(data, "fields")
    df = pd.DataFrame({
        "Column": [f.name for f in fields],
        "Type": [f.type for f in fields],
        "Description": [getattr(f, "description", "-") for f in fields],
        "Mode": [f.mode for f in fields],
    })
    print(df)


# Displays information about a BigQuery data source
def display_datasource(datasource):
    table_ref = datasource.bigquery_table_reference
    source_name = f"{table_ref.project_id}.{table_ref.dataset_id}.{table_ref.table_id}"
    print(source_name)
    display_schema(datasource.schema)


# Handles and displays schema resolution responses
def handle_schema_response(resp):
    if "query" in resp:
        print(resp.query.question)
    elif "result" in resp:
        display_section_title("Schema resolved")
        print("Data sources:")
        for datasource in resp.result.datasources:
            display_datasource(datasource)


# Handles and prints simple text responses
def handle_text_response(resp):
    parts = resp.parts
    print("".join(parts))


# Processes and displays different types of system messages
def show_message(msg, chart_generated_flag: list):
    m = msg.system_message
    if "text" in m:
        handle_text_response(getattr(m, "text"))
    elif "schema" in m:
        handle_schema_response(getattr(m, "schema"))
    elif "data" in m:
        handle_data_response(getattr(m, "data"))
    elif "chart" in m:
        handle_chart_response(getattr(m, "chart"), chart_generated_flag)
    print("\n")
