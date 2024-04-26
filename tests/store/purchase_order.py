class PurchaseOrder:
    def __init__(self, status_code, po_id, pet_id, quantity, shipdate, status, complete):
        self.status_code = status_code
        self.po_id = po_id
        self.pet_id = pet_id
        self.quantity = quantity
        self.shipdate = shipdate
        self.status = status
        self.complete = complete
