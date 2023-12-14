import{g as W,c as v,m as Y,d as $,u as pe,o as b,a as V,w as S,b as ue,e as be,s as L,f as p,h as ke,i as z,j as N,k as se,C as Se,p as U,l as Ve,n as Te,q as xe,t as ae,r as Me,v as Be,x as re,y as F,z as Ce,A as Ee,T as Le,F as A,B as Pe,D as Re,E as j,G as q,H as Ie,I as Ne,J as He}from"./index-74d9aecf.js";import{m as $e,u as O,V as De,a as Ye,b as Ae,w as ie,c as We,d as Z,e as ze,f as Oe,g as Xe,h as ce,i as Fe,j as ne,k as je,l as qe,n as Ue,o as ve,p as Ze,t as Ge,q as Je,r as de,s as H,v as D,x as Ke,y as Qe,z as et,A as tt,B as at,C as nt,D as lt,E as ot}from"./scopeId-66a2197a.js";const ut=W()({name:"VAppBarTitle",props:$e(),setup(e,l){let{slots:n}=l;return O(()=>v(De,Y(e,{class:"v-app-bar-title"}),n)),{}}}),st=be("h2",null," BAAS ",-1),rt=$({__name:"AppBar",setup(e){const l=pe();function n(){l.global.name.value=l.global.current.value.dark?"light":"dark"}return(o,a)=>(b(),V(Ae,null,{append:S(()=>[v(Ye,{label:ue(l).global.name.value,onClick:a[0]||(a[0]=t=>n())},null,8,["label"])]),default:S(()=>[v(ut,null,{default:S(()=>[st]),_:1})]),_:1}))}}),me=e=>e==null?void 0:e.data;async function it(){return ie.get("/static/render.json").then(me)}async function ct(){return ie.get("/static/baas.json").then(me)}function vt(e){let{rootEl:l,isSticky:n,layoutItemStyles:o}=e;const a=L(!1),t=L(0),s=p(()=>{const y=typeof a.value=="boolean"?"top":a.value;return[n.value?{top:"auto",bottom:"auto",height:void 0}:void 0,a.value?{[y]:ke(t.value)}:{top:o.value.top}]});z(()=>{N(n,y=>{y?window.addEventListener("scroll",_,{passive:!0}):window.removeEventListener("scroll",_)},{immediate:!0})}),se(()=>{window.removeEventListener("scroll",_)});let d=0;function _(){const y=d>window.scrollY?"up":"down",c=l.value.getBoundingClientRect(),m=parseFloat(o.value.top??0),f=window.scrollY-Math.max(0,t.value-m),g=c.height+Math.max(t.value,m)-window.scrollY-window.innerHeight,h=parseFloat(getComputedStyle(l.value).getPropertyValue("--v-body-scroll-y"))||0;c.height<window.innerHeight-m?(a.value="top",t.value=m):y==="up"&&a.value==="bottom"||y==="down"&&a.value==="top"?(t.value=window.scrollY+c.top-h,a.value=!0):y==="down"&&g<=0?(t.value=0,a.value="bottom"):y==="up"&&f<=0&&(h?a.value!=="top"&&(t.value=-f+h+m,a.value="top"):(t.value=c.top+f,a.value="top")),d=window.scrollY}return{isStuck:a,stickyStyles:s}}const dt=100,mt=20;function le(e){const l=1.41421356237;return(e<0?-1:1)*Math.sqrt(Math.abs(e))*l}function oe(e){if(e.length<2)return 0;if(e.length===2)return e[1].t===e[0].t?0:(e[1].d-e[0].d)/(e[1].t-e[0].t);let l=0;for(let n=e.length-1;n>0;n--){if(e[n].t===e[n-1].t)continue;const o=le(l),a=(e[n].d-e[n-1].d)/(e[n].t-e[n-1].t);l+=(a-o)*Math.abs(a),n===e.length-1&&(l*=.5)}return le(l)*1e3}function ft(){const e={};function l(a){Array.from(a.changedTouches).forEach(t=>{(e[t.identifier]??(e[t.identifier]=new Se(mt))).push([a.timeStamp,t])})}function n(a){Array.from(a.changedTouches).forEach(t=>{delete e[t.identifier]})}function o(a){var y;const t=(y=e[a])==null?void 0:y.values().reverse();if(!t)throw new Error(`No samples for touch id ${a}`);const s=t[0],d=[],_=[];for(const c of t){if(s[0]-c[0]>dt)break;d.push({t:c[0],d:c[1].clientX}),_.push({t:c[0],d:c[1].clientY})}return{x:oe(d),y:oe(_),get direction(){const{x:c,y:m}=this,[f,g]=[Math.abs(c),Math.abs(m)];return f>g&&c>=0?"right":f>g&&c<=0?"left":g>f&&m>=0?"down":g>f&&m<=0?"up":gt()}}}return{addMovement:l,endTouch:n,getVelocity:o}}function gt(){throw new Error}function ht(e){let{isActive:l,isTemporary:n,width:o,touchless:a,position:t}=e;z(()=>{window.addEventListener("touchstart",I,{passive:!0}),window.addEventListener("touchmove",x,{passive:!1}),window.addEventListener("touchend",B,{passive:!0})}),se(()=>{window.removeEventListener("touchstart",I),window.removeEventListener("touchmove",x),window.removeEventListener("touchend",B)});const s=p(()=>["left","right"].includes(t.value)),{addMovement:d,endTouch:_,getVelocity:y}=ft();let c=!1;const m=L(!1),f=L(0),g=L(0);let h;function P(u,i){return(t.value==="left"?u:t.value==="right"?document.documentElement.clientWidth-u:t.value==="top"?u:t.value==="bottom"?document.documentElement.clientHeight-u:E())-(i?o.value:0)}function R(u){let i=arguments.length>1&&arguments[1]!==void 0?arguments[1]:!0;const r=t.value==="left"?(u-g.value)/o.value:t.value==="right"?(document.documentElement.clientWidth-u-g.value)/o.value:t.value==="top"?(u-g.value)/o.value:t.value==="bottom"?(document.documentElement.clientHeight-u-g.value)/o.value:E();return i?Math.max(0,Math.min(1,r)):r}function I(u){if(a.value)return;const i=u.changedTouches[0].clientX,r=u.changedTouches[0].clientY,w=25,T=t.value==="left"?i<w:t.value==="right"?i>document.documentElement.clientWidth-w:t.value==="top"?r<w:t.value==="bottom"?r>document.documentElement.clientHeight-w:E(),M=l.value&&(t.value==="left"?i<o.value:t.value==="right"?i>document.documentElement.clientWidth-o.value:t.value==="top"?r<o.value:t.value==="bottom"?r>document.documentElement.clientHeight-o.value:E());(T||M||l.value&&n.value)&&(c=!0,h=[i,r],g.value=P(s.value?i:r,l.value),f.value=R(s.value?i:r),_(u),d(u))}function x(u){const i=u.changedTouches[0].clientX,r=u.changedTouches[0].clientY;if(c){if(!u.cancelable){c=!1;return}const T=Math.abs(i-h[0]),M=Math.abs(r-h[1]);(s.value?T>M&&T>3:M>T&&M>3)?(m.value=!0,c=!1):(s.value?M:T)>3&&(c=!1)}if(!m.value)return;u.preventDefault(),d(u);const w=R(s.value?i:r,!1);f.value=Math.max(0,Math.min(1,w)),w>1?g.value=P(s.value?i:r,!0):w<0&&(g.value=P(s.value?i:r,!1))}function B(u){if(c=!1,!m.value)return;d(u),m.value=!1;const i=y(u.changedTouches[0].identifier),r=Math.abs(i.x),w=Math.abs(i.y);(s.value?r>w&&r>400:w>r&&w>3)?l.value=i.direction===({left:"right",right:"left",top:"down",bottom:"up"}[t.value]||E()):l.value=f.value>.5}const C=p(()=>m.value?{transform:t.value==="left"?`translateX(calc(-100% + ${f.value*o.value}px))`:t.value==="right"?`translateX(calc(100% - ${f.value*o.value}px))`:t.value==="top"?`translateY(calc(-100% + ${f.value*o.value}px))`:t.value==="bottom"?`translateY(calc(100% - ${f.value*o.value}px))`:E(),transition:"none"}:void 0);return{isDragging:m,dragProgress:f,dragStyles:C}}function E(){throw new Error}const yt=["start","end","left","right","top","bottom"],wt=U({color:String,disableResizeWatcher:Boolean,disableRouteWatcher:Boolean,expandOnHover:Boolean,floating:Boolean,modelValue:{type:Boolean,default:null},permanent:Boolean,rail:{type:Boolean,default:null},railWidth:{type:[Number,String],default:56},scrim:{type:[Boolean,String],default:!0},image:String,temporary:Boolean,touchless:Boolean,width:{type:[Number,String],default:256},location:{type:String,default:"start",validator:e=>yt.includes(e)},sticky:Boolean,...We(),...Z(),...ze(),...Oe(),...Xe(),...ce({tag:"nav"}),...Ve()},"VNavigationDrawer"),fe=W()({name:"VNavigationDrawer",props:wt(),emits:{"update:modelValue":e=>!0,"update:rail":e=>!0},setup(e,l){let{attrs:n,emit:o,slots:a}=l;const{isRtl:t}=Te(),{themeClasses:s}=xe(e),{borderClasses:d}=Fe(e),{backgroundColorClasses:_,backgroundColorStyles:y}=ne(ae(e,"color")),{elevationClasses:c}=je(e),{mobile:m}=Me(),{roundedClasses:f}=qe(e),g=Ue(),h=Be(e,"modelValue",null,k=>!!k),{ssrBootStyles:P}=ve(),{scopeId:R}=Ze(),I=re(),x=L(!1),B=p(()=>e.rail&&e.expandOnHover&&x.value?Number(e.width):Number(e.rail?e.railWidth:e.width)),C=p(()=>Ge(e.location,t.value)),u=p(()=>!e.permanent&&(m.value||e.temporary)),i=p(()=>e.sticky&&!u.value&&C.value!=="bottom");F(()=>e.expandOnHover&&e.rail!=null,()=>{N(x,k=>o("update:rail",!k))}),F(()=>!e.disableResizeWatcher,()=>{N(u,k=>!e.permanent&&Pe(()=>h.value=!k))}),F(()=>!e.disableRouteWatcher&&!!g,()=>{N(g.currentRoute,()=>u.value&&(h.value=!1))}),N(()=>e.permanent,k=>{k&&(h.value=!0)}),Ce(()=>{e.modelValue!=null||u.value||(h.value=e.permanent||!m.value)});const{isDragging:r,dragProgress:w,dragStyles:T}=ht({isActive:h,isTemporary:u,width:B,touchless:ae(e,"touchless"),position:C}),M=p(()=>{const k=u.value?0:e.rail&&e.expandOnHover?Number(e.railWidth):B.value;return r.value?k*w.value:k}),{layoutItemStyles:X,layoutItemScrimStyles:ge}=Je({id:e.name,order:p(()=>parseInt(e.order,10)),position:C,layoutSize:M,elementSize:B,active:p(()=>h.value||r.value),disableTransitions:p(()=>r.value),absolute:p(()=>e.absolute||i.value&&typeof G.value!="string")}),{isStuck:G,stickyStyles:he}=vt({rootEl:I,isSticky:i,layoutItemStyles:X}),J=ne(p(()=>typeof e.scrim=="string"?e.scrim:null)),ye=p(()=>({...r.value?{opacity:w.value*.2,transition:"none"}:void 0,...ge.value}));Ee({VList:{bgColor:"transparent"}});function we(){x.value=!0}function _e(){x.value=!1}return O(()=>{const k=a.image||e.image;return v(A,null,[v(e.tag,Y({ref:I,onMouseenter:we,onMouseleave:_e,class:["v-navigation-drawer",`v-navigation-drawer--${C.value}`,{"v-navigation-drawer--expand-on-hover":e.expandOnHover,"v-navigation-drawer--floating":e.floating,"v-navigation-drawer--is-hovering":x.value,"v-navigation-drawer--rail":e.rail,"v-navigation-drawer--temporary":u.value,"v-navigation-drawer--active":h.value,"v-navigation-drawer--sticky":i.value},s.value,_.value,d.value,c.value,f.value,e.class],style:[y.value,X.value,T.value,P.value,he.value,e.style]},R,n),{default:()=>{var K,Q,ee,te;return[k&&v("div",{key:"image",class:"v-navigation-drawer__img"},[a.image?(K=a.image)==null?void 0:K.call(a,{image:e.image}):v("img",{src:e.image,alt:""},null)]),a.prepend&&v("div",{class:"v-navigation-drawer__prepend"},[(Q=a.prepend)==null?void 0:Q.call(a)]),v("div",{class:"v-navigation-drawer__content"},[(ee=a.default)==null?void 0:ee.call(a)]),a.append&&v("div",{class:"v-navigation-drawer__append"},[(te=a.append)==null?void 0:te.call(a)])]}}),v(Le,{name:"fade-transition"},{default:()=>[u.value&&(r.value||h.value)&&!!e.scrim&&v("div",Y({class:["v-navigation-drawer__scrim",J.backgroundColorClasses.value],style:[ye.value,J.backgroundColorStyles.value],onClick:()=>h.value=!1},R),null)]})])}),{isStuck:G}}}),_t=$({__name:"NavServ",setup(e){const l=re([]);let n;async function o(){try{await H.loadServs(),l.value=H.ls_servs}finally{n=setTimeout(()=>o(),1e3)}}Re(()=>{clearTimeout(n)}),z(async()=>{o();const[t,s]=await Promise.all([it(),ct()]);et(t,s)});const a=async t=>{await H.selectServ(t)};return(t,s)=>(b(),V(fe,{permanent:"",width:"166"},{default:S(()=>[v(de,{lines:"one"},{default:S(()=>[(b(!0),j(A,null,q(l.value,d=>(b(),V(D,{key:d.serv_name,title:d.serv_name,value:d.serv_name,onClick:_=>a(d.serv_name)},{prepend:S(()=>[d.is_running?(b(),V(Ke,{key:0,indeterminate:"",class:"mr-2",size:"15",color:"success"})):(b(),V(Qe,{key:1,icon:"mdi-circle",size:"15",color:"grey"}))]),_:2},1032,["title","value","onClick"]))),128))]),_:1})]),_:1}))}});const pt=$({__name:"NavConf",setup(e){const l=Ie([]);z(async()=>{const o=await tt();l.push(...o.list)});const n=async o=>{await H.selectConfig(o)};return(o,a)=>(b(),V(fe,{permanent:"",width:"166"},{default:S(()=>[ue(H).cur_serv?(b(),V(de,{key:0,"onClick:select":a[0]||(a[0]=t=>n(t.id))},{default:S(()=>[v(D,{title:"总览",value:"builtin:summary"}),(b(!0),j(A,null,q(l,t=>(b(),V(at,{key:t.text},{activator:S(({props:s})=>[v(D,Y(s,{title:t.text}),null,16,["title"])]),default:S(()=>[(b(!0),j(A,null,q(t.child,s=>(b(),V(D,{key:s.name,title:s.text,value:s.name},null,8,["title","value"]))),128))]),_:2},1024))),128))]),_:1})):Ne("",!0)]),_:1}))}});const bt=U({scrollable:Boolean,...Z(),...ce({tag:"main"})},"VMain"),kt=W()({name:"VMain",props:bt(),setup(e,l){let{slots:n}=l;const{mainStyles:o}=nt(),{ssrBootStyles:a}=ve();return O(()=>v(e.tag,{class:["v-main",{"v-main--scrollable":e.scrollable},e.class],style:[o.value,a.value,e.style]},{default:()=>{var t,s;return[e.scrollable?v("div",{class:"v-main__scroller"},[(t=n.default)==null?void 0:t.call(n)]):(s=n.default)==null?void 0:s.call(n)]}})),{}}}),St=$({__name:"View",setup(e){return(l,n)=>{const o=He("router-view");return b(),V(kt,null,{default:S(()=>[v(o)]),_:1})}}});const Vt=U({...Z(),...lt()},"VLayout"),Tt=W()({name:"VLayout",props:Vt(),setup(e,l){let{slots:n}=l;const{layoutClasses:o,layoutStyles:a,getLayoutItem:t,items:s,layoutRef:d}=ot(e);return O(()=>{var _;return v("div",{ref:d,class:[o.value,e.class],style:[a.value,e.style]},[(_=n.default)==null?void 0:_.call(n)])}),{getLayoutItem:t,items:s}}}),Bt=$({__name:"Default",setup(e){return(l,n)=>(b(),V(Tt,null,{default:S(()=>[v(rt),v(_t),v(pt),v(St)]),_:1}))}});export{Bt as default};
