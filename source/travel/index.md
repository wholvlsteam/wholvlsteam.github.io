---
title: 旅行足迹
date: 2026-09-25 14:40:00
layout: page
comments: false
top_img: false
---

<div class="hist">

<div class="hist-hero">
  <img class="ornament" src="/img/history/ornament.svg" alt="">
  <h1>旅行足迹</h1>
  <p class="sub">到过的历史现场</p>
</div>

<p>记的是真正到过的地方，不是想去的地方。图上的点按经纬度定位，编号和下面的条目一一对应。</p>

<div class="map-wrap">
  <div class="map-inner">
  <img src="/img/history/china-map.jpg" alt="中国地图，标注了到访过的 13 个地点">
  <span class="pin" style="left:62.48%; top:43.36%; --tx:16px; --ty:0px; --len:16.0px; --ang:0.0deg" title="西安"><i></i><b>1</b></span>
  <span class="pin" style="left:62.06%; top:43.39%; --tx:-8px; --ty:14px; --len:16.1px; --ang:119.7deg" title="咸阳"><i></i><b>2</b></span>
  <span class="pin" style="left:62.45%; top:42.36%; --tx:-16px; --ty:0px; --len:16.0px; --ang:180.0deg" title="铜川"><i></i><b>3</b></span>
  <span class="pin" style="left:62.95%; top:41.13%; --tx:-14px; --ty:-8px; --len:16.1px; --ang:-150.3deg" title="黄陵"><i></i><b>4</b></span>
  <span class="pin" style="left:63.51%; top:36.28%; --tx:0px; --ty:0px; --len:0.0px; --ang:0.0deg" title="榆林"><i></i><b>5</b></span>
  <span class="pin" style="left:65.74%; top:34.85%; --tx:0px; --ty:0px; --len:0.0px; --ang:0.0deg" title="府谷"><i></i><b>6</b></span>
  <span class="pin" style="left:65.01%; top:40.03%; --tx:0px; --ty:0px; --len:0.0px; --ang:0.0deg" title="壶口瀑布"><i></i><b>7</b></span>
  <span class="pin" style="left:54.39%; top:36.08%; --tx:0px; --ty:0px; --len:0.0px; --ang:0.0deg" title="阿拉善"><i></i><b>8</b></span>
  <span class="pin" style="left:74.69%; top:32.63%; --tx:0px; --ty:0px; --len:0.0px; --ang:0.0deg" title="北京"><i></i><b>9</b></span>
  <span class="pin" style="left:84.89%; top:46.95%; --tx:4px; --ty:18px; --len:18.4px; --ang:77.5deg" title="苏州"><i></i><b>10</b></span>
  <span class="pin" style="left:84.19%; top:46.55%; --tx:-6px; --ty:-18px; --len:19.0px; --ang:-108.4deg" title="无锡"><i></i><b>11</b></span>
  <span class="pin" style="left:78.43%; top:46.70%; --tx:-14px; --ty:8px; --len:16.1px; --ang:150.3deg" title="合肥"><i></i><b>12</b></span>
  <span class="pin is-next" style="left:72.02%; top:39.68%; --tx:0px; --ty:0px; --len:0.0px; --ang:0.0deg" title="安阳（计划中）"><i></i><b>13</b></span>
  </div>
</div>

<p class="map-cap">
  <b>底图</b>：自然资源部标准地图服务 · 中国地图（1:1000 万，竖版，分省设色，无邻国），<b>审图号 GS(2022)4312号</b>。整幅图廓含南海诸岛及图例完整保留，未裁切、未改动边界或图内要素，仅为适配网页做了等比缩小；图上的圆点是按经纬度换算后叠加的标注，不属于底图内容。<br>
  实心点 = 已到过，空心点 = 计划中。<span class="map-hint">窄屏上这张图可以左右拖动。</span>
</p>

<!--
  加新地点：改 _pins.py 里的 PLACES（编号, 地名, 经度, 纬度, 徽章偏移x, 徽章偏移y），
  跑一下 python _pins.py，把输出的 <span class="pin"> 贴到上面的 .map-inner 里。
  徽章偏移是为了把挨太近的点岔开（西安到咸阳在图上只有 8px），改完看一眼有没有叠住。
  底图不能换 —— 换了之后 _pins.py 开头那组投影拟合常数就全作废了。
-->

<h2>陕北那条线</h2>

<p>从关中一路往北，地貌一层层抬上去：过了铜川进黄土高原，再往北就是毛乌素沙地的边缘。</p>

<ul class="foot-list">
  <li><span class="idx">1</span><span><b>西安</b> · 陕西 —— 十三朝古都。汉长安城和隋唐长安城叠在同一片地方，今天看到的城墙是明代的，但城址从隋代起就没挪过。</span></li>
  <li><span class="idx">2</span><span><b>咸阳</b> · 陕西 —— 秦都。咸阳宫在渭河北岸，和西安隔河相望——秦汉和隋唐的都城其实挤在一小块地方。</span></li>
  <li><span class="idx">3</span><span><b>铜川</b> · 陕西 —— 耀州窑的产地，宋代北方青瓷的中心之一。</span></li>
  <li><span class="idx">4</span><span><b>黄陵</b> · 陕西 —— 黄帝陵所在。桥山的柏树林是有名的。</span></li>
  <li><span class="idx">5</span><span><b>榆林</b> · 陕西 —— 明长城九边重镇之一（延绥镇）。城北就是毛乌素沙地。</span></li>
  <li><span class="idx">6</span><span><b>府谷</b> · 陕西 —— 陕西最北的县。黄河在这里拐弯，对岸是山西。</span></li>
</ul>

<h2>黄河与沙漠</h2>

<ul class="foot-list">
  <li><span class="idx">7</span><span><b>壶口瀑布</b> · 晋陕交界 —— 黄河在晋陕峡谷收窄成一道壶口。下游河道在黄土里摆动得厉害，「三十年河东，三十年河西」说的就是这一段。</span></li>
  <li><span class="idx">8</span><span><b>阿拉善</b> · 内蒙古 —— 内蒙古最西边的盟。腾格里、巴丹吉林、乌兰布和三个沙漠都在境内。</span></li>
</ul>

<h2>北京</h2>

<ul class="foot-list">
  <li><span class="idx">9</span><span><b>北京</b> —— 元大都、明清北京城。中轴线从元代定下来，一直用到今天。</span></li>
</ul>

<h2>江淮</h2>

<ul class="foot-list">
  <li><span class="idx">10</span><span><b>苏州</b> · 江苏 —— 春秋吴国的都城。今天看到的园林和水巷格局是明清留下的。</span></li>
  <li><span class="idx">11</span><span><b>无锡</b> · 江苏 —— 太湖边。鸿山遗址出过春秋战国的越国贵族墓。</span></li>
  <li><span class="idx">12</span><span><b>合肥</b> · 安徽 —— 三国时的合肥新城，魏和吴在这里拉锯了几十年。</span></li>
</ul>

<h2>下一站</h2>

<ul class="foot-list">
  <li><span class="idx">13</span><span><b>安阳</b> · 河南 <span class="todo">计划中</span> —— 殷墟。甲骨文出自这里，商代后期的都城。</span></li>
</ul>

<h2>这条线怎么串起来</h2>

<ul class="card-grid">
  <li>
    <div class="card">
      <span class="card-kicker">地形</span>
      <h3>关中到河套</h3>
      <p>从西安往北是一条完整的剖面：渭河平原、黄土高原、毛乌素沙地。这条线大致也是古代从中原通往河套的路，榆林、府谷这些点就是这么摆上去的。</p>
    </div>
  </li>
  <li>
    <div class="card">
      <span class="card-kicker">河流</span>
      <h3>黄河的中段</h3>
      <p>壶口在晋陕峡谷的中段，黄河在这里被两岸的黄土夹住。出了峡谷往南，河道在冲积平原上摆动得很厉害，改道是常态。</p>
    </div>
  </li>
  <li>
    <div class="card">
      <span class="card-kicker">下游</span>
      <h3>长江三角洲</h3>
      <p>苏州、无锡都贴着太湖，一东一西。这一带春秋时是吴、越拉锯的地方；合肥稍靠西，三国时又成了魏吴对峙的前线。</p>
    </div>
  </li>
</ul>

<div class="note">
  <b>说明。</b>每条下面给的是这处地方在历史上的位置，用来和清单里的条目对照。自己的见闻和照片还在慢慢补，<span class="todo">待补充</span>。
</div>

</div>
