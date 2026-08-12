docker exec -it 822f7e8fed41 mysql -uroot -p -e "SHOW DATABASES;"


docker compose -f mysql-setup.yaml up -d
docker compose -f mysql-setup.yaml down -v



导入数据
docker exec -i -e MYSQL_PWD=654321 mysql-dev mysql --default-character-set=utf8mb4 -u root data_mind < sales_orders_mysql.sql



数据概况

时间跨度：2024-01-01 ~ 2025-12-31（2年，25,606 条订单明细）
字段：order_id, order_date, region(区域), city(城市), product_category(品类), sku, sales_rep(销售代表), channel(线上/线下), customer_type(新/老客户), quantity, unit_price, discount_rate, revenue, cost, profit
内置真实感规律：618/双11/双12大促脉冲、春节走低、周末效应、整体年增长约25%、线上占比逐年上升、6个销售代表业绩强弱不同、老客户折扣更多


准备好的问题（从不同角度看图表）

趋势类

过去两年的月度销售额趋势是怎样的？
618和双11期间销售额和平时比涨了多少？
今年和去年同期相比，销售额同比增长了多少？

结构 / 占比类
4. 各产品品类的销售额占比是多少？
5. 线上和线下渠道的销售额占比变化趋势如何？
6. 新客户和老客户分别贡献了多少销售额？

区域 / 城市类
7. 各区域的销售额排名如何？
8. 哪个城市的利润率最高？

人员 / 绩效类
9. 各销售代表的业绩排名（Top6）？
10. 表现最好和最差的销售代表差距有多大？

利润 / 定价类
11. 各产品品类的利润率对比如何？
12. 折扣力度和利润之间有什么关系？

交叉分析类
13. 各区域在不同产品品类上的销售额分布（热力图）？
14. 各渠道在新老客户上的转化差异？