#ДЗ5
import platform
import aiohttp
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
from datetime import datetime, timedelta
from rich.console import Console
console = Console()

async def main():
    rah_day = 9
    res_dict = {}
    res = {}
    async with aiohttp.ClientSession() as session:
        for _ in range(10):   
            day_first = datetime.now() - timedelta(days=rah_day)
            date_to_day = day_first.strftime("%d.%m.%Y")            
            rah_day = rah_day - 1
            async with session.get('https://api.privatbank.ua/p24api/exchange_rates?json&date='+date_to_day) as response:
                
                result = await response.json()
                ress_list = result['exchangeRate']
                                
                for ress_dict in ress_list:
                    ress_currency = ress_dict['currency']
                    ress_sale = ress_dict['saleRateNB']
                    ress_purchase = ress_dict['purchaseRateNB']
                    if ress_currency == 'EUR' or ress_currency == 'USD':
                        ress_value = {ress_currency: {'sale': ress_sale, 'purchase': ress_purchase}}                    
                        res_dict.update(ress_value)                   
            
                res.update({result['date']: res_dict})             
                    
        return res

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
        
    console.print(r)