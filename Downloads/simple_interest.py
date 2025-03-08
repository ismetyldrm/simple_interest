# simple_interest.py

def calculate_simple_interest(principal, rate, time):
   
    return (principal * rate * time) / 100

if __name__ == "__main__":
 
    principal = float(input("Anapara miktarını girin: "))
    rate = float(input("Faiz oranını girin: "))
    time = float(input("Yıl cinsinden süreyi girin: "))
    
    interest = calculate_simple_interest(principal, rate, time)
    print(f"Basit faiz miktarı: {interest}")
