# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n 
        self.discount = discount 
        self.product_prices = {products[i]: prices[i] for i in range(len(products))} 
        self.customer_count = 0  

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        
        subtotal = sum(self.product_prices[product[i]] * amount[i] for i in range(len(product)))
        
        if self.customer_count % self.n == 0:
            subtotal *= (100 - self.discount) / 100
        
        return subtotal


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)