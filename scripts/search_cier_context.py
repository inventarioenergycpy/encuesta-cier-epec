#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIER Context Search Engine (Single Source of Truth)
Buscador contextual sobre el corpus de documentos CIER (PDFs, tabulaciones, microdatos).
"""
import sys
import os
import json
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

CORPUS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed", "context_embeddings", "corpus_extracted_texts.json")

def search_corpus(query, top_k=5):
    if not os.path.exists(CORPUS_PATH):
        print(f"[ERROR] Corpus de contexto no encontrado en: {CORPUS_PATH}")
        return

    with open(CORPUS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = data.get("pdfs", [])
    query_terms = [t.lower() for t in query.split() if len(t) > 2]
    
    results = []
    for doc in docs:
        filename = doc.get("filename", "")
        text = doc.get("text", "")
        
        matches = 0
        snippets = []
        for term in query_terms:
            for m in re.finditer(re.escape(term), text, re.IGNORECASE):
                matches += 1
                start = max(0, m.start() - 120)
                end = min(len(text), m.end() + 120)
                snippet = text[start:end].replace("\n", " ").strip()
                if len(snippets) < 3:
                    snippets.append(f"...{snippet}...")

        if matches > 0:
            results.append({
                "file": filename,
                "score": matches,
                "snippets": snippets,
                "page": doc.get("pages", 1)
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    print(f"=== BUSQUEDA CONTEXTUAL CIER: '{query}' ({len(results)} coincidencias) ===")
    if not results:
        print("No se encontraron coincidencias exactas para los términos buscados.")
        return

    for i, r in enumerate(results[:top_k], 1):
        print(f"\n[{i}] Documento: {r['file']} (Paginas ~{r['page']} | Relevancia: {r['score']})")
        for snip in r["snippets"]:
            print(f"    * {snip}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python search_cier_context.py <termino_de_busqueda>")
        sys.exit(1)
    q = " ".join(sys.argv[1:])
    search_corpus(q)
