'use strict';
const english=document.documentElement.lang==='en';
const local=(en,zh)=>english?en:zh;
const languageSwitch=document.querySelector('.language-switch');
languageSwitch.addEventListener('click',()=>{languageSwitch.hash=location.hash});
const menu=document.querySelector('.menu-toggle'),mobileNav=document.querySelector('#mobile-nav');
function closeMenu(){menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label',local('Open navigation','打开导航'));mobileNav.hidden=true}
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?local('Close navigation','关闭导航'):local('Open navigation','打开导航'));mobileNav.hidden=!open});
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
  "description": "低频目标随机混入常见刺激，被试计数或按键；观察与目标相关的 P3b。",
  "question": "两类刺激 · 目标检测或计数 · 随机呈现。",
  "knowledge": "来源：颞顶联合区（B）。反映上下文更新与注意分配（B）。",
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
  "description": "按箭头提示想象左手或右手运动，以感觉运动 mu／β 节律区分两类。",
  "question": "左／右手二分类 · 视觉提示 · 试次内无反馈。",
  "knowledge": "来源：感觉运动皮层（A）。关联运动想象（B）。",
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
  "description": "注视不同频率闪烁的目标，通过枕区脑电频率特征完成选择。",
  "question": "多目标频率编码 · 同步试次 · 选择反馈。",
  "knowledge": "来源：视觉皮层（B）。关联持续性视觉注意（B）。",
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
if(english)[{"stage": "draft · concrete paradigm", "title": "Oddball: detecting rare targets", "description": "Detect rare targets among frequent stimuli and observe the target-related P3b response.", "question": "Two stimulus types · Target detection or counting · Random presentation.", "knowledge": "Source: temporoparietal junction (B). Indexes context updating and attention allocation (B).", "label": "CONCEPTUAL TIMELINE", "events": ["Standard stimulus", "Rare target", "Target response"]}, {"stage": "draft · concrete paradigm", "title": "Motor imagery: left vs. right hand", "description": "Imagine moving the left or right hand. Compare lateralized sensorimotor mu/beta rhythms.", "question": "Left/right hand · Visual cues · No within-trial feedback.", "knowledge": "Source: sensorimotor cortex (A). Indexes motor imagery (B).", "label": "CONCEPTUAL TIMELINE", "events": ["Visual cue", "Left/right imagery", "Rest without feedback"]}, {"stage": "draft · concrete paradigm", "title": "SSVEP: selecting by frequency", "description": "Look at a flickering target. Decode its frequency from occipital EEG to select it.", "question": "Multi-target frequency coding · Synchronous trials · Selection feedback.", "knowledge": "Source: visual cortex (B). Indexes sustained visual attention (B).", "label": "CONCEPTUAL TIMELINE", "events": ["Target cue", "Frequency-coded stimuli", "Selection feedback"]}].forEach((text,i)=>Object.assign(tasks[i],text));
const taskButtons=[...document.querySelectorAll('[data-task]')];
function selectTask(index){const t=tasks[index];document.querySelector('#task-source').href='https://github.com/savorcode/bci-paradigm-atlas/blob/main/paradigms/'+t.source;document.querySelector('#marker-source').href='https://github.com/savorcode/bci-paradigm-atlas/blob/main/knowledge/markers/'+t.marker+'.yaml';document.querySelector('#task-knowledge').textContent=t.knowledge;taskButtons.forEach((b,i)=>{b.setAttribute('aria-selected',String(i===index));b.tabIndex=i===index?0:-1;b.querySelector('.task-symbol').textContent=i===index?'−':'＋'});document.querySelector('#task-panel').setAttribute('aria-labelledby','task-tab-'+index);for(const [id,value] of Object.entries({'task-en':t.en,'task-stage':t.stage,'task-title':t.title,'task-description':t.description,'task-question':t.question,'signal-label':t.label}))document.getElementById(id).textContent=value;document.querySelector('#signal-events').replaceChildren(...t.events.map(text=>{const s=document.createElement('span');s.textContent=text;return s}));document.querySelector('#signal-path').setAttribute('d',t.path);document.querySelector('#signal-point').setAttribute('cx',t.point[0]);document.querySelector('#signal-point').setAttribute('cy',t.point[1]);document.querySelector('#task-signal').setAttribute('aria-label',english?'Conceptual timeline: '+t.events.join(', ')+'. Not measured data.':t.events.join('、')+'的概念时间线，不代表实测数据')}
taskButtons.forEach((b,i)=>{b.addEventListener('click',()=>selectTask(i));b.addEventListener('keydown',e=>{let next;if(e.key==='ArrowDown'||e.key==='ArrowRight')next=(i+1)%3;if(e.key==='ArrowUp'||e.key==='ArrowLeft')next=(i+2)%3;if(e.key==='Home')next=0;if(e.key==='End')next=2;if(next!==undefined){e.preventDefault();selectTask(next);taskButtons[next].focus()}})});

selectTask(0);

// The static catalog is generated from the same YAML records as the atlas tools.
const catalogQuery=document.querySelector('#catalog-query'),catalogFamily=document.querySelector('#catalog-family'),catalogModality=document.querySelector('#catalog-modality');
const catalogResults=document.querySelector('#catalog-results'),catalogCount=document.querySelector('#catalog-count'),catalogPrev=document.querySelector('#catalog-prev'),catalogNext=document.querySelector('#catalog-next'),catalogClear=document.querySelector('#catalog-clear');
let catalogItems=[],catalogPage=0;
const catalogPageSize=6;
function renderCatalog(){
 const words=catalogQuery.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
 const filtered=catalogItems.filter(item=>(!catalogFamily.value||item.family===catalogFamily.value)&&(!catalogModality.value||item.modalities.includes(catalogModality.value))&&words.every(word=>item.search.includes(word)));
 const pages=Math.max(1,Math.ceil(filtered.length/catalogPageSize));catalogPage=Math.min(catalogPage,pages-1);
 catalogResults.replaceChildren();
 for(const item of filtered.slice(catalogPage*catalogPageSize,(catalogPage+1)*catalogPageSize)){
  const card=document.createElement('article');card.className='catalog-card';
  const id=document.createElement('span');id.className='record-id';id.textContent=item.id+' / '+item.status;
  const title=document.createElement('h4');title.textContent=english?item.english:item.name;
  const description=document.createElement('p');description.textContent=english?item.descriptionEnglish:item.description;
  const tags=document.createElement('div');tags.className='record-tags';
  const allTags=[...item.modalities,...item.markers],visibleTags=[...item.modalities.slice(0,2),...item.markers.slice(0,1)];
  if(allTags.length>visibleTags.length)visibleTags.push('+'+(allTags.length-visibleTags.length));
  for(const value of visibleTags){const tag=document.createElement('span');tag.textContent=value;tags.append(tag)}
  const link=document.createElement('a');link.textContent=local('Open protocol','打开协议');link.className='external-link action-primary';link.target='_blank';link.rel='noopener noreferrer';link.href='https://github.com/savorcode/bci-paradigm-atlas/blob/main/'+item.path;
  link.setAttribute('aria-label',english?'View protocol and sources for '+item.id+' '+item.english:'查看 '+item.id+' '+item.name+' 的协议与出处');
  card.append(id,title,description,tags,link);catalogResults.append(card);
 }
 catalogCount.textContent=filtered.length+' / '+catalogItems.length+local(' active protocols',' 个有效协议');
 document.querySelector('#catalog-empty').hidden=filtered.length!==0;
 document.querySelector('#catalog-page').textContent=filtered.length?(catalogPage+1)+' / '+pages:'0 / 0';
 catalogPrev.disabled=catalogPage===0;catalogNext.disabled=catalogPage>=pages-1;
}
for(const control of [catalogQuery,catalogFamily,catalogModality])control.addEventListener(control===catalogQuery?'input':'change',()=>{catalogPage=0;renderCatalog()});
catalogClear.addEventListener('click',()=>{catalogQuery.value='';catalogFamily.value='';catalogModality.value='';catalogPage=0;renderCatalog();catalogQuery.focus()});
catalogPrev.addEventListener('click',()=>{catalogPage--;renderCatalog()});catalogNext.addEventListener('click',()=>{catalogPage++;renderCatalog()});
async function loadCatalog(){
 try{
  const response=await fetch('./catalog.json');if(!response.ok)throw new Error('Catalog unavailable');
  const data=await response.json();
  catalogItems=data.items.map(item=>({...item,search:[item.id,item.name,item.english,...item.aliases,...item.markers,...item.modalities].join(' ').toLowerCase()}));
  for(const family of data.families){const option=document.createElement('option');option.value=family.id;option.textContent=(english?family.english:family.name)+' ('+family.count+')';catalogFamily.append(option)}
  for(const modality of [...new Set(catalogItems.flatMap(item=>item.modalities))].sort()){const option=document.createElement('option');option.value=modality;option.textContent=modality;catalogModality.append(option)}
  for(const control of [catalogQuery,catalogFamily,catalogModality,catalogClear])control.disabled=false;
  renderCatalog();
 }catch{catalogCount.textContent=local('The catalog could not load. Refresh or open the source directory below.','目录暂时无法加载，请刷新重试或打开下方完整源目录。')}
}
loadCatalog();
document.querySelector('#copy-setup').addEventListener('click',async()=>{
 const status=document.querySelector('#copy-status');
 try{await navigator.clipboard.writeText(document.querySelector('#setup-code').textContent);status.textContent=local('Commands copied.','命令已复制。');}
 catch{status.textContent=local('Clipboard unavailable. Select and copy the commands below.','未能访问剪贴板，请选中下方命令手动复制。');}
});

// A curated v0.1.0 subgraph. Layout is artistic; edges retain their source direction.
const heroGraph={"nodes":[{"id":"MK.P3b","kind":"marker","x":0.1914,"y":0.432,"z":-0.1857},{"id":"MK.SMR_ERD","kind":"marker","x":0.1642,"y":-0.3775,"z":-0.2315},{"id":"MK.SSVEP","kind":"marker","x":-0.4249,"y":0.7889,"z":-0.2326},{"id":"MK.alpha_posterior","kind":"marker","x":0.361,"y":0.1803,"z":0.2808},{"id":"MK.BOLD_striatum_reward","kind":"marker","x":-0.4884,"y":-0.4455,"z":0.2568},{"id":"MK.FRN","kind":"marker","x":-0.5532,"y":0.0328,"z":0.3656},{"id":"MK.high_gamma","kind":"marker","x":-0.323,"y":0.1408,"z":-0.0438},{"id":"MK.frontal_midline_theta","kind":"marker","x":0.4929,"y":0.1011,"z":0.2206},{"id":"MK.BOLD_hippocampus","kind":"marker","x":-0.4466,"y":-0.7761,"z":-0.146},{"id":"MK.BOLD_amygdala","kind":"marker","x":0.049,"y":-0.7985,"z":0.1396},{"id":"MK.BOLD_frontoparietal","kind":"marker","x":0.5622,"y":0.4426,"z":-0.2758},{"id":"MK.HbO_prefrontal","kind":"marker","x":0.6809,"y":0.1778,"z":-0.0162},{"id":"PER-ODD-001","kind":"paradigm","x":0.1509,"y":0.5212,"z":-0.378},{"id":"CTL-ANT-001","kind":"paradigm","x":0.2515,"y":0.5024,"z":0.2929},{"id":"ERR-ADAPT-002","kind":"paradigm","x":-0.1721,"y":0.2424,"z":0.0162},{"id":"MEM-NBK-001","kind":"paradigm","x":0.4477,"y":0.274,"z":0.0912},{"id":"PER-NAVON-001","kind":"paradigm","x":0.0642,"y":0.4695,"z":0.2879},{"id":"PER-ODD-006","kind":"paradigm","x":0.0761,"y":0.3972,"z":-0.1648},{"id":"SOC-CYB-001","kind":"paradigm","x":0.1268,"y":0.6009,"z":-0.1575},{"id":"BR.temporoparietal_junction","kind":"region","x":0.2022,"y":0.6119,"z":0.3467},{"id":"CN.context_updating","kind":"construct","x":0.0648,"y":0.5445,"z":-0.0615},{"id":"CN.attention_allocation","kind":"construct","x":0.266,"y":0.574,"z":-0.002},{"id":"MOT-MI-001","kind":"paradigm","x":0.2467,"y":-0.4269,"z":0.3643},{"id":"IMG-CMD-001","kind":"paradigm","x":0.316,"y":-0.4787,"z":0.0027},{"id":"MOT-ATT-002","kind":"paradigm","x":0.0834,"y":-0.4576,"z":0.0106},{"id":"MOT-GRASP-004","kind":"paradigm","x":0.1563,"y":-0.4923,"z":-0.1496},{"id":"MOT-MI-002","kind":"paradigm","x":0.0819,"y":-0.3082,"z":-0.3815},{"id":"MOT-MI-008","kind":"paradigm","x":0.0465,"y":-0.3842,"z":0.0871},{"id":"MOT-PASS-001","kind":"paradigm","x":0.2686,"y":-0.333,"z":0.2987},{"id":"BR.sensorimotor_cortex","kind":"region","x":0.236,"y":-0.5106,"z":0.2847},{"id":"CN.motor_execution","kind":"construct","x":0.1795,"y":-0.2867,"z":0.3312},{"id":"CN.motor_imagery","kind":"construct","x":0.3285,"y":-0.3958,"z":0.0714},{"id":"SSR-SSVEP-002","kind":"paradigm","x":-0.4794,"y":0.8776,"z":0.0759},{"id":"PER-BR-002","kind":"paradigm","x":-0.3974,"y":0.8968,"z":0.0992},{"id":"SSR-SSVEP-001","kind":"paradigm","x":-0.4914,"y":0.687,"z":-0.0305},{"id":"SSR-SSVEP-003","kind":"paradigm","x":-0.3025,"y":0.8012,"z":0.0467},{"id":"SSR-SSVEP-004","kind":"paradigm","x":-0.3377,"y":0.7292,"z":0.146},{"id":"SSR-SSVEP-005","kind":"paradigm","x":-0.4112,"y":0.6842,"z":-0.0984},{"id":"SSR-SSVEP-008","kind":"paradigm","x":-0.5476,"y":0.7372,"z":-0.3658},{"id":"BR.visual_cortex","kind":"region","x":-0.3233,"y":0.8736,"z":0.0904},{"id":"CN.sustained_visual_attention","kind":"construct","x":-0.5338,"y":0.8136,"z":-0.2548},{"id":"CTL-AUT-001","kind":"paradigm","x":0.3138,"y":0.0396,"z":-0.3377},{"id":"IMG-VIS-001","kind":"paradigm","x":0.2245,"y":0.077,"z":-0.0712},{"id":"STA-DRV-001","kind":"paradigm","x":0.2494,"y":0.2256,"z":-0.2205},{"id":"STA-MED-001","kind":"paradigm","x":0.4123,"y":0.0868,"z":-0.2593},{"id":"STA-PSY-001","kind":"paradigm","x":0.1996,"y":0.1655,"z":0.0784},{"id":"STM-PBM-001","kind":"paradigm","x":0.2813,"y":0.122,"z":-0.3964},{"id":"CTL-AMBIG-001","kind":"paradigm","x":-0.2087,"y":-0.6177,"z":-0.2887},{"id":"EMO-HUMOR-001","kind":"paradigm","x":-0.5393,"y":-0.5092,"z":-0.3418},{"id":"ERR-APC-001","kind":"paradigm","x":-0.6381,"y":-0.4204,"z":-0.0887},{"id":"ERR-PCL-001","kind":"paradigm","x":-0.6155,"y":-0.4916,"z":-0.0925},{"id":"ERR-TS-002","kind":"paradigm","x":-0.5827,"y":-0.3709,"z":0.1935},{"id":"SOC-GAZE-002","kind":"paradigm","x":-0.4916,"y":-0.355,"z":0.1038},{"id":"SOC-TRUST-003","kind":"paradigm","x":-0.3993,"y":-0.4103,"z":0.1845},{"id":"CTL-BART-001","kind":"paradigm","x":-0.6509,"y":0.0475,"z":0.009},{"id":"ERR-ADAPT-001","kind":"paradigm","x":-0.7001,"y":-0.0161,"z":-0.3183},{"id":"ERR-GAM-001","kind":"paradigm","x":-0.6274,"y":0.1354,"z":0.2316},{"id":"ERR-GAM-003","kind":"paradigm","x":-0.7072,"y":0.0926,"z":-0.0704},{"id":"ERR-PRT-001","kind":"paradigm","x":-0.5097,"y":-0.0393,"z":0.3121},{"id":"ERR-TS-001","kind":"paradigm","x":-0.5321,"y":-0.2053,"z":-0.3166},{"id":"SOC-UG-001","kind":"paradigm","x":-0.6218,"y":-0.052,"z":0.0938},{"id":"IMG-AUD-001","kind":"paradigm","x":-0.3748,"y":0.0778,"z":0.3229},{"id":"IMG-SPI-003","kind":"paradigm","x":-0.2541,"y":0.1614,"z":-0.0011},{"id":"LAN-OVS-002","kind":"paradigm","x":-0.3165,"y":0.2681,"z":-0.0486},{"id":"LAN-PN-001","kind":"paradigm","x":-0.3789,"y":0.2371,"z":0.2629},{"id":"MOT-GRASP-001","kind":"paradigm","x":-0.4455,"y":0.2608,"z":-0.0836},{"id":"MOT-ME-001","kind":"paradigm","x":-0.0934,"y":-0.1196,"z":0.0045},{"id":"MOT-TRACK-001","kind":"paradigm","x":-0.4388,"y":0.1721,"z":-0.0539},{"id":"CTL-DT-001","kind":"paradigm","x":0.3269,"y":0.292,"z":0.3307},{"id":"CTL-SW-002","kind":"paradigm","x":0.4736,"y":-0.0378,"z":-0.1469},{"id":"ERR-OGNG-001","kind":"paradigm","x":0.5382,"y":-0.0719,"z":0.2782},{"id":"IMG-MA-002","kind":"paradigm","x":0.5828,"y":0.0224,"z":-0.294},{"id":"MEM-DS-002","kind":"paradigm","x":0.6101,"y":-0.0455,"z":0.1702},{"id":"MEM-NBK-002","kind":"paradigm","x":0.4797,"y":0.2776,"z":-0.0099},{"id":"MEM-EFT-001","kind":"paradigm","x":-0.5373,"y":-0.7371,"z":0.12},{"id":"MEM-MST-002","kind":"paradigm","x":-0.3386,"y":-0.812,"z":-0.3161},{"id":"MEM-NAV-002","kind":"paradigm","x":-0.5484,"y":-0.8193,"z":-0.0116},{"id":"MEM-PA-001","kind":"paradigm","x":-0.3882,"y":-0.8776,"z":0.3796},{"id":"MEM-RMEM-001","kind":"paradigm","x":-0.4665,"y":-0.6094,"z":-0.1143},{"id":"MEM-TMR-002","kind":"paradigm","x":-0.4751,"y":-0.8762,"z":-0.3762},{"id":"PER-CTXC-001","kind":"paradigm","x":-0.3691,"y":-0.7261,"z":0.0998},{"id":"EMO-FACE-001","kind":"paradigm","x":0.1277,"y":-0.7534,"z":-0.3349},{"id":"EMO-FACE-002","kind":"paradigm","x":0.1656,"y":-0.8667,"z":-0.2206},{"id":"EMO-FC-002","kind":"paradigm","x":0.1049,"y":-0.907,"z":0.1153},{"id":"EMO-IAPS-001","kind":"paradigm","x":0.0232,"y":-0.8991,"z":0.0062},{"id":"EMO-REG-002","kind":"paradigm","x":-0.0289,"y":-0.8089,"z":0.1706},{"id":"STA-NF-002","kind":"paradigm","x":0.1967,"y":-0.8016,"z":0.2111},{"id":"CTL-RAVEN-001","kind":"paradigm","x":0.6967,"y":0.4929,"z":-0.1547},{"id":"ERR-AWARE-003","kind":"paradigm","x":0.6494,"y":0.5497,"z":0.0844},{"id":"IMG-ROT-001","kind":"paradigm","x":0.4574,"y":0.3572,"z":0.3306},{"id":"MEM-NBK-004","kind":"paradigm","x":0.5897,"y":0.59,"z":-0.35},{"id":"MEM-SWM-001","kind":"paradigm","x":0.5238,"y":0.5593,"z":0.1757},{"id":"PER-MOT-001","kind":"paradigm","x":0.6642,"y":0.429,"z":-0.0094},{"id":"CTL-TOL-001","kind":"paradigm","x":0.7896,"y":0.1367,"z":-0.207},{"id":"EMO-STRESS-001","kind":"paradigm","x":0.7511,"y":0.0505,"z":0.0885},{"id":"EMO-STRESS-002","kind":"paradigm","x":0.8386,"y":0.1921,"z":-0.3943},{"id":"LAN-VF-001","kind":"paradigm","x":0.8248,"y":0.0697,"z":0.2983},{"id":"LAN-VF-003","kind":"paradigm","x":0.7789,"y":0.2462,"z":0.0872},{"id":"STA-MATB-001","kind":"paradigm","x":0.5408,"y":0.1593,"z":0.1003}],"edges":[[29,1],[19,0],[39,2],[47,9],[47,4],[13,0],[41,3],[54,5],[68,0],[68,7],[87,10],[69,7],[93,11],[81,9],[82,9],[83,9],[48,4],[84,9],[85,9],[94,11],[95,11],[55,5],[14,5],[14,0],[49,4],[88,10],[56,5],[57,5],[70,7],[50,4],[58,5],[59,4],[59,5],[51,4],[61,6],[23,1],[71,7],[89,10],[89,3],[62,6],[42,3],[63,6],[64,6],[96,11],[97,11],[72,7],[74,8],[75,8],[76,8],[15,10],[15,11],[15,0],[15,3],[15,7],[73,10],[73,11],[73,0],[73,3],[73,7],[90,10],[77,8],[78,8],[78,4],[91,10],[79,8],[0,21],[0,20],[1,30],[1,31],[2,40],[24,1],[65,6],[25,1],[66,1],[66,6],[22,1],[26,1],[27,1],[28,1],[67,6],[33,2],[80,8],[92,10],[16,0],[12,0],[17,0],[18,0],[52,4],[53,4],[60,5],[34,2],[32,2],[35,2],[36,2],[37,2],[38,2],[43,3],[98,11],[98,3],[98,7],[44,3],[44,7],[86,9],[45,3],[46,3]]};
const canvas=document.querySelector('#cognition'),ctx=canvas.getContext('2d');
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
let paused=reduced.matches,visible=true,frame=0,last=0,time=0,width=0,height=0;
const motionButton=document.querySelector('#motion-toggle');
const tau=Math.PI*2;
function updateMotionButton(){motionButton.setAttribute('aria-pressed',String(paused));motionButton.setAttribute('aria-label',paused?local('Play all animations','播放所有动图'):local('Pause all animations','暂停所有动图'));document.querySelector('#motion-label').textContent=paused?local('Play motion','播放动效'):local('Pause motion','暂停动效');document.body.classList.toggle('motion-paused',paused)}
function fit(){const r=canvas.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);ctx.setTransform(d,0,0,d,0,0);draw()}
function draw(){
 if(!width)return;
 ctx.clearRect(0,0,width,height);
 const mobile=width<761,t=reduced.matches?6:time;
 const scale=mobile?width*.46:Math.min(width*.25,height*.39);
 const cx=width*(mobile?.51:.745),cy=height*(mobile?(english?.73:.71):.47);
 const turn=.16*Math.sin(t*.075),tilt=.08*Math.cos(t*.06),breathe=1+.025*Math.sin(t*.4);
 const nodes=heroGraph.nodes.map((n,i)=>{
  const drift=.011*Math.sin(t*.35+i*1.7),x=n.x*Math.cos(turn)+n.z*Math.sin(turn),z=n.z*Math.cos(turn)-n.x*Math.sin(turn);
  return {x:cx+(x*breathe+drift)*scale,y:cy+(n.y*Math.cos(tilt)-z*Math.sin(tilt)+drift*.7)*scale,z,kind:n.kind};
 });
 // A soft vellum halo lets thin ink links read against the light page.
 const halo=ctx.createRadialGradient(cx,cy,scale*.1,cx,cy,scale*1.12);
 halo.addColorStop(0,'rgba(218,230,246,.38)');halo.addColorStop(.6,'rgba(226,234,246,.14)');halo.addColorStop(1,'rgba(240,245,251,0)');
 ctx.fillStyle=halo;ctx.fillRect(cx-scale*1.2,cy-scale*1.2,scale*2.4,scale*2.4);
 // Fine registration marks evoke a scientific atlas without a cage or mesh.
 ctx.strokeStyle='rgba(47,76,112,.14)';ctx.lineWidth=.7;
 for(let i=0;i<48;i++){
  const a=i*tau/48,r=scale*1.075;ctx.beginPath();
  ctx.moveTo(cx+Math.cos(a)*r,cy+Math.sin(a)*r);
  ctx.lineTo(cx+Math.cos(a)*(r+(i%4===0?6:2)),cy+Math.sin(a)*(r+(i%4===0?6:2)));ctx.stroke();
 }
 const activity=new Float32Array(nodes.length);
 for(let i=0;i<heroGraph.edges.length;i++){
  const [s,e]=heroGraph.edges[i],a=nodes[s],b=nodes[e];
  const dx=b.x-a.x,dy=b.y-a.y,bend=.08*Math.sin(i*2.4),mx=(a.x+b.x)/2-dy*bend,my=(a.y+b.y)/2+dx*bend;
  const depth=.7+(a.z+b.z)*.25;
  ctx.strokeStyle=`rgba(45,75,116,${.25*depth})`;ctx.lineWidth=mobile?.7:.85;
  ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.quadraticCurveTo(mx,my,b.x,b.y);ctx.stroke();
  // Pulses traverse documented directed links, staggered into quiet waves.
  const p=((t*.17+i*.137)%2.6),strength=Math.sin(Math.min(1,p)*Math.PI);
  if(p<1){
   const u=1-p,x=u*u*a.x+2*u*p*mx+p*p*b.x,y=u*u*a.y+2*u*p*my+p*p*b.y;
   ctx.strokeStyle=`rgba(30,69,120,${.2*strength})`;ctx.lineWidth=1.2;
   ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.quadraticCurveTo(mx,my,b.x,b.y);ctx.stroke();
   const glow=ctx.createRadialGradient(x,y,0,x,y,9);glow.addColorStop(0,`rgba(84,132,194,${.32*strength})`);glow.addColorStop(1,'rgba(84,132,194,0)');
   ctx.fillStyle=glow;ctx.beginPath();ctx.arc(x,y,9,0,tau);ctx.fill();
   ctx.fillStyle=`rgba(30,66,111,${.8*strength})`;ctx.beginPath();ctx.arc(x,y,1.65,0,tau);ctx.fill();
   activity[s]=Math.max(activity[s],Math.max(0,1-p*5));activity[e]=Math.max(activity[e],Math.max(0,(p-.75)*4));
  }
 }
 nodes.map((n,i)=>({...n,i})).sort((a,b)=>a.z-b.z).forEach(n=>{
  const active=activity[n.i],hub=n.kind==='marker',r=(hub?4.3:n.kind==='paradigm'?2.2:3.2)*(1+n.z*.24)*(mobile?.86:1);
  ctx.fillStyle=`rgba(250,252,255,${.9})`;ctx.strokeStyle=`rgba(30,61,101,${.48+n.z*.2+active*.3})`;ctx.lineWidth=hub?1.4:.9;
  ctx.beginPath();
  if(n.kind==='construct'){ctx.moveTo(n.x,n.y-r*1.3);ctx.lineTo(n.x+r*1.3,n.y);ctx.lineTo(n.x,n.y+r*1.3);ctx.lineTo(n.x-r*1.3,n.y);ctx.closePath()}
  else if(n.kind==='region')ctx.rect(n.x-r,n.y-r,r*2,r*2);
  else ctx.arc(n.x,n.y,r,0,tau);
  if(n.kind==='paradigm')ctx.fillStyle=`rgba(39,73,117,${.52+n.z*.2})`;
  ctx.fill();ctx.stroke();
  if(hub){
   ctx.strokeStyle=`rgba(47,83,134,${.13+active*.2})`;ctx.lineWidth=.7;ctx.beginPath();ctx.arc(n.x,n.y,r+5+active*3,0,tau);ctx.stroke();
   ctx.fillStyle='rgba(35,68,113,.78)';ctx.beginPath();ctx.arc(n.x,n.y,1.5,0,tau);ctx.fill();
  }
 });
}
function animate(now){frame=0;if(paused||!visible||document.hidden)return;if(now-last>30){time+=Math.min((now-last)/1000,.08);draw();last=now}frame=requestAnimationFrame(animate)}
function start(){last=performance.now();if(!frame&&!paused&&visible&&!document.hidden)frame=requestAnimationFrame(animate)}
function stop(){cancelAnimationFrame(frame);frame=0}
motionButton.addEventListener('click',()=>{paused=!paused;updateMotionButton();if(paused)stop();else start()});
new ResizeObserver(fit).observe(canvas);new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;if(visible)start();else stop()},{threshold:.05}).observe(canvas);
const sectionObserver=new IntersectionObserver(entries=>entries.forEach(e=>e.target.classList.toggle('motion-visible',e.isIntersecting)),{threshold:0});document.querySelectorAll('main>section').forEach(s=>sectionObserver.observe(s));
document.addEventListener('visibilitychange',()=>{document.body.classList.toggle('page-hidden',document.hidden);if(document.hidden)stop();else start()});reduced.addEventListener('change',e=>{paused=e.matches;updateMotionButton();if(paused){stop();draw()}else start()});updateMotionButton();start();
