# Shipping cost Calculator

#input package weight and shipping rate
weight = float(input("Enter a package weight in Kg"))
rate = float(input("Enter the shipping rate per Kg"))

# Calculate Shipping Cost

Shipping_cost = weight * rate

# Display the shipping cost 
print(f"Shipping Cost :{shipping_cost} USD")
