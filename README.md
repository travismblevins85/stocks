# stocks
___ This code is about joining two different datasets, the purpose anyways, from two different sources.  I chose to use YahooFinanceAPI which is at https://pypi.org/project/YahooFinanceAPI/, and historical data from Yahoo Finance at https://finance.yahoo.com/quotes/Historical,DATA/view/v1.  You will have to search for the symbols of the stocks which I chose AAPL, AMZN, and MSFT which are 3 of my favorite and most popular stocks. ___

𝑇𝑜 𝑟𝑢𝑛 𝑡ℎ𝑖𝑠 𝑝𝑟𝑜𝑗𝑒𝑐𝑡, 𝐼 𝑤𝑜𝑢𝑙𝑑 𝑟𝑒𝑐𝑜𝑚𝑚𝑒𝑛𝑑 𝑐𝑟𝑒𝑎𝑡𝑖𝑛𝑔 𝑎 𝑣𝑖𝑟𝑡𝑢𝑎𝑙 𝑒𝑛𝑣𝑖𝑟𝑜𝑛𝑚𝑒𝑛𝑡 𝑓𝑜𝑟 𝑎𝑙𝑙 𝑜𝑓 𝑡ℎ𝑒 𝑝𝑎𝑐𝑘𝑎𝑔𝑒𝑠, 𝑡ℎ𝑒𝑛 𝑖𝑛𝑠𝑡𝑎𝑙𝑙 𝑡ℎ𝑒𝑠𝑒𝑠 𝑙𝑖𝑏𝑟𝑎𝑟𝑖𝑒𝑠 -
(𝑡ℎ𝑖𝑠 𝑖𝑠 𝑎𝑙𝑠𝑜 ℎ𝑜𝑤 𝑡ℎ𝑒𝑦 𝑎𝑟𝑒 𝑢𝑠𝑒𝑑, 𝑠𝑜 𝑦𝑜𝑢 𝑐𝑎𝑛 𝑐𝑜𝑝𝑦 𝑎𝑛𝑑 𝑝𝑎𝑠𝑡𝑒 𝑡ℎ𝑖𝑠 𝑎𝑠 𝑖𝑠)
-𝑓𝑟𝑜𝑚 𝑦𝑓𝑎𝑝𝑖 𝑖𝑚𝑝𝑜𝑟𝑡 𝑌𝑎ℎ𝑜𝑜𝐹𝑖𝑛𝑎𝑛𝑐𝑒𝐴𝑃𝐼, 𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙
-𝑓𝑟𝑜𝑚 𝑑𝑎𝑡𝑒𝑡𝑖𝑚𝑒 𝑖𝑚𝑝𝑜𝑟𝑡 𝑑𝑎𝑡𝑒𝑡𝑖𝑚𝑒, 𝑡𝑖𝑚𝑒𝑑𝑒𝑙𝑡𝑎
-𝑖𝑚𝑝𝑜𝑟𝑡 𝑝𝑎𝑛𝑑𝑎𝑠 𝑎𝑠 𝑝𝑑 
-𝑖𝑚𝑝𝑜𝑟𝑡 𝑛𝑢𝑚𝑝𝑦 𝑎𝑠 𝑛𝑝
-𝑖𝑚𝑝𝑜𝑟𝑡 𝑚𝑎𝑡𝑝𝑙𝑜𝑡𝑙𝑖𝑏.𝑝𝑦𝑝𝑙𝑜𝑡 𝑎𝑠 𝑝𝑙𝑡
-𝑓𝑟𝑜𝑚 𝑝𝑎𝑛𝑑𝑎𝑠 𝑖𝑚𝑝𝑜𝑟𝑡 𝐷𝑎𝑡𝑎𝐹𝑟𝑎𝑚𝑒
-𝑓𝑟𝑜𝑚 𝑓𝑢𝑛𝑐𝑡𝑜𝑜𝑙𝑠 𝑖𝑚𝑝𝑜𝑟𝑡 𝑟𝑒𝑑𝑢𝑐𝑒
-𝑓𝑟𝑜𝑚 𝑠𝑘𝑙𝑒𝑎𝑟𝑛.𝑑𝑎𝑡𝑎𝑠𝑒𝑡𝑠 𝑖𝑚𝑝𝑜𝑟𝑡 𝑙𝑜𝑎𝑑_𝑖𝑟𝑖𝑠
-𝑖𝑚𝑝𝑜𝑟𝑡 𝑝𝑙𝑜𝑡𝑙𝑦.𝑔𝑟𝑎𝑝ℎ_𝑜𝑏𝑗𝑒𝑐𝑡𝑠 𝑎𝑠 𝑔𝑜
-𝑖𝑚𝑝𝑜𝑟𝑡 𝑛𝑏𝑓𝑜𝑟𝑚𝑎𝑡 

___The only issue that I encountered when running the program was after installing plotly.graph_objects, I had to install nbformat => 4.2.0 to display the candlestick chart.  After installing the nbformat, I also had to restart VS Code before it would plot the chart. ___

___ 3 𝐹𝑒𝑎𝑡𝑢𝑟𝑒𝑠 𝑇ℎ𝑎𝑡 𝐼 𝑈𝑠𝑒𝑑 𝑃𝑙𝑢𝑠 𝑂𝑡ℎ𝑒𝑟𝑠:
1) 𝑈𝑠𝑒𝑑 𝐴𝑃𝐼 𝑑𝑎𝑡𝑎 𝑎𝑛𝑑 𝐶𝑆𝑉 𝑑𝑎𝑡𝑎
2)𝑀𝑒𝑟𝑔𝑒, 𝐶𝑜𝑛𝑐𝑎𝑡, 𝑎𝑛𝑑 𝐽𝑜𝑖𝑛
3)𝐶𝑙𝑒𝑎𝑛𝑖𝑛𝑔 𝑜𝑓 𝑑𝑎𝑡𝑎
4) 𝑠𝑒𝑝𝑎𝑟𝑎𝑡𝑒 𝑝𝑙𝑜𝑡𝑙𝑦 𝑐ℎ𝑎𝑟𝑡𝑠, 5 𝑡𝑜𝑡𝑎𝑙
5)𝑐𝑟𝑒𝑎𝑡𝑖𝑛𝑔 𝑜𝑓 𝑎 𝑣𝑖𝑟𝑡𝑢𝑎𝑙 𝑒𝑛𝑣𝑖𝑟𝑜𝑛𝑚𝑒𝑛𝑡 ___

___This is just the beginning of this project, I plan on adding much more, especially visualizations with Tableau and other python libraries.  I also plan on possibly adding many more stocks and trying different sources and dataframes.  I would like to querie stock data in the end, and make it eligible for the user to do so also at will. ___


