# LOLHelper
League Of Legends LCU(LegueClient) API usage example.   
英雄联盟客户端API调用示例，调用API时需要先运行游戏并保证RiotClientServices通讯正常。
你可以通过以下方式确定：
```python
# lHelper = LoLHelper(port,token);
lHelper.get("riot-messaging-service/v1/state") # 如果返回 "Connected" 则说明 RiotClientServices 通讯正常。
```
此外，还需要确定账号的登录状态：
```python
# lHelper = LoLHelper(port,token);
lHelper.get("lol-summoner/v1/status") # 如果返回 { "ready":true } 则说明登录成功；否则可能登录失败或正在服务器排队队列中。
```
在这之后你可以正常调用LCU API（当然上述情况是先运行程序后运行游戏的情况下要做的，如果是后运行程序你完全可以爱搞不搞）   
你还可以在以下文档中了解到更多的LCU API：   
[LCU API文档](https://lcu.vivide.re/)   
Riot官方的开发者(LOL)文档：   
[Riot Developer Document](https://developer.riotgames.com/docs/lol)   
   
你可以在官方开发者文档里的Data Dragon（数据龙）中找到游戏中基本能看到的所有资源，例如召唤师技能，装备和英雄的图片资源等，Data Dragon会随着游戏版本的更新而更新（也可能提前或延后），Data Dragon是静态的数据，获取Data Dragon数据需要指定游戏版本，你可以通过 (https://ddragon.leagueoflegends.com/api/versions.json) 中第[1]个项、下标[0]来获取当前游戏的的版本。   
   
还有一件事：用到的第三方库需要自己去下载：requests 和 pustil，嗯、当然你也可以选择其他的。   
