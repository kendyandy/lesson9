import streamlit as st


def render_layout() -> None:
	st.set_page_config(page_title="OpenRouter Streaming Prompt UI", layout="wide")

	# Sidebar: placeholders only
	sidebar = st.sidebar
	sidebar.header("Settings")
	api_key: str = sidebar.text_input("API Key", type="password", help="Placeholder only; not used.")
	model: str = sidebar.selectbox(
		"Model",
		["openrouter/auto", "anthropic/claude-3.5-sonnet", "openai/gpt-4o"],
		index=0,
		help="Static options; no backend calls.",
	)
	temperature: float = sidebar.slider("Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.05)
	max_tokens: int = sidebar.slider("Max Tokens", min_value=64, max_value=8192, value=1024, step=64)
	sidebar.divider()
	trace_enabled: bool = sidebar.checkbox("Langfuse Trace (placeholder)", value=False, help="No tracing initialized.")
	session_name: str = sidebar.text_input("Session Name", value="demo-session", help="Not persisted.")

	# Main content
	st.title("Streaming Prompt App (Mockup)")
	st.caption("Enter a system prompt, optional context, and a question. Buttons are non-functional.")

	tab_prompt, tab_context, tab_question = st.tabs(["Prompt", "Context", "Question"])

	with tab_prompt:
		st.subheader("System Prompt")
		system_prompt: str = st.text_area(
			"",
			placeholder="You are a helpful assistant...",
			height=200,
			label_visibility="collapsed",
		)

	with tab_context:
		st.subheader("Context")
		context_text: str = st.text_area(
			"",
			placeholder="Paste any relevant context here...",
			height=200,
			label_visibility="collapsed",
		)
		st.file_uploader("Upload context file (unused)", type=["txt", "md", "json"], help="No parsing performed.")

	with tab_question:
		st.subheader("Question")
		question_text: str = st.text_area(
			"",
			placeholder="What would you like to ask?",
			height=140,
			label_visibility="collapsed",
		)

	st.divider()

	# Actions row (no-op)
	left, mid, right, extra = st.columns([1, 1, 1, 2])
	with left:
		start_clicked: bool = st.button("Start Streaming", type="primary", help="No-op in mockup.")
	with mid:
		stop_clicked: bool = st.button("Stop", help="No-op in mockup.")
	with right:
		clear_clicked: bool = st.button("Clear", help="No-op in mockup.")
	with extra:
		st.button("Copy Last Response", disabled=True)

	# Output panel placeholder
	st.subheader("Output")
	output_container = st.container()
	with output_container:
		st.info("Streaming response will appear here (placeholder). No network calls are made.")

	# Footer notes
	st.caption(
		"This is a UI mockup only. No OpenRouter or Langfuse integrations are active. "
		"All inputs are placeholders to visualize the layout."
	)


if __name__ == "__main__":
	render_layout()
