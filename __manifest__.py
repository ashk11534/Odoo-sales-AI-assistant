{
    "name": "Sales AI Assistant",
    "version": "1.0",
    "summary": "Ask questions about Odoo Sales using RAG + Local LLM",
    "category": "Sales",
    "author": "Ashik",
    "depends": ["sale", "account"],
    "data": [
        "views/rag_chat_view.xml",
        "views/rag_menu.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "odoo_sales_ai_assistant/static/src/js/rag_chat.js",
            "odoo_sales_ai_assistant/static/src/xml/rag_chat.xml",
            "odoo_sales_ai_assistant/static/src/css/rag_chat.css",
        ],
    },
    "installable": True,
    "application": True,
}