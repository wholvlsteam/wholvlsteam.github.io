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

<p>去过的地方不多，但每到一个有历史层积的城市，都会发现书本上的地名突然有了重量。下面这张图是我到过的地方。</p>

<div class="note">
  <b>底图说明。</b>底图是本页原创绘制的<b>简化示意图</b>（见 <code>/img/history/world-map.svg</code>），只为标位置用，不是精确地图，也没有使用任何商业地图服务的截图。要换成更精细的底图，找公有领域或 ODbL 授权的世界地图替换即可。
</div>

<div class="map-wrap">
  <img src="/img/history/world-map.svg" alt="世界地图示意图，标注了到访过的城市位置">
  <span class="marker" style="left:76.29%; top:27.70%">1</span>
  <span class="marker" style="left:53.47%; top:26.72%">2</span>
  <span class="marker" style="left:87.71%; top:30.55%">3</span>
</div>

<!--
  加新地点的方法：在 <div class="map-wrap"> 里加一行
  <span class="marker" style="left:X%; top:Y%">序号</span>
  其中（按等距圆柱投影）：
    X = (经度 + 180) / 360 × 100
    Y = (90 − 纬度) / 180 × 100
  例如西安（东经108.95°，北纬34.27°）→ left:80.26%; top:30.96%
-->

<ul class="foot-list">
  <li><span class="idx">1</span><span><b>敦煌</b> · 甘肃 —— 莫高窟的洞窟比照片里暗得多，讲解员用手电扫过壁画时，颜色是一块一块浮出来的。</span></li>
  <li><span class="idx">2</span><span><b>罗马</b> · 意大利 —— 斗兽场旁边就是现代马路，古代和当下没有隔着围栏，是挤在一起的。</span></li>
  <li><span class="idx">3</span><span><b>京都</b> · 日本 —— 城市格局基本沿用了一千多年前的棋盘格，走在路上能感觉到规划本身是有年头的。</span></li>
</ul>

<h2>记录</h2>

<ul class="card-grid">
  <li>
    <div class="card">
      <span class="card-kicker">甘肃</span>
      <h3>敦煌</h3>
      <p>冲着莫高窟去的。真正意外的是鸣沙山——站在沙丘顶上能看见整个绿洲的边界，会立刻明白为什么这里能成为丝路的节点。</p>
    </div>
  </li>
  <li>
    <div class="card">
      <span class="card-kicker">意大利</span>
      <h3>罗马</h3>
      <p>把「文艺复兴」和「罗马帝国」两个条目从清单里的「简单了解」往「深度了解」推了一把。万神殿的穹顶和斗兽场的地下结构，看实物比看图强太多。</p>
    </div>
  </li>
  <li>
    <div class="card">
      <span class="card-kicker">日本</span>
      <h3>京都</h3>
      <p>去看唐风建筑的留存。逛寺院时反而对「日本怎么保存这些」更感兴趣——很多是近代重新营造的，但营造的逻辑本身值得琢磨。</p>
    </div>
  </li>
</ul>

<div class="note">
  <b>这些是示例条目，等你换成自己的。</b>把 <code>source/travel/index.md</code> 里的三个地点改成自己到过的地方，照片放进 <code>source/img/history/travel/</code>，然后在卡片里加 <code>&lt;img&gt;</code> 就行。自己拍的照片没有版权问题。
</div>

</div>
