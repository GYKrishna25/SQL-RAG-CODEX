# generate_flow_diagram.py
from graphviz import Digraph

# Create a new directed graph
dot = Digraph("Text2SQL_RAG_Hybrid_Engine", format="png")
dot.attr(rankdir="TB", size="12,12", dpi="300")
dot.attr("node", shape="box", style="rounded,filled", fillcolor="lightcyan", fontname="Arial", fontsize="10")
dot.attr("edge", arrowhead="vee", arrowsize="0.8", fontname="Arial", fontsize="9")

# Nodes and edges
dot.node("A", "User Opens App", shape="ellipse", fillcolor="honeydew")
dot.node("B", "OpenRouter API Key Provided?", shape="diamond", fillcolor="wheat")

dot.edge("A", "B")

dot.node("C", "Show API Key Prompt in Sidebar", fillcolor="lightcoral")
dot.edge("B", "C", label="No")

dot.node("D", "Initialize LLM: qwen/qwen-turbo", fillcolor="lightblue")
dot.edge("B", "D", label="Yes")

dot.node("E", "Initialize Embedding Model: BAAI/bge-small-en-v1.5", fillcolor="lightblue")
dot.edge("D", "E")

dot.node("F", "Set Settings.llm & Settings.embed_model", fillcolor="lightblue")
dot.edge("E", "F")

dot.node("G", "Documents Uploaded?", shape="diamond", fillcolor="wheat")
dot.edge("F", "G")

dot.node("H", "Upload via Streamlit File Uploader", fillcolor="lavender")
dot.edge("G", "H", label="Yes")

dot.node("I", "Save to Temp Directory", fillcolor="lavender")
dot.edge("H", "I")

dot.node("J", "Process with DoclingReader", fillcolor="lavender")
dot.edge("I", "J")

dot.node("K", "Chunk using MarkdownNodeParser", fillcolor="lavender")
dot.edge("J", "K")

dot.node("L", "Embed with HuggingFace Model", fillcolor="lavender")
dot.edge("K", "L")

dot.node("M", "Store in Milvus Vector DB (dim=384)", fillcolor="lavender")
dot.edge("L", "M")

dot.node("N", "Create VectorStoreIndex", fillcolor="lavender")
dot.edge("M", "N")

dot.node("O", "Build document_tool with Codex Validation", fillcolor="lightskyblue")
dot.edge("N", "O")

dot.node("P", "SQL Database Available?", shape="diamond", fillcolor="wheat")
dot.edge("G", "P", label="No/Yes")

dot.node("Q", "Connect to enterprise_database.sqlite", fillcolor="lavender")
dot.edge("P", "Q")

dot.node("R", "Inspect Tables via SQLAlchemy Inspector", fillcolor="lavender")
dot.edge("Q", "R")

dot.node("S", "Create SQLDatabase Object", fillcolor="lavender")
dot.edge("R", "S")

dot.node("T", "Create NLSQLTableQueryEngine", fillcolor="lavender")
dot.edge("S", "T")

dot.node("U", "Wrap as sql_tool with Codex Validation", fillcolor="lightskyblue")
dot.edge("T", "U")

dot.node("V", "Initialize RouterOutputAgentWorkflow", fillcolor="gold")
dot.edge("O", "V")
dot.edge("U", "V")

dot.node("W", "Wait for User Query", fillcolor="lightcyan")
dot.edge("V", "W")

dot.node("X", "User Asks Question", shape="ellipse", fillcolor="honeydew")
dot.edge("W", "X")

dot.node("Y", "Add to chat_history as user message", fillcolor="lightgray")
dot.edge("X", "Y")

dot.node("Z", "LLM decides: use tool?", fillcolor="lightgray")
dot.edge("Y", "Z")

dot.node("AA", "Tool Call Needed?", shape="diamond", fillcolor="wheat")
dot.edge("Z", "AA")

dot.node("AB", "Return direct LLM response", fillcolor="lightgreen")
dot.edge("AA", "AB", label="No")

dot.node("AC", "GatherToolsEvent: Extract tool calls", fillcolor="lightgray")
dot.edge("AA", "AC", label="Yes")

dot.node("AD", "dispatch_calls(): Send one ToolCallEvent per tool", fillcolor="lightgray")
dot.edge("AC", "AD")

dot.node("AE", "call_tool(): Execute selected tool async", fillcolor="lightgray")
dot.edge("AD", "AE")

dot.node("AF", "Tool = sql_tool?", shape="diamond", fillcolor="wheat")
dot.edge("AE", "AF")

dot.node("AG", "Generate SQL → Run on SQLite → Validate with Codex → Return {sql, results, trust_score}", fillcolor="plum")
dot.edge("AF", "AG", label="Yes")

dot.node("AH", "Semantic Search → Retrieve from Milvus → Validate with Codex → Return {response, trust_score}", fillcolor="plum")
dot.edge("AF", "AH", label="No")

dot.node("AI", "ToolCallEventResult: Wrap result in ChatMessage", fillcolor="lightgray")
dot.edge("AG", "AI")
dot.edge("AH", "AI")

dot.node("AJ", "gather(): Collect all tool results", fillcolor="lightgray")
dot.edge("AI", "AJ")

dot.node("AK", "All Tools Done?", shape="diamond", fillcolor="wheat")
dot.edge("AJ", "AK")

dot.node("AL", "Wait for more results", fillcolor="lightgray")
dot.edge("AK", "AL", label="No")

dot.node("AM", "Append tool responses to chat_history", fillcolor="lightgray")
dot.edge("AK", "AM", label="Yes")

dot.node("AN", "Return to InputEvent → loop continues", fillcolor="lightgray")
dot.edge("AM", "AN")

dot.node("AO", "Format Final Response with Tool Used + Trust Score", fillcolor="lightgreen")
dot.edge("AN", "AO")

dot.node("AP", "Stream Response in Chat UI", fillcolor="lightgreen")
dot.edge("AO", "AP")

dot.node("AQ", "Update st.session_state.messages", fillcolor="lightgreen")
dot.edge("AP", "AQ")

dot.node("AR", "User Clicks 'View Database'", shape="ellipse", fillcolor="honeydew")
dot.edge("W", "AR")

dot.node("AS", "render_database_tab()", fillcolor="orchid")
dot.edge("AR", "AS")

dot.node("AT", "Show Table Overview: Rows, Columns, Types", fillcolor="orchid")
dot.edge("AS", "AT")

dot.node("AU", "Interactive Data Table with Filter & Sort", fillcolor="orchid")
dot.edge("AT", "AU")

dot.node("AV", "Custom SQL Query Input", fillcolor="orchid")
dot.edge("AU", "AV")

dot.node("AW", "Run Query on SQLite", fillcolor="orchid")
dot.edge("AV", "AW")

dot.node("AX", "Display Results + Download CSV", fillcolor="orchid")
dot.edge("AW", "AX")

dot.node("AY", "User Clicks Reset", shape="ellipse", fillcolor="honeydew")
dot.edge("W", "AY")

dot.node("AZ", "reset_chat()", fillcolor="indianred")
dot.edge("AY", "AZ")

dot.node("BA", "Clear messages, workflow, temp files", fillcolor="indianred")
dot.edge("AZ", "BA")

dot.node("BB", "Return to initial state", fillcolor="indianred")
dot.edge("BA", "BB")

# Render and save
dot.render("Text2SQL_RAG_Hybrid_Engine_Flow", cleanup=True)

print("✅ Flow diagram generated: Text2SQL_RAG_Hybrid_Engine_Flow.png")