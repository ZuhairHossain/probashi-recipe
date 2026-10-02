#!/bin/bash
ollama serve &
sleep 5
ollama pull llama3.2
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
