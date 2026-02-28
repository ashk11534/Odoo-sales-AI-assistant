class SalesDataExtractor:

    def __init__(self, env):
        self.env = env

    def get_sales_text(self):
        sales = self.env['sale.order'].search([])

        documents = []

        for sale in sales:
            print(sale.name)
            text = f"""
            Order: {sale.name}
            Customer: {sale.partner_id.name}
            Date: {sale.date_order}
            Amount: {sale.amount_total}
            Status: {sale.state}
            """
            documents.append(" ".join(text.split()))

        print(documents)

        return documents