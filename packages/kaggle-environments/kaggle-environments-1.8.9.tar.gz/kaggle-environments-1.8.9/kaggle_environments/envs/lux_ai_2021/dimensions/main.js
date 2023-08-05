(()=>{var e,t,r,s={8967:e=>{function t(e){var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}t.keys=()=>[],t.resolve=t,t.id=8967,e.exports=t},4120:e=>{function t(e){var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}t.keys=()=>[],t.resolve=t,t.id=4120,e.exports=t},5689:(e,t,r)=>{var s={"./bin":6973,"./bin.js":6973,"./helpers/cpu":9322,"./helpers/cpu.js":9322,"./helpers/parallel":4014,"./helpers/parallel.js":4014,"./history":8307,"./history.js":8307,"./procfile":7645,"./procfile.js":7645,"./ps":9614,"./ps.js":9614,"./stats":8610,"./stats.js":8610,"./wmic":2677,"./wmic.js":2677};function o(e){var t=i(e);return r(t)}function i(e){if(!r.o(s,e)){var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}return s[e]}o.keys=function(){return Object.keys(s)},o.resolve=i,e.exports=o,o.id=5689},2791:function(e,t,r){"use strict";var s=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};Object.defineProperty(t,"__esModule",{value:!0});const o=r(2272),i=s(r(1058)),n=r(3651),a=new n.LuxDesign("lux_ai_2021"),u=o.create(a,{name:"Lux AI 2021",loggingLevel:o.Logger.LEVEL.NONE,activateStation:!1,observe:!1,createBotDirectories:!1}),c=i.default.createInterface({input:process.stdin,output:process.stdout,terminal:!1});(async()=>{let e=null;for await(const t of c){const r=JSON.parse(t);if(r.type&&"start"===r.type){const t={detached:!0,agentOptions:{detached:!0},storeReplay:!1,storeErrorLogs:!1,loggingLevel:parseInt(r.config.loglevel),seed:parseInt(r.config.seed),mapType:r.config.mapType,parameters:{MAX_DAYS:r.config.episodeSteps}};e=await u.createMatch([{file:"blank",name:"team-0"},{file:"blank",name:"team-1"}],t),r.state&&n.LuxDesignLogic.reset(e,r.state),e.agents.forEach(((e,t)=>{console.error(JSON.stringify(e.messages)),e.messages=[]}));const s=e.state;console.error(JSON.stringify({width:s.game.map.width,height:s.game.map.height,globalCityIDCount:s.game.globalCityIDCount,globalUnitIDCount:s.game.globalUnitIDCount}))}else if(r.length){const t=[];[0,1].forEach((e=>{if(r[e].action){const s=r[e].action.map((t=>({agentID:e,command:t})));t.push(...s)}}));const s=await e.step(t);e.agents.forEach((e=>{console.error(JSON.stringify(e.messages)),e.messages=[]}));const o=e.state;console.error(JSON.stringify({width:o.game.map.width,height:o.game.map.height,globalCityIDCount:o.game.globalCityIDCount,globalUnitIDCount:o.game.globalUnitIDCount})),console.error(JSON.stringify({status:s,turn:o.game.state.turn,max:e.configs.parameters.MAX_DAYS}))}}})()},2357:e=>{"use strict";e.exports=require("assert")},4293:e=>{"use strict";e.exports=require("buffer")},3129:e=>{"use strict";e.exports=require("child_process")},7619:e=>{"use strict";e.exports=require("constants")},6417:e=>{"use strict";e.exports=require("crypto")},881:e=>{"use strict";e.exports=require("dns")},8614:e=>{"use strict";e.exports=require("events")},5747:e=>{"use strict";e.exports=require("fs")},8605:e=>{"use strict";e.exports=require("http")},7211:e=>{"use strict";e.exports=require("https")},1631:e=>{"use strict";e.exports=require("net")},2087:e=>{"use strict";e.exports=require("os")},5622:e=>{"use strict";e.exports=require("path")},1191:e=>{"use strict";e.exports=require("querystring")},1058:e=>{"use strict";e.exports=require("readline")},2413:e=>{"use strict";e.exports=require("stream")},4304:e=>{"use strict";e.exports=require("string_decoder")},3867:e=>{"use strict";e.exports=require("tty")},8835:e=>{"use strict";e.exports=require("url")},1669:e=>{"use strict";e.exports=require("util")},8761:e=>{"use strict";e.exports=require("zlib")}},o={};function i(e){var t=o[e];if(void 0!==t)return t.exports;var r=o[e]={id:e,loaded:!1,exports:{}};return s[e].call(r.exports,r,r.exports,i),r.loaded=!0,r.exports}i.m=s,i.x=()=>{var e=i.O(void 0,[540],(()=>i(2791)));return i.O(e)},i.amdD=function(){throw new Error("define cannot be used indirect")},i.amdO={},e=[],i.O=(t,r,s,o)=>{if(!r){var n=1/0;for(c=0;c<e.length;c++){for(var[r,s,o]=e[c],a=!0,u=0;u<r.length;u++)(!1&o||n>=o)&&Object.keys(i.O).every((e=>i.O[e](r[u])))?r.splice(u--,1):(a=!1,o<n&&(n=o));a&&(e.splice(c--,1),t=s())}return t}o=o||0;for(var c=e.length;c>0&&e[c-1][2]>o;c--)e[c]=e[c-1];e[c]=[r,s,o]},i.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return i.d(t,{a:t}),t},i.d=(e,t)=>{for(var r in t)i.o(t,r)&&!i.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},i.f={},i.e=e=>Promise.all(Object.keys(i.f).reduce(((t,r)=>(i.f[r](e,t),t)),[])),i.u=e=>e+".js",i.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),r={179:1},i.O.require=e=>r[e],i.f.require=(e,t)=>{r[e]||(e=>{var t=e.modules,s=e.ids,o=e.runtime;for(var n in t)i.o(t,n)&&(i.m[n]=t[n]);o&&o(i);for(var a=0;a<s.length;a++)r[s[a]]=1;i.O()})(require("./"+i.u(e)))},t=i.x,i.x=()=>(i.e(540),t()),i.x()})();