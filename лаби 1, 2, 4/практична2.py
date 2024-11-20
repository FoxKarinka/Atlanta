import requests
from bs4 import BeautifulSoup
import time
import threading

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def get_example_data(url, class_name):
    soup = get_data(url)
    if soup:
        items = soup.find_all('div', class_=class_name)
        return [item.text for item in items]
    return []

def get_gasoline_prices():
    return get_example_data('https://www.pinterest.com/search/pins/?q=медуза%20горгона&rs=typed', 'price-class')

def get_exchange_rates():
    return get_example_data('https://www.pinterest.com/search/pins/?q=медуза%20горгона&rs=typed', 'rate-class')

def get_product_quantities():
    return get_example_data('https://www.pinterest.com/search/pins/?q=медуза%20горгона&rs=typed', 'product-class')

def measure_execution_time():
    times = []
    for _ in range(5):
        start_time = time.time()
        get_gasoline_prices()
        time.sleep(1)  
        get_exchange_rates()
        time.sleep(1)  
        get_product_quantities()
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)

def measure_execution_time_with_threads():
    def thread_function(func):
        func()
    
    times = []
    for _ in range(5):
        threads = []
        start_time = time.time()
        
        for func in [get_gasoline_prices, get_exchange_rates, get_product_quantities]:
            thread = threading.Thread(target=thread_function, args=(func,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)

average_time = measure_execution_time()
print(f'Середній час виконання запитів без потоків: {average_time:.2f} секунд')

average_time_with_threads = measure_execution_time_with_threads()
print(f'Середній час виконання запитів з потоками: {average_time_with_threads:.2f} секунд')
