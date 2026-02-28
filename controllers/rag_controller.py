from odoo import http
from odoo.http import request
from ..services.data_extractor import SalesDataExtractor
from ..services.rag_engine import RAGEngine

class SalesRAGController(http.Controller):

    @http.route('/sales/rag/build', auth='user', type='json')
    def build_rag(self):
        extractor = SalesDataExtractor(request.env)
        docs = extractor.get_sales_text()

        rag = RAGEngine()
        rag.build_index(docs)

        return {"status": "Sales RAG index built successfully"}

    @http.route('/sales/rag/ask', auth='user', type='json')
    def ask_rag(self, **kw):
        question = kw.get("question")
        rag = RAGEngine()
        answer = rag.ask(question)

        return {"answer": answer}
