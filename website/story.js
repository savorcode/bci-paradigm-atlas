// BCI Paradigm Atlas one-page site. The brain-signal traces in the mini games are simulated; all atlas numbers and links come from story-data.json.
"use strict";
fetch("./story-data.json").then(r=>{ if(!r.ok) throw new Error(r.status); return r.json(); }).then(boot).catch(err=>{ console.error(err); const m=document.getElementById("loadErr"); if(m) m.hidden=false; });
function boot(DATA){

const T = {
zh:{brand:"脑机范式图谱",tag:"开放数据 · 每条连线都有出处",
 h1:'<span class="nw">让大脑开口说话的</span> <span class="nw"><span class="num">404</span> 个<span class="hl">小游戏</span></span>',
 lede:"脑机接口靠“范式”和大脑对话：一个精心设计的小任务，让大脑发出能被读出来的信号。图谱把范式、信号、脑区和心理过程连成一张有出处的网。",
 mini:["个具体范式","种神经信号","条有出处的连线"],go1:"▶ 先玩一局",go2:"看知识网络",stageHint:"在大脑上划一划，让神经元放电",
 lobes:{frontal:"额叶",central:"中央区",parietal:"顶叶",temporal:"颞叶",occipital:"枕叶",deep:"深部",cerebellum:"小脑"},
 l1k:"大脑实验室",l1h:"三个小游戏，三种让大脑“开口”的方法",tab1:"Oddball 反应",tab2:"SSVEP 目光打字",tab3:"运动想象",
 oddReady:"点“开始”，看到粉色就点屏幕或按空格",oddGo:"看到粉色就点！",oddDone:"完成！看看右边的平均波形",
 oddP:"每次稀有的粉色出现，约 300–600 毫秒后头顶偏后会冒出一个正波，叫 P3b。单次试次被噪声淹没，平均的次数越多，它就越清楚。脑机拼写器就是靠它工作的。",
 lgT:"粉色平均",lgS:"蓝色平均",lgR:"单次试次",sHit:"抓到粉色",sFa:"误点蓝色",sRt:"平均反应 ms",start:"开始（约 25 秒）",again:"再来一局",stop:"停止",
 sim:"脑电为模拟信号，时间与极性按真实 P3b 设定",
 ssP:"每个方块以不同频率明暗变化。盯着哪个，视觉皮层就跟着哪个频率“共振”，频谱上冒出尖峰，电脑据此判断你在看哪里。盯住 1 秒，字母就打出来了。",
 ssIdle:"把鼠标停在（或手指按住）一个方块上",ssLook:"正在盯 {f} Hz…",clear:"清空",ssSafe:"方块用柔和的明暗变化代替真实闪烁；真实实验的闪烁频率在 6–20 Hz。",
 miGoal:"把小球推进粉色的门",miBest:"用时 {s} 秒",miWin:"进门！用时 {s} 秒，再来一次会换门",L:"左",R:"右",hL:"按住：想象左手握拳",hR:"按住：想象右手握拳",
 miP:"想象一只手运动时，对侧运动皮层的 μ 节律（8–13 Hz）会减弱：想左手，右脑 C4 下降；想右手，左脑 C3 下降。这种左右差异可以用来控制轮椅或光标。",
 miNote:"也可以用键盘 ← → 。信号为模拟，偏侧化方向与真实的感觉运动节律一致。",mu:"μ 节律功率",
 l2k:"知识网络",l2h:"信号从哪个脑区来，又在说什么",l2p:"圆环分三段：粉色是脑区，黄色是神经信号，蓝色是心理过程。点任意一个点，相连的线就亮起来；每条线都有证据等级和文献。",
 grades:{A:"元分析或跨实验室反复验证",B:"多项独立研究支持",C:"单项研究或间接证据"},
 caps:["脑区","神经信号","心理过程"],gen:"来源脑区",idx:"反映的心理过程",usedIn:"出现在 {n} 个范式中",linkedM:"与它相连的信号",all:"选择一个信号…",
 types:{erp_component:"事件相关电位",oscillatory:"节律变化",steady_state:"稳态响应",hemodynamic:"血流信号",single_unit:"神经元放电",field_potential:"场电位",connectivity:"脑区间连接"},
 region:"脑区",construct:"心理过程",
 l3k:"全图谱",l3h:"12 个家族，404 个范式",l3p:"每个圆点是一个可以复现的具体范式。点一点，或者随机抽一个。",rand:"🎲 随机抽一个",
 sigs:"会引出的信号（点击查看网络）",noSig:"这个范式的信号还在整理",statL:["范式类","神经信号","文献"],allFam:"全部",
 l4k:"范式工厂试运行",l4h:"说出想测什么，图谱帮你挑信号和范式",l4p:"这是范式工厂的第一步：从图谱里找到能反映这个心理过程、证据最硬的信号，再挑出能引出它们的范式，拼成一个试次结构。",
 pick:"选一个心理过程",st1:"你想测",st2:"能反映它的信号",st3:"能引出信号的范式",st4:"一个试次长这样",nSig:"图谱里有 {n} 个信号能反映它，亮起的是它们的来源脑区",mEmpty:"图谱里还没有反映它的信号",clickSig:"点信号可在知识网络里查看",
 tl:{fix:"注视",cue:"提示",stim:"刺激",resp:"反应",fb:"反馈",rest:"休息",task:"任务",flick:"闪烁"},tlNote:"按{t}的典型时长示意；真实工厂会按设备、导联和总时长生成完整方案。",
 endH:"数据全部开源，欢迎一起补充",cta1:"在 GitHub 上浏览 ↗",cta2:"参与贡献 ↗",f1:"思维刻度 SavorCode 发起并维护 · 脑机范式图谱",classic:"完整范式目录（可检索）",f2:"代码 Apache-2.0 · 数据 CC BY 4.0",ms:"毫秒"},
en:{brand:"BCI Paradigm Atlas",tag:"Open data · every link is cited",
 h1:'<span class="num">404</span> little <span class="hl">games</span> that make the brain talk',
 lede:"Brain–computer interfaces talk to the brain through paradigms: small, carefully designed tasks that make the brain produce a readable signal. The atlas links paradigms, signals, brain regions and mental processes into one cited network.",
 mini:["concrete paradigms","neural signals","cited links"],go1:"▶ Play a round",go2:"Explore the network",stageHint:"Swipe across the brain to fire some neurons",
 lobes:{frontal:"Frontal",central:"Central",parietal:"Parietal",temporal:"Temporal",occipital:"Occipital",deep:"Deep",cerebellum:"Cerebellum"},
 l1k:"Brain lab",l1h:"Three mini games, three ways to make the brain talk",tab1:"Oddball reaction",tab2:"SSVEP gaze typing",tab3:"Motor imagery",
 oddReady:"Press Start, then tap the screen or hit Space on pink",oddGo:"Tap on pink!",oddDone:"Done! See the averaged waves",
 oddP:"About 300–600 ms after each rare pink one, a positive wave called the P3b rises over the back of the head. A single trial is buried in noise; the more trials you average, the clearer it gets. P300 spellers work this way.",
 lgT:"Pink average",lgS:"Blue average",lgR:"Single trials",sHit:"Pink caught",sFa:"Blue clicked",sRt:"Mean RT ms",start:"Start (about 25 s)",again:"Play again",stop:"Stop",
 sim:"Simulated EEG with the real P3b timing and polarity",
 ssP:"Each tile pulses at its own frequency. Whichever one you look at, your visual cortex locks onto that frequency and the spectrum shows a peak, so the computer knows where you are looking. Hold your gaze for a second to type the letter.",
 ssIdle:"Hover over (or press and hold) a tile",ssLook:"Looking at {f} Hz…",clear:"Clear",ssSafe:"Tiles use a gentle brightness change instead of real flicker; real experiments flicker at 6–20 Hz.",
 miGoal:"Push the ball into the pink gate",miBest:"Time {s} s",miWin:"In! {s} s. The gate switches sides next round",L:"L",R:"R",hL:"Hold: imagine squeezing your left hand",hR:"Hold: imagine squeezing your right hand",
 miP:"Imagining a hand movement weakens the mu rhythm (8–13 Hz) over the opposite motor cortex: left hand, C4 on the right drops; right hand, C3 on the left drops. That left–right difference can steer a wheelchair or a cursor.",
 miNote:"Arrow keys ← → work too. Simulated signal with the real lateralisation.",mu:"Mu power",
 l2k:"Knowledge network",l2h:"Where a signal comes from, and what it says",l2p:"The ring has three arcs: pink for brain regions, yellow for neural signals, blue for mental processes. Click any dot to light up its links; each link carries an evidence grade and a paper.",
 grades:{A:"Meta-analysis or replicated across labs",B:"Several independent studies",C:"A single study or indirect evidence"},
 caps:["Regions","Signals","Processes"],gen:"Generated in",idx:"Reflects",usedIn:"Used in {n} paradigms",linkedM:"Linked signals",all:"Pick a signal…",
 types:{erp_component:"Event-related potential",oscillatory:"Rhythm change",steady_state:"Steady-state response",hemodynamic:"Blood-flow signal",single_unit:"Neuron firing",field_potential:"Field potential",connectivity:"Connectivity"},
 region:"Brain region",construct:"Mental process",
 l3k:"The whole atlas",l3h:"12 families, 404 paradigms",l3p:"Each dot is a concrete, reproducible paradigm. Click one, or draw one at random.",rand:"🎲 Random pick",
 sigs:"Signals it evokes (click for the network)",noSig:"Signals for this paradigm are still being curated",statL:["Paradigm classes","Neural signals","Papers"],allFam:"All",
 l4k:"Paradigm Factory test run",l4h:"Say what you want to measure; the atlas picks signals and paradigms",l4p:"This is the factory's first step: find the signals that reflect the process with the strongest evidence, pick paradigms that evoke them, and lay out a trial.",
 pick:"Pick a mental process",st1:"You want to measure",st2:"Signals that reflect it",st3:"Paradigms that evoke them",st4:"One trial looks like this",nSig:"{n} signals in the atlas reflect it; their source regions light up",mEmpty:"No signal in the atlas reflects this yet",clickSig:"Click a signal to see it in the network",
 tl:{fix:"Fixation",cue:"Cue",stim:"Stimulus",resp:"Response",fb:"Feedback",rest:"Rest",task:"Task",flick:"Flicker"},tlNote:"Typical timing for {t}; the real factory builds the full plan for your device, channels and time budget.",
 endH:"All data is open. Come and add to it",cta1:"Browse on GitHub ↗",cta2:"Contribute ↗",f1:"Initiated and maintained by SavorCode · BCI Paradigm Atlas",classic:"Full searchable catalog",f2:"Code Apache-2.0 · Data CC BY 4.0",ms:"ms"}
};
let lang="zh"; try{const s=localStorage.getItem("atlas-lang"); if(s==="en"||s==="zh") lang=s;}catch(e){}
if(location.hash==="#en"||location.hash==="#zh") lang=location.hash.slice(1);
const L=()=>T[lang];
const t=(k,v)=>{let s=L()[k]??k; if(v) for(const[a,b] of Object.entries(v)) s=s.replace("{"+a+"}",b); return s;};
const fmt=n=>n.toLocaleString(lang==="zh"?"zh-CN":"en-US");
const nm=o=>o?(lang==="zh"?o[0]:o[1]):"";
const short=s=>s.replace(/（.*?）|\s*\(.*?\)/g,"").trim();
const css=v=>getComputedStyle(document.documentElement).getPropertyValue(v).trim();
const reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;
const $=id=>document.getElementById(id);
const FAMCOL={PER:"--sky",MOT:"--sun",SSR:"--mint",ERR:"--pink",LAN:"--grape",MEM:"--sky",EMO:"--pink",CTL:"--mint",IMG:"--grape",SOC:"--sun",STA:"--sky",STM:"--pink"};
const LOBECOL={frontal:"--pink",central:"--sun",parietal:"--mint",temporal:"--sky",occipital:"--grape",deep:"--sun",cerebellum:"--mint"};
const MK=Object.fromEntries(DATA.M.map(m=>[m.id,m]));

/* ================= hero: particle brain ================= */
const Brain=(()=>{
  const cv=$("brainc"),ctx=cv.getContext("2d"); let W,H,dpr,nodes=[],edges=[],pulses=[],glow=new Set(),ptr=null;
  const lobeShapes={ // in a 300x230 box, brain facing left
    frontal:"M24 128 C14 82 46 40 104 32 C118 30 130 30 140 32 L132 134 C96 142 56 142 24 128 Z",
    central:"M140 32 C150 33 160 36 170 40 L152 132 L132 134 Z",
    parietal:"M170 40 C210 46 240 68 252 100 L210 124 L152 132 Z",
    occipital:"M252 100 C270 120 274 148 258 166 C238 158 222 146 210 124 Z",
    temporal:"M58 140 C96 146 146 138 204 126 C214 146 226 160 244 168 C214 184 160 190 112 180 C84 172 64 158 58 140 Z",
    cerebellum:"M196 176 C222 168 252 168 266 182 C270 202 242 214 216 208 C202 204 194 192 196 176 Z"};
  const paths=Object.fromEntries(Object.entries(lobeShapes).map(([k,d])=>[k,new Path2D(d)]));
  let sc,ox,oy;
  function build(){
    dpr=Math.min(devicePixelRatio||1,2); W=cv.clientWidth; H=cv.clientHeight; cv.width=W*dpr; cv.height=H*dpr; ctx.setTransform(dpr,0,0,dpr,0,0);
    sc=Math.min(W/300,H/235)*.92; ox=(W-300*sc)/2; oy=(H-225*sc)/2+6;
    nodes=[]; const per=Math.round(Math.max(260,Math.min(520,W*H/700)));
    let tries=0; const off=document.createElement("canvas").getContext("2d");
    while(nodes.length<per && tries<per*40){ tries++;
      const x=10+Math.random()*265,y=25+Math.random()*195;
      for(const k in paths){ if(off.isPointInPath(paths[k],x,y)){ nodes.push({x:ox+x*sc,y:oy+y*sc,l:k,e:0}); break; } }
      if(Math.random()<.002){ const x2=150+(Math.random()-.5)*44,y2=118+(Math.random()-.5)*28; nodes.push({x:ox+x2*sc,y:oy+y2*sc,l:"deep",e:0}); }
    }
    edges=[]; const R=17*sc;
    for(let i=0;i<nodes.length;i++){ let c=0; for(let j=i+1;j<nodes.length&&c<4;j++){ const dx=nodes[i].x-nodes[j].x,dy=nodes[i].y-nodes[j].y; if(dx*dx+dy*dy<R*R){ edges.push([i,j]); c++; } } }
    nodes.forEach((n,i)=>n.nb=[]); edges.forEach(([a,b])=>{nodes[a].nb.push(b);nodes[b].nb.push(a);});
  }
  function fire(i,str=1){ const n=nodes[i]; if(!n) return; n.e=Math.max(n.e,str); if(str>.25) n.nb.forEach(j=>{ if(Math.random()<.55) pulses.push({a:i,b:j,t:0,s:str*.82}); }); }
  function near(x,y){ let best=-1,bd=1e9; nodes.forEach((n,i)=>{const d=(n.x-x)**2+(n.y-y)**2; if(d<bd){bd=d;best=i;}}); return bd<900?best:-1; }
  let last=0;
  function frame(tm){
    const dt=Math.min(50,tm-last||16); last=tm;
    ctx.clearRect(0,0,W,H);
    const col={}; for(const k in LOBECOL) col[k]=css(LOBECOL[k]); const base=css("--on-deep");
    ctx.save(); ctx.translate(ox,oy); ctx.scale(sc,sc); for(const k in paths){ ctx.globalAlpha=glow.has(k)?.22:.07; ctx.fillStyle=col[k]; ctx.fill(paths[k]); ctx.globalAlpha=.18; ctx.strokeStyle=base; ctx.lineWidth=1.2/sc; ctx.stroke(paths[k]); } ctx.restore();
    ctx.lineWidth=1;
    for(const [a,b] of edges){ const A=nodes[a],B=nodes[b]; const e=Math.max(A.e,B.e); ctx.strokeStyle=base; ctx.globalAlpha=.07+e*.4; ctx.beginPath(); ctx.moveTo(A.x,A.y); ctx.lineTo(B.x,B.y); ctx.stroke(); }
    for(let k=pulses.length-1;k>=0;k--){ const p=pulses[k]; p.t+=dt/260; const A=nodes[p.a],B=nodes[p.b];
      if(p.t>=1){ pulses.splice(k,1); if(p.s>.22 && nodes[p.b].e<p.s*.9) fire(p.b,p.s); continue; }
      const x=A.x+(B.x-A.x)*p.t,y=A.y+(B.y-A.y)*p.t; ctx.globalAlpha=Math.min(1,p.s+.2); ctx.fillStyle=col[A.l]; ctx.beginPath(); ctx.arc(x,y,2.4,0,7); ctx.fill(); }
    if(pulses.length>900) pulses.splice(0,pulses.length-900);
    for(const n of nodes){ n.e*=Math.pow(.93,dt/16); const r=1.6+n.e*3.4+(glow.has(n.l)?1:0);
      ctx.globalAlpha=.45+n.e*.55+(glow.has(n.l)?.3:0); ctx.fillStyle=col[n.l]; ctx.beginPath(); ctx.arc(n.x,n.y,r,0,7); ctx.fill(); }
    ctx.globalAlpha=1;
    if(!reduce && Math.random()<dt/420) fire(Math.floor(Math.random()*nodes.length),.7);
    requestAnimationFrame(frame);
  }
  cv.addEventListener("pointermove",e=>{const r=cv.getBoundingClientRect(); const i=near(e.clientX-r.left,e.clientY-r.top); if(i>=0) fire(i,.9);});
  cv.addEventListener("pointerdown",e=>{const r=cv.getBoundingClientRect(); const i=near(e.clientX-r.left,e.clientY-r.top); if(i>=0) fire(i,1);});
  build(); addEventListener("resize",()=>{clearTimeout(Brain._t); Brain._t=setTimeout(build,150);});
  requestAnimationFrame(frame); for(let k=0;k<6;k++) fire(Math.floor(Math.random()*nodes.length),1);
  return {lightLobes(ls){glow=new Set(ls); nodes.forEach((n,i)=>{ if(glow.has(n.l)&&Math.random()<.12) fire(i,.8); });}};
})();
function renderLobeLegend(){ $("lobeLegend").innerHTML=Object.entries(L().lobes).map(([k,v])=>`<span>${v}<i style="background:var(${LOBECOL[k]})"></i></span>`).join(""); }

/* ================= game 1: oddball ================= */
const erp=$("erp"); const X0=40,X1=430,Y0=112,SC=10;
const xp=ms=>X0+(ms+100)/900*(X1-X0);
const MS=[]; for(let ms=-100;ms<=800;ms+=10) MS.push(ms);
const clean=(tg)=>MS.map(ms=>{ if(ms<=0) return 0; let v=1.6*Math.exp(-(((ms-100)/22)**2))-2.2*Math.exp(-(((ms-170)/30)**2))+1.4*Math.exp(-(((ms-230)/35)**2)); if(tg) v+=7.5*Math.exp(-(((ms-400)/95)**2)); return v; });
const CLEAN={t:clean(true),s:clean(false)};
const noisy=tg=>{ let ph=Math.random()*6, a=2+Math.random()*2; return CLEAN[tg?"t":"s"].map((v,i)=>v*(.7+Math.random()*.6)+a*Math.sin(i*.55+ph)+ (Math.random()-.5)*3.5); };
let odd={trials:[],sum:{t:null,s:null},n:{t:0,s:0},hits:0,fa:0,rts:[],timer:null,cur:null,shownAt:0,count:0,responded:false};
function seedOdd(){ odd={...odd,trials:[],sum:{t:CLEAN.t.map(()=>0),s:CLEAN.s.map(()=>0)},n:{t:0,s:0}}; for(let k=0;k<60;k++){ addTrial(k%4===0); } }
function addTrial(tg){ const tr=noisy(tg); odd.trials.push({tg,tr}); if(odd.trials.length>10) odd.trials.shift(); const key=tg?"t":"s"; odd.sum[key]=odd.sum[key].map((v,i)=>v+tr[i]); odd.n[key]++; }
const pathOf=arr=>arr.map((v,i)=>(i?"L":"M")+xp(MS[i]).toFixed(1)+" "+(Y0-v*SC).toFixed(1)).join("");
function drawERP(){
  const avg=k=>odd.n[k]?odd.sum[k].map(v=>v/odd.n[k]):CLEAN[k].map(()=>0);
  const at=avg("t"), peak=Math.max(...at.slice(40,70));
  erp.innerHTML=`<rect x="${xp(300)}" y="10" width="${xp(600)-xp(300)}" height="168" rx="10" fill="var(--sun)" opacity=".2"/>
   <line x1="${X0}" y1="${Y0}" x2="${X1}" y2="${Y0}" stroke="var(--line)" stroke-width="2"/>
   <line x1="${xp(0)}" y1="14" x2="${xp(0)}" y2="178" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 4"/>
   ${[0,200,400,600,800].map(v=>`<text x="${xp(v)}" y="194" text-anchor="middle" font-size="11" font-weight="700" fill="var(--muted)">${v}</text>`).join("")}
   <text x="${X1}" y="182" text-anchor="end" font-size="10" fill="var(--muted)">${t("ms")}</text><text x="6" y="22" font-size="10" font-weight="800" fill="var(--muted)">+µV</text>
   ${odd.trials.map(x=>`<path d="${pathOf(x.tr)}" fill="none" stroke="var(${x.tg?"--pink":"--sky"})" stroke-width="1" opacity=".22"/>`).join("")}
   <path d="${pathOf(avg("s"))}" fill="none" stroke="var(--sky)" stroke-width="3.2" stroke-linecap="round"/>
   <path d="${pathOf(at)}" fill="none" stroke="var(--pink)" stroke-width="4" stroke-linecap="round"/>
   <g transform="translate(${xp(400)},${Math.max(28,Y0-peak*SC-12)})"><rect x="-44" y="-17" width="88" height="22" rx="11" fill="var(--ink)"/><text y="-2" text-anchor="middle" font-size="11.5" font-weight="800" fill="var(--bg)">P3b · n=${odd.n.t}</text></g>`;
}
const blob=$("blob"), oddScreen=$("oddScreen");
function oddUI(){ $("oddTrial").textContent=`${odd.count} / 40`; $("sHit").textContent=odd.count?odd.hits:"–"; $("sFa").textContent=odd.count?odd.fa:"–"; $("sRt").textContent=odd.rts.length?Math.round(odd.rts.reduce((a,b)=>a+b,0)/odd.rts.length):"–"; }
function oddStep(){
  if(odd.count>=40){ oddStop(true); return; }
  const tg=odd.count>1 && Math.random()<.2; odd.cur=tg; odd.responded=false; odd.count++; odd.shownAt=performance.now();
  blob.classList.toggle("t",tg); blob.classList.remove("hit"); blob.classList.add("pop"); setTimeout(()=>blob.classList.remove("pop"),120);
  addTrial(tg); drawERP(); oddUI();
}
function oddStop(done){ clearInterval(odd.timer); odd.timer=null; $("oddGo").textContent=t("again"); $("oddMsg").textContent=done?t("oddDone"):t("oddReady"); }
function oddRespond(){
  if(!odd.timer||odd.responded) return; odd.responded=true;
  if(odd.cur){ odd.hits++; odd.rts.push(performance.now()-odd.shownAt); blob.classList.add("hit"); } else { odd.fa++; }
  oddUI();
}
$("oddGo").addEventListener("click",()=>{ if(odd.timer){ oddStop(false); return; }
  odd.trials=[]; odd.sum={t:CLEAN.t.map(()=>0),s:CLEAN.s.map(()=>0)}; odd.n={t:0,s:0}; odd.hits=0; odd.fa=0; odd.rts=[]; odd.count=0;
  $("oddGo").textContent=t("stop"); $("oddMsg").textContent=t("oddGo"); oddStep(); odd.timer=setInterval(oddStep,620); oddScreen.focus({preventScroll:true}); });
oddScreen.addEventListener("pointerdown",oddRespond);
document.addEventListener("keydown",e=>{ if(e.code==="Space" && odd.timer && !$("g-odd").hidden){ e.preventDefault(); oddRespond(); }
  if(!$("g-mi").hidden && (e.key==="ArrowLeft"||e.key==="ArrowRight")){ e.preventDefault(); mi.dir=e.key==="ArrowLeft"?-1:1; } });
document.addEventListener("keyup",e=>{ if(e.key==="ArrowLeft"||e.key==="ArrowRight") mi.dir=0; });

/* ================= game 2: SSVEP ================= */
const FREQ=[8.6,10,12,15];
const LETTERS=["B","C","I","!"];
let ss={look:-1,since:0,last:1};
function buildTiles(){
  const cols=["--sky","--pink","--mint","--sun"];
  $("tiles").style.gridTemplateColumns="repeat(2,minmax(0,1fr))";
  $("tiles").innerHTML=FREQ.map((f,i)=>`<button class="tile" type="button" data-ix="${i}" style="background:var(${cols[i]})"><span class="fill"></span>${LETTERS[i]}<small>${f} Hz</small></button>`).join("");
  $("tiles").querySelectorAll(".tile").forEach(b=>{ const i=+b.dataset.ix;
    b.addEventListener("pointerenter",()=>{ss.look=i;ss.since=performance.now();});
    b.addEventListener("pointerdown",e=>{ss.look=i;ss.since=performance.now(); b.setPointerCapture?.(e.pointerId);});
    b.addEventListener("pointerleave",()=>{ if(ss.look===i) ss.look=-1; });
    b.addEventListener("pointerup",e=>{ if(e.pointerType!=="mouse") ss.look=-1; });
    b.addEventListener("click",e=>{ if(e.detail===0) type(i); }); });
}
function type(i){ const s=$("typed"); s.textContent=(s.textContent+LETTERS[i]).slice(-14); }
$("ssClear").addEventListener("click",()=>{$("typed").textContent="";});
function drawSpec(tm){
  if(ss.look>=0) ss.last=ss.look; const f0=FREQ[ss.last], X=f=>36+(f-4)/30*390, Y=v=>166-v*140;
  let bars=""; for(let f=4;f<=34;f+=.5){ let v=.07+.05*Math.abs(Math.sin(f*3.1+tm/700))+.04/(f/4);
    if(f0){ v+=.85*Math.exp(-(((f-f0)/.45)**2))+.38*Math.exp(-(((f-2*f0)/.5)**2)); }
    bars+=`<rect x="${X(f)-4}" y="${Y(v)}" width="8" height="${166-Y(v)}" rx="3" fill="var(${f0&&Math.abs(f-f0)<.6?"--pink":(f0&&Math.abs(f-2*f0)<.6?"--sun":"--sky")})" opacity="${f0&&(Math.abs(f-f0)<.6||Math.abs(f-2*f0)<.6)?1:.45}"/>`; }
  $("spec").innerHTML=`<line x1="36" y1="166" x2="430" y2="166" stroke="var(--line)" stroke-width="2"/>${bars}
   ${[5,10,15,20,25,30].map(f=>`<text x="${X(f)}" y="184" text-anchor="middle" font-size="11" font-weight="700" fill="var(--muted)">${f}</text>`).join("")}
   <text x="430" y="16" text-anchor="end" font-size="11" font-weight="800" fill="var(--muted)">Hz · Oz</text>
   ${f0?`<g transform="translate(${X(f0)},${Y(.95)-8})"><rect x="-34" y="-16" width="68" height="20" rx="10" fill="var(--ink)"/><text y="-2" text-anchor="middle" font-size="11" font-weight="800" fill="var(--bg)">${f0} Hz</text></g>`:""}`;
}
function ssLoop(tm){
  if(!$("g-ssvep").hidden){
    document.querySelectorAll(".tile").forEach((b,i)=>{ const k=reduce?1:(.78+.22*Math.sin(tm/1000*2*Math.PI*FREQ[i]/8)); b.style.filter=`brightness(${k.toFixed(3)})`;
      const fill=b.querySelector(".fill"); fill.style.height=(ss.look===i?Math.min(100,(tm-ss.since)/10):0)+"%"; });
    if(ss.look>=0 && tm-ss.since>1000){ type(ss.look); ss.since=tm; }
    $("ssNote").textContent=ss.look>=0?t("ssLook",{f:FREQ[ss.look]}):t("ssIdle");
    drawSpec(tm);
  }
  requestAnimationFrame(ssLoop);
}

/* ================= game 3: motor imagery ================= */
const mi={pos:0,dir:0,goal:1,start:0,best:null};
const ball=$("ball");
["hL","hR"].forEach((id,k)=>{ const b=$(id); const on=()=>{mi.dir=k?1:-1;b.classList.add("on");}; const off=()=>{ if(mi.dir===(k?1:-1)) mi.dir=0; b.classList.remove("on"); };
  b.addEventListener("pointerdown",e=>{e.preventDefault();on();}); ["pointerup","pointerleave","pointercancel"].forEach(ev=>b.addEventListener(ev,off)); });
function drawTopo(){
  const c3=mi.dir===1?.35:1, c4=mi.dir===-1?.35:1, cz=.85;
  const col=v=>v<.6?"var(--sky)":"var(--pink)";
  const bar=(x,v,lab)=>`<rect x="${x}" y="${170-v*120}" width="34" height="${v*120}" rx="8" fill="${col(v)}"/><text x="${x+17}" y="188" text-anchor="middle" font-size="12" font-weight="800" fill="var(--muted)">${lab}</text>`;
  $("topo").innerHTML=`<g transform="translate(110,100)">
     <circle r="78" fill="var(--soft)" stroke="var(--line)" stroke-width="3"/><path d="M-10 -77 L0 -92 L10 -77" fill="var(--soft)" stroke="var(--line)" stroke-width="3"/>
     <ellipse cx="-80" cy="0" rx="7" ry="16" fill="var(--soft)" stroke="var(--line)" stroke-width="3"/><ellipse cx="80" cy="0" rx="7" ry="16" fill="var(--soft)" stroke="var(--line)" stroke-width="3"/>
     ${[["C3",-42,c3],["Cz",0,cz],["C4",42,c4]].map(([l,x,v])=>`<circle cx="${x}" cy="0" r="${12+v*12}" fill="${col(v)}" opacity="${.35+v*.5}"/><text x="${x}" y="4" text-anchor="middle" font-size="11" font-weight="800" fill="var(--ink)">${l}</text>`).join("")}
     <text y="62" text-anchor="middle" font-size="11" font-weight="800" fill="var(--muted)">${t("mu")}</text></g>
   <line x1="250" y1="170" x2="430" y2="170" stroke="var(--line)" stroke-width="2"/>${bar(262,c3,"C3")}${bar(322,cz,"Cz")}${bar(382,c4,"C4")}`;
}
function miLoop(tm){
  if(!$("g-mi").hidden){
    if(!mi.start) mi.start=tm;
    mi.pos=Math.max(-1,Math.min(1,mi.pos+mi.dir*.012+(Math.random()-.5)*.006));
    ball.style.left=`calc(${50+mi.pos*41}% - 20px)`;
    if(mi.pos*mi.goal>=.98){ const s=((tm-mi.start)/1000).toFixed(1); $("miTime").textContent=t("miWin",{s}); mi.best=mi.best?Math.min(mi.best,+s):+s; $("miBest").textContent=t("miBest",{s:mi.best});
      mi.goal*=-1; mi.pos=0; mi.start=tm+600; setGoal(); }
    drawTopo();
  }
  requestAnimationFrame(miLoop);
}
function setGoal(){ document.querySelector(".goal.l").style.background=`color-mix(in srgb,var(${mi.goal<0?"--pink":"--sky"}) 40%,transparent)`; document.querySelector(".goal.r").style.background=`color-mix(in srgb,var(${mi.goal>0?"--pink":"--sky"}) 40%,transparent)`; }

/* tabs */
$("tabs").querySelectorAll(".tab").forEach(b=>b.addEventListener("click",()=>{
  $("tabs").querySelectorAll(".tab").forEach(x=>x.setAttribute("aria-selected",x===b)); ["odd","ssvep","mi"].forEach(g=>$("g-"+g).hidden=g!==b.dataset.g);
  if(b.dataset.g!=="odd" && odd.timer) oddStop(false); mi.start=0; }));

/* ================= network ================= */
let selNode={k:"m",id:"P3b"}; const gOn={A:true,B:true,C:true};
const LOBEORD=["frontal","central","parietal","temporal","occipital","deep","cerebellum"];
const TYPEORD=["erp_component","oscillatory","steady_state","field_potential","single_unit","hemodynamic","connectivity"];
const NET=(()=>{
  const regs=Object.keys(DATA.R).sort((a,b)=>LOBEORD.indexOf(DATA.R[a][2])-LOBEORD.indexOf(DATA.R[b][2])||a.localeCompare(b));
  const mks=DATA.M.slice().sort((a,b)=>TYPEORD.indexOf(a.type)-TYPEORD.indexOf(b.type)||b.n-a.n).map(m=>m.id);
  const cons=Object.keys(DATA.C).sort();
  const gap=5, total=regs.length+mks.length+cons.length+gap*3, step=2*Math.PI/total;
  const pos={}; let k=0; const start=Math.PI*.5+step*gap*.5; // begin at bottom-left, go clockwise via left (regions), top (markers), right (constructs)
  const place=(arr,kind)=>{ arr.forEach(id=>{ const a=start+(k++)*step; pos[kind+":"+id]={a,kind,id}; }); k+=gap; };
  place(regs,"r"); place(mks,"m"); place(cons,"c");
  const edges=[]; DATA.M.forEach(m=>{ m.g.forEach(g=>edges.push({a:"r:"+g[0],b:"m:"+m.id,gr:g[1]})); m.x.forEach(x=>edges.push({a:"m:"+m.id,b:"c:"+x[0],gr:x[1]})); });
  return {regs,mks,cons,pos,edges};
})();
const CX=450,CY=450,RR=300;
const P=a=>[CX+RR*Math.cos(a+Math.PI/2),CY+RR*Math.sin(a+Math.PI/2)];
function drawNet(){
  const col={r:"--pink",m:"--sun",c:"--sky"};
  const label=(key)=>{ const p=NET.pos[key]; if(p.kind==="m") return short(nm([MK[p.id].zh,MK[p.id].en])); const d=p.kind==="r"?DATA.R[p.id]:DATA.C[p.id]; return short(nm(d)); };
  let s=`<circle class="ring" cx="${CX}" cy="${CY}" r="${RR}"/>`;
  [["regs","r","--pink"],["mks","m","--sun"],["cons","c","--sky"]].forEach(([k,p,c])=>{ const ids=NET[k]; const a0=NET.pos[p+":"+ids[0]].a, a1=NET.pos[p+":"+ids[ids.length-1]].a; const [x0,y0]=P(a0),[x1,y1]=P(a1);
    s+=`<path class="arc" d="M${x0.toFixed(1)} ${y0.toFixed(1)} A${RR} ${RR} 0 ${a1-a0>Math.PI?1:0} 1 ${x1.toFixed(1)} ${y1.toFixed(1)}" stroke="var(${c})"/>`; });
  NET.edges.forEach((e,i)=>{ const [x1,y1]=P(NET.pos[e.a].a),[x2,y2]=P(NET.pos[e.b].a); s+=`<path class="e" data-e="${i}" d="M${x1.toFixed(1)} ${y1.toFixed(1)} Q${CX} ${CY} ${x2.toFixed(1)} ${y2.toFixed(1)}" stroke="var(--g${e.gr})"/>`; });
  for(const key in NET.pos){ const p=NET.pos[key]; const [x,y]=P(p.a); const deg=(p.a+Math.PI/2)*180/Math.PI; const flip=Math.cos(p.a+Math.PI/2)<0;
    let lab=label(key); const max=lang==="zh"?9:20; if(lab.length>max) lab=lab.slice(0,max-1)+"…";
    s+=`<g class="n" data-k="${key}" tabindex="0"><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${p.kind==="m"?5:4.5}" fill="var(${col[p.kind]})"/>
      <text transform="translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${flip?deg+180:deg})" x="${flip?-10:10}" y="3" text-anchor="${flip?"end":"start"}">${lab}</text></g>`; }
  const capA=k=>{ const ids=NET[k]; const mid=NET.pos[(k==="regs"?"r:":k==="mks"?"m:":"c:")+ids[Math.floor(ids.length/2)]].a; return P(mid); };
  const caps=[["regs",0],["mks",1],["cons",2]].map(([k,i])=>{ const [x,y]=capA(k); const dx=(x-CX)*.62+CX, dy=(y-CY)*.62+CY; return `<text class="cap" x="${dx}" y="${dy}" text-anchor="middle">${L().caps[i]}</text>`; }).join("");
  $("netsvg").innerHTML=s+caps;
  $("netsvg").querySelectorAll(".n").forEach(g=>{ const go=()=>{ const [k,id]=g.dataset.k.split(":"); selNode={k,id}; highlight(); renderDetail(); };
    g.addEventListener("click",go); g.addEventListener("keydown",e=>{ if(e.key==="Enter"||e.key===" "){e.preventDefault();go();} });
    g.addEventListener("pointerenter",()=>highlight(g.dataset.k)); g.addEventListener("pointerleave",()=>highlight()); });
  highlight();
}
function highlight(hover){
  const key=hover||selNode.k+":"+selNode.id; const on=new Set([key]);
  $("netsvg").querySelectorAll(".e").forEach(p=>{ const e=NET.edges[+p.dataset.e]; const vis=gOn[e.gr]; const hit=vis&&(e.a===key||e.b===key); p.classList.toggle("on",hit); p.style.display=vis?"":"none"; if(hit){on.add(e.a);on.add(e.b);} });
  $("netsvg").querySelectorAll(".n").forEach(g=>{ g.classList.toggle("on",on.has(g.dataset.k)); g.classList.toggle("dim",!on.has(g.dataset.k)); const c=g.querySelector("circle"); c.setAttribute("r",on.has(g.dataset.k)?(g.dataset.k===key?9:6.5):(g.dataset.k.startsWith("m")?5:4.5)); });
}
const WAVES={erp_component:"M0 30 C20 30 24 30 30 34 S40 10 52 8 S66 30 74 30 L120 30",oscillatory:"M0 24 C6 12 12 36 18 24 S30 12 36 24 S48 34 54 26 S66 20 72 24 S90 26 96 24 S112 22 120 24",
 steady_state:"M0 24 L8 10 L16 38 L24 10 L32 38 L40 10 L48 38 L56 10 L64 38 L72 10 L80 38 L88 10 L96 38 L104 10 L112 38 L120 24",hemodynamic:"M0 34 C20 34 26 34 34 30 S50 8 64 10 S84 32 100 36 S114 34 120 34",
 connectivity:"M0 30 C20 10 40 10 60 30 S100 50 120 30 M0 18 C20 38 40 38 60 18 S100 -2 120 18",field_potential:"M0 26 L10 22 L14 30 L18 14 L22 34 L26 18 L30 28 L36 22 L44 30 L50 16 L56 34 L62 20 L70 28 L80 22 L90 30 L100 20 L110 28 L120 24",
 single_unit:"M0 30 L18 30 L20 6 L23 40 L26 30 L52 30 L54 6 L57 40 L60 30 L70 30 L72 6 L75 40 L78 30 L120 30"};
const ORD={A:0,B:1,C:2};
const lk=(name,x)=>`<div class="lk"><span class="g ${x[1]}" title="${L().grades[x[1]]}">${x[1]}</span><b>${name}</b>${x[5]?`<a href="https://doi.org/${x[5]}">${x[3]} · ${x[4]} ↗</a>`:`<em>${x[3]||""}</em>`}</div>`;
function renderDetail(){
  const d=$("detail");
  if(selNode.k==="m"){ const m=MK[selNode.id];
    const gs=m.g.filter(x=>gOn[x[1]]).sort((a,b)=>ORD[a[1]]-ORD[b[1]]), xs=m.x.filter(x=>gOn[x[1]]).sort((a,b)=>ORD[a[1]]-ORD[b[1]]);
    d.innerHTML=`<div class="dhead" style="background:var(--sun)"><span class="k">${L().types[m.type]||m.type}</span><b>${nm([m.zh,m.en])}</b>
      <svg viewBox="0 0 120 44" preserveAspectRatio="none" aria-hidden="true"><path d="${WAVES[m.type]||WAVES.erp_component}"/></svg><span class="k">MK.${m.id} · ${t("usedIn",{n:m.n})}</span></div>
      <div class="sub">${t("gen")}</div><div class="links">${gs.map(x=>lk(short(nm(DATA.R[x[0]])),x)).join("")}</div>
      <div class="sub">${t("idx")}</div><div class="links">${xs.map(x=>lk(short(nm(DATA.C[x[0]])),x)).join("")}</div>`;
    Brain.lightLobes(m.g.map(g=>DATA.R[g[0]][2]));
  } else {
    const isR=selNode.k==="r", info=isR?DATA.R[selNode.id]:DATA.C[selNode.id];
    const rows=[]; DATA.M.forEach(m=>(isR?m.g:m.x).forEach(x=>{ if(x[0]===selNode.id&&gOn[x[1]]) rows.push([m,x]); })); rows.sort((a,b)=>ORD[a[1][1]]-ORD[b[1][1]]);
    d.innerHTML=`<div class="dhead" style="background:var(${isR?"--pink":"--sky"})"><span class="k">${isR?t("region"):t("construct")}</span><b>${nm(info)}</b><span class="k">${selNode.id}</span></div>
      <div class="sub">${t("linkedM")}</div><div class="links">${rows.map(([m,x])=>lk(`<button class="chip" type="button" data-m="${m.id}">${short(nm([m.zh,m.en]))}</button>`,x)).join("")}</div>`;
    d.querySelectorAll("[data-m]").forEach(b=>b.addEventListener("click",()=>selectMarker(b.dataset.m)));
    if(isR) Brain.lightLobes([info[2]]);
  }
}
function selectMarker(id,scroll){ selNode={k:"m",id}; $("msel").value=id; highlight(); renderDetail(); if(scroll) $("net").scrollIntoView({behavior:reduce?"auto":"smooth"}); }
function renderFilters(){
  $("gfil").innerHTML=["A","B","C"].map(g=>`<button class="gbtn" type="button" data-g="${g}" aria-pressed="${gOn[g]}" title="${L().grades[g]}"><span class="g ${g}">${g}</span>${L().grades[g]}</button>`).join(" ");
  $("gfil").querySelectorAll(".gbtn").forEach(b=>b.addEventListener("click",()=>{ gOn[b.dataset.g]=!gOn[b.dataset.g]; if(!gOn.A&&!gOn.B&&!gOn.C) gOn[b.dataset.g]=true; renderFilters(); highlight(); renderDetail(); }));
  $("msel").innerHTML=`<option value="">${t("all")}</option>`+DATA.M.slice().sort((a,b)=>b.n-a.n).map(m=>`<option value="${m.id}">${nm([m.zh,m.en])}</option>`).join("");
  if(selNode.k==="m") $("msel").value=selNode.id;
}
$("msel").addEventListener("change",e=>{ if(e.target.value) selectMarker(e.target.value); });

/* ================= dots ================= */
let famSel=null, curP="PER-ODD-001";
const famOf=id=>id.split("-")[0];
function renderDots(){
  $("famLegend").innerHTML=`<button class="fchip" type="button" data-f="" aria-pressed="${!famSel}"><i style="background:var(--line)"></i>${t("allFam")}</button>`+
    DATA.F.map(f=>`<button class="fchip" type="button" data-f="${f.p}" aria-pressed="${famSel===f.p}"><i style="background:var(${FAMCOL[f.p]})"></i>${short(lang==="zh"?f.zh:f.en)} ${f.n}</button>`).join("");
  $("famLegend").querySelectorAll(".fchip").forEach(b=>b.addEventListener("click",()=>{ famSel=b.dataset.f||null; renderDots(); }));
  const P2=DATA.P.slice().sort((a,b)=>DATA.F.findIndex(f=>f.p===famOf(a[0]))-DATA.F.findIndex(f=>f.p===famOf(b[0]))||a[0].localeCompare(b[0]));
  $("dotf").innerHTML=P2.map(p=>`<button class="dot${famSel&&famOf(p[0])!==famSel?" off":""}${p[0]===curP?" on":""}" type="button" data-p="${p[0]}" style="background:var(${FAMCOL[famOf(p[0])]})" title="${nm([p[1],p[2]])}" aria-label="${nm([p[1],p[2]])}"></button>`).join("");
  $("dotf").querySelectorAll(".dot").forEach(b=>{ b.addEventListener("click",()=>{curP=b.dataset.p; renderDots();}); b.addEventListener("pointerenter",()=>renderPCard(b.dataset.p)); b.addEventListener("pointerleave",()=>renderPCard(curP)); });
  renderPCard(curP);
  const S=DATA.S; $("stats").innerHTML=[S.classes,S.markers,S.lit].map((v,i)=>`<div><b>${fmt(v)}</b><span>${L().statL[i]}</span></div>`).join("");
}
function renderPCard(pid){
  const p=DATA.P.find(x=>x[0]===pid); const f=DATA.F.find(x=>x.p===famOf(pid));
  const sigs=p[3].filter(id=>MK[id]);
  $("pcard").innerHTML=`<span class="fam" style="color:var(--muted)"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(${FAMCOL[f.p]});margin-right:6px"></span>${short(lang==="zh"?f.zh:f.en)}</span>
    <b>${nm([p[1],p[2]])}</b><span class="mono" style="color:var(--muted)">${p[0]}</span>
    <div class="sub">${t("sigs")}</div><div class="chipset">${sigs.length?sigs.map(id=>`<button class="chip" type="button" data-m="${id}">${short(nm([MK[id].zh,MK[id].en]))} →</button>`).join(""):`<span class="note">${t("noSig")}</span>`}</div>`;
  $("pcard").querySelectorAll("[data-m]").forEach(b=>b.addEventListener("click",()=>selectMarker(b.dataset.m,true)));
}
$("rand").addEventListener("click",()=>{ const pool=DATA.P.filter(p=>(!famSel||famOf(p[0])===famSel)&&p[3].some(id=>MK[id])); curP=pool[Math.floor(Math.random()*pool.length)][0]; renderDots(); });

/* ================= factory ================= */
const CONS=Object.keys(DATA.C).map(id=>({id,n:DATA.M.filter(m=>m.x.some(x=>x[0]===id)).length})).sort((a,b)=>b.n-a.n);
let curC="CN.working_memory"; if(!DATA.C[curC]) curC=CONS[0].id;
const FEAT_C=["CN.working_memory","CN.sustained_attention","CN.error_monitoring","CN.motor_imagery","CN.emotional_salience","CN.semantic_integration","CN.reward_prediction_error","CN.face_perception","CN.spatial_attention"].filter(c=>DATA.C[c]);
const TL={erp_component:[["fix",500,"--line"],["stim",200,"--pink"],["resp",800,"--sun"],["rest",700,"--soft"]],
 oscillatory:[["fix",2000,"--line"],["cue",1000,"--sun"],["task",4000,"--pink"],["rest",2000,"--soft"]],
 steady_state:[["fix",1000,"--line"],["cue",1000,"--sun"],["flick",4000,"--pink"],["rest",1000,"--soft"]],
 hemodynamic:[["task",20000,"--pink"],["rest",20000,"--soft"]],
 connectivity:[["rest",60000,"--soft"],["task",60000,"--pink"]],
 field_potential:[["fix",1000,"--line"],["cue",1000,"--sun"],["task",3000,"--pink"],["rest",1000,"--soft"]],
 single_unit:[["fix",1000,"--line"],["cue",1000,"--sun"],["task",3000,"--pink"],["rest",1000,"--soft"]]};
const LOBE_D={frontal:"M24 128 C14 82 46 40 104 32 C118 30 130 30 140 32 L132 134 C96 142 56 142 24 128 Z",central:"M140 32 C150 33 160 36 170 40 L152 132 L132 134 Z",
 parietal:"M170 40 C210 46 240 68 252 100 L210 124 L152 132 Z",occipital:"M252 100 C270 120 274 148 258 166 C238 158 222 146 210 124 Z",
 temporal:"M58 140 C96 146 146 138 204 126 C214 146 226 160 244 168 C214 184 160 190 112 180 C84 172 64 158 58 140 Z",cerebellum:"M196 176 C222 168 252 168 266 182 C270 202 242 214 216 208 C202 204 194 192 196 176 Z"};
const SYM={fix:"+",cue:"◆",stim:"●",resp:"?",fb:"✓",rest:"☾",task:"★",flick:"▦"};
let tlRun={seq:null,i:0,t0:0};
function renderFactory(lit){
  $("cpick").innerHTML=FEAT_C.map(c=>`<button class="chip" type="button" data-c="${c}" aria-pressed="${c===curC}">${short(nm(DATA.C[c]))}</button>`).join("");
  $("cpick").querySelectorAll("[data-c]").forEach(b=>b.addEventListener("click",()=>{curC=b.dataset.c; renderFactory(true);}));
  $("csel").innerHTML=CONS.map(c=>`<option value="${c.id}"${c.id===curC?" selected":""}>${nm(DATA.C[c.id])} (${c.n})</option>`).join("");
  const sig=[]; DATA.M.forEach(m=>m.x.forEach(x=>{ if(x[0]===curC) sig.push([m,x]); })); sig.sort((a,b)=>ORD[a[1][1]]-ORD[b[1][1]]||b[0].n-a[0].n);
  const top=sig.slice(0,3);
  const pars=[]; const seen=new Set(); top.forEach(([m])=>m.ex.forEach(e=>{ if(!seen.has(e[0])&&pars.length<4){ seen.add(e[0]); pars.push(e); } }));
  const lobes=new Set(); top.forEach(([m])=>m.g.forEach(g=>lobes.add(DATA.R[g[0]][2])));
  $("st1").innerHTML=`<div class="hd"><b style="background:var(--grape)">1</b>${t("st1")}</div><div class="want">${nm(DATA.C[curC])}</div>
    <svg class="mbrain" viewBox="10 20 270 200" aria-hidden="true">${Object.entries(LOBE_D).map(([k,d])=>`<path d="${d}" class="${lobes.has(k)?"on":""}"/>`).join("")}<ellipse cx="150" cy="118" rx="26" ry="18" class="${lobes.has("deep")?"on":""}"/></svg>
    <div class="note">${t("nSig",{n:sig.length})}</div>`;
  $("st2").innerHTML=`<div class="hd"><b style="background:var(--sun)">2</b>${t("st2")}</div>`+(top.length?top.map(([m,x])=>`<button class="sc" type="button" data-m="${m.id}"><svg viewBox="0 0 120 44" preserveAspectRatio="none"><path d="${WAVES[m.type]||WAVES.erp_component}"/></svg><b><span class="g ${x[1]}" style="width:20px;height:20px;font-size:12px;border-radius:6px;margin-right:6px;vertical-align:-3px">${x[1]}</span>${short(nm([m.zh,m.en]))}</b><em>${x[3]} · ${x[4]}</em></button>`).join("")+`<div class="tlnote">${t("clickSig")}</div>`:`<div class="empty">${t("mEmpty")}</div>`);
  $("st3").innerHTML=`<div class="hd"><b style="background:var(--mint)">3</b>${t("st3")}</div>`+pars.map(e=>`<div class="pc"><i style="background:var(${FAMCOL[famOf(e[0])]})"></i><div><b>${nm([e[1],e[2]])}</b><span class="mono">${e[0]}</span></div></div>`).join("");
  const typ=top.length?top[0][0].type:"erp_component", seq=TL[typ];
  const sec=ms=>ms>=1000?(ms/1000)+" s":ms+" ms";
  $("st4").innerHTML=`<div class="hd"><b style="background:var(--pink)">4</b>${t("st4")}</div>
    <div class="monitor"><span class="ph" id="tlPh"></span><span class="dur" id="tlDur"></span><span class="sym" id="tlSym"></span></div>
    <div class="tl" id="tlBar">${seq.map((p,i)=>`<i style="flex:${Math.max(p[1],600)};background:var(${p[2]==="--soft"?"--grape":p[2]==="--line"?"--sky":p[2]})">${L().tl[p[0]]}</i>`).join("")}<span class="head" id="tlHead"></span></div>
    <div class="tlnote">${t("tlNote",{t:L().types[typ]})}</div>`;
  $("st2").querySelectorAll("[data-m]").forEach(b=>b.addEventListener("click",()=>selectMarker(b.dataset.m,true)));
  tlRun={seq,i:-1,t0:performance.now()};
  if(lit) ["st1","st2","st3","st4"].forEach((id,i)=>{ const el=$(id); el.classList.remove("lit"); void el.offsetWidth; el.style.animationDelay=(i*.22)+"s"; el.classList.add("lit"); });
}
function tlLoop(tm){
  const r=tlRun; if(r.seq&&$("tlBar")){
    const w=r.seq.map(p=>Math.max(p[1],600)), tot=w.reduce((a,b)=>a+b,0), loop=6000, el=((tm-r.t0)%loop)/loop*tot;
    let acc=0,i=0; while(i<w.length-1&&acc+w[i]<=el){acc+=w[i];i++;}
    $("tlHead").style.left=`calc(${(el/tot*100).toFixed(2)}% - 1px)`;
    if(i!==r.i){ r.i=i; const p=r.seq[i]; $("tlSym").textContent=SYM[p[0]]||"•"; $("tlPh").textContent=L().tl[p[0]]; $("tlDur").textContent=p[1]>=1000?(p[1]/1000)+" s":p[1]+" ms";
      $("tlBar").querySelectorAll("i").forEach((x,k)=>x.classList.toggle("cur",k===i)); }
  }
  requestAnimationFrame(tlLoop);
}
requestAnimationFrame(tlLoop);
$("csel").addEventListener("change",e=>{curC=e.target.value; renderFactory(true);});

/* ================= i18n + boot ================= */
function applyLang(){
  document.documentElement.lang=lang==="zh"?"zh-CN":"en";
  document.querySelectorAll("[data-i]").forEach(el=>{ const v=L()[el.dataset.i]; if(typeof v==="string"){ el.hasAttribute("data-html")?el.innerHTML=v:el.textContent=v; } });
  $("lang").textContent=lang==="zh"?"EN":"中文";
  const S=DATA.S; $("mini").innerHTML=[S.paradigms,S.markers,S.links].map((v,i)=>`<span><b>${fmt(v)}</b>${L().mini[i]}</span>`).join("");
  $("oddGo").textContent=odd.timer?t("stop"):(odd.count?t("again"):t("start"));
  if(!odd.timer) $("oddMsg").textContent=odd.count>=40?t("oddDone"):t("oddReady");
  renderLobeLegend(); drawERP(); drawTopo(); renderFilters(); drawNet(); renderDetail(); renderDots(); renderFactory(); setGoal();
}
(()=>{ let th="light"; try{ if(localStorage.getItem("atlas-theme")==="dark") th="dark"; }catch(e){}
  const set=v=>{ th=v; document.documentElement.dataset.theme=v; $("theme").textContent=v==="dark"?"☀":"☾"; };
  set(th); $("theme").addEventListener("click",()=>{ set(th==="dark"?"light":"dark"); try{localStorage.setItem("atlas-theme",th);}catch(e){} }); })();
$("lang").addEventListener("click",()=>{ lang=lang==="zh"?"en":"zh"; try{localStorage.setItem("atlas-lang",lang);}catch(e){} applyLang(); });
seedOdd(); buildTiles(); applyLang(); drawSpec(0); requestAnimationFrame(ssLoop); requestAnimationFrame(miLoop);

}
