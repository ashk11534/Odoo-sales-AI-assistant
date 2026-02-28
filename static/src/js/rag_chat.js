/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

class SalesRAGChat extends Component {
    setup() {
        this.state = useState({
            messages: [],
            input: "",
            loading: false,
        });
    }

    onKeydown(ev) {
        if (ev.key === "Enter") {
            this.sendMessage();
        }
    }

    async sendMessage() {
        if (!this.state.input) return;

        const userMsg = this.state.input;

        this.state.messages.push({
            role: "user",
            text: userMsg,
        });

        this.state.input = "";
        this.state.loading = true;

        try {
            const result = await rpc("/sales/rag/ask", {
                question: userMsg,
            });

            this.state.messages.push({
                role: "ai",
                text: result.answer,
            });
        } catch (err) {
            this.state.messages.push({
                role: "ai",
                text: "⚠️ AI server error",
            });
        }

        this.state.loading = false;
    }
}

SalesRAGChat.template = "odoo_sales_ai_assistant.RAGChat";

registry.category("actions").add(
    "sales_rag_chat_action",
    SalesRAGChat
);