'use strict';
const menu=document.querySelector('.menu-toggle'),mobileNav=document.querySelector('#mobile-nav');
function closeMenu(){menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','打开导航');mobileNav.hidden=true}
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'关闭导航':'打开导航');mobileNav.hidden=!open});
mobileNav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!mobileNav.hidden){closeMenu();menu.focus()}});
document.querySelector('#year').textContent=new Date().getFullYear();

const tasks=[
 {
  "source": "perception/PER-ODD-001.yaml",
  "marker": "MK.P3b",
  "en": "PER-ODD-001 / ODDBALL",
  "stage": "draft · 具体范式",
  "title": "Oddball：检测低频目标",
  "description": "高频标准刺激与低频靶刺激随机出现，被试对靶刺激计数或按键。仓库将这一具体范式关联到 P3b，并记录视觉、听觉刺激及 EEG、MEG、fMRI 记录模态。",
  "question": "两类刺激；目标检测或计数；刺激与间隔组成试次。完整条目保留参数范围、变体与源头文献。",
  "knowledge": "P3b 的产生脑区：颞顶联合区（B）；关联认知构念：上下文更新与注意分配（B）。这些是知识库当前记录的关联，尚未完成内容核实。",
  "label": "概念时间线",
  "events": [
   "标准刺激",
   "低频靶刺激",
   "目标响应"
  ],
  "path": "M0 95H180C195 95 200 104 212 95S230 90 240 95H285C315 95 325 130 348 108S380 22 409 30S442 98 475 95H660",
  "point": [
   409,
   30
  ]
 },
 {
  "source": "motor/MOT-MI-001.yaml",
  "marker": "MK.SMR_ERD",
  "en": "MOT-MI-001 / MOTOR IMAGERY",
  "stage": "draft · 具体范式",
  "title": "运动想象：左手与右手",
  "description": "视觉箭头提示被试想象左手或右手动作，不实际执行。条目关注感觉运动 mu／β 节律的偏侧化去同步化，用于研究两类运动想象的信号差异。",
  "question": "左／右手二分类；视觉箭头提示；同步试次；试次内无反馈。四分类、连续反馈和异步设计分别记录为同类下的其他具体范式。",
  "knowledge": "SMR ERD 的产生脑区：感觉运动皮层（A）；关联认知构念：运动想象（B）。脑区关联与认知关联分别评级，条目当前仍为 draft。",
  "label": "概念时间线",
  "events": [
   "视觉提示",
   "左／右手想象",
   "无反馈休息"
  ],
  "path": "M0 78H130L140 55L150 100L160 52L170 101L180 66L190 80H235L245 72L255 86L265 75L275 81H390L400 74L410 84L420 78H470L480 57L490 101L500 51L510 100L520 68L530 78H660",
  "point": [
   275,
   81
  ]
 },
 {
  "source": "steady_state/SSR-SSVEP-002.yaml",
  "marker": "MK.SSVEP",
  "en": "SSR-SSVEP-002 / FREQUENCY CODING",
  "stage": "draft · 具体范式",
  "title": "SSVEP：用频率区分目标",
  "description": "多个目标以不同频率同时闪烁。用户注视期望目标，系统依据枕区脑电中的频率特征完成选择，再向用户反馈结果。",
  "question": "多目标频率编码；同步试次；离散反馈。与单光源被动观察的 -001、联合频率与相位编码的 -005 分别记录。",
  "knowledge": "SSVEP 的产生脑区：视觉皮层（B）；关联认知构念：持续性视觉注意（B）。记录刺激频率及谐波响应，文献与审核状态可在标记物条目中追溯。",
  "label": "概念时间线",
  "events": [
   "目标提示",
   "频率编码刺激",
   "选择反馈"
  ],
  "path": "M0 75H100C110 30 120 30 130 75S150 120 160 75S180 30 190 75S210 120 220 75S240 30 250 75S270 120 280 75S300 30 310 75S330 120 340 75S360 30 370 75S390 120 400 75S420 30 430 75S450 120 460 75S480 30 490 75H660",
  "point": [
   340,
   75
  ]
 }
];
const taskButtons=[...document.querySelectorAll('[data-task]')];
function selectTask(index){const t=tasks[index];document.querySelector('#task-source').href='https://github.com/savorcode/bci-paradigm-atlas/blob/main/paradigms/'+t.source;document.querySelector('#marker-source').href='https://github.com/savorcode/bci-paradigm-atlas/blob/main/knowledge/markers/'+t.marker+'.yaml';document.querySelector('#task-knowledge').textContent=t.knowledge;taskButtons.forEach((b,i)=>{b.setAttribute('aria-selected',String(i===index));b.tabIndex=i===index?0:-1;b.querySelector('.task-symbol').textContent=i===index?'−':'＋'});document.querySelector('#task-panel').setAttribute('aria-labelledby','task-tab-'+index);for(const [id,value] of Object.entries({'task-en':t.en,'task-stage':t.stage,'task-title':t.title,'task-description':t.description,'task-question':t.question,'signal-label':t.label}))document.getElementById(id).textContent=value;document.querySelector('#signal-events').replaceChildren(...t.events.map(text=>{const s=document.createElement('span');s.textContent=text;return s}));document.querySelector('#signal-path').setAttribute('d',t.path);document.querySelector('#signal-point').setAttribute('cx',t.point[0]);document.querySelector('#signal-point').setAttribute('cy',t.point[1]);document.querySelector('#task-signal').setAttribute('aria-label',t.events.join('、')+'的概念时间线，不代表实测数据')}
taskButtons.forEach((b,i)=>{b.addEventListener('click',()=>selectTask(i));b.addEventListener('keydown',e=>{let next;if(e.key==='ArrowDown'||e.key==='ArrowRight')next=(i+1)%3;if(e.key==='ArrowUp'||e.key==='ArrowLeft')next=(i+2)%3;if(e.key==='Home')next=0;if(e.key==='End')next=2;if(next!==undefined){e.preventDefault();selectTask(next);taskButtons[next].focus()}})});

selectTask(0);

// One continuous ink form: smoke, neural impulse, an idea taking shape, a falling apple.
const canvas=document.querySelector('#cognition'),gl=canvas.getContext('webgl',{alpha:true,antialias:false});
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
let paused=reduced.matches,visible=true,frame=0,last=0,time=0,width=0,height=0;
const motionButton=document.querySelector('#motion-toggle');
let program,clockUniform,sizeUniform,layoutUniform,strokeUniform,tailUniform;
const smooth=(a,b,x)=>{const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return t*t*t*(t*(t*6-15)+10)};
// Open organic branches, never a mesh. The same points become the apple's contours and stem.
const branches=[
 [[-.98,.36],[-.78,-.28],[-.10,.32],[.08,-.18]],
 [[.08,-.18],[.27,-.68],[.58,-.12],[.86,-.64]],
 [[-.71,-.71],[-.12,-.83],[-.62,-.08],[.08,-.18]],
 [[.08,-.18],[.36,.02],[.55,.62],[.91,.37]]
];
function curve(branch,u){const v=1-u;return [0,1].map(k=>v*v*v*branch[0][k]+3*v*v*u*branch[1][k]+3*v*u*u*branch[2][k]+u*u*u*branch[3][k])}
branches.push(
 [curve(branches[0],.38),[-.76,.11],[-.92,.69],[-.58,.79]],
 [curve(branches[1],.52),[.57,-.50],[.34,-.93],[.67,-1.04]],
 [curve(branches[2],.42),[-.41,-.56],[-.91,-.41],[-1.04,-.62]],
 [curve(branches[3],.52),[.53,.31],[.13,.64],[.31,.85]]
);
// Two finer dendrites on each existing branch, following its local tangent.
for(let b=0;b<8;b++)for(let fork=0;fork<2;fork++){
 const u=fork?.73:.39,origin=curve(branches[b],u),ahead=curve(branches[b],u+.02);
 const dx=ahead[0]-origin[0],dy=ahead[1]-origin[1],length=Math.hypot(dx,dy);
 const tx=dx/length,ty=dy/length,side=(b%2?1:-1)*(fork?-1:1),reach=fork?.25:.34;
 branches.push([origin,
  [origin[0]+tx*reach*.32,origin[1]+ty*reach*.32],
  [origin[0]+tx*reach*.55-ty*side*reach*.66,origin[1]+ty*reach*.55+tx*side*reach*.66],
  [origin[0]+tx*reach*.72-ty*side*reach,origin[1]+ty*reach*.72+tx*side*reach]
 ]);
}
function impulse(t){const progress=smooth(5.3,10.6,t)*1.999999,index=Math.floor(progress);return curve(branches[index],progress-index)}
if(gl){
 const vertex=`attribute vec2 position;void main(){gl_Position=vec4(position,0.,1.);}`;
 const fragment=`precision mediump float;
 uniform vec2 size;uniform vec3 layout;uniform float clock;uniform vec2 strokes[192];uniform vec2 tail[12];
 float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
 float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1.,0.)),f.x),mix(hash(i+vec2(0.,1.)),hash(i+vec2(1.,1.)),f.x),f.y);}
 float flow(vec2 p){return noise(p)*.58+noise(p*2.02+3.7)*.28+noise(p*4.03+1.2)*.14;}
 float ease(float a,float b,float t){float x=clamp((t-a)/(b-a),0.,1.);return x*x*x*(x*(x*6.-15.)+10.);}
 float segmentDistance(vec2 p,vec2 a,vec2 b){vec2 pa=p-a,ba=b-a;return length(pa-ba*clamp(dot(pa,ba)/max(dot(ba,ba),.000001),0.,1.));}
 void main(){
 vec2 pixel=vec2(gl_FragCoord.x,size.y-gl_FragCoord.y),p=(pixel-layout.xy)/layout.z;
 float t=mod(clock,30.),form=ease(10.3,16.8,t),fall=clamp((t-17.)/3.,0.,1.),drop=fall*fall;
 float disperse=ease(22.,29.,t),fade=1.-disperse,reveal=ease(1.8,6.,t),driftTime=clock*.065;
 float bounceA=clamp((t-20.)/1.2,0.,1.),bounceB=clamp((t-21.2)/.7,0.,1.);
 float bounce=-.20*4.*bounceA*(1.-bounceA)-.055*4.*bounceB*(1.-bounceB);
 vec3 paper=vec3(.9804,.9843,.9882),navy=vec3(.09,.16,.28),silver=vec3(.49,.58,.69);
 vec2 drift=vec2(flow(p*1.8+vec2(driftTime,-driftTime*.4)),flow(p*1.8+vec2(-driftTime*.3,driftTime)+8.));
 float cloud=exp(-dot(p*vec2(1.03,.85),p*vec2(1.03,.85))*1.8);
 float ink=flow(p*2.6+drift*1.9+vec2(driftTime*.45,-driftTime*.6));
 float ribbon=flow(p*1.65+vec2(ink*2.,driftTime*.15));
 float folds=smoothstep(.37,.51,ribbon)-smoothstep(.53,.73,ribbon);
 float fogBase=cloud*(.10+.40*ink+folds*.24)*.92;
 // Released ink expands from the apple and drifts back into the opening smoke field.
 vec2 vaporCenter=mix(vec2(.625,.59),vec2(0.),disperse);
 vec2 vaporPoint=(p-vaporCenter)/mix(.44,1.0,disperse);
 float vapor=exp(-dot(vaporPoint,vaporPoint)*1.8)*(.22+ink*.30+folds*.18);
 float fog=fogBase*((1.-reveal*.77)*(1.-form)+ease(26.,30.,t));
 fog+=vapor*sin(disperse*3.14159)*.85;
 vec3 color=mix(paper,mix(silver,navy,smoothstep(.30,.70,ink)),fog);
 // Broad, translucent ink ribbons resolve from the fog and reshape without changing assets.
 vec2 dispersed=p+vec2(.20,.55)*disperse+(drift-.5)*disperse*.85;
 vec2 q=dispersed+(drift-.5)*(.16*(1.-reveal));float distance=10.;
 for(int b=0;b<8;b++){for(int i=0;i<15;i++){distance=min(distance,segmentDistance(q,strokes[b*16+i],strokes[b*16+i+1]));}}
 for(int b=0;b<16;b++){for(int i=0;i<3;i++){float d=segmentDistance(q,strokes[128+b*4+i],strokes[128+b*4+i+1]);distance=min(distance,d*mix(1.55,1.,form));}}
 float softness=mix(.038,.009,reveal)*(1.+.75*sin(form*3.14159))+disperse*.12;
 float body=exp(-distance*distance/(softness*softness));
 float halo=exp(-distance*distance/.007);
 float erosion=1.-smoothstep(.15+ink*.48,.48+ink*.48,disperse);
 float stroke=reveal*fade*erosion;
 color=mix(color,silver,halo*stroke*.18);
 color=mix(color,navy,body*stroke*(.26+.13*form));
 float active=ease(5.,5.7,t)*(1.-ease(10.3,15.2,t)),trail=0.,core=0.;
 for(int i=0;i<11;i++){float d=segmentDistance(p,tail[i],tail[i+1]),weight=1.-float(i)/12.;trail=max(trail,exp(-d*d/.0025)*weight);core=max(core,exp(-d*d/.00012)*weight);}
 color=mix(color,vec3(.21,.38,.57),trail*active*.8);color=mix(color,vec3(.94,.97,1.),core*active*.9);
 // A soft ink volume grows inside the very same contour; no photographic cut or crossfade.
 vec2 center=vec2(.57+.055*drop,-.35+.94*drop+bounce);float angle=fall*.18+bounce*.12;
 vec2 local=mat2(cos(angle),-sin(angle),sin(angle),cos(angle))*(dispersed-center)/.56;
 float radius=length(vec2(local.x,local.y*1.20));
 float notch=.17*exp(-local.x*local.x/.07)*(1.-smoothstep(-.6,.0,local.y));
 float volume=(1.-smoothstep(.67,.94,radius+notch))*ease(12.5,17.,t)*fade*erosion;
 float light=clamp(.65-local.x*.32-local.y*.20,0.,1.);
 color=mix(color,mix(navy,silver,light),volume*.44);
 float shadow=exp(-pow((p.x-center.x)/(.36-.13*drop-bounce*.25),2.)-pow((p.y-.99)/.035,2.));
 color=mix(color,navy,shadow*ease(16.,20.,t)*fade*(.10+bounce*.15));
 gl_FragColor=vec4(color,1.);
 }`;
 const shaders=[vertex,fragment].map((source,i)=>{const shader=gl.createShader(i?gl.FRAGMENT_SHADER:gl.VERTEX_SHADER);gl.shaderSource(shader,source);gl.compileShader(shader);if(!gl.getShaderParameter(shader,gl.COMPILE_STATUS))throw new Error(gl.getShaderInfoLog(shader));return shader});
 program=gl.createProgram();shaders.forEach(s=>gl.attachShader(program,s));gl.linkProgram(program);if(!gl.getProgramParameter(program,gl.LINK_STATUS))throw new Error(gl.getProgramInfoLog(program));gl.useProgram(program);
 const buffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),gl.STATIC_DRAW);
 const position=gl.getAttribLocation(program,'position');gl.enableVertexAttribArray(position);gl.vertexAttribPointer(position,2,gl.FLOAT,false,0,0);
 clockUniform=gl.getUniformLocation(program,'clock');sizeUniform=gl.getUniformLocation(program,'size');layoutUniform=gl.getUniformLocation(program,'layout');strokeUniform=gl.getUniformLocation(program,'strokes[0]');tailUniform=gl.getUniformLocation(program,'tail[0]');
}
function updateMotionButton(){motionButton.setAttribute('aria-pressed',String(paused));motionButton.setAttribute('aria-label',paused?'播放所有动图':'暂停所有动图');document.querySelector('#motion-label').textContent=paused?'播放动效':'暂停动效';document.body.classList.toggle('motion-paused',paused)}
function fit(){const r=canvas.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,1.5);canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);if(gl)gl.viewport(0,0,canvas.width,canvas.height);draw()}
function draw(){
 if(!gl||!width)return;
 const mobile=width<761,d=canvas.width/width,scale=mobile?width*.49:Math.min(width*.32,height*.39);
 const sceneTime=reduced.matches?8:time,t=sceneTime%30;
 const form=smooth(10.3,16.8,t),fall=Math.max(0,Math.min(1,(t-17)/3)),drop=fall*fall;
 const bounceA=Math.max(0,Math.min(1,(t-20)/1.2)),bounceB=Math.max(0,Math.min(1,(t-21.2)/.7));
 const bounce=-.20*4*bounceA*(1-bounceA)-.055*4*bounceB*(1-bounceB);
 const center=[.57+.055*drop,-.35+.94*drop+bounce],angle=fall*.18+bounce*.12,points=[];
 for(let b=0;b<24;b++)for(let i=0;i<(b<8?16:4);i++){
  const u=i/(b<8?15:3),source=curve(branches[b],u);let x,y;
  if(b!==3){const theta=b<3?(b+u)*Math.PI*2/3:b<8?(b-4+u)*Math.PI/2:(b-8+u)*Math.PI/8;x=Math.sin(theta)*(.84+.084*Math.cos(theta));y=-.82*Math.cos(theta)+.06*Math.cos(theta*2)+.18*Math.exp(-(Math.sin(theta)**2)/.12)*Math.cos(theta)}
  else{x=.13*u-.055*Math.sin(u*Math.PI);y=-.58-.36*u}
  const target=[center[0]+.56*(x*Math.cos(angle)-y*Math.sin(angle)),center[1]+.56*(x*Math.sin(angle)+y*Math.cos(angle))];
  const curl=Math.sin(form*Math.PI)*.19,phase=(b+u)*Math.PI*1.3;
  points.push(source[0]*(1-form)+target[0]*form+curl*Math.sin(phase),source[1]*(1-form)+target[1]*form+curl*Math.cos(phase));
 }
 gl.uniform2f(sizeUniform,canvas.width,canvas.height);gl.uniform3f(layoutUniform,width*(mobile?.43:.72)*d,height*(mobile?.67:.44)*d,scale*d);gl.uniform1f(clockUniform,sceneTime);
 gl.uniform2fv(strokeUniform,new Float32Array(points));
 gl.uniform2fv(tailUniform,new Float32Array(Array.from({length:12},(_,i)=>{
  const p=impulse(Math.max(5.3,t-i*.065)),u=smooth(10.3,15.2,t-i*.065);
  const theta=u*Math.PI*2.5,r=.36*Math.sin(Math.PI*u);
  return [p[0]*(1-u)+(center[0]+r*Math.sin(theta))*u,p[1]*(1-u)+(center[1]+r*Math.cos(theta))*u];
 }).flat()));gl.drawArrays(gl.TRIANGLES,0,3);
}
function animate(now){frame=0;if(paused||!visible||document.hidden)return;if(now-last>30){time+=Math.min((now-last)/1000,.08);draw();last=now}frame=requestAnimationFrame(animate)}
function start(){last=performance.now();if(!frame&&!paused&&visible&&!document.hidden)frame=requestAnimationFrame(animate)}
function stop(){cancelAnimationFrame(frame);frame=0}
motionButton.addEventListener('click',()=>{paused=!paused;updateMotionButton();if(paused)stop();else start()});
new ResizeObserver(fit).observe(canvas);new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;if(visible)start();else stop()},{threshold:.05}).observe(canvas);
const sectionObserver=new IntersectionObserver(entries=>entries.forEach(e=>e.target.classList.toggle('motion-visible',e.isIntersecting)),{threshold:0});document.querySelectorAll('main>section').forEach(s=>sectionObserver.observe(s));
document.addEventListener('visibilitychange',()=>{document.body.classList.toggle('page-hidden',document.hidden);if(document.hidden)stop();else start()});reduced.addEventListener('change',e=>{paused=e.matches;updateMotionButton();if(paused){stop();draw()}else start()});updateMotionButton();start();
